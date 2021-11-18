# QUIRATE
Whatever you want to learn, let Quirate help you learn it.

Quirate lets you curate your own flashcards and quiz yourself for learning in any subject you choose.

Follow the ways of the Quirator and you too can become a Quizard.

<!-- ![](static/images/quirator.png) -->

<img src="static/images/quirator.png"
     style="height: 300px;">

#quirate


## Installation

- Clone Quirate from github at (https://github.com/Momentum-Team-10/django-duplex-team-ravenclaw)
- In the local main Quirate directory set up your virtual enviornment in 'pipenv' or 'virtualenv'.  Also, you'll need to have Python and Django installed. If using pip run  `pipenv install`, `pipenv shell`, `python manage.py migrate`, and `python manage.py runserver` one after the other.


## Playing Quirate

- At the home page, login or register.
- If you've never played before, press <img src="static/images/Screen Shot 2021-11-18 at 11.57.50 AM.png" style="height: 20px;"> to make your first deck of flashcards.
- Press <img src="static/images/Screen Shot 2021-11-18 at 11.57.50 AM.png" style="height: 20px;"> again to make new cards for your deck.  As you add them they'll show up here.  Come back here anytime you want to add, delete or edit the questions on cards in this deck. 
- When you're ready to play simply press the play button on your deck <img src="static/images/Screen Shot 2021-11-18 at 12.02.36 PM.png" style="height: 20px;">and you're ready to become a Quizard!
- Your cards will pop up in random order.  First you'll see the question.  When you think you know the answer, click on the card and it will flip over to show you the answer.  
- Did you get it right?  If so press the smiley face, if not press the uh-oh face. As you go from card to card check how you're doing on the counter down below.  
- You can only answer a card once.  Don't worry, you can play this deck over and over until you know it all. 
- After you've answered all your cards, check your score.  If you want to play that deck again hit "Reset Deck" and Quirate will shuffle the cards giving you another chance to get them all right.  
- When you've mastered that deck go to "Home" and pick another deck to play.  You can also add decks and cards from here. 
- After you're all done learning, logout and go show everyone what a Quizard you are!



## Product Goals Achieved for Option 2: Flashcards

You want to make an application to help people learn via flashcards. You are going to build a web application that has these goals:

- Logged in users can create multiple decks of flashcards, each with a prompt or question and an answer.
- Logged in users can quiz themselves on a deck.
- Success and failure for each card is recorded.

