import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-settings',
  templateUrl: './settings.component.html',
  styleUrls: ['./settings.component.css']
})
export class SettingsComponent implements OnInit {
  threshold = 1.6
  constructor() { }

  ngOnInit(): void {
  }

  rangeChange(t: any){
    this.threshold = t
  }
}
