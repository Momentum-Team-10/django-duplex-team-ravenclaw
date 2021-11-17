

const cards = document.querySelectorAll(".card")
for (let card of cards) {
    card.addEventListener ("click", () => {
        card.classList.toggle("flipcard")
    })
}

// const cards = document.querySelectorAll(".card")
// for (const card of cards) {
// 	card.addEventListener("click", flipCard(card));}
// function flipCard(item) {
// 	item.classList.toggle("flipcard");
// }

// Below is the counter action
var wrong = (function () {
    var counter = 0;
    return function () {return counter += 1;}
  })();

  var right = (function () {
    var counter = 0;
    return function () {return counter += 1;}
  })();

  
  function wrongAnswer(){
    document.getElementById("wrong").innerHTML = wrong();
  }

  function rightAnswer(){
    document.getElementById("right").innerHTML = right();
  }


