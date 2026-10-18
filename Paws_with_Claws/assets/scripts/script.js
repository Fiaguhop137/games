const body=document.getElementById("body");
body.innerHTML="<div id='title-screen'><h1 id='title'>Paws with Claws</h1><p id='welcome'>Welcome to the game!</p><button id='startButton'>Start Game</button></p></div>";
const startButton=document.getElementById("startButton");
startButton.addEventListener("click",function(){
    body.innerHTML="<div id='game-screen'><div id='channel-up'></div><div id='channel-down'></div><div id='channel-left'></div><div id='channel-right'></div></div>";
    const channelUp=document.getElementById("channel-up");
    const channelDown=document.getElementById("channel-down");
    const channelLeft=document.getElementById("channel-left");
    const channelRight=document.getElementById("channel-right");
    channelUp.innerHTML="<img id='arrow-up' src='../textures/arrow_up_back.svg' alt='Up'>";
    channelDown.innerHTML="<img id='arrow-down' src='../textures/arrow_down_back.svg' alt='Down'>";
    channelLeft.innerHTML="<img id='arrow-left' src='../textures/arrow_left_back.svg' alt='Left'>";
    channelRight.innerHTML="<img id='arrow-right' src='../textures/arrow_right_back.svg' alt='Right'>";
});