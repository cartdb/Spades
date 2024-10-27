import pygame
backside = pygame.image.load("png/back-side.png")
c2 = pygame.image.load("png/2_of_clubs.png")
d2 = pygame.image.load("png/2_of_diamonds.png")
h2 = pygame.image.load("png/2_of_hearts.png")
s2 = pygame.image.load("png/2_of_spades.png")
c3 = pygame.image.load("png/3_of_clubs.png")
d3 = pygame.image.load("png/3_of_diamonds.png")
h3 = pygame.image.load("png/3_of_hearts.png")
s3 = pygame.image.load("png/3_of_spades.png")
c4 = pygame.image.load("png/4_of_clubs.png")
d4 = pygame.image.load("png/4_of_diamonds.png")
h4 = pygame.image.load("png/4_of_hearts.png")
s4 = pygame.image.load("png/4_of_spades.png")
c5 = pygame.image.load("png/5_of_clubs.png")
d5 = pygame.image.load("png/5_of_diamonds.png")
h5 = pygame.image.load("png/5_of_hearts.png")
s5 = pygame.image.load("png/5_of_spades.png")
c6 = pygame.image.load("png/6_of_clubs.png")
d6 = pygame.image.load("png/6_of_diamonds.png")
h6 = pygame.image.load("png/6_of_hearts.png")
s6 = pygame.image.load("png/6_of_spades.png")
c7 = pygame.image.load("png/7_of_clubs.png")
d7 = pygame.image.load("png/7_of_diamonds.png")
h7 = pygame.image.load("png/7_of_hearts.png")
s7 = pygame.image.load("png/7_of_spades.png")
c8 = pygame.image.load("png/8_of_clubs.png")
d8 = pygame.image.load("png/8_of_diamonds.png")
h8 = pygame.image.load("png/8_of_hearts.png")
s8 = pygame.image.load("png/8_of_spades.png")
c9 = pygame.image.load("png/9_of_clubs.png")
d9 = pygame.image.load("png/9_of_diamonds.png")
h9 = pygame.image.load("png/9_of_hearts.png")
s9 = pygame.image.load("png/9_of_spades.png")
Tc = pygame.image.load("png/10_of_clubs.png")
Td = pygame.image.load("png/10_of_diamonds.png")
Th = pygame.image.load("png/10_of_hearts.png")
Ts = pygame.image.load("png/10_of_spades.png")
Jc = pygame.image.load("png/jack_of_clubs.png")
Jd = pygame.image.load("png/jack_of_diamonds.png")
Jh = pygame.image.load("png/jack_of_hearts.png")
Js = pygame.image.load("png/jack_of_spades.png")
Qc = pygame.image.load("png/queen_of_clubs.png")
Qd = pygame.image.load("png/queen_of_diamonds.png")
Qh = pygame.image.load("png/queen_of_hearts.png")
Qs = pygame.image.load("png/queen_of_spades.png")
Kc = pygame.image.load("png/king_of_clubs.png")
Kd = pygame.image.load("png/king_of_diamonds.png")
Kh = pygame.image.load("png/king_of_hearts.png")
Ks = pygame.image.load("png/king_of_spades.png")
Ac = pygame.image.load("png/ace_of_clubs.png")
Ad = pygame.image.load("png/ace_of_diamonds.png")
Ah = pygame.image.load("png/ace_of_hearts.png")
As = pygame.image.load("png/ace_of_spades.png")
bj = pygame.image.load("png/black_joker.png")
rj = pygame.image.load("png/red_joker.png")
def cardDeck(screen_width, screen_height, screen):
    x = 0
    y = screen_height * 0.3
    cardImg = pygame.transform.scale(backside, (screen_width * 0.1, screen_height * 0.375))
    screen.blit(cardImg, (x, y))
def card(type, player, num, cards, screen_width, screen_height, screen, currentCard=[], arr=[], draw="", tricks=int(), tricks2=int(), bid=int(), bid2=int()):
    facedown = True
    (mousex, mousey) = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()[0]
    types = list(type)
    try:
        characters = list(currentCard[len(currentCard) - 1])
        facedown = True
        if types[1] == 's' and characters[1] != 's' and characters[1] != 'j' or types[1] == 'j':
            facedown = False
        elif characters[1] == types[1]:
            for card in range(len(cards)):
                if characters[0] in cards[card]:
                    characters = card
                    break
            for card in range(len(cards)):
                if types[0] in cards[card]:
                    types = card
                    break
            if types > characters:
                facedown = False
    except:
        pass
    if player == 0:
        facedown = False
    if cards[0] == type:
        cardImg = c2
    elif cards[1] == type:
        cardImg = d2
    elif cards[2] == type:
        cardImg = h2
    elif cards[3] == type:
        cardImg = s2
    elif cards[4] == type:
        cardImg = c3
    elif cards[5] == type:
        cardImg = d3
    elif cards[6] == type:
        cardImg = h3
    elif cards[7] == type:
        cardImg = s3
    elif cards[8] == type:
        cardImg = c4
    elif cards[9] == type:
        cardImg = d4
    elif cards[10] == type:
        cardImg = h4
    elif cards[11] == type:
        cardImg = s4
    elif cards[12] == type:
        cardImg = c5
    elif cards[13] == type:
        cardImg = d5
    elif cards[14] == type:
        cardImg = h5
    elif cards[15] == type:
        cardImg = s5
    elif cards[16] == type:
        cardImg = c6
    elif cards[17] == type:
        cardImg = d6
    elif cards[18] == type:
        cardImg = h6
    elif cards[19] == type:
        cardImg = s6
    elif cards[20] == type:
        cardImg = c7
    elif cards[21] == type:
        cardImg = d7
    elif cards[22] == type:
        cardImg = h7
    elif cards[23] == type:
        cardImg = s7
    elif cards[24] == type:
        cardImg = c8
    elif cards[25] == type:
        cardImg = d8
    elif cards[26] == type:
        cardImg = h8
    elif cards[27] == type:
        cardImg = s8
    elif cards[28] == type:
        cardImg = c9
    elif cards[29] == type:
        cardImg = d9
    elif cards[30] == type:
        cardImg = h9
    elif cards[31] == type:
        cardImg = s9
    elif cards[32] == type:
        cardImg = Tc
    elif cards[33] == type:
        cardImg = Td
    elif cards[34] == type:
        cardImg = Th
    elif cards[35] == type:
        cardImg = Ts
    elif cards[36] == type:
        cardImg = Jc
    elif cards[37] == type:
        cardImg = Jd
    elif cards[38] == type:
        cardImg = Jh
    elif cards[39] == type:
        cardImg = Js
    elif cards[40] == type:
        cardImg = Qc
    elif cards[41] == type:
        cardImg = Qd
    elif cards[42] == type:
        cardImg = Qh
    elif cards[43] == type:
        cardImg = Qs
    elif cards[44] == type:
        cardImg = Kc
    elif cards[45] == type:
        cardImg = Kd
    elif cards[46] == type:
        cardImg = Kh
    elif cards[47] == type:
        cardImg = Ks
    elif cards[48] == type:
        cardImg = Ac
    elif cards[49] == type:
        cardImg = Ad
    elif cards[50] == type:
        cardImg = Ah
    elif cards[51] == type:
        cardImg = As
    elif cards[52] == type:
        cardImg = bj
    elif cards[53] == type:
        cardImg = rj
    if player == 0:
        y = 0
    elif player == 1:
        y = screen_height * 0.675
    elif player == 2:
        y = screen_height * 0.3
    if num == -1:
        x = screen_width * 0.1
    else:
        x = (screen_width / len(arr)) * num
    if player == 0 or facedown == True and num != -1:
        cardImg = backside
    if draw == "spades":
        if facedown == False and player == 0:
            x = screen_width * 0.1
            y = screen_height * 0.3
            num = -1
            type2 = type
            currentCard.append(type)
            arr.remove(type2)
        elif facedown == False and player == 1 and pressed == True and mousex >= x and mousex <= x + (screen_width / len(arr)) and mousey >= y and mousey <= y + (screen_height * 0.3):
            x = screen_width * 0.1
            y = screen_height * 0.3
            num = -1
            type2 = type
            currentCard.append(type)
            arr.remove(type2)
            if tricks < bid * 10:
                tricks += 10
            else:
                tricks += 1
        elif mousex >= 0 and mousex <= screen_width * 0.1 and mousey >= screen_height * 0.3 and mousey <= screen_height * 0.675 and pressed == True and facedown == True:
            x = screen_width * 0.1
            y = screen_height * 0.3
            num = -1
            type2 = type
            currentCard.append(type)
            arr.remove(type2)
            if tricks2 < bid2 * 10:
                tricks2 += 10
            else:
                tricks2 += 1
    if num != -1:
        if len(arr) != 0:
            cardImg = pygame.transform.scale(cardImg, (screen_width / len(arr), screen_height * 0.3))
        else:
            cardImg = pygame.transform.scale(cardImg, (screen_width * 0.1, screen_height * 0.375))
    else:
        if len(arr) != 0:
            cardImg = pygame.transform.scale(cardImg, (screen_width / len(arr), screen_height * 0.375))
        else:
            cardImg = pygame.transform.scale(cardImg, (screen_width * 0.1, screen_height * 0.375))
    screen.blit(cardImg, (x, y))
    return tricks, tricks2