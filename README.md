# QUIRATE
Whatever you want to learn, let Quirate help you learn it.

Quirate lets you curate your own flashcards and quiz yourself for learning in any subject you choose. 

#quirate


## Installation

- Clone Quirate from github at (https://github.com/Momentum-Team-10/django-duplex-team-ravenclaw)
- In the local main Quirate directory set up your virtual enviornment in 'pipenv' or 'virtualenv'.  Also, you'll need to have Python and Django installed. If using pup run  `pipenv install`, `pipenv shell`, `python manage.py migrate`, and `python manage.py runserver` one after the other.


## Playing Quirate

- At the home page, login or register.
- If you've never played before, go to 'Add Deck' to make your first deck of flashcards.
- Go to "View Cards" to make new cards for your deck.  As you add them they'll show up here.  Come here anytime you want to add, delete or edit the questions on cards in this deck. 
- When you're ready to play simply press  "Play a Deck" and you're ready to become a Quizard!
- First you'll see the question.  When you think you know the answer, click on the card and it will flip over to show you the answer.  
- Did you get it right?  If so press ✔, if not press X. As you go from card to card check how you're doing on the counter.  
- You can only answer a card once.  Don't worry, you can play this deck over and over until you know it all. 
- After you've answered all your cards, check your score.  If you want to play that deck again hit the "Reset Deck" and you've got another chance to get them all right.  
- When you've mastered that deck go to "Home" and pick another deck to play.  You can also add decks and cards from here. 
- After you're all done learning, logout and go show everyone what a Quizard you are!



## Product Goals Achieved for Option 2: Flashcards

You want to make an application to help people learn via flashcards. You are going to build a web application that has these goals:

- Logged in users can create multiple decks of flashcards, each with a prompt or question and an answer.
- Logged in users can quiz themselves on a deck.
- Success and failure for each card is recorded.

