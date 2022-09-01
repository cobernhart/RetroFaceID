import { Component, OnInit } from '@angular/core';
import {Service} from "../services";
import {NotificationService} from "../notification-service";

@Component({
  selector: 'search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})
export class SearchComponent implements OnInit {

  constructor(private service: Service, private notService: NotificationService) { }

  ngOnInit(): void {
  }

  search(){
    this.service.requestSearch().subscribe(
      res =>{
        this.notService.clearAllMessages()
        this.notService.setSuccessMessage("Success: " + res.message)
      },
      error => { // @ts-ignore
        this.notService.clearAllMessages()
        this.notService.setErrorMessage("Error: " + error.error.message)
      }
    );
  }


}
