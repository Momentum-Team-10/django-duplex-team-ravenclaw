

// const cards = document.querySelectorAll(".card")
// for (let card of cards) {
//     card.addEventListener ("click", () => {
//         card.classList.toggle("flipcard")
//     })
// }

const cards = document.querySelectorAll(".card")
for (let card of cards) {
    card.addEventListener ("click", () => {
      if (!(card.classList.contains("flipcard"))) {
        card.classList.add("flipcard")
    }})
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

const right_answer_buttons = document.querySelectorAll(".right_answer")
for (let button of right_answer_buttons) {
  button.addEventListener("click", () => {
    button.parentElement.parentElement.style.display = "none";
    button.parentElement.parentElement.nextElementSibling.classList.remove('hidden-card')
  })
}

const wrong_answer_buttons = document.querySelectorAll(".wrong_answer")
for (let button of wrong_answer_buttons) {
  button.addEventListener("click", () => {
    button.parentElement.parentElement.style.display = "none";
    button.parentElement.parentElement.nextElementSibling.classList.remove('hidden-card')
  })
}
