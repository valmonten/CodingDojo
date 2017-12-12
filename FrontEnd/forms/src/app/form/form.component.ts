import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Pwv } from "./pwv"

@Component({
  selector: 'app-form',
  templateUrl: './form.component.html',
  styleUrls: ['./form.component.css']
})
export class FormComponent implements OnInit {
  user =
  {
    firstname: "",
    lastname: "",
    email: "",
    password: "",
    passwordconf: ""
  }
  users = []
  constructor() { }

  ngOnInit() {
  }
  entered() {
    console.log("Started");
    console.log(this.user);
    this.users.push(this.user);
    this.user =
      {
      firstname: "",
      lastname: "",
      email: "",
      password: "",
      passwordconf: ""

      }
    console.log(this.users);
  }
}
