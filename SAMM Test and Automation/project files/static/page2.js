let elem=document.getElementById("ss" );
let elem1=document.getElementById("hh" );
let elem2=document.getElementsByClassName("tickets");
console.log(elem);
console.log(elem2[1]);


function create (){

    elem2[1].style.display = "block";
    elem2[0].style.display = "none";
 
 };
 function show (){

    elem2[0].style.display = "block";
    elem2[1].style.display = "none";
 
 };
 function prevent(){
   sumbit.preventDefualt();

 }
 elem1.addEventListener('click',create) ;
 elem.addEventListener('click',show) ;
 let sumbit=document.getElementById('submit');
 sumbit.addEventListener('submit',prevent);
 console.log(sumbit);


