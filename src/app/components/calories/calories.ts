import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-calories',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './calories.html',
  styleUrl: './calories.css',
})
export class Calories {
  //ngshki novye
  weight:any;
  height: any;
  age: any;
  gender:string ='male';
  result: number = 0;

  //чтобы рассчитать сколько нужно похавать
  calculateDaily(){
    if(!this.weight ||!this.height||!this.age){
      alert("Пожалуйста заполните все поля!");
      return;
    }
 

    if(this.gender === 'male'){
      this.result = this.weight* 10 + 6.25*this.height - 5 * this.age+ 5;
    }else{
      this.result = this.weight * 10 + 6.25*this.height - 5 * this.age- 161;
    }

    this.result= Math.round(this.result);//округляем, чтобы понятнее было да
  }

  //калории сбрасывать надо
  resetData(){
    this.weight = undefined;
    this.height = undefined;
    this.age = undefined;
    this.result = 0;
  }
}

