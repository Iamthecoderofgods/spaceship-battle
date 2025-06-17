# Initialize pygame modules
import pygame
import os

# Set up window size and title

pygame.init()

screen = pygame.display.set_mode((850,850))
screen.fill(("Blue"))
pygame.display.update()
# Define color constants (RGB values)
R =(255,255,255)
G = (255,255,255)
B = (255,255,255)




# Define game constants: FPS, velocity, bullet velocity, max bullets, spaceship size
FPS = 60
Velocity = 20
bullet_velocity = 20.1
Max_bullets = 20
spaceship_Height = 40
Spaceship_width = 30



# Create a border rectangle to separate the two sides
class Rectangle():
    #constructor
    def __init__(self):
        self.surface = screen
        self.color = "black"
        self.dimension =(425,0, 50, 850)

    def drawrect(self):
        self.Draw_rectangle = pygame.draw.rect(self.surface,self.color,self.dimension)
        pygame.display.update()
        

#create an object for the rectangle class
Object_r = Rectangle()
Object_r.drawrect()
running = True

while running:
    pygame.display.update()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
pygame.display.update()

# Load fonts for health display and winner text
font = pygame.font.SysFont("Times New Roman",36)
health = font.render("Health:",True,0,0)
winner_blue = font.render("the winner is blue",True,0,0)
winner_red = font.render("the winner is red",True,0,0)

# Define custom events for hits
# Load and transform spaceship images (resize and rotate)
spaceship_yellow = pygame.image.load("images/Spaceship_yellow.png")
spaceship_red = pygame.image.load("images/spaceship_red.png")





# Load and scale background image
Backround = pygame.image.load("images/space_backround.png")
Backround_image1 = pygame.transform.scale(Backround,(850,850))


# Function to draw all game elements on the screen
#   - background, border, health text, spaceships, bullets
# Function to handle yellow spaceship movement within its bounds
# Function to handle red spaceship movement within its bounds
# Function to move bullets, check collisions, and remove off-screen bullets
# Function to display winner text and pause before restarting
# Main game loop:
#   - initialize positions, health, bullets
#   - handle events (quit, fire bullets, detect hits)
#   - update movement, bullet positions
#   - check for winner
#   - redraw the screen each frame