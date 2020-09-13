import pygame
import random

# Golbal Variables...
WIDTH = 1080
HEIGHT = 720
FPS = 60
ROUNDPLAY = 3 #How Many Round You Want To Play Including Trial-Round..

#Colors........
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255,255,0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Random Motion Game!')
clock = pygame.time.Clock()

pygame.font.init()
BIG_FONT = pygame.font.SysFont('Times New Roman', 50)
MEDIUM_FONT = pygame.font.SysFont('Times New Roman', 32)
SMALL_FONT = pygame.font.SysFont('Times New Roman', 24)

class RandomMovementGame:
	def __init__(self):
		self.playerScore = []
		
		self.computer = pygame.image.load('quit.png')
		self.player = pygame.image.load('correct.png')
		self.sound = pygame.mixer.Sound("beep.wav")

	def Theme(self):
		pygame.draw.rect(screen, (0,50,50), (0,0,180,720))

		flying_solo_icon = pygame.image.load('jet.png')
		screen.blit(flying_solo_icon,(35,20))
	
		flying_solo_text = SMALL_FONT.render("The Flying Solo", True, WHITE)
		screen.blit(flying_solo_text,(12, 150))

		
		


	def startingScreen(self):
		current_time = pygame.time.get_ticks()/1000
		running = True
		while running:
			clock.tick(FPS)
			screen.fill(BLACK)
			self.Theme()
			timer = pygame.time.get_ticks()/1000
			for event in pygame.event.get():
			    if event.type == pygame.QUIT:
			        running = False
			        pygame.quit()
			        quit()
			if(current_time+10-timer) <= 0:
			    running = False
			text = BIG_FONT.render("Random Movement", True, GREEN)
			screen.blit(text,((screen.get_width()/2-text.get_width()/2)+100, screen.get_height()/2-text.get_height()/2))
			pygame.display.update()


	def roundStartingScreen(self, round_name):
		current_time = pygame.time.get_ticks()/1000
		running = True
		while running:
			clock.tick(FPS)
			screen.fill(BLACK)
			self.Theme()
			timer = pygame.time.get_ticks()/1000

			text = BIG_FONT.render(round_name, True, (250, 0, 250))
			screen.blit(text, (screen.get_width()/2-text.get_width()/2+100, screen.get_height()/2-text.get_height()/2-20))

			text = MEDIUM_FONT.render("Loading the game...", True, (150, 250, 0))
			screen.blit(text,(screen.get_width()/2-text.get_width()/2+105, screen.get_height()/2-text.get_height()/2+20))

			for event in pygame.event.get():
			    if event.type == pygame.QUIT:
			        running = False
			        pygame.quit()
			        quit()
			if(current_time+5-timer) <= 0:
			    running = False
			pygame.display.update()


	def gammeRoundPlay(self, round_time, round_name):
		score = 0
		x, y = 380, 450
		pos_x, pos_y = 200, 230

		change = 5
		x_change, y_change = 3, 3

		x_lower_limit, x_upper_limit = 180, 920
		y_lower_limit, y_upper_limit = 200, 650

		x_direction, y_direction = "RIGHT", "DOWN"

		state = "not_blinking"
		music = "not_playing"

		red_pressed_1 = 0
		red_pressed_2 = 0

		yellow_pressed_1 = 0
		yellow_pressed_2 =0

		music_click = 0

		time = list(range(0, round_time, 4))
		values = random.sample(time,k=5)

		count = list(range(0,5))     
		num = random.sample(count,k=5)

		current_time = pygame.time.get_ticks()/1000
		#main loop
		running = True
		while running:
			clock.tick(FPS)
			screen.fill(BLACK)
			self.Theme()
			timer = pygame.time.get_ticks()//1000
			pygame.draw.rect(screen, (0,50,50), (185,170,889,889))

			for event in pygame.event.get():
			    if event.type == pygame.QUIT:
			        running = False
			        pygame.quit()

			        
			keys = pygame.key.get_pressed()
			if keys[pygame.K_s] and pos_y < 710-64-change:
			    pos_y += change
			if keys[pygame.K_w] and pos_y > 170:
			    pos_y -= change
			if keys[pygame.K_RIGHT]and pos_x < 1078-64-change:
			    pos_x += change
			if keys[pygame.K_LEFT]and pos_x > 185:
			    pos_x -= change

			if x<=x_lower_limit and x_direction == "LEFT":
			    x_change*=-1
			    x_direction = "RIGHT"
			    x_upper_limit = random.uniform(580,920)
			if x>=x_upper_limit and x_direction == "RIGHT":
			    x_change*=-1
			    x_direction = "LEFT"
			    x_lower_limit = random.uniform(180,580)

			if y<=y_lower_limit and y_direction == "UP":
			    y_change*=-1
			    y_direction = "DOWN"
			    y_upper_limit = random.uniform(420,650)
			if y>=y_upper_limit and y_direction == "DOWN":
			    y_change*=-1
			    y_direction = "UP"
			    y_lower_limit = random.uniform(170,420)

			x+=x_change
			y+=y_change

			if values[num[0]]-timer == 0 or (values[num[0]]-1)-(timer-1) == 0 or (values[num[0]]+1)-(timer+1) == 0:
			    state = "is_blinking"
			    if red_pressed_1 == 0:
			        pygame.draw.circle(screen, RED, (470,112),7)
			    if state == "is_blinking":
			        keys = pygame.key.get_pressed()
			        if keys[pygame.K_SPACE] and red_pressed_1 == 0 :
			            score += 1.000
			            red_pressed_1 = 1
			            state = "not_blinking"

			if values[num[1]]-timer == 0  or (values[num[1]]-1)-(timer-1) == 0 or (values[num[1]]+1)-(timer+1) == 0:
			    state = "is_blinking"
			    if red_pressed_2 == 0:
			        pygame.draw.circle(screen, RED, (470,112),7)
			    if state == "is_blinking":
			        keys = pygame.key.get_pressed()
			        if keys[pygame.K_SPACE] and red_pressed_2 == 0 :
			            score += 1.000
			            red_pressed_2 = 1
			            state = "not_blinking"

			if values[num[2]]-timer == 0  or (values[num[2]]-1)-(timer-1) == 0 or (values[num[2]]+1)-(timer+1) == 0:
			    state = "is_blinking"
			    if yellow_pressed_1 == 0:
			        pygame.draw.circle(screen, YELLOW, (770,112),7)
			    if state == "is_blinking":
			        keys = pygame.key.get_pressed()
			        if keys[pygame.K_SPACE] and yellow_pressed_1 == 0 :
			            score += 1.000
			            yellow_pressed_1 = 1
			            state = "not_blinking"

			if values[num[3]]-timer == 0 or (values[num[3]]-1)-(timer-1) == 0 or (values[num[3]]+1)-(timer+1) == 0:
			    state = "is_blinking"
			    if yellow_pressed_2 == 0:
			        pygame.draw.circle(screen, YELLOW, (770,112),7)
			    if state == "is_blinking":
			        keys = pygame.key.get_pressed()
			        if keys[pygame.K_SPACE] and yellow_pressed_2 == 0 :
			            score += 1.000
			            yellow_pressed_2 = 1
			            state = "not_blinking"

			if values[num[4]]-timer == 0 or (values[num[4]]-1)-(timer-1) == 0 or (values[num[4]]+1)-(timer+1) == 0:
			    music = "is_playing"
			    if music_click == 0:
			        self.sound.play()
			    if music == "is_playing":
			        keys = pygame.key.get_pressed()
			        if keys[pygame.K_SPACE] and music_click == 0 :
			            score += 1.000
			            music_click = 1
			            music = "not_playing"

			if (pos_x <= x + 64 and pos_x >= x):
			    if (pos_y <= y + 64 and pos_y >= y):
			        score += 0.005
			elif(pos_x <= x + 64-2 and pos_x >= x+2):
			    if (pos_y <= y + 64-2 and pos_y >= y+2):
			        score += 0.0025
			elif(pos_x <= x + 64-3 and pos_x >= x+3):
			    if (pos_y <= y + 64-3 and pos_y >= y+3):
			        score += 0.0001
			else:
			    score += 0

			score_txt = MEDIUM_FONT.render("Score : " + str(round((score)*4,7)), True, WHITE)
			screen.blit(score_txt,(850, 50))
			score_txt = MEDIUM_FONT.render("Timer : " + str(int(current_time+round_time-timer)), True, WHITE)
			screen.blit(score_txt,(250, 50))
			score_txt = MEDIUM_FONT.render(round_name, True, WHITE)
			screen.blit(score_txt,(560, 50))


			screen.blit(self.computer,(x,y))
			screen.blit(self.player,(pos_x,pos_y))

			if(current_time+round_time-timer)<=0:
			    running = False
			pygame.display.update()

		return score

	def displayScore(self, score):
		current_time = pygame.time.get_ticks()/1000
		running = True
		while running:
			clock.tick(FPS)
			timer = pygame.time.get_ticks()/1000
			screen.fill(BLACK)
			self.Theme()
			for event in pygame.event.get():
			    if event.type == pygame.QUIT:
			        running = False
			        pygame.quit()
			        quit()

			text = BIG_FONT.render("Score: " + str(round((score)*4,5)), True, GREEN)
			screen.blit(text,(450+100, 350))
		
			if(current_time+10-timer)<=0:
			    running = False

			pygame.display.update()

	def lastScore(self):
		current_time = pygame.time.get_ticks()/1000
		running = True
		while running:
			clock.tick(FPS)
			screen.fill(BLACK)
			self.Theme()
			timer = pygame.time.get_ticks()/1000
			for num, line in enumerate(self.playerScore):
				text = BIG_FONT.render(f'Round-{num+1}: {line}', True, WHITE)
				screen.blit(text, (screen.get_width()/2-text.get_width()/2-40, 
					               screen.get_height()/2-text.get_height()/2-40+50*num))
			for event in pygame.event.get():
			    if event.type == pygame.QUIT:
			        running = False
			        pygame.quit()
			        quit()
			pygame.display.update()
			if (current_time+15-timer)<=0:
			    running = False

	def gameLoop(self, count):
		round_time = 0
		if count == 0:
			round_time, round_name = 60, 'Trial-Round'
		else:
			round_time, round_name = 90, f"Round: {count}"
		self.roundStartingScreen(round_name)

		self.playerScore.append(self.gammeRoundPlay(round_time, round_name))
		self.displayScore(self.playerScore[-1])
			
def main():
	Game = RandomMovementGame() 
	Game.startingScreen()
	count = 0
	while count <= ROUNDPLAY:
		Game.gameLoop(count)
		count += 1
	Game.lastScore()

if __name__ == '__main__':
	main()
