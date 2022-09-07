import {Component, ElementRef, OnInit, ViewChild} from '@angular/core';
import {Service} from "../services";
import {NotificationService} from "../notification-service";

@Component({
  selector: 'select-reference-face',
  templateUrl: './select-reference-face.component.html',
  styleUrls: ['./select-reference-face.component.scss']
})


export class SelectReferenceFaceComponent implements OnInit {
  selectedFile = null;
  selectedFace = null;
  imgWidth = 0;
  imgHeight = 0;
  imageDisplayHeight = 300;
  reader = new FileReader();
  url = null;
  boxes = null;
  ngOnInit(): void {

  }
  constructor(private service: Service,
              private notService : NotificationService) { }

  resizeBoxes(length: number){
    let resizeFactor = this.imgHeight /  this.imageDisplayHeight;
    return length / resizeFactor;
  }
  onFileSelected(event:any){
    this.selectedFace = null; //set to unset as new image is choosen
    this.selectedFile = event.target.files[0];
    // @ts-ignore
    const img = new Image();
    // @ts-ignore
    img.onload = () => {
      this.imgHeight = img.height
      this.imgWidth = img.width
    }
    // @ts-ignore
    this.reader.readAsDataURL(this.selectedFile);
    this.reader.onload = (event) => {
      // @ts-ignore
      this.url = event.target.result
      // @ts-ignore
      img.src = this.url;
    }
    const fd = new FormData()
    // @ts-ignore
    fd.append('image',this.selectedFile,this.selectedFile.name)
    // @ts-ignore
    this.service.sendRefForFaceDetection(fd).subscribe(
      res => {
        this.boxes = JSON.parse(res.boxes);
        this.notService.clearAllMessages()
        this.notService.setSuccessMessage("Success: " + res.message)
        },
      error => { // @ts-ignore
        this.boxes = undefined;
        this.notService.clearAllMessages()
        this.notService.setErrorMessage("Error: " + error.error.message)
      }
    );
  }

  faceSelect(event: any){
    this.selectedFace = event.target.id
    // @ts-ignore
    this.service.sendFaceSelection(this.selectedFace).subscribe(
      res => {
        this.notService.clearAllMessages()
        this.notService.setSuccessMessage("Success: " + res.message)
      },
      error => {
        this.notService.clearAllMessages()
        this.notService.setErrorMessage("Error: " + error.error.message)
      }
    )
  }
}
