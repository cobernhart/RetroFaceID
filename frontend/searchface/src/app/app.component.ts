import { Component } from '@angular/core';
import {NotificationService} from "./notification-service";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'searchface';
  successMessage$ = this.notService.successMessageAction$
  errorMessage$ = this.notService.errorMessageAction$
  constructor(private notService: NotificationService) {
  }
}
