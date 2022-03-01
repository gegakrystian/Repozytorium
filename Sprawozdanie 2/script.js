const input = document.querySelector("#add");
const  btn = document.querySelector("#btn");
const list = document.querySelector("#list");
var el = document.getElementsByTagName('li');

// Dodawanie zadan po kliknieciu przycisku
btn.onclick = function(){
    
    var txt = input.value;
    if(txt ==''){
        alert('Musisz cos wpisac!');
    }else{
        li = document.createElement('li');
    li.innerHTML = txt;
    list.insertBefore(li,list.childNodes[0]);
    input.value = '';
    }
    
};

//Sprawdzanie klikanych elementów
list.onclick = function(ev){
    if(ev.target.tagName == 'LI'){
         ev.target.classList.toggle('checked');
    }
};