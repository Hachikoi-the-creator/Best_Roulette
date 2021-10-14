import pygame
import sys
import random

def rotate(surface, angle):
	rotated_surface = pygame.transform.rotozoom(surface, -angle, 1)#image to rotate, angle, scale
	#Create a new center
	rotated_rect = rotated_surface.get_rect(center = (450, 300))
	return rotated_surface, rotated_rect

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([900, 600])

arrow = pygame.image.load("my_arrow.png")
arrow_smol = pygame.transform.scale(arrow,(90,90))

padoru = pygame.image.load("circle.png")
# padoru_rect = padoru.get_rect(center = (300, 300)), seems like no problem to remove
angle = 0

mod4_angle = [i*2 for i in range(30,400)]
rnd_stop_angle = random.choice(mod4_angle)#Random angle to stop 

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			pygame.quit()

	
	
	if angle < rnd_stop_angle:#While the angle is lower than 
		angle += 4	#The bigger, the faster it rotates
	screen.fill((60,100,90))#Purple
	padoru_rotated, padoru_rotated_rect = rotate(padoru, angle)

	screen.blit(padoru_rotated, padoru_rotated_rect)
	screen.blit(arrow_smol,(420,30))

	pygame.display.flip()
	pygame.display.update()#Not sure what this is
	clock.tick(30)

"""
+Image leaves the screen, solved by creeating a new center 
+Whit rotate, crashes due to creating a new image constantly 
+Whit rotozoom, amazing amount of lag, not even time can save me 
+Now an insteressting trick of ratating the same image from te starting point to the next angle (rotate func),if -angle rotates clockwise!
+Got the image rotating, and the arrow in screen
+Got a random number/angle to stop rotating after a key is pressed. to run again close and open the program im lazy lol
"""