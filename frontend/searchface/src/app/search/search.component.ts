import { Component, OnInit } from '@angular/core';
import {Service} from "../services";

@Component({
  selector: 'search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css']
})
export class SearchComponent implements OnInit {

  constructor(private service: Service) { }

  ngOnInit(): void {
  }

  search(){
    this.service.requestSearch().subscribe(
      res => { console.log(res)},
      error => { // @ts-ignore
      console.log(error)}
    );
  }


}
