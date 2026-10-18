const body=document.getElementById("body");
body.innerHTML="<div id='title-screen'><h1 id='title'>Paws with Claws</h1><p id='welcome'>Welcome to the game!</p><button id='startButton'><img src='../textures/key_icons/enter_pink.svg' alt='Enter' height='16px'>Start Game</button></div>";
const startButton=document.getElementById("startButton");
let up_pressed=false;
let down_pressed=false;
let left_pressed=false;
let right_pressed=false;
let started=false;
startButton.addEventListener("click",function(){
    start()
});
function start(){
    started=true;
    body.innerHTML="<div id='game-screen'><div id='channel-up'></div><div id='channel-down'></div><div id='channel-left'></div><div id='channel-right'></div></div>";
    const channelUp=document.getElementById("channel-up");
    const channelDown=document.getElementById("channel-down");
    const channelLeft=document.getElementById("channel-left");
    const channelRight=document.getElementById("channel-right");
    channelUp.innerHTML="<img id='arrow-up' src='../textures/arrow_up_back.svg' alt='Up'>";
    channelDown.innerHTML="<img id='arrow-down' src='../textures/arrow_down_back.svg' alt='Down'>";
    channelLeft.innerHTML="<img id='arrow-left' src='../textures/arrow_left_back.svg' alt='Left'>";
    channelRight.innerHTML="<img id='arrow-right' src='../textures/arrow_right_back.svg' alt='Right'>";
}
document.addEventListener("keydown",function(event){
    if(started){
        if(event.key==="ArrowUp"){
            up_pressed=true;
            event.preventDefault();
            document.getElementById("arrow-up").src="../textures/arrow_up_front.svg";
        }else if(event.key==="ArrowDown"){
            down_pressed=true;
            event.preventDefault();
            document.getElementById("arrow-down").src="../textures/arrow_down_front.svg";
        }else if(event.key==="ArrowLeft"){
            left_pressed=true;
            event.preventDefault();
            document.getElementById("arrow-left").src="../textures/arrow_left_front.svg";
        }else if(event.key==="ArrowRight"){
            right_pressed=true;
            event.preventDefault();
            document.getElementById("arrow-right").src="../textures/arrow_right_front.svg";
        }
    }else{
        if(event.key==="Enter"){
            start();
        }
    }
});
document.addEventListener("keyup",function(event){
    if(started){
        if(event.key==="ArrowUp"){
            up_pressed=false;
            document.getElementById("arrow-up").src="../textures/arrow_up_back.svg";
        }else if(event.key==="ArrowDown"){
            down_pressed=false;
            document.getElementById("arrow-down").src="../textures/arrow_down_back.svg";
        }else if(event.key==="ArrowLeft"){
            left_pressed=false;
            document.getElementById("arrow-left").src="../textures/arrow_left_back.svg";
        }else if(event.key==="ArrowRight"){
            right_pressed=false;
            document.getElementById("arrow-right").src="../textures/arrow_right_back.svg";
        }
    }
});