import { Component, OnInit } from '@angular/core';
import {Service} from "../services";
import {NotificationService} from "../notification-service";

@Component({
  selector: 'app-settings',
  templateUrl: './settings.component.html',
  styleUrls: ['./settings.component.css']
})
export class SettingsComponent implements OnInit {
  threshold = 0
  method = 'efArc'
  optimalThresholds = [
    {  name: 'efCos', limit : 1.61 },
    { name: 'efCos+', limit: 1.62},
    {name : 'efArc' , limit : 1.63},
    {name : 'efArc+', limit : 1.64},
    {name : 'arcFace', limit : 1.65}
    ]

  constructor(private service: Service, private notService: NotificationService) { }

  ngOnInit(): void {
    this.threshold = this.getOptimalThreshold(this.method)
  }

  updateWeight(method: string){
    this.method = method
    this.threshold = this.getOptimalThreshold(this.method)
  }
  getOptimalThreshold(method: string){
    // @ts-ignore
    return this.optimalThresholds.find(a => a.name == method).limit

  }
  rangeChange(t: any){
    this.threshold = t
  }

  saveSetting(){
    this.service.sendSettings({
      'method': this.method,
      'threshold': this.threshold
    }).subscribe(
      res => {
        this.notService.clearAllMessages()
        this.notService.setSuccessMessage(res.message)
      },
      error => { // @ts-ignore
        this.notService.clearAllMessages()
        this.notService.setErrorMessage("Error: " + error.error.message)
      }
    )
  }
}
