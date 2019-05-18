#Para este proyecto vamos a importar lo que es una libreria llamada random la cual tiene una funcion llamada shuffle
#la cual nos permite mexclar las cartas
from random import shuffle
# Definimos mediante un rango de 2 a 11 los ranks y suits
ranks = [_ for _ in range(2, 11)] + ['J', 'Q', 'K', 'A']
suits = ['♠', '♥', '♦', '♣']
def blackjack_game():
 #Este try and except lo creamos en el caso hipotetico que el usuario cometiera un error de digitacion
 try:
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
            response = int(input('Hit or stay? (Hit = 1, Stay = 0): '))
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

    restart=input("Want to play again?, Yes/No: ")
    if restart.lower()=="yes":
        blackjack_game()
    else:
        print("Thanks for playing, have a nice day.")
 except:
     print("You have done something wrong")
     error=input("Want to restart the game? yes/no: ")
     #En el posible caso que el error ocurra, se le imprimira una opcion de volver a intentarlo para que el usuario no se que anodado a la situacion de error
     if error.lower()=="yes":
         if start.lower() == "yes":
             blackjack_game()
         # Si la persona llegara a decir que no, se le imprimiria un mensaje
         else:
             print("Have a good day.")
     else:
         print("Ok, you can leave now.")



#Esta variable la creamos para que la persona al entrar a jugar sepa a que estara participando y le de opcion de participar.

start=input("You want to play some blackjack?: Yes/No: ")
#Si la persona llegara a cometer el error de escribir algo aparte de lo pedido, le reiterara que debe escribirlo bien.
if start.lower()!="yes" and start.lower()!="no":
    while start.lower()!="yes" and start.lower()!="no":
        start=input("Please write yes or no: ")


#Si la persona llegara a aceptar, comenzaria todo el proceso de nuestra funcion.
if start.lower()=="yes":
        blackjack_game()
#Si la persona llegara a decir que no, se le imprimiria un mensaje
else:
    print("Have a good day.")



#Developed by Pedro Felipe Gomez Bonilla/ ID:000396221
#and Camilo Andres Serrano Pertuz/ ID: 000404139
