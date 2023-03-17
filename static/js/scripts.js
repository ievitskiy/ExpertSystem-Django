let modal = document.getElementById('enterform')
let regist = document.getElementById('regform')
let btn = document.getElementById('myBtn');
let enter = document.getElementById('entbtn')
let x = false; // reg non used
let y = false; // ent non used

btn.onclick = function (){
    if(x){
        regist.style.display = 'none';
        x = false;
    }
    else{
        modal.style.display = 'none';
        regist.style.display = 'flex';
        y = false;
        x = true;

    }
}

enter.onclick = function (){
    if(y){
        modal.style.display = 'none';
        y = false;
    }
    else{
        regist.style.display = 'none';
        modal.style.display = 'flex';
        x = false;
        y = true;
    }
}

