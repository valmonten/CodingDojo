import { AbstractControl } from '@angular/forms';
export class Pwv {
  static MatchPassword(AC: AbstractControl) {
    let password = AC.get('password').value;
    let passwordconf = AC.get('passwordconf').value;
    if (password != passwordconf) {
      AC.get('passwordconf').setErrors({MatchPassword: true})
    } else {
      return null;
    }
  }
}
