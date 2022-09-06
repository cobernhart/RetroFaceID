import { Component, OnInit } from '@angular/core';
import {Service} from "../services";
import {NotificationService} from "../notification-service";
import { interval, Subscription } from 'rxjs';
@Component({
  selector: 'search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})
export class SearchComponent implements OnInit {

  constructor(private service: Service, private notService: NotificationService) { }
  subscription = new Subscription();
  imageCount = 0
  faceCount = 0
  matchCount = 0
  started = false
  ngOnInit(): void {
  }

  search(){
    this.imageCount = 0
    this.faceCount = 0
    this.matchCount = 0
    this.started = true
    this.searchProgress()
    this.service.requestSearch().subscribe(
      res =>{
        this.started = false
        this.queryProgress()
        this.subscription.unsubscribe();
        this.notService.clearAllMessages()
        this.notService.setSuccessMessage("Success: " + res.message)
      },
      error => { // @ts-ignore
        this.started = false
        this.notService.clearAllMessages()
        this.notService.setErrorMessage("Error: " + error.error.message)
        this.subscription.unsubscribe(); //unsubscribe get request every 10 seconds
      }
    );
  }

  stopSearch(){
    this.service.stopSearch().subscribe(
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

  searchProgress(){
    const source = interval(5000);
    this.subscription = source.subscribe(val => this.queryProgress());
  }


queryProgress(){
    this.service.requestSearchProgress().subscribe
    (res =>{
        this.imageCount = res.imageCount
        this.faceCount = res.faceCount
        this.matchCount = res.matchCount
      },
      error => {
        this.started = false
        this.notService.clearAllMessages()
        this.notService.setErrorMessage("Error: " + error.error.message)
      }
      )
  }


}
