#Steve and Josh are bored and want to play something. They don't want to think too much, so they come up with a really simple game. Write a function called winner and figure out who is going to win.
#They are dealt the same number of cards. They both flip the card on the top of their deck. Whoever has a card with higher value wins the round and gets one point (if the cards are of the same value, neither of them gets a point). After this, the two cards are discarded and they flip another card from the top of their deck. They do this until they have no cards left.
#deckSteve and deckJosh are arrays representing their decks. They are filled with cards, represented by a single character. The card rank is as follows (from lowest to highest):

def winner(deck_steve, deck_josh):
    steveWins = 0
    joshWins = 0
    nonNumbers = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    
    for i in range(len(deck_steve)):
        i -= 1
        if deck_steve[i] in nonNumbers: #check if any nonNumber cards that need to be converted were drawn by steve
            value = nonNumbers.get(deck_steve[i])
            deck_steve[i] = value
        if deck_josh[i] in nonNumbers: #check if any nonNumber cards that need to be converted were drawn by steve
            value = nonNumbers.get(deck_josh[i])
            deck_josh[i] = value
        if int(deck_steve[i]) > int(deck_josh[i]):
            steveWins += 1
        elif int(deck_steve[i]) < int(deck_josh[i]):
            joshWins += 1
    if steveWins > joshWins:
        return f"Steve wins {steveWins} to {joshWins}"
    elif joshWins > steveWins:
        return f"Josh wins {joshWins} to {steveWins}"
    else:    
        return "Tie"
