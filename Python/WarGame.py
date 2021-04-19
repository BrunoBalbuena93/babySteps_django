from random import shuffle
import itertools
palo = "C D P T".split()
rank = "2 3 4 5 6 7 8 9 10 J Q K A".split()


def shuffleDeck():
    # Función para barajear y repartir
    deck = list(itertools.product(rank, palo))
    shuffle(deck)
    return deck[:26], deck[26:]
        

def compareCards(card1, card2):
    # Compare the cards. First cast them
    cards = []
    for value in [card1, card2]:
        try:
            cards.append(int(value[0]))
        except ValueError:
            if "J" in value[0]: cards.append(11)
            elif "Q" in value[0]:   cards.append(12)
            elif "K" in value[0]:   cards.append(13)
            else:   cards.append(14)
    if cards[0] > cards[1]:
        return 1
    elif cards[0] < cards[1]:
        return 2
    else:
        return 0


class Player:
    def __init__(self, N, hand):
        # Debe tener una mano este usuario
        self.name = N
        self.hand = hand
    

    def remainingCards(self):
        return len(self.hand)


    def drawCard(self):
        self.card = self.hand.pop(0)
        return self.card

    def draw3Cards(self):
        self.card = [self.hand.pop(0) for i in range(3)]
        return self.card[-1]

    def addCards(self, card):
        # Agrega cartas 
        if type(card) is tuple:
            # En caso que solo sea una
            self.hand.append(card)
        else:
            # Mas de una carta
            self.hand.extend(card)

    
    def currentCard(self):
        return self.card


    def giveCard(self):
        card = self.card
        self.card = None
        return card


    def turn(self):
        return "{}: {} {}".format(self.name, self.card[0], self.card[1])


if __name__ == "__main__":
    p1 = input("Dame el jugador 1: ")
    p2 = input("Dame el jugador 2: ")
    print("Revolviendo el deck...")
    h1, h2 = shuffleDeck()
    # Generando usuarios
    P1 = Player(p1, h1)
    P2 = Player(p2, h2)

    while P1.remainingCards() > 10 and P2.remainingCards() > 10:
        for player in [P1, P2]:
            # if player.name == p1:
            #     input("presiona para sacar una carta: ")
            player.drawCard()
        result = compareCards(P1.currentCard(), P2.currentCard())
        if result == 1:
            # Gano el primero
            print("Ganó {}  {}  {}".format(P1.name, P1.turn(), P2.turn()))
            P1.addCards([P2.giveCard(), P1.giveCard()])
        elif result == 2:
            # Gano el segundo
            print("Ganó {}  {}  {}".format(P2.name, P1.turn(), P2.turn()))
            P2.addCards([P1.giveCard(), P2.giveCard()])
        else:
            #Empate
            print(P1.turn() + "  " + P2.turn())
            input("Empate, hay que volver a sacar, presiona para continuar ")
            result = compareCards(P1.draw3Cards(), P2.draw3Cards())
            if result == 1:
                # Gano el primero
                print("Ganó {}".format(P1.name))
                P1.addCards([P2.giveCard(), P1.giveCard()])
            elif result == 2:
                # Gano el segundo
                print("Ganó {}".format(P2.name))
                P2.addCards([P1.giveCard(), P2.giveCard()])

        print("{}: {}, {}:{}".format(p1, P1.remainingCards(), p2, P2.remainingCards()))

        

