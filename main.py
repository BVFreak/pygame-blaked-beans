import pygame, sys
from pygame.locals import *
from crosshair import Crosshair
from settings import *
from level import Level

pygame.init()
pygame.mixer.init()

# general setup
screen = pygame.display.set_mode([screen_width, screen_height])
BACKGROUND_MENU = "black"
BACKGROUND_GAME = "black"
BACKGROUND_SETTINGS = "black"
BACKGROUND_WARNING = "red"

pygame.display.set_caption("Blaked Beans")

clock = pygame.time.Clock()

# audio

icon = pygame.image.load("assets/sprites/bobba.png")

pygame.display.set_icon(icon)

level = Level(level_map,screen)


class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)

crosshair = Crosshair('assets/sprites/crosshair.png')
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

def start_menu():
    pygame.mixer.music.stop()
    SONG80 = pygame.mixer.music.load("assets/audio/80.mp3")
    pygame.mixer.music.play()
    while True:
        pygame.mouse.set_visible(True)
        screen.fill((0,0,0))

        mouse_pos = pygame.mouse.get_pos()
        start_text = get_font(100).render("Blaked Beans", True, "purple")
        start_rect = start_text.get_rect(center=(600, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/sprites/Warning Rect.png"), pos=(600, 250),
                             text_input="play", font=get_font(75), base_color="White", hovering_color="Green")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/sprites/Warning Rect.png"), pos=(600, 400),
                             text_input="quit", font=get_font(75), base_color="White", hovering_color="Red")
        SETTINGS_BUTTON = Button(image=pygame.image.load("assets/sprites/settings_gear.png"), pos=(1150, 50),
                                 text_input="", font=get_font(30), base_color="White", hovering_color="Black")
        HOWTOPLAY_BUTTON = Button(image=pygame.image.load("assets/sprites/ques.png"), pos=(1145, 255),
                             text_input="", font=get_font(75), base_color="White", hovering_color="Red")
        INFO_BUTTON = Button(image=pygame.image.load("assets/sprites/info.png"), pos=(1150, 150),
                             text_input="", font=get_font(75), base_color="White", hovering_color="Red")

        screen.blit(start_text, start_rect)

        for button in [PLAY_BUTTON, SETTINGS_BUTTON, QUIT_BUTTON, HOWTOPLAY_BUTTON, INFO_BUTTON]:
            button.changeColor(mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                warning_quit()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(mouse_pos):
                    play()
                if SETTINGS_BUTTON.checkForInput(mouse_pos):
                    settings()
                if QUIT_BUTTON.checkForInput(mouse_pos):
                    warning_quit()
                if HOWTOPLAY_BUTTON.checkForInput(mouse_pos):
                    howtoplay()
                if INFO_BUTTON.checkForInput(mouse_pos):
                    info()

        pygame.display.update()

def death():
    while True:
        pygame.mouse.set_visible(True)
        screen.fill((0,0,0))

        mouse_pos = pygame.mouse.get_pos()

        bye_text = get_font(100).render("you have gotten to the death", True, "red")
        bye_rect = bye_text.get_rect(center=(600, 100))

        EXIT_BUTTON = Button(image=pygame.image.load("assets/sprites/Warning rect.png"), pos=(600, 250),
                        text_input="exit", font=get_font(75), base_color="red", hovering_color="Darkred")

        screen.blit(bye_text,bye_rect)

        for button in [EXIT_BUTTON]:
            button.changeColor(mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if EXIT_BUTTON.checkForInput(mouse_pos):
                    pygame.quit()
                    sys.exit()
        
        pygame.display.update()

def howtoplay():
    while True:
        pygame.mouse.set_visible(True)
        screen.fill((0,0,0))

        mouse_pos = pygame.mouse.get_pos()

        howtoplay_text = get_font(100).render("HOW TO PLAY", True, "white")
        howtoplay_rect = howtoplay_text.get_rect(center=(600, 100))

        howtoplay2_text = get_font(75).render("movement: WASD to move, SPACE to jump", True, "white")
        howtoplay2_rect = howtoplay2_text.get_rect(center=(600, 300))

        RETURN_BUTTON = Button(image=pygame.image.load("assets/sprites/Warning rect.png"), pos=(600, 500),
                        text_input="return", font=get_font(50), base_color="white", hovering_color="Darkgray")

        screen.blit(howtoplay_text,howtoplay_rect)
        screen.blit(howtoplay2_text,howtoplay2_rect)

        for button in [RETURN_BUTTON]:
            button.changeColor(mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RETURN_BUTTON.checkForInput(mouse_pos):
                    return
        
        pygame.display.update()

def play():
    pygame.mixer.music.stop()
    SONG = pygame.mixer.music.load("assets/audio/music.mp3")
    pygame.mixer.music.play()
    while True:
        screen.fill("darkblue")

        mouse_pos = pygame.mouse.get_pos()
        pygame.mouse.set_visible(False)

        RETURN_BUTTON = Button(image=pygame.image.load("assets/sprites/Warning Rects.png"), pos=(35, 25),
                            text_input="return", font=get_font(17), base_color="White", hovering_color="Red")

        for button in [RETURN_BUTTON]:
            button.changeColor(mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            pass

            if event.type == pygame.MOUSEBUTTONDOWN:
                if RETURN_BUTTON.checkForInput(mouse_pos):
                    pygame.mixer.music.stop()
                    SONG80 = pygame.mixer.music.load("assets/audio/80.mp3")

                    pygame.mixer.music.play()
                    return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            warning_quit()

        level.run()

        crosshair_group.draw(screen)
        crosshair_group.update()

        pygame.display.flip()
        clock.tick(60)

def settings():
    while True:
        pygame.mouse.set_visible(True)
        screen.fill(BACKGROUND_SETTINGS)

        mouse_pos = pygame.mouse.get_pos()

        SETTINGS_TEXT = get_font(100).render("SETTINGS", True, "gray")
        SETTINGS_RECT = SETTINGS_TEXT.get_rect(center=(600, 100))

        RETURN_BUTTON = Button(image=pygame.image.load("assets/sprites/Quit Rect.png"), pos=(600, 400),
                            text_input="return", font=get_font(75), base_color="White", hovering_color="DarkGray")

        AUDIO_ON_BUTTON = Button(image=pygame.image.load("assets/sprites/audio_on.png"), pos=(500, 250),
                            text_input="", font=get_font(75), base_color="White", hovering_color="DarkGray")
        AUDIO_OFF_BUTTON = Button(image=pygame.image.load("assets/sprites/audio_off.png"), pos=(700, 250),
                            text_input="", font=get_font(75), base_color="White", hovering_color="DarkGray")
        
        screen.blit(SETTINGS_TEXT, SETTINGS_RECT)
        for button in [AUDIO_ON_BUTTON]:
            button.changeColor(mouse_pos)
            button.update(screen)
        for button in [AUDIO_OFF_BUTTON]:
            button.changeColor(mouse_pos)
            button.update(screen)
            

        for button in [RETURN_BUTTON]:
            button.changeColor(mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                warning_quit()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RETURN_BUTTON.checkForInput(mouse_pos):
                    return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if AUDIO_ON_BUTTON.checkForInput(mouse_pos):
                    pygame.mixer.music.set_volume(1)
                elif AUDIO_OFF_BUTTON.checkForInput(mouse_pos):
                    pygame.mixer.music.set_volume(0)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            warning_quit()

        pygame.display.update()


def warning_quit():
    while True:
        pygame.mouse.set_visible(True)
        screen.fill(BACKGROUND_WARNING)

        mouse_pos = pygame.mouse.get_pos()

        warning_text = get_font(75).render("Are you sure you want to quit?", True, (255, 255, 255))
        warning_rect = warning_text.get_rect(center=(600, 100))

        YES_BUTTON = Button(image=pygame.image.load("assets/sprites/Warning Rect.png"), pos=(425, 250),
                             text_input="yes", font=get_font(75), base_color="White", hovering_color="Green")
        NO_BUTTON = Button(image=pygame.image.load("assets/sprites/Warning rect.png"), pos=(775, 250),
                                 text_input="no", font=get_font(75), base_color="White", hovering_color="Red")

        screen.blit(warning_text, warning_rect)

        for button in [YES_BUTTON, NO_BUTTON]:
            button.changeColor(mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if NO_BUTTON.checkForInput(mouse_pos):
                    start_menu()
                if YES_BUTTON.checkForInput(mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def info():
    while True:
        pygame.mouse.set_visible(True)
        screen.fill(BACKGROUND_SETTINGS)

        mouse_pos = pygame.mouse.get_pos()

        INFO_TEXT = get_font(100).render("INFO", True, "blue")
        INFO_RECT = INFO_TEXT.get_rect(center=(600, 100))

        CREDITS1_TEXT = get_font(50).render("this was made by blake verner copyright lololol", True, "silver")
        CREDITS1_RECT = CREDITS1_TEXT.get_rect(center=(600, 200))

        CREDITS2_TEXT = get_font(60).render("made in pygame", True, "gold")
        CREDITS2_RECT = CREDITS2_TEXT.get_rect(center=(600, 300))

        RETURN_BUTTON = Button(image=pygame.image.load("assets/sprites/Quit Rect.png"), pos=(600, 400),
                            text_input="return", font=get_font(75), base_color="White", hovering_color="DarkGray")

        screen.blit(INFO_TEXT, INFO_RECT)
        screen.blit(CREDITS1_TEXT, CREDITS1_RECT)
        screen.blit(CREDITS2_TEXT, CREDITS2_RECT)

        for button in [RETURN_BUTTON]:
            button.changeColor(mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                warning_quit()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RETURN_BUTTON.checkForInput(mouse_pos):
                    return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            warning_quit()
            
        pygame.display.update()

start_menu()