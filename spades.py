import pyautogui
import pygame
import random
from func import card
from func import cardDeck
pygame.init()
screen_width, screen_height = pyautogui.size()
screen_height = screen_height - 60
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True
cards = ['2c', '2d', '2h', '2s', '3c', '3d', '3h', '3s', '4c', '4d', '4h', '4s', '5c', '5d', '5h', '5s', '6c', '6d', '6h', '6s', '7c', '7d', '7h', '7s', '8c', '8d', '8h', '8s', '9c', '9d', '9h', '9s', 'Tc', 'Td', 'Th', 'Ts', 'Jc', 'Jd', 'Jh', 'Js', 'Qc', 'Qd', 'Qh', 'Qs', 'Kc', 'Kd', 'Kh', 'Ks', 'Ac', 'Ad', 'Ah', 'As', 'bj', 'rj']
deck = ['2c', '2d', '2h', '2s', '3c', '3d', '3h', '3s', '4c', '4d', '4h', '4s', '5c', '5d', '5h', '5s', '6c', '6d', '6h', '6s', '7c', '7d', '7h', '7s', '8c', '8d', '8h', '8s', '9c', '9d', '9h', '9s', 'Tc', 'Td', 'Th', 'Ts', 'Jc', 'Jd', 'Jh', 'Js', 'Qc', 'Qd', 'Qh', 'Qs', 'Kc', 'Kd', 'Kh', 'Ks', 'Ac', 'Ad', 'Ah', 'As', 'bj', 'rj']
random.shuffle(deck)
player1 = []
player2 = []
trick1 = random.randint(1, 26)
trick2 = 27 - trick1
pts1 = 0
pts2 = 0
pts1Gained = 0
pts2Gained = 0
count = 0
while count < 27:
    player1.append(deck[count])
    count += 1
while count < 54:
    player2.append(deck[count])
    count += 1
del deck[:54]
currentCard = []
turn = False
while running:
    if len(player1) == 0 and len(player2) == 0:
        if pts1Gained < trick1 * 10:
            pts1Gained = 0
        if pts2Gained < trick2 * 10:
            pts2Gained = 0
        pts1 += pts1Gained
        pts2 += pts2Gained
        deck = ['2c', '2d', '2h', '2s', '3c', '3d', '3h', '3s', '4c', '4d', '4h', '4s', '5c', '5d', '5h', '5s', '6c', '6d', '6h', '6s', '7c', '7d', '7h', '7s', '8c', '8d', '8h', '8s', '9c', '9d', '9h', '9s', 'Tc', 'Td', 'Th', 'Ts', 'Jc', 'Jd', 'Jh', 'Js', 'Qc', 'Qd', 'Qh', 'Qs', 'Kc', 'Kd', 'Kh', 'Ks', 'Ac', 'Ad', 'Ah', 'As', 'bj', 'rj']
        random.shuffle(deck)
        player1 = []
        player2 = []
        trick1 = random.randint(1, 26)
        trick2 = 27 - trick1
        pts1Gained = 0
        pts2Gained = 0
        count = 0
        while count < 27:
            player1.append(deck[count])
            count += 1
        while count < 54:
            player2.append(deck[count])
            count += 1
        del deck[:54]
        currentCard = []
        turn = False
    (mousex, mousey) = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()[0]
    deck2 = []
    for entrys in range(len(cards)):
        deck2.append(cards[entrys])
    random.shuffle(deck2)
    for entrys in range(len(deck2)):
        deck.append(deck2[entrys])
    facedown2 = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("white")
    if turn == True:
        for entry in range(len(player1)):
            length = len(player1)
            (pts1Gained, pts2Gained) = card(player1[entry], 1, entry, cards, screen_width, screen_height, screen, currentCard, player1, "spades", pts1Gained, pts2Gained, trick1, trick2)
            if len(player1) != length:
                turn = False
                break
    elif turn == False:
        for entry in range(len(player2)):
            length = len(player2)
            (pts1Gained, pts2Gained) = card(player2[entry], 0, entry, cards, screen_width, screen_height, screen, currentCard, player2, "spades", pts1Gained, pts2Gained, trick1, trick2)
            if len(player2) != length:
                turn = True
                facedown2 = 0
                break
            facedown2 += 1
    card(currentCard[len(currentCard) - 1], 2, -1, cards, screen_width, screen_height, screen)
    cardDeck(screen_width, screen_height, screen)
    for entry in range(len(player1)):
        card(player1[entry], 1, entry, cards, screen_width, screen_height, screen, currentCard, player1)
    for entry in range(len(player2)):
        card(player2[entry], 0, entry, cards, screen_width, screen_height, screen, currentCard, player2)
    pygame.display.flip()
    clock.tick(10)
pygame.quit()
print("Player 1: " + str(pts1))
print("Player 2: " + str(pts2))
