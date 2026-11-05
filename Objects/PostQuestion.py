import pygame
from GameFrame import TextObject, Globals   


class PostQuestion(TextObject):
    def __init__(self, room, x, y):
        TextObject.__init__(
            self, room, x, y,
            "Post a photo showing your home address?",
            size=36,
            font="Arial",
            colour=(255, 255, 255)
        )

        self.handle_key_events = True
        self.answered = False
        self.finished = False
        self.question_index = 0

        self.questions = [
            {
                "question": "Post a photo showing your home address?",
                "post": "Someone learns where you live.",
                "pass": "Your home address stays private.",
                "risky": True
            },
            {
                "question": "Post your phone number publicly?",
                "post": "Strangers can contact your phone.",
                "pass": "Your phone number stays private.",
                "risky": True
            },
            {
                "question": "Post a drawing with no personal information?",
                "post": "You share your creativity safely.",
                "pass": "You choose to keep your drawing private.",
                "risky": False
            },
            {
                "question": "Post your password in a comment?",
                "post": "Someone could access your account.",
                "pass": "You protect your account.",
                "risky": True
            },
            {
                "question": "Post your live location publicly?",
                "post": "Strangers can see where you are right now.",
                "pass": "Your current location stays private.",
                "risky": True
            }
        ]

        if Globals.DIFFICULTY == "Medium":
            self.questions = [
                {
                    "question": "Post a selfie with your school ID visible?",
                    "post": "Your ID reveals personal details in the background.",
                    "pass": "You hide your ID before sharing the photo.",
                    "risky": True
                },
                {
                    "question": "Post a friend's photo after they agree?",
                    "post": "You share a harmless photo with their permission.",
                    "pass": "You choose to keep the photo private.",
                    "risky": False
                },
                {
                    "question": "Post your daily walking route publicly?",
                    "post": "People could work out where to find you.",
                    "pass": "You keep your daily routine private.",
                    "risky": True
                }
            ]
        if Globals.DIFFICULTY == "Hard":
            self.questions = [
                {
                    "question": "Post a holiday photo with your boarding pass visible?",
                    "post": "The booking code could expose travel details.",
                    "pass": "You cover the booking details before sharing.",
                    "risky": True
                },
                {
                    "question": "Post a scenery photo after leaving, with location off?",
                    "post": "You share scenery without revealing where you are now.",
                    "pass": "You choose to keep the photo private.",
                    "risky": False
                },
                {
                    "question": "Post a quiz answer naming your first pet?",
                    "post": "It could reveal an answer to a security question.",
                    "pass": "You keep possible account recovery details private.",
                    "risky": True
                }
            ]

        self.text = self.questions[0]["question"]
        self.update_text()

    def key_pressed(self, key):
        if self.finished:
            if key[pygame.K_r]:
                Globals.next_level = 0
                self.room.running = False
            return

        if self.answered:
            if key[pygame.K_SPACE]:
                if Globals.FOOTPRINTS >= Globals.DIFFICULTY_LIVES[Globals.DIFFICULTY]:
                    self.text = "Game over: you left too much private information online."
                    self.update_text()
                    self.room.instructions.text = "Press R to restart"
                    self.room.instructions.update_text()
                    self.finished = True
                    return

                self.question_index += 1

                if self.question_index >= len(self.questions):
                    if Globals.FOOTPRINTS == 0:
                        self.text = "Years later, you have kept your personal details private."
                    elif Globals.FOOTPRINTS == 1:
                        self.text = "Years later, an old post reminds you to check your privacy."
                    else:
                        self.text = "Years later, you find old personal details still online."
                    self.update_text()
                    self.room.instructions.text = "Press R to restart"
                    self.room.instructions.update_text()
                    self.finished = True
                    return

                self.text = self.questions[self.question_index]["question"]
                self.update_text()

                self.room.instructions.text = "P = Post     X = Pass"
                self.room.instructions.update_text()
                self.answered = False

            return

        question = self.questions[self.question_index]

        if key[pygame.K_p]:
            self.text = question["post"]

            if question["risky"]:
                Globals.FOOTPRINTS += 1

        elif key[pygame.K_x]:
            self.text = question["pass"]

        else:
            return

        self.answered = True
        self.update_text()
        self.room.footprints.refresh()

        self.room.instructions.text = "Press SPACE to continue"
        self.room.instructions.update_text()
