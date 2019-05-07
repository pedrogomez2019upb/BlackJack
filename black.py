#Para este proyecto vamos a importar lo que es una libreria llamada random la cual tiene una funcion llamada shuffle
#la cual nos permite mexclar las cartas
from random import shuffle
# Definimos mediante un rango de 2 a 11 los ranks y suits
ranks = [_ for _ in range(2, 11)] + ['J', 'Q', 'K', 'A']
suits = ['SPADE', 'HEART ', 'DIAMOND', 'CLUB']

#Planteamos una definición para que creémos una nueva baraja de cartas
def get_deck():
    #Retornará el valor de las barajas
    return [[rank, suit] for rank in ranks for suit in suits]

#Gracias a la función de la vez pasada , mezclamos la baraja
deck = get_deck()
shuffle(deck)

# Creamos una valor booleano para establecer cuando el jugador sigue vivo o no
player_in = True

# Distribuimos las cartas a los dos jugadores
player_hand = [deck.pop(), deck.pop()]
dealer_hand = [deck.pop(), deck.pop()]


def card_value(card):
    #Retornamos el valor de una sola carta
    rank = card[0]
    if rank in ranks[0:-4]:
        return int(rank)
    elif rank is 'A':
        return 11
    else:
        return 10


def hand_value(hand):
    """Returns the integer value of a set of cards."""
    #Vamos sumando de a poco el valor de las cartas
    tmp_value = sum(card_value(_) for _ in hand)
    # Count the number of Aces in the hand.
    num_aces = len([_ for _ in hand if _[0] is 'A'])

    #Como "A" puede llegar de 1 a 11 ,entonces nos toca ir revisando 
    while num_aces > 0:

        if tmp_value > 21 and 'A' in ranks:
            tmp_value -= 10
            num_aces -= 1
        else:
            break

    #Retorna un string del valor de la baraja . Si sobre pasa , retorna 100
    if tmp_value < 21:
        return [str(tmp_value), tmp_value]
    elif tmp_value == 21:
        return ['Blackjack!', 21]
    else:
        return ['Bust!', 100]

#Siempre y cuando el jugador siga en el juego , le preguntamos si quiere recibir alguna otra carta 
while player_in:
    # Mostramos la baraja del jugador al igual que la cantidad que tiene
    current_score_str = '''\nYou are currently at %s\nwith the hand %s\n'''
    print (current_score_str % (hand_value(player_hand)[0], player_hand))
    # Si ya sobrepaso los 21 , dejar de preguntarle al jugador si sigue
    if hand_value(player_hand)[1] == 100:
        break

    if player_in:
        response = int(input('Hit or stay? (Hit = 1, Stay = 0)'))
        #Si el jugador pide seguir , coger la primera carta y ponerla en su baraja, si no retornamos False y
        #nos devolvemos a la baraja del dealer
        if response:
            player_in = True
            new_player_card = deck.pop()
            player_hand.append(new_player_card)
            print ('You draw %s' % new_player_card)
        else:
            player_in = False

player_score_label, player_score = hand_value(player_hand)
dealer_score_label, dealer_score = hand_value(dealer_hand)

if player_score <= 21:
    dealer_hand_string = '''\nDealer is at %s\nwith the hand %s\n'''
    print (dealer_hand_string % (dealer_score_label, dealer_hand))

while hand_value(dealer_hand)[1] < 17 and player_score <= 21:
    new_dealer_card = deck.pop()
    dealer_hand.append(new_dealer_card)
    print ('Dealer draws %s' % new_dealer_card)

dealer_score_label, dealer_score = hand_value(dealer_hand)

if player_score == 100:
    print ('Dealer wins!')
elif player_score < 100 and dealer_score == 100:
    print ('You beat the dealer!')
elif player_score > dealer_score:
    print ('You beat the dealer!')
elif player_score == dealer_score:
    print ('You tied the dealer, nobody wins.')
elif player_score < dealer_score:
    print ("Dealer wins!")

#Developed by Pedro Gómez / ID:000396221