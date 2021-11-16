

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


