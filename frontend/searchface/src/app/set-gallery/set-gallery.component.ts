import { Component, OnInit } from '@angular/core';
import {FormControl, Validators} from '@angular/forms';
import {Service} from "../services";



@Component({
  selector: 'set-gallery',
  templateUrl: './set-gallery.component.html',
  styleUrls: ['./set-gallery.component.css']
})
export class SetGalleryComponent implements OnInit {
  selectedFile = null;
  url = "";
  reader = new FileReader();
  constructor(private service: Service) { }

  ngOnInit(): void {
  }
  savePath(path:any){
   this.service.sendGalleryPath(path).subscribe(
     res => console.log(res),
     error => console.log(error)
   )
  }

}
