import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-settings',
  templateUrl: './settings.component.html',
  styleUrls: ['./settings.component.css']
})
export class SettingsComponent implements OnInit {
  threshold = 0
  method = 'efCos'
  optimalThresholds = [
    {  name: 'efCos', limit : 1.61 },
    { name: 'efCos+', limit: 1.62},
    {name : 'efArc' , limit : 1.63},
    {name : 'efArc+', limit : 1.64},
    {name : 'arcFace', limit : 1.65}
    ]

  constructor() { }

  ngOnInit(): void {
  }

  updateWeight(method: string){
    console.log(method)
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
}
