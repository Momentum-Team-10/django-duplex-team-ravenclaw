from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Deck, Card
from .forms import DeckForm, CardForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    user = request.user
    decks = Deck.objects.filter(owner=user.pk)

    return render(request, "flashcards/home.html", {
        "user": user, "decks": decks,})

@login_required
def add_deck(request):
    user = request.user
    if request.method == 'GET':
        form = DeckForm()
    else:
        form = DeckForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='home')

    return render(request, "flashcards/add_deck.html", {
        "user": user, "form": form})

# This may need some work
@login_required
def edit_deck(request, pk):
    deck = get_object_or_404(Deck, pk=pk)
    if request.method == 'GET':
        form = DeckForm(instance=deck)
    else:
        form = DeckForm(data=request.POST, instance=deck)
        if form.is_valid():
            form.save()
            return redirect(to='/')

    return render(request, "flashcards/edit_deck.html", {
        "form": form, "deck": deck, "pk": pk})

# This will almost definitely need some work
@login_required
def add_card(request, pk):
    deck = get_object_or_404(Deck, pk=pk)
    user = request.user
    if request.method == 'GET':
        form = CardForm()
    else:
        form = CardForm(data=request.POST)
        if form.is_valid():
            # Unsure about this next line
            form.instance.deck_id = pk
            form.save()
            return redirect(to='edit_deck', pk=pk)

    return render(request, "flashcards/add_card.html", {
        "user": user, "form": form, "deck":deck, "pk":pk})


@login_required
def delete_deck(request, pk):
    deck = get_object_or_404(Deck, pk=pk)
    if request.method == 'POST':
        deck.delete()
        return redirect(to='/')
    return render(request, "flashcards/delete_deck.html",
                  {"deck": deck})

# Not sure exactly how to implement this yet
@login_required
def play_deck(request, pk):
    pass

def view_cards():
    pass

def edit_card(request, deck_pk, card_pk):
    deck = get_object_or_404(Deck, pk=deck_pk)
    card = get_object_or_404(Card, pk=card_pk)
    if request.method == 'GET':
        form = CardForm(instance=card)
    else:
        form = CardForm(data=request.POST, instance=card)
        if form.is_valid():
            form.save()
            return redirect(to='/')

    return render(request, "flashcards/edit_deck.html", {
        "form": form, "deck": deck, "card": card, "deck_pk": deck_pk, "card_pk": card_pk})

def delete_card(request, deck_pk, card_pk):
    deck = get_object_or_404(Deck, pk=deck_pk)
    card = get_object_or_404(Card, pk=card_pk)
    if request.method == 'POST':
        card.delete()
        return redirect(to='/')
    return render(request, "flashcards/delete_card.html",
                  {"deck": deck, "card": card, "deck_pk": deck_pk, "card_pk": card_pk})