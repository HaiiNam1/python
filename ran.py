import pygame as pg
import random
pg.init()
# Windows game
screen = pg.display.set_mode((800, 800))
pg.display.set_caption('Snake Game')
# Var

score = 0
highscore = 0
snake_part = 20
x = y = 200
x_change = 0
y_change = 0
body_snake = []
length = 1  
# Tao thuc an cho ran
food_x = random.randint(0, 39) * snake_part
food_y = random.randint(0, 39) * snake_part

clock = pg.time.Clock()
speed = 10
# ktra va cham 
def check_collision():
    if x < 0 or x > 800 or y < 0 or y > 800 or (x, y) in body_snake[:-1]:
        return False
    return True

def score_view():
    font = pg.font.Font(None, 36) 
    if gameplay:
        score_txt = font.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(score_txt, (0, 0))
        hscore_txt = font.render(f'HighScore: {highscore}', True, (255, 255, 255))
        screen.blit(hscore_txt, (170, 0))
    else:
        note_txt = font.render(f'Press space to play again:', True, (255, 255, 255))
        screen.blit(note_txt, (0, 0))

# Thiet lap game
gameplay = True
# Tốc đọ của rắn khi chạy nhanh hơn 
moultiples_to_increase_speed = 5  
multiplier = 2  


while True:
    for event in pg.event.get():
        # Quit
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        # Dieu khien ran
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT and x_change == 0:
                x_change = -snake_part
                y_change = 0
            elif event.key == pg.K_RIGHT and x_change == 0:
                x_change = snake_part
                y_change = 0
            elif event.key == pg.K_UP and y_change == 0:
                x_change = 0
                y_change = -snake_part
            elif event.key == pg.K_DOWN and y_change == 0:
                x_change = 0  
                y_change = snake_part
            elif event.key == pg.K_SPACE:
                gameplay = True
    # Clear screen
    screen.fill((255, 192, 203))
    score_view()
    if gameplay:
        # Cap nhat vi tri cua ran
        x += x_change
        y += y_change
        # Them than ran 
        body_snake.append((x, y))
        # Xoa cac san trong body_snake
        if len(body_snake) > length:
            del body_snake[0]
            if score > highscore:
                highscore = score
        # Xem ran co an dc moi ko
        if x == food_x and y == food_y:
            length += 1
            score += 1
            
            # Random food
            food_x = random.randint(0, 39) * snake_part
            food_y = random.randint(0, 39) * snake_part
        # Draw snake
        for part in body_snake:
            pg.draw.rect(screen, (0, 255, 0), (part[0], part[1], snake_part, snake_part)) 
        # Ve thuc an
        pg.draw.rect(screen, (0, 0, 0), (food_x, food_y, snake_part, snake_part))
        gameplay = check_collision()
        clock.tick(speed)
   
   
    else:
        # Reset
        x = y = 200
        x_change = 0
        y_change = 0
        body_snake = []
        length = 1
        score = 0

    # Update screen
    pg.display.update()
