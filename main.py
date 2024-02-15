import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
BG_COLOR = (0, 0, 0)
WHITE = (255, 255, 255)
FONT = pygame.font.Font(None, 36)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Set up the game objects
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 15
PADDLE_SPEED = 8  # Increase paddle speed
BALL_SPEED_X, BALL_SPEED_Y = 5, 5

player1 = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
player2 = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

# Set up movement variables
player1_up = False
player1_down = False
player2_up = False
player2_down = False

# Set up scores
score_player1 = 0
score_player2 = 0

# Function to display scores
def display_scores():
    score_text = FONT.render(f"{score_player1}   {score_player2}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 10))

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player1_up = True
            elif event.key == pygame.K_s:
                player1_down = True
            elif event.key == pygame.K_UP:
                player2_up = True
            elif event.key == pygame.K_DOWN:
                player2_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player1_up = False
            elif event.key == pygame.K_s:
                player1_down = False
            elif event.key == pygame.K_UP:
                player2_up = False
            elif event.key == pygame.K_DOWN:
                player2_down = False

    # Move paddles
    if player1_up and player1.top > 0:
        player1.y -= PADDLE_SPEED
    elif player1_down and player1.bottom < HEIGHT:
        player1.y += PADDLE_SPEED
    if player2_up and player2.top > 0:
        player2.y -= PADDLE_SPEED
    elif player2_down and player2.bottom < HEIGHT:
        player2.y += PADDLE_SPEED

    # Move ball
    ball.x += BALL_SPEED_X
    ball.y += BALL_SPEED_Y

    # Ball collision with walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        BALL_SPEED_Y = -BALL_SPEED_Y  # Reverse the direction along the y-axis
    # Ball collision with paddles
    if ball.colliderect(player1) or ball.colliderect(player2):
        BALL_SPEED_X = -BALL_SPEED_X  # Reverse the direction along the x-axis

    # Ball out of bounds
    if ball.left <= 0:
        score_player2 += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)  # Reset ball position
    elif ball.right >= WIDTH:
        score_player1 += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)  # Reset ball position

    # Clear the screen
    screen.fill(BG_COLOR)

    # Draw paddles and ball
    pygame.draw.rect(screen, WHITE, player1)
    pygame.draw.rect(screen, WHITE, player2)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Display scores
    display_scores()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

