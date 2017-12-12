import { Component, OnInit } from '@angular/core';
import { Switch } from '../switch'

@Component({
  selector: 'app-board',
  templateUrl: './board.component.html',
  styleUrls: ['./board.component.css']
})
export class BoardComponent implements OnInit {
  switchArr: Array<Switch>;

  constructor() { }

  ngOnInit() {
    this.switchArr = [
      {green: true, texty: "On"},
      {green: false, texty:"Off"},
      {green: true, texty: "On"},
      {green: false, texty:"Off"},
      {green: true, texty: "On"},
      {green: false, texty:"Off"},
      {green: true, texty: "On"},
      {green: false, texty:"Off"}
    ]
  }
  turnoff(idx){
    this.switchArr[idx].green = false;
    this.switchArr[idx].texty = "Off";

  }
  turnon(idx){
    this.switchArr[idx].green = true;
    this.switchArr[idx].texty = "On";
  }

}
