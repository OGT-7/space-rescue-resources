from Objects.PostQuestion import PostQuestion 
from GameFrame import Level, Globals, TextObject
from Objects.Ship import Ship
from Objects.Zork import Zork
from Objects.Hud import Score
from Objects.Hud import Score, Lives
from Objects.Hud import Footprints

class GamePlay(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # set background image
        self.set_background_image("PostOrPass_Background.png")

        Globals.FOOTPRINTS = 0
        self.footprints = Footprints(self, 30, 20)
        self.add_room_object(self.footprints)


        self.question = PostQuestion(self, 150, 250)
        self.add_room_object(self.question)

        self.instructions = TextObject(
            self, 350, 500,
            "P = Post     X = Pass",
            size=36, font="Arial", colour=(255, 255, 255)
        )
        self.add_room_object(self.instructions)
  

        # apply difficulty-based starting lives
        Globals.LIVES = Globals.DIFFICULTY_LIVES[Globals.DIFFICULTY]
        
        # add HUD items
        self.score = Score(self, 
                           Globals.SCREEN_WIDTH/2 - 20, 20, 
                           str(Globals.SCORE))
        self.add_room_object(self.score)

        # load sound files
        self.shoot_laser = self.load_sound("Laser_shot.ogg")
        self.asteroid_shot = self.load_sound("Asteroid_shot.wav")
        self.astronaut_saved = self.load_sound("Astronaut_saved.ogg")
        self.asteroid_collision = self.load_sound("Ship_damage.ogg")
        self.astronaut_shot = self.load_sound("Astronaut_hit.ogg")