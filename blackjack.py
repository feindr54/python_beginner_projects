import random
#from IPython.display import clear_output
"""
CODE FOR A GAME OF BLACKJACK
"""
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three': 3, 'Four': 4, 'Five':5, 'Six': 6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

game_on = True
player_turn = True
dealer_turn = False

class Card:
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]
    
    def __str__(self):
         return f"{self.rank} of {self.suit}" 
    
class Deck:
    
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(rank, suit))
        
    def deal(self, player):
        player.hand.append(deck.all_cards.pop())
    
    def shuffle(self, amount = 1):
        for num in range(amount):
            random.shuffle(self.all_cards)
    
class Player:
    
    def __init__(self, name = "Player", balance = 20):
        self.name = name
        self.balance = balance
        self.hand = []
        self.sum_of_hand = 0
    
    #drawing a card
    def hit(self, deck):
        #clear_output()
        #print(f"{self.name} has chosen to hit.")
        self.hand.append(deck.all_cards.pop())
        
    def stand(self):
        global player_turn
        print(f"{self.name} has chosen to stand.")
        print("\n" *2)
        player_turn = False
    
    def print_hand(self):
        print(f"You currently have {', '.join(list(map(str,self.hand)))}.")
        
    def amount_of_aces(self):
        aces = 0
        for card in self.hand:
            if card.rank == "Ace":
                aces += 1
        return aces
    
    def sum_of_cards(self):
        #accepts a list only
        card_sum = 0

        for cards in self.hand:
            card_sum += cards.value
        
        #special condition: to determine the value of Ace: if there are enough aces to counter the "potentially" busted sum
        
        for i in range(self.amount_of_aces()):
            if card_sum > 21:
                card_sum -= 10
            else: 
                break
        
        return card_sum
    
    def input_bet(self):
        
        while True:
            bet = input(f"{self.name}, please input your bet. You currently have ${self.balance}.")
            
            if bet.isdigit():
                bet = int(bet)
                if bet <= self.balance:
                    print(f"{self.name} has bet ${bet}!")
                    print("\n" * 2)
                    return bet
                elif bet == 0:
                    print(f"$0 is not a valid input! Please input your bet again. You currently have ${self.balance}.")
                    continue
                    
                else:
                    #clear_output()
                    print(f"You don't have enough money to bet so much! Please input your bet again. You currently have ${self.balance}.")
                    continue
            else:
                #clear_output()
                print(f"That is not a number. Please input your bet again. You currently have ${self.balance}.")
                    
            
        
class AI(Player):
    def __init__(self, name = "Dealer"):
        Player.__init__(self)
        self.name = name
    def print_hand(self):
        print(f"The dealer currently have {', '.join(list(map(str,self.hand)))}.")    
    def hit(self, deck):
        #print(f"{self.name} has chosen to hit.")
        self.hand.append(deck.all_cards.pop())    
        
    def print_one_card(self):
        print(f"The dealer currently have {self.hand[0]}.")  

def player_choice(player):
    global player_turn
    global dealer_turn
    
    while True:
        
        choice = input("Do you want to hit or stand?")
        
        if choice.lower() == 'hit':
            
            player.hit(deck)
            print("\n"*2)
            print(f"Hit! You got the {str(player.hand[-1])}")
            player.print_hand()
            break
            
        elif choice.lower() == 'stand':
            player.stand()
            player_turn = False
            dealer_turn = True
            break
            
        else:
            
            print("Invalid response, please answer again. Hit or Stand?")
            
def game_on():
    global game_on
    while True:
        
        choice = input("Do you want to play again? Input Y or N.")
        
        if choice.lower() == 'y':
            print("\n" * 2)
            print("Another round of Blackjack begins.")
            break
            
        elif choice.lower() == 'n':
            
            print("Thank you for playing Blackjack by cx!")
            game_on = False
            break
            
        else:
            
            print("Invalid response, please answer again. Y or N?")

    

#sets up player and AI
player1 = Player("player1", 100)
ai = AI()

while game_on: #maybe game_on not needed
    #creates and shuffles deck
    deck = Deck()
    #reshuffles deck and redistributes cards
    deck.shuffle(20)
    
    #empty player and dealer hands
    player1.hand = []
    ai.hand = []
    
    #ask the player to input bet
    bet = player1.input_bet()
    
    #deal cards to player and AI
    deck.deal(player1)
    deck.deal(ai)
    deck.deal(player1)
    deck.deal(ai)
    
    #reset player and dealer turn
    player_turn = True
    dealer_turn = False
    
    #check if either player blackjacked/won
    if player1.sum_of_cards() == ai.sum_of_cards() == 21:
        player1.print_hand()
        ai.print_hand()
        print(f"Both {player1.name} and dealer got BlackJack!! {player1.name} will have his/her bet returned")
        

    elif player1.sum_of_cards() == 21:
        player1.print_hand()
        print(f"{player1.name} has Blackjack!! {player1.name} has won ${2 * bet}!!")
        player1.balance += 2*bet
        

    elif ai.sum_of_cards() == 21:
        player1.print_hand()
        ai.print_hand()
        print(f"The dealer has Blackjack!! {player1.name} has lost ${2 * bet}")
        player1.balance -= 2*bet
        

    else:
        #display the hand
        player1.print_hand()
        
        while player_turn:

            #gather and validate input
            ai.print_one_card()
            player_choice(player1)

            #check if bust
            if player1.sum_of_cards() > 21:
                print(f"{player1.name} has busted. {player1.name} has lost ${bet}")
                player1.balance -= bet
                player_turn = False
                break
            elif len(player1.hand) >= 5:
                print(f"{player1.name} has 5 cards!. {player1.name} has won ${bet}")
                player1.balance += bet
                player_turn = False
                break

        if dealer_turn:
            ai.print_hand() 

            #dealer will keep hitting till he busts or he beats the player, whichever comes first
            while ai.sum_of_cards() < 17:
                ai.hit(deck)
                ai.print_hand()
                
            else:
                if ai.sum_of_cards() > 21:
                    print(f"The dealer has busted. {player1.name} has won ${bet}")
                    player1.balance += bet
                    dealer_turn = False
                    
                elif ai.sum_of_cards() < player1.sum_of_cards():
                    print(f"{player1.name} has a higher card value. {player1.name} has won ${bet}")
                    player1.balance += bet
                    dealer_turn = False
                    
                elif ai.sum_of_cards() > player1.sum_of_cards():
                    print(f"The dealer has a higher card value! {player1.name} has lost ${bet}")
                    player1.balance -= bet
                    dealer_turn = False
                else:
                    print(f"It's a draw!! {player1.name} has his/her bet returned.")
                    dealer_turn = False
    game_on()