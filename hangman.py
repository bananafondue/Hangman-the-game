import pygame
import random


def imageloop(add):
    screen.blit(add, (50, 50))


def listtostring(s):
    list_to_string = " ".join(s)
    return list_to_string


def blank_display(text):
    myfont = pygame.font.SysFont("arial", 60)
    font_ob = myfont.render(text, True, black)
    screen.blit(font_ob, (460, 150))


def letter_display(text, position):
    myfont = pygame.font.SysFont("dokchampa", 24)
    font_ob = myfont.render(text, True, aqua)
    screen.blit(font_ob, position)

def tries(count):
    myfont = pygame.font.SysFont("dokchampa", 18)
    font_ob1 = myfont.render("Tries left:", True, small_violet)
    font_ob2 = myfont.render(str(count), True, small_violet)
    screen.blit(font_ob1, (0, 0))
    screen.blit(font_ob2, (75, 0))

def button(text, x, y, w, h, inactive, active):
    mouse = pygame.mouse.get_pos()  # 450, 450, 40, 40
    if x < mouse[0] < x + w and y < mouse[1] < y + h:
        pygame.draw.rect(screen, active, (x, y, w, h))  # x, y, width ,height
        event = pygame.event.wait()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                answer = text
                numb_of_letters = movie.count(answer)
                if numb_of_letters == 0:
                    pygame.draw.rect(screen, red, (x, y, w, h))
                    hangman.pop(0)
                    length_of_hangman = len(hangman)
                    global pictureno
                    pictureno = length_of_hangman

                else:
                    pygame.draw.rect(screen, green, (x, y, w, h))
                    ob = [i for i, a in enumerate(movie) if a == answer]
                    for tt in ob:
                        list[tt] = answer
                        blank_display(listtostring(list))
    else:
        pygame.draw.rect(screen, inactive, (x, y, w, h))

    letter_display(text, (x + 7, y + 7))


def intro_button(text, x, y, w, h, inactive, active, action = None):
    mouse = pygame.mouse.get_pos()  # 450, 450, 40, 40
    click = pygame.mouse.get_pressed()
    if x < mouse[0] < x + w and y < mouse[1] < y + h:
        pygame.draw.rect(screen, active, (x, y, w, h))  # x, y, width ,height
        if click[0] == 1 and action != None:
            if action == "PLAY":
                game_loop()
            elif action == "QUIT":
                pygame.quit()
                quit()
    else:
         pygame.draw.rect(screen, inactive, (x, y, w, h))

    letter_display(text, (x + 8, y + 8))

def button_loop():
    button("A", 450, 450, 40, 40, yellow, bright_yellow)
    button("B", 505, 450, 40, 40, yellow, bright_yellow)
    button("C", 560, 450, 40, 40, yellow, bright_yellow)
    button("D", 615, 450, 40, 40, yellow, bright_yellow)
    button("E", 670, 450, 40, 40, yellow, bright_yellow)
    button("F", 725, 450, 40, 40, yellow, bright_yellow)
    button("G", 780, 450, 40, 40, yellow, bright_yellow)
    button("H", 835, 450, 40, 40, yellow, bright_yellow)
    button("I", 890, 450, 40, 40, yellow, bright_yellow)
    button("J", 450, 505, 40, 40, yellow, bright_yellow)
    button("K", 505, 505, 40, 40, yellow, bright_yellow)
    button("L", 560, 505, 40, 40, yellow, bright_yellow)
    button("M", 615, 505, 40, 40, yellow, bright_yellow)
    button("N", 670, 505, 40, 40, yellow, bright_yellow)
    button("O", 725, 505, 40, 40, yellow, bright_yellow)
    button("P", 780, 505, 40, 40, yellow, bright_yellow)
    button("Q", 835, 505, 40, 40, yellow, bright_yellow)
    button("R", 890, 505, 40, 40, yellow, bright_yellow)
    button("S", 475, 560, 40, 40, yellow, bright_yellow)
    button("T", 530, 560, 40, 40, yellow, bright_yellow)
    button("U", 585, 560, 40, 40, yellow, bright_yellow)
    button("V", 640, 560, 40, 40, yellow, bright_yellow)
    button("W", 695, 560, 40, 40, yellow, bright_yellow)
    button("X", 750, 560, 40, 40, yellow, bright_yellow)
    button("Y", 805, 560, 40, 40, yellow, bright_yellow)
    button("Z", 860, 560, 40, 40, yellow, bright_yellow)


def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(welcome_blue)
        largetext = pygame.font.SysFont("arial", 115)
        font_ob = largetext.render("Murdered By Words.", True, black)
        minitext = pygame.font.SysFont("arial", 20)
        font_ob2 = minitext.render("Developer - Soham Kulkarni", True, black)
        screen.blit(font_ob, (250, 150))
        screen.blit(font_ob2, (0, 650))
        intro_button("PLAY", 400, 560, 80, 40, green, bright_green, "PLAY")
        intro_button("QUIT", 800, 560, 80, 40, red, bright_red, "QUIT")
        pygame.display.flip()
        clock.tick(100)


def game_loop():
    while not running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(white)
        #screen.fill(white, (458, 150, 550, 150))
        button_loop()
        tries(pictureno)
        imageloop(imagelist[pictureno])
        blank_display(listtostring(list))
        if hangman == []:
            screen.fill(white)
            largetext = pygame.font.SysFont("arial", 160)
            largetext2 = pygame.font.SysFont("comicsnasms", 75)
            font_ob1 = largetext.render("YOU LOST.", True, bright_red)
            font_ob2 = largetext2.render("The movie was:", True, orange)
            font_ob3 = largetext2.render(movie, True, orange)
            screen.blit(font_ob1, (390, 150))
            screen.blit(font_ob2, (60, 430))
            screen.blit(font_ob3, (460, 430))

        if movie == ("".join(list)):
            screen.fill(white)
            largetext = pygame.font.SysFont("arial", 160)
            largetext2 = pygame.font.SysFont("comicsnasms", 75)
            font_ob1 = largetext.render("GG MATE!", True, bright_green)
            font_ob2 = largetext2.render("The movie was:", True, orange)
            font_ob3 = largetext2.render(movie, True, orange)
            screen.blit(font_ob1, (390, 150))
            screen.blit(font_ob2, (60, 430))
            screen.blit(font_ob3, (460, 430))


        pygame.display.flip()
        clock.tick(100)

pygame.init()
display_width = 1280
display_height = 720

Answer = ""
bright_green = (0, 255, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
red = (200, 0, 0)
yellow = (255, 234, 0)
bright_yellow = (255, 251, 125)
black = (0, 0, 0)
white = (255, 255, 255)
blue = (92, 201, 255)
orange = (255, 159, 0)
aqua = (30, 0, 181)
violet = (193, 122, 255)
small_violet = (159, 52, 235)
welcome_blue = (255, 195, 74)

stage1 = pygame.image.load("stage1.png")
stage2 = pygame.image.load("stage2.png")
stage3 = pygame.image.load("stage3.png")
stage4 = pygame.image.load("stage4.png")
stage5 = pygame.image.load("stage5.png")
stage6 = pygame.image.load("stage6.png")
stage7 = pygame.image.load("stage7.png")
stage8 = pygame.image.load("stage8.png")

imagelist = [stage1, stage2, stage3, stage4, stage5, stage6, stage7, stage8]
clock = pygame.time.Clock()
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Hangman 2.0')
running = False
hangman = ['H', 'A', 'N', 'G', 'M', 'A', 'N']
pictureno = 7
store = ["TERMINATOR", "BLACKPANTHER", "TRANSFORMERS", "GODFATHER", "INCEPTION", "AVATAR", "THELIONKING",
         "AQUAMAN", "JURASSICPARK", "FINDINGNEMO", "DESPICABLEME", "INTERSTELLAR", "ZOOTOPIA", "FINDINGNEMO",
         "THEHOBBIT", "HARRYPOTTER", "STARWARS", "STARTREK", "MUNICH", "LIFEOFPI", "WOLVERINE", "THEMARTIAN",
         "KINGSMAN", "MAZERUNNER", "FERDINAND", "THEMATRIX"]
movie = random.choice(store)
list = []
length_of_movie = len(movie)
for j in range(length_of_movie):
    list.append('_')

screen.fill(white)
game_intro()