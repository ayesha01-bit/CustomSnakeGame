import pygame as game
from random import randrange

game.init()
WINDOW = 700
screen = game.display.set_mode([WINDOW]*2) 
clock = game.time.Clock()
level = 10

headingFont = game.font.SysFont("Arial", 40)
subTitleFont = game.font.SysFont("Arial", 20)

def showWelcomeScreen():
    waiting_for_input = True

    # Event loop for displaying the welcome screen
    while waiting_for_input:
        # Fill the screen with a black background
        screen.fill('black')

        # Render the welcome text
        welcome_text = headingFont.render("Welcome to Snake Game!", True, (0, 255, 0))
        start_text = subTitleFont.render("Choose your Level", True, (255, 255, 255))

        # Positioning the text on the screen
        screen.blit(welcome_text, (WINDOW // 4, WINDOW // 3))
        screen.blit(start_text, (WINDOW // 2.5, WINDOW // 2.5))

        # Define the rectangle for the "easy" level button
        easyRectx, easyRecty, easyRectWidth, easyRectHeight = 250, 350, 200, 75  # Easy level rectangle
        # Define the rectangle for the "easy" level button
        mediumRectx, mediumRecty, mediumRectWidth, mediumRectHeight = 250, 450, 200, 75  # Easy level rectangle
        # Define the rectangle for the "easy" level button
        hardRectx, hardRecty, hardRectWidth, hardRectHeight = 250, 550, 200, 75  # Easy level rectangle

        # Draw the rectangles for each level
        game.draw.rect(screen, (0, 255, 0), (easyRectx, easyRecty, easyRectWidth, easyRectHeight))
        game.draw.rect(screen, (0, 0, 255), (mediumRectx, mediumRecty, mediumRectWidth, mediumRectHeight))
        game.draw.rect(screen, (255, 0, 0), (hardRectx, hardRecty, hardRectWidth, hardRectHeight))

        # Render text for each level and position it at the center of each rectangle
        easy_text = subTitleFont.render("Easy", True, (0, 0, 0))  # Black text for easy
        medium_text = subTitleFont.render("Medium", True, (255, 255, 255))  # White text for medium
        hard_text = subTitleFont.render("Hard", True, (255, 255, 255))  # White text for hard

        screen.blit(easy_text, (easyRectx + (easyRectWidth - easy_text.get_width()) // 2, easyRecty + (easyRectHeight - easy_text.get_height()) // 2))
        screen.blit(medium_text, (mediumRectx + (mediumRectWidth - medium_text.get_width()) // 2, mediumRecty + (mediumRectHeight - medium_text.get_height()) // 2))
        screen.blit(hard_text, (hardRectx + (hardRectWidth - hard_text.get_width()) // 2, hardRecty + (hardRectHeight - hard_text.get_height()) // 2))

        # Update the display to render the changes
        game.display.flip()
        global level

        # Event handling
        for event in game.event.get():
            if event.type == game.QUIT:
                exit()  # Close the game window
            if event.type == game.MOUSEBUTTONDOWN:
                # Get the mouse position
                mouse_x, mouse_y = game.mouse.get_pos()

                # Check if the mouse click is inside the rectangle
                if easyRectx <= mouse_x <= easyRectx + easyRectWidth and easyRecty <= mouse_y <= easyRecty + easyRectHeight:
                    level = 7
                    waiting_for_input = False  # Exit the loop when clicked inside the rectangle
                elif mediumRectx <= mouse_x <= mediumRectx + mediumRectWidth and mediumRecty <= mouse_y <= mediumRecty + mediumRectHeight:
                    level = 10
                    waiting_for_input = False  # Exit the loop when clicked inside the rectangle
                elif hardRectx <= mouse_x <= hardRectx + hardRectWidth and hardRecty <= mouse_y <= hardRecty + hardRectHeight:
                    level = 15
                    waiting_for_input = False  # Exit the loop when clicked inside the rectangle

            if event.type == game.KEYDOWN:
                # Check for keypress (optional to handle any other key event)
                if event.key == game.K_ESCAPE:  # For example, ESC to quit
                    exit()

def showGame():   
    snake = [(200, 200)]    
    direction = (20,0)
    food = (randrange(0, 400, 20), randrange(0, 400, 20))    
    isGameOver = False  
    while not isGameOver: 
        for event in game.event.get(): 
            if event.type == game.QUIT:
                exit()
            if event.type == game.KEYDOWN:
                if event.key == game.K_UP: direction = (0, -20)
                if event.key == game.K_DOWN: direction = (0, 20)
                if event.key == game.K_RIGHT: direction = (20, 0)
                if event.key == game.K_LEFT: direction = (-20, 0)

        newHead = (snake[0][0] + direction[0], snake[0][1] + direction[1])

        if newHead == food:
            food = (randrange(0, 400, 20), randrange(0, 400, 20))  # New food position
            snake.append(snake[-1])  # Add a new segment to the snake (grow)
        if snake[0][0] > WINDOW or snake[0][0] < 0 or snake[0][1] > WINDOW or snake[0][1] < 0:
            isGameOver = True
        # snakeBody = snake[1:]
        # if newHead in snakeBody:
        #     isGameOver = True
        snake = [newHead] + snake[:-1]

        screen.fill('black')
        segment_width = 20  # Define the width of a snake segment
        segment_height = 20  # Define the height of a snake segment

        for segment in snake:
            game.draw.rect(screen, (0, 255, 0), (segment[0], segment[1], segment_width, segment_height))
            game.draw.rect(screen, (255, 0, 0), (food[0], food[1], 20, 20))
        game.display.flip()
        clock.tick(level)

def showGameOver():
    # Fill the screen with a black background
        screen.fill('black')
        gameOverText = headingFont.render("Game Over!", True, (0, 255, 0))
        # Get the width and height of the text to position it in the center
        text_width = gameOverText.get_width()
        text_height = gameOverText.get_height()

        # Calculate the center position of the screen
        x_pos = (WINDOW - text_width) // 2
        y_pos = (WINDOW - text_height) // 2 

        screen.blit(gameOverText, (x_pos, y_pos))
        game.display.flip()
        game.time.wait(1000)

def main():
    showWelcomeScreen()
    showGame()
    showGameOver()

main()