import pygame
import sys
import random

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Load the background music (change 'bgm.mp3' to your audio file)
# pygame.mixer.music.load('C:\Ashutosh\Python\Extras\BGM.mp3')
pygame.mixer.music.load('data\BGM.mp3')
icon_img = pygame.image.load('data\pong.ico')
pygame.display.set_icon(icon_img)

# Constants
WIDTH, HEIGHT = 1000, 600
BALL_SPEED = 1
PADDLE_SPEED = 1
YELLOW = (247, 255, 0)
BLACK = (0, 0, 0)
BLUE = (32, 35, 242)
GREEN = (36, 242, 13)
RED = (255, 0, 0)

# Create the game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Game")

# Initialize paddles and ball
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
player_paddle = pygame.Rect(WIDTH - 20, HEIGHT // 2 - 60, 10, 120)
opponent_paddle = pygame.Rect(10, HEIGHT // 2 - 60, 10, 120)

# Initialize ball direction
ball_direction_x = random.choice((1, -1))
ball_direction_y = random.choice((1, -1))

# Initialize scores
player_score = 0
opponent_score = 0

# Load fonts
font = pygame.font.Font(None, 36)

# Game over screen variables
game_over = False
font = pygame.font.Font(None, 36)
winner = None

# Game states
START_GAME = 0
GAME_PLAYING = 1
GAME_OVER = 2
current_state = START_GAME  # Initialize the game state

# Function to change game state


def change_state(new_state):
    global current_state
    current_state = new_state

# Function to start the game


def start_game():
    global player_score, opponent_score, game_over
    player_score = 0
    opponent_score = 0
    game_over = False

    pygame.mixer.music.play(-1)

# FUNCTIONS USED


def restart():
    global player_score, opponent_score, game_over
    player_score = 0
    opponent_score = 0
    game_over = False


def quit_game():
    pygame.mixer.music.stop()
    pygame.quit()
    sys.exit()


# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if current_state == START_GAME:
                if event.key == pygame.K_RETURN:
                    start_game()
                    change_state(GAME_PLAYING)
                elif event.key == pygame.K_c:
                    quit_game()
            elif current_state == GAME_PLAYING:
                if event.key == pygame.K_r:
                    restart()
                elif event.key == pygame.K_c:
                    change_state(GAME_OVER)
            elif current_state == GAME_OVER:
                if event.key == pygame.K_r:
                    start_game()
                    change_state(GAME_PLAYING)
                elif event.key == pygame.K_c:
                    quit_game()

    if current_state == START_GAME:
        # Clear the screen
        window.fill(BLACK)

        # Display start game instructions
        start_text = font.render("Press Enter to Start the Game", True, YELLOW)
        quit_text = font.render("Press C to Quit the Game", True, YELLOW)
        window.blit(start_text, (WIDTH // 2 - 200, HEIGHT // 2 - 30))
        window.blit(quit_text, (WIDTH // 2 - 150, HEIGHT // 2 + 10))

    elif current_state == GAME_PLAYING:
        # Clear the screen
        window.fill(BLACK)

        # Move paddles
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and player_paddle.top > 0:
            player_paddle.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and player_paddle.bottom < HEIGHT:
            player_paddle.y += PADDLE_SPEED

        # Control opponent's paddle
        if keys[pygame.K_w] and opponent_paddle.top > 0:
            opponent_paddle.y -= PADDLE_SPEED
        if keys[pygame.K_s] and opponent_paddle.bottom < HEIGHT:
            opponent_paddle.y += PADDLE_SPEED

        # Ball movement
        ball.x += BALL_SPEED * ball_direction_x
        ball.y += BALL_SPEED * ball_direction_y

        # Ball collision with walls
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_direction_y *= -1

        # Ball collision with paddles
        if ball.colliderect(player_paddle) or ball.colliderect(opponent_paddle):
            ball_direction_x *= -1

        # Scoring
        if ball.left <= 0:
            player_score += 1
            if player_score == 10:
                change_state(GAME_OVER)
                winner = "Player 1"
                pygame.mixer.music.stop()
            else:
                ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
                ball_direction_x *= -1

        if ball.right >= WIDTH:
            opponent_score += 1
            if opponent_score == 10:
                change_state(GAME_OVER)
                winner = "Player 2"
                pygame.mixer.music.stop()
            else:
                ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
                ball_direction_x *= -1

        # Draw everything
        pygame.draw.rect(window, BLUE, player_paddle)
        pygame.draw.rect(window, GREEN, opponent_paddle)
        pygame.draw.ellipse(window, RED, ball)
        pygame.draw.aaline(window, YELLOW, (WIDTH // 2, 0),
                           (WIDTH // 2, HEIGHT))

        player_text = font.render(f"Player 1: {player_score}", True, YELLOW)
        opponent_text = font.render(
            f"Player 2: {opponent_score}", True, YELLOW)
        window.blit(player_text, (WIDTH - 180, 10))
        window.blit(opponent_text, (10, 10))

        # Display instructions
        instruction_text = font.render(
            "Press 'r' to Restart the Game", True, YELLOW)
        instruction_text2 = font.render(
            "Press 'c' to Quit the Game", True, YELLOW)
        window.blit(instruction_text, (10, HEIGHT - 30))
        window.blit(instruction_text2, (WIDTH // 2, HEIGHT - 30))

    elif current_state == GAME_OVER:  # Game over screen
        # Clear the screen
        window.fill(BLACK)

        # Draw game over screen
        game_over_text = font.render(f"{winner} wins!", True, YELLOW)
        window.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2 - 100))

        restart_text = font.render(
            "Press 'r' to Restart the Game", True, YELLOW)
        quit_text = font.render("Press 'c' to Quit the Game", True, YELLOW)
        window.blit(restart_text, (WIDTH//2 - 200, HEIGHT//2))
        window.blit(quit_text, (WIDTH//2-200, HEIGHT//2+40))

    # Update the display
    pygame.display.flip()
