'''
Created on Nov 14, 2013

@author: Deuvarney
'''
import pygame, random
from pygame.locals import *
from sys import exit

pygame.init()

CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
cards_file = 'cards.png'

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_backs_file = 'card_back.png'

frame = pygame.display.set_mode((600,525), 0, 32)
card_backs = pygame.image.load(card_backs_file).convert()
card_images = pygame.image.load(cards_file).convert()

#mouse_over_sound = pygame.mixer.music.load("sound_effects/multimedia_rollover_078.mp3")
mouse_over_sound = pygame.mixer.Sound("switch4.wav")
mouse_over_sound.set_volume(.5)


# initialize some useful global variables
in_play = False
outcome = ""
score = 0
color = (0,255,255)

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5,
          '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print("Invalid card: ", suit, rank)

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images,
                          card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], 
                                                pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.pHand=[]

    def __str__(self):
        return str(self.pHand)    # return a string representation of a hand

    def add_card(self, card):
        return self.pHand.append(str(card))
        
    def get_value(self):
            # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        pHandValue = 0
        point = 0
        aceList = []
        for hand in self.pHand:
            pHandValue+= VALUES[hand[1]]
            if (hand[1] == 'A'):
                aceList.append(hand)
        for hand in aceList:
            if ((pHandValue + 10) <= 21):
                pHandValue +=10            
        return pHandValue
            # compute the value of the hand, see Blackjack video

    def draw(self, pos):
        # draw a hand on the canvas, use the draw method for cards
        n=0
        constant = 100
        if len(self.pHand) == 6:
            pos[0] = 25
            constant = 95
        elif len(self.pHand) == 7:
            pos[0] = 10
            constant = 85
        else:
            pos[0] = 100
            constant = 100
            
            
        for card in self.pHand:
            card_loc = ( CARD_SIZE[0] * RANKS.index(self.pHand[n][1]), 
                    CARD_SIZE[1] * SUITS.index(self.pHand[n][0]))
        
        
            frame.blit(card_images, (pos[0]  + constant*n, pos[1]),   (card_loc, CARD_SIZE))  
            n+=1
            
'''
            card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.pHand[n][1]), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.pHand[n][0]))
        
        
            frame.blit(card_images, (pos[0] + CARD_CENTER[0] + 100*n, pos[1] + CARD_CENTER[1]),   (card_loc, CARD_SIZE))
'''
            
# define deck class 
class Deck:
    def __init__(self):
        self.cardies=[]
        for suit in SUITS:
            for rank in RANKS:
                self.cardies.append([suit, rank])

    def shuffle(self):
        return random.shuffle(self.cardies)

    def deal_card(self):
        cardie = self.cardies.pop()
        return Card(cardie[0], cardie[1])
    
    def __str__(self):
        return str(self.cardies)
        # return a string representing the deck

player_hand = Hand()
oppo_hand = Hand()
playing_deck = Deck()

'''
def deal():
    global outcome, in_play, color

    global player_hand, oppo_hand, player_deck

    playing_deck = Deck()
    player_hand = Hand()
    oppo_hand = Hand()
    
    playing_deck.shuffle()
    print playing_deck
    outcome = ""    
    
    player_hand.add_card(playing_deck.deal_card())
    oppo_hand.add_card(playing_deck.deal_card())
    player_hand.add_card(playing_deck.deal_card()) 
    in_play = True
    if (player_hand.get_value() == 21):
        stand() #########################################
        outcome = "Player Wins :)"
        in_play= False
        color = (0,255,255)
    
    
    print "Player hand",player_hand, player_hand.get_value() 
    #oppo_hand.add_card(playing_deck.deal_card())
    #oppo_hand.add_card(playing_deck.deal_card())
    print "Opponent Hand", oppo_hand, oppo_hand.get_value()
    

    # your code goes here
'''
def deal():  
    global outcome, in_play, color

    global player_hand, oppo_hand, playing_deck

    playing_deck = Deck()
    player_hand = Hand()
    oppo_hand = Hand()
    print(playing_deck)
    playing_deck.shuffle()
    print(playing_deck)
    outcome = ""    
    
    player_hand.add_card(playing_deck.deal_card())
    oppo_hand.add_card(playing_deck.deal_card())
    player_hand.add_card(playing_deck.deal_card()) 
    
    in_play = True
    
    if (player_hand.get_value() == 21):
        stand()
        
           
    print("Player hand",player_hand, player_hand.get_value())
    #oppo_hand.add_card(playing_deck.deal_card())
    #oppo_hand.add_card(playing_deck.deal_card())
    print("Opponent Hand", oppo_hand, oppo_hand.get_value())

'''      
def hit():
    global outcome, in_play, color
        # replace with your code below
    if (in_play ==True):    
        player_hand.add_card(playing_deck.deal_card())
        print "Player" + str(player_hand.get_value())
        
        if (player_hand.get_value() > 21):
            outcome = "You've busted"
            in_play = False
            color = (250,0,00)
        if (player_hand.get_value() == 21):
            stand()
            
'''
def hit():   
    global outcome, in_play, color
    
    global player_hand, oppo_hand, playing_deck
        # replace with your code below
    if (in_play ==True):    
        player_hand.add_card(playing_deck.deal_card())
        print("Player" + str(player_hand.get_value()))
        
        if (player_hand.get_value() > 21):
            outcome = "You've busted"
            in_play = False
            color = (250,0,0)
         
        if (player_hand.get_value() == 21):
            stand()  
             
def stand():
    global in_play, outcome, color
    
    global player_hand, oppo_hand, playing_deck

        # replace with your code below
    #while (in_play == True) &
    if (in_play == True):
        if(oppo_hand.get_value() <= player_hand.get_value()):
            if(oppo_hand.get_value() <= 17):
                while(oppo_hand.get_value() <= player_hand.get_value()):
                    if (oppo_hand.get_value() < 17):
                   # if (oppo_hand.get_value() < player_hand.get_value()):
                        oppo_hand.add_card(playing_deck.deal_card())
                    if (oppo_hand.get_value() >= 17):
                        break
    else:
        pass

    if (in_play == True):
        if (oppo_hand.get_value() <= 21):
            if (oppo_hand.get_value() > player_hand.get_value()): #&& if (oppo_hand.get_value() >= player_hand.get_value()):
                outcome="Computer Wins :("
                color = (250,0,0)
            if (oppo_hand.get_value() == player_hand.get_value()):
                outcome="Draw"
                color = (255,255,255)
            if (oppo_hand.get_value() < player_hand.get_value()):
                outcome="Player Wins :)"
                color = (0,255,255)
        else:
            outcome="Player Wins :)"
            color = (0,255,255)
 
    in_play = False
            
'''    
def stand():
    global in_play, outcome, color
        # replace with your code below
    #while (in_play == True) &
    if (in_play == True):
        if(oppo_hand.get_value() <= player_hand.get_value()):
            if(oppo_hand.get_value() <= 17):
                while(oppo_hand.get_value() < 17):
                    if(oppo_hand.get_value() < player_hand.get_value()):
                   # if (oppo_hand.get_value() < player_hand.get_value()):
                        oppo_hand.add_card(playing_deck.deal_card())

        print oppo_hand.get_value()
   
        if (oppo_hand.get_value() <= 21):
            if (oppo_hand.get_value() > player_hand.get_value()): #&& if (oppo_hand.get_value() >= player_hand.get_value()):
                outcome="Computer Wins :("
                color = (250,0,0)
            if (oppo_hand.get_value() == player_hand.get_value()):
                outcome="Draw"
                color = (255,255,255)
        else:
            outcome="Player Wins :)"
            color = (0,255,255)
 
    in_play = False 
    print outcome
    

# draw handler    
def draw(canvas):
    global oppon, player
    player_hand.draw(canvas, [100, 400])# test to make sure that card.draw works, replace with your code below
    canvas.draw_image(card_back, (CARD_BACK_CENTER), (CARD_BACK_SIZE), (237,149), (70, 100))
    oppo_hand.draw(canvas, [100, 100])
    #canvas.draw_text(outcome, [250, 300], 20, color)
    #canvas.draw_text("Player Hand Count: " + str(player_hand.get_value()), [125,550], 15, "Blue")
    #canvas.draw_text("Computer Hand Count: " + str(oppo_hand.get_value()), [125,50], 15, "Blue")
'''
play_number = 0
def sound_control(number):
    global play_number
    if number == 0:
        play_number = 0
    if number == 1:
        play_number += 1
    if play_number == 2:
        mouse_over_sound.play()
        
play_number2 = 0
def sound_control2(number):
    global play_number2
    if number == 0:
        play_number2 = 0
    if number == 1:
        play_number2 += 1
    if play_number2 == 2:
        mouse_over_sound.play()
        
play_number3 = 0
def sound_control3(number):
    global play_number3
    if number == 0:
        play_number3 = 0
    if number == 1:
        play_number3 += 1
    if play_number3 == 2:
        mouse_over_sound.play()        

deal_pos = (100,445)
hit_pos = (250, 445)
stand_pos = (400, 445)
rect_end_pos = (75, 50)

#For when mouse is positioned over the buttons
deal_pos_over = (105,450)
hit_pos_over = (255, 450)
stand_pos_over = (405, 450)

outcome_text = pygame.font.SysFont('arial', 20)
#.draw_text(outcome, [250, 300], 20, color)
hand_count_text = pygame.font.SysFont('arial', 15)
#, size, bold, italic)canvas.draw_text("Player Hand Count: " + str(player_hand.get_value()), [125,550], 15, "Blue")
#canvas.draw_text("Computer Hand Count: " + str(oppo_hand.get_value()), [125,50], 15, "Blue")


deal()

#Button Colors
button_red = (200, 0, 0)
button_yellow = (200, 200, 0)
button_blue = (0,0,200)
color_gray = (150, 150, 150)
dark_gray = (100,100,100)

while True:
    
    #player_hand.draw([100, 400])
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == MOUSEBUTTONUP:
            pl = pygame.mouse.get_pos()
            #Deal Button
            if (pl[0] >= deal_pos[0] and pl[0] <= deal_pos[0] + rect_end_pos[0]) and (pl[1] >= deal_pos[1] and pl[1] <= deal_pos[1] + rect_end_pos[1]):
                print("Deal Button pressed")
                deal()
            #Hit Button
            elif (pl[0] >= hit_pos[0] and pl[0] <= hit_pos[0] + rect_end_pos[0]) and (pl[1] >= hit_pos[1] and pl[1] <= hit_pos[1] + rect_end_pos[1]):
                hit()    
                print("Hit Button pressed")
            #Stand Button      
            elif  (pl[0] >= stand_pos[0] and pl[0] <= stand_pos[0] + rect_end_pos[0]) and (pl[1] >= stand_pos[1] and pl[1] <= stand_pos[1] + rect_end_pos[1]):              
                stand()
                print("Stand Button pressed")
                
    mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos() #Getting mouse position for button color change and movement when mouse over
    #Deal Button 
    
    if (mouse_pos_x >= deal_pos[0] and mouse_pos_x <= deal_pos[0] + rect_end_pos[0]) and (mouse_pos_y >= deal_pos[1] and mouse_pos_y  <= deal_pos[1] + rect_end_pos[1]):
        button_blue = color_gray
        deal_pos = deal_pos_over
        sound_control(1)
        #mouse_over_sound.play(0)
    else:
        button_blue = (0,0,200)
        deal_pos = (100,445)
        sound_control(0)   
    #Hit button
    if in_play:
        if (mouse_pos_x >= hit_pos[0] and mouse_pos_x <= hit_pos[0] + rect_end_pos[0]) and (mouse_pos_y >= hit_pos[1] and mouse_pos_y <= hit_pos[1] + rect_end_pos[1]):
            button_red = color_gray
            hit_pos = hit_pos_over
            sound_control2(1)
            #mouse_over_sound.play()
        else:
            button_red = (200, 0, 0)
            hit_pos = (250, 445)
            sound_control2(0)
    #Stand button

        if (mouse_pos_x >= stand_pos[0] and mouse_pos_x <= stand_pos[0] + rect_end_pos[0]) and (mouse_pos_y >= stand_pos[1] and mouse_pos_y <= stand_pos[1] + rect_end_pos[1]):
            button_yellow = color_gray
            stand_pos = stand_pos_over
            sound_control3(1)
            #mouse_over_sound.play()
        else:
            button_yellow = (200, 200, 0)
            stand_pos = (400, 445)
            sound_control3(0)
    else:
        button_red = dark_gray
        hit_pos = (250, 445)
        sound_control2(0)
        button_yellow = dark_gray
        stand_pos = (400, 445)
        sound_control3(0)
    
     
    
    #Draw objects to the frame                        
    frame.fill((0,200,0))    
    frame.blit(card_backs, (400,185))     
    #frame.blit(card_images, (200, 200), (CARD_SIZE[0]*12, CARD_SIZE[1]*0, 73, 98))
    
    deal_button = pygame.draw.rect(frame, button_blue, Rect((deal_pos),rect_end_pos))
    hit_button = pygame.draw.rect(frame, button_red, Rect(hit_pos,rect_end_pos))
    stand_button = pygame.draw.rect(frame, button_yellow, Rect(stand_pos, rect_end_pos))
    
    #Draw hands
    player_hand.draw([50, 300])# test to make sure that card.draw works, replace with your code below    
    oppo_hand.draw([50, 65])
    
    #Draw fonts
    frame.blit(outcome_text.render(outcome, True, color),(175,225))
    frame.blit(hand_count_text.render("Player Hand Count: " + str(player_hand.get_value()), True, (0,0,250)),(125,420))
    frame.blit(hand_count_text.render("Computer Hand Count: " + str(oppo_hand.get_value()), True, (0,0,250)),(125,25))
    
    frame.blit(hand_count_text.render("Deal", True, (255,255,255)), (deal_pos[0] + 15, deal_pos[1] + 15) )
    frame.blit(hand_count_text.render("Hit", True, (255,255,255)), (hit_pos[0] + 15, hit_pos[1] + 15) )
    frame.blit(hand_count_text.render("Stand", True, (255,255,255)), (stand_pos[0] + 15, stand_pos[1] + 15) )    
    pygame.display.update()
    
    
    