import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-time',
  templateUrl: './time.component.html',
  styleUrls: ['./time.component.css']
})
export class TimeComponent implements OnInit {
  options: object = { month: "short", day: "numeric", year: "numeric", hour: "numeric", minute: "2-digit", second: "2-digit" }
  curr: Date = new Date();
  date: Date = new Date();
  MST: string = this.date.setHours(this.date.getHours() + 7).toLocaleString('en-US', this.options);
  CST: string = this.date.setHours(this.date.getHours() + 8).toLocaleString('en-US', this.options);
  EST: string = this.date.setHours(this.date.getHours() + 9).toLocaleString('en-US', this.options);
  constructor() { }

  ngOnInit() {
  }
  PSTonclick() {
    console.log("curr is " + this.curr);
    this.date.setDate(this.curr.getDate());
    console.log("date is " + this.date);
    //this.date.setHours(this.date.getHours() + 6);
  }
  MSTonclick() {
    this.date.setDate(this.curr.getDate());
    this.date.setHours(this.date.getHours() + 7);
  }



}
