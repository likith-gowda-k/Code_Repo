var x = 130;
let y = 230;
const z = 330;
// console.log(x);
// console.log(y);
// console.log(z);

ab = 150;
// console.log(x);


function sample(){
    if(true){
    var a = 200;
    let b = 300;
    const c = 400;
    //console.log(b);
  
    }
    // console.log(a);
    // console.log(b);

}

function sample2(){
    var x ='Hello'
  // console.log(x[0]);
   //console.log(x.length);

   var myarray = [50, 'Hello', 55.4]
   //console.log('Before ' + myarray);

   myarray.push(45);
//    /console.log('After ' + myarray);

   myarray[6] = 'hi';

   //console.log(myarray);

   var array_2d = [ [50, 'Hello', 55.4] , ['Test', 45.4] ]
  // console.log(array_2d);
   
  
 // console.log(array_2d[0][1]);
}



sample2()

//CLASS

class Student{

    constructor(name, rno){
        this.Student_Name = name;
        this.Rno = rno;
        this.email = name + "@mygmail.com";
    }

    showDetails(){
        console.log("name: " + this.Student_Name);
        console.log("Rno: " + this.Rno);
        console.log("Email: " + this.email);
    }

}

//1st OBJECT
const SampleObject = new Student("Likith", 35);
SampleObject.showDetails();

//2nd Object
const SampleObject2 = new Student("Ram", "50");
SampleObject2.showDetails();
