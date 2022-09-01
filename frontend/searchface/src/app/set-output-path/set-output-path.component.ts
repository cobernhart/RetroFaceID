import { Component, OnInit } from '@angular/core';
import {NotificationService} from "../notification-service";
import {Service} from "../services";

@Component({
  selector: 'app-set-output-path',
  templateUrl: './set-output-path.component.html',
  styleUrls: ['./set-output-path.component.css']
})
export class SetOutputPathComponent implements OnInit {

  constructor(private service: Service, private notService: NotificationService) {
  }

  ngOnInit(): void {
  }

  savePath(path: any) {
    this.service.sendOutputPath(path).subscribe(
      res => {
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
