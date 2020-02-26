import pygame

class Character:
    def __init__(self, screen):
        self.x = 100
        self.y = 100
        self.speed = 2
        self.direction = 0
        self.up_velocity = 0
        self.gravitation = 1
        self.grounded = True
        self.screen = screen
        self.running = False
        self.jump_force = 20
        self.size = 96

        self.animations = {
            "idle": {
                "sprite": pygame.image.load('character/Pink_Monster_Idle_4.png'),
                "stages": 4,
                "speed": 0,
                "ticks": 10
            },
            "walk": {
                "sprite": pygame.image.load('character/Pink_Monster_Walk_6.png'),
                "stages": 6,
                "speed": 1,
                "ticks": 8
            },
            "run": {
                "sprite": pygame.image.load('character/Pink_Monster_Run_6.png'),
                "stages": 6,
                "speed": 3,
                "ticks": 5
            },
            "jump": {
                "sprite": pygame.image.load('character/Pink_Monster_Jump_8.png'),
                "stages": 8,
                "speed": 0,
                "ticks": 12
            }
        }

        self.animation = {
            "last": "idle",
            "current": "idle",
            "stage": 0,
            "tick": 0
        }

    def current_animation_speed(self):
        if self.animation["current"] == "jump":
            self.animations[self.animation["current"]]["speed"] = self.animations[self.animation["last"]]["speed"]

        return self.animations[self.animation["current"]]["speed"]

    def set_idle(self):
        if self.grounded:
            self.animation["current"] = "idle"
        else:
            self.animation["current"] = "jump"

    def move(self, dir):
        self.direction = dir
            
        if self.grounded:
            if self.running:
                self.animation["current"] = "run"
            else:
                self.animation["current"] = "walk"
        else:
            self.animation["current"] = "jump"

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def jump(self):
        if(self.grounded):
            self.up_velocity = self.jump_force
            self.grounded = False

    def update(self, obstacles):
        self.x = self.x + self.speed * self.direction * self.current_animation_speed()
        self.y = self.y - self.up_velocity

        for o in obstacles:
            if (self.y + self.size) > o.y and (self.y+self.size+self.up_velocity) <= o.y and o.x < (self.x+self.size/2) and (o.x + o.width) > (self.x+self.size/2):
                self.y = o.y - self.size
                self.up_velocity = 0
                self.grounded = True

        self.up_velocity = self.up_velocity - self.gravitation
        
        if(self.animation["last"] != self.animation["current"]):
            self.animation["stage"] = 0

        self.animation["last"] = self.animation["current"]

        print(self.y)

    def draw(self):
        ca = self.animations[self.animation["current"]]

        c = pygame.Surface((32, 32))
        start = 32 * self.animation["stage"]
        image = ca["sprite"]
        c.blit(image, (0, 0), (start, 0, 32, 32))

        if(self.direction == -1):
            c = pygame.transform.flip(c,1,0)

        c = pygame.transform.scale(c, (self.size, self.size))

        self.screen.blit(c, (self.x, self.y))
        
        self.animation["tick"] = (self.animation["tick"] + 1) % ca["ticks"]

        if(self.animation["tick"] == 0):
            self.animation["stage"] = (self.animation["stage"] + 1) % ca["stages"]