import pygame


def count_down(t):
    while int(t):
        mins, secs = divmod(t, 60)
        timer = "{:02d}:{:02d}".format(mins, secs)
        return timer


def main():
    pygame.init()

    X = 800
    Y = 600

    t = "25:00"

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    display_surface = pygame.display.set_mode((X, Y))
    pygame.display.set_caption("Show Test")
    font = pygame.font.Font("DroidSans.ttf", 32)
    text = font.render(count_down(t), True, WHITE, BLACK)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)

    while True:
        display_surface.fill(BLACK)
        display_surface.blit(text, textRect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()


if __name__ == "__main__":
    main()
