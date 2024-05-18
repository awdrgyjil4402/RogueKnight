import pygame

TITLE = "Game"
SIZE = (1000, 600)


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

    # keys = pygame.key.get_pressed()

    return True


def draw():
    screen.fill((0, 0, 0))
    # screen.blit()


def game_logic():
    pass


def run_game():
    while handle_events():
        game_logic()

        draw()

        pygame.display.update(window_rect)

        clock.tick(30)