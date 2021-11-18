"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from flashcards import views 

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('registration.backends.simple.urls')),
    
    # Landing page, will ask user to login. Once logged in, it will display user's decks:
    path('', views.home, name='home'),
    
    # Page for creating a new deck (but not adding new cards to it yet)
    path('add_deck/', views.add_deck, name='add_deck'),
    
    # Page for editting basic deck information, should have a button for adding a card
    path('<int:pk>/edit_deck/', views.edit_deck, name='edit_deck'),
    
    # Page for adding a card to a deck
    path('<int:pk>/add_card/', views.add_card, name='add_card'),
    
    # Simple page that prompts the user if they are sure they want to delete a deck
    path('<int:pk>/delete_deck/', views.delete_deck, name='delete_deck'),
    
    # Page to play a deck, will probably use Javascript to go through cards without
    # reloading the page or moving to a new page
    path('<int:pk>/play_deck/', views.play_deck, name='play_deck'),
    
    # Page for viewing all cards on a deck, so that the user can delete or edit
    # individual cards
    path('<int:pk>', views.view_cards, name='view_cards'),
    
    # Page for editing an individual card
    path('<int:deck_pk>/<int:card_pk>/edit_card', views.edit_card, name='edit_card'),
    
    # Page with a prompt to delete an individual card
    path('<int:deck_pk>/<int:card_pk>/delete_card', views.delete_card, name='delete_card')

    
]
