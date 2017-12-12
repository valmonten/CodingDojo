import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';


import { AppComponent } from './app.component';
import { DayviewComponent } from './dayview/dayview.component';
import { NotesComponent } from './dayview/notes/notes.component';
import { AgendaComponent } from './dayview/agenda/agenda.component';
import { ReviewComponent } from './dayview/review/review.component';


@NgModule({
  declarations: [
    AppComponent,
    DayviewComponent,
    NotesComponent,
    AgendaComponent,
    ReviewComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
