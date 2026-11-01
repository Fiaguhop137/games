const body=document.getElementById("body")
body.innerHTML=`
<div id='header'>
    <h1>i can haz clicks</h1>
</div>
<div id='content'>
    <div id='catContainer'>
    <p>Click the button below to generate clicks!</p>
        <button id='clickButton'><img src='../textures/cat.png' alt='Click'></button>
        <p id='clickCount'>Clicks: 0</p>
    </div>
    <div id='sidebar'>
        <div id='shop'>
            <h2>Shop</h2>
            <p id='shopAlert'>Buy items to increase your clicks per click (CPC) or clicks per second (CPS)!</p>
            <p>Welcome to the shop!</p>
        </div>
    </div>
</div>
`
const clickButton=document.getElementById("clickButton")
const clickCount=document.getElementById("clickCount")
let count=0
let cpc=1
clickButton.addEventListener("click",function(){
    count+=cpc
    clickCount.innerHTML="Clicks: "+count
})
const shopItems={
    "pat": {
        "price": 5,
        "description": "A simple pat.",
        "type": "cpc",
        "amount": 1
    },
    "pat 2: electric boogaloo": {
        "price": 15,
        "description": "A sequel to the original pat.",
        "type": "cpc",
        "amount": 5
    },
    "pat 3: revenge of the pats": {
        "price": 50,
        "description": "The pats are back and they're mad!",
        "type": "cpc",
        "amount": 15
    },
    "pat 4: the final pat": {
        "price": 150,
        "description": "The ultimate pat experience.",
        "type": "cpc",
        "amount": 50
    },
    "passive entertainment": {
        "price": 50,
        "description": "Passively satisfy your cat.",
        "type": "cps",
        "amount": 1
    }
}
const shop=document.getElementById("shop")
const shopAlert=document.getElementById("shopAlert")
for (const item in shopItems){
    const itemDiv=document.createElement("div")
    itemDiv.classList.add("shopItem")
    const itemName=document.createElement("h3")
    itemName.innerHTML=item
    const itemPrice=document.createElement("p")
    itemPrice.innerHTML="Price: "+shopItems[item].price+" clicks"
    const itemDescription=document.createElement("p")
    itemDescription.innerHTML=shopItems[item].description
    const buyButton=document.createElement("button")
    buyButton.innerHTML="Buy"
    buyButton.addEventListener("click",function(){
        if (count>=shopItems[item].price){
            count-=shopItems[item].price
            clickCount.innerHTML="Clicks: "+count
            if (shopItems[item].type==="cpc"){
                cpc+=shopItems[item].amount
            }
            shopAlert.textContent="You bought "+item+"!"
        } else {
            shopAlert.textContent="You don't have enough clicks to buy "+item+"."
        }
    })
    itemDiv.appendChild(itemName)
    itemDiv.appendChild(itemPrice)
    itemDiv.appendChild(itemDescription)
    itemDiv.appendChild(buyButton)
    shop.appendChild(itemDiv)
}
