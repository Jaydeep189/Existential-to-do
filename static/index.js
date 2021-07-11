function Questions(){
    document.querySelector(".question-box").style.display = 'flex';
}


document.getElementById("add").addEventListener("click", Questions());

document.querySelector(".close").addEventListener("click", function Close(){
    document.querySelector(".question-box").style.display = 'none';
});