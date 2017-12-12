import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-dayview',
  templateUrl: './dayview.component.html',
  styleUrls: ['./dayview.component.css']
})
export class DayviewComponent implements OnInit {

  DaysNotes: string;
  constructor() { }

  ngOnInit() {
    this.DaysNotes = "Today we learned about observers and observables."
  }

}
