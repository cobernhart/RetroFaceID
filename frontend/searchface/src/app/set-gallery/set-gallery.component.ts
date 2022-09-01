import { Component, OnInit } from '@angular/core';
import {FormControl, Validators} from '@angular/forms';
import {Service} from "../services";
import {NotificationService} from "../notification-service";



@Component({
  selector: 'set-gallery',
  templateUrl: './set-gallery.component.html',
  styleUrls: ['./set-gallery.component.css']
})
export class SetGalleryComponent implements OnInit {
  selectedFile = null;
  url = "";
  reader = new FileReader();
  constructor(private service: Service, private notService: NotificationService) { }

  ngOnInit(): void {
  }
  savePath(path:any){
   this.service.sendGalleryPath(path).subscribe(
     res =>{
       this.notService.clearAllMessages()
       this.notService.setSuccessMessage("Success: " + res.message)
     },
     error => { // @ts-ignore
       this.notService.clearAllMessages()
       this.notService.setErrorMessage("Error: " + error.error.message)
     }
   )
  }

}
