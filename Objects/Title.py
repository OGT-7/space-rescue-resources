from GameFrame import RoomObject, Globals
import pygame

class Title(RoomObject):
    """
    The object for displaying the title and difficulty selection
    """
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        # load and scale the title artwork
        title_img = pygame.image.load(self.load_image("PostOrPass_Title.png")).convert_alpha()
        title_img = pygame.transform.scale(title_img, (800, 350))

        # build a taller canvas so there's room below the art to place text
        # lower on the screen (art stays at the top, unchanged)
        canvas_height = 550
        canvas = pygame.Surface((800, canvas_height), pygame.SRCALPHA)
        canvas.blit(title_img, (0, 0))

        self.image_orig = canvas
        self.width = 800
        self.height = canvas_height
        self.image = self.image_orig.copy()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        # register for key events
        self.handle_key_events = True

        # difficulty selection setup
        self.font = pygame.font.SysFont(None, 48)
        self.difficulties = ["Easy", "Medium", "Hard"]
        self.diff_index = self.difficulties.index(Globals.DIFFICULTY)
        self.input_delay = 0

        self.draw_difficulty_text()

    def draw_difficulty_text(self):
        """
        Redraws the canvas (art + difficulty text near the bottom)
        """
        self.image = self.image_orig.copy()
        text = f"Difficulty: {self.difficulties[self.diff_index]}   (<- / -> to change)"
        text_surface = self.font.render(text, True, (255, 255, 0))
        text_x = self.width // 2 - text_surface.get_width() // 2
        text_y = self.height - text_surface.get_height() - 10
        self.image.blit(text_surface, (text_x, text_y))

    def step(self):
        """
        Counts down the input delay so holding a key doesn't spam-cycle options
        """
        if self.input_delay > 0:
            self.input_delay -= 1

    def key_pressed(self, key):
        """
        Handles difficulty selection and starting the game
        """
        if self.input_delay <= 0:
            if key[pygame.K_LEFT]:
                self.diff_index = (self.diff_index - 1) % len(self.difficulties)
                Globals.DIFFICULTY = self.difficulties[self.diff_index]
                self.draw_difficulty_text()
                self.input_delay = 10
            elif key[pygame.K_RIGHT]:
                self.diff_index = (self.diff_index + 1) % len(self.difficulties)
                Globals.DIFFICULTY = self.difficulties[self.diff_index]
                self.draw_difficulty_text()
                self.input_delay = 10

        if key[pygame.K_SPACE]:
            self.room.running = False