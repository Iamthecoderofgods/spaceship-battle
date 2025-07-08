# Initialize pygame modules
import pygame
import os

# Set up window size and title

pygame.init()


screen = pygame.display.set_mode((850,850))
pygame.display.update()
# Define color constants (RGB values)
R =(255,255,255)
G = (255,255,255)
B = (255,255,255)




# Define game constants: FPS, velocity, bullet velocity, max bullets, spaceship size
FPS = 60
Dead = False
Velocity = 20
bullet_velocity = 20.1
Max_bullets = 20
spaceship_Height = 10
Spaceship_width = 10
Red_health = 10
yellow_health = 10
border = pygame.Rect(420,0,50,850)
red_bullet = []
Yellow_bullet = []
yellow_hit = pygame.USEREVENT+1
red_hit = pygame.USEREVENT+1


# Create a border rectangle to separate the two sides

running = True
# Load fonts for health display and winner text
font = pygame.font.SysFont("Times New Roman",36)
winner_blue = font.render("the winner is blue",True,0,0)
winner_red = font.render("the winner is red",True,0,0)

# Define custom events for hits
# Load and transform spaceship images (resize and rotate)
spaceship_yellow = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("images/Spaceship_yellow.png"),(150,150)),-90)
spaceship_red = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("images/spaceship_red.png"),(150,150)),90)
spaceship_Red_rect = pygame.Rect(0,100,50,50)
spaceship_yellow_rect = pygame.Rect(700,100,50,50)



# Load and scale background image
Backround = pygame.image.load("images/space_backround.png")
Backround_image1 = pygame.transform.scale(Backround,(850,850))

def draw_window():
    pass


# Function to draw all game elements on the screen
while running:
    Health_yellow = font.render("Health:"+str(yellow_health),True,"White","black")
    Health_red = font.render("Health:"+str(Red_health),True,"white","black")
    screen.blit(Backround_image1,(0,0))
    pygame.draw.rect(screen,(0,0,0),border)
    screen.blit(Health_yellow,(670,20))
    screen.blit(Health_red,(20,20))
    screen.blit(spaceship_red,(0,100))
    screen.blit(spaceship_yellow,(700,100))
    for e in red_bullet:
        pygame.draw.rect(screen,"red",e)
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        
    
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_q:
                red_bullet.append(pygame.Rect(spaceship_Red_rect.x+75,spaceship_Red_rect.y+75,20,15))
                
                
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q] and spaceship_yellow_rect.x - 10 > 0:
            spaceship_yellow_rect.x += 100
    
    for e in red_bullet:
        e.x += 5
        pygame.draw.rect(screen,"red",e)
        if e.colliderect(spaceship_yellow_rect):
            print("hg")
            pygame.event.post(pygame.event.Event(yellow_hit))
            red_bullet.remove(e)
            yellow_health -= 1
            print(yellow_health)
        elif e.x > 850:
            red_bullet.remove(e)
        
            
    draw_window()
    pygame.display.update()

    
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