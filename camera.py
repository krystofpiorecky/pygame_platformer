class Camera:
    def __init__(self, character, width, height):
        self.speed = 0.1
        self.character = character
        self.x = character.x + width/2
        self.y = character.y + height/2
        self.width = width
        self.height = height

    def update(self):
        self.x = self.x + self.width/2
        self.y = self.y + self.height/2

        self.x = self.x + (self.character.x - self.x) * self.speed
        self.y = self.y + (self.character.y - self.y) * self.speed

        self.x = self.x - self.width/2
        self.y = self.y - self.height/2