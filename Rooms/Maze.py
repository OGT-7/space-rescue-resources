import pygame

class Maze:
    def __init__(self, screen, joysticks):
        self.screen = screen
        self.joysticks = joysticks
        self.ship_x = 100
        self.ship_y = 100
        self.clock = pygame.time.Clock()
        self.running = True

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.ship_x -= 5
        if keys[pygame.K_RIGHT]:
            self.ship_x += 5
        if keys[pygame.K_UP]:
            self.ship_y -= 5
        if keys[pygame.K_DOWN]:
            self.ship_y += 5

    def draw(self):
        self.screen.fill((0, 0, 0))
        pygame.draw.rect(self.screen, (255, 255, 255),
                         (self.ship_x, self.ship_y, 20, 20))
        pygame.display.flip()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    return False

            keys = pygame.key.get_pressed()
            self.update(keys)
            self.draw()
            self.clock.tick(60)

        return True
