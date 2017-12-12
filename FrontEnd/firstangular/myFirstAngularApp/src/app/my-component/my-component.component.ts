import { Component, OnInit } from '@angular/core';
import { User } from '../user'

@Component({
  selector: 'app-my-component',
  templateUrl: './my-component.component.html',
  styleUrls: ['./my-component.component.css']
})
export class MyComponentComponent implements OnInit {
  my_name: string;
  users: User[];
  
  constructor() { }

  ngOnInit() {
    this.my_name = "Nathan";
    this.users = [
      {email: "bill@gates.com", importance: "High", subject: "newwindows", content:"windows in 2100"},
      {email: "ada@gates.com", importance: "High", subject: "newwinsdafs", content:"windows in 2190"},
      {email: "bil3t@gates.com", importance: "lowh", subject: "n82dows", content:"windo5 in 2100"},
    ]
  }

}
