import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {MatToolbarModule} from "@angular/material/toolbar";
import {MatStepperModule} from "@angular/material/stepper";

import { SelectReferenceFaceComponent } from './select-reference-face/select-reference-face.component';
import { HttpClientModule } from '@angular/common/http';
import { SearchComponent } from './search/search.component';
import { SetGalleryComponent } from './set-gallery/set-gallery.component';
import {ReactiveFormsModule} from "@angular/forms";




@NgModule({
  declarations: [
    AppComponent,
    SelectReferenceFaceComponent,
    SearchComponent,
    SetGalleryComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    BrowserAnimationsModule,
    ReactiveFormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
