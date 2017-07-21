import ccircle
North = 0
East = 1
South = 2
West = 3

class Ambrose:
    def __init__(self, x, y):
        self.speed = 310
        self.counter = 0
        self.x = x
        self.y = y
        self.facing = "right"
        self.action = "idle"
        self.image = {
            "walk_left":[ccircle.Image("image/AA_AmbroseSideW(2).png"),
                            ccircle.Image("image/AA_AmbroseSideW.png"),
                           ],
            "walk_right":[ccircle.Image("image/AA_AmbroseCharModel(4).png"),
                             ccircle.Image("image/AA_AmbroseCharModel(5).png"),
                             ],
            "walk_front":[ccircle.Image("image/AA_AmbroseCharModel(6).png"),
                               ccircle.Image("image/AA_AmbroseCharModel(2).png"),
                               ],
            "walk_back":[ccircle.Image("image/AA_AmbroseBehind(W).png"),
                                ccircle.Image("image/AA_AmbroseBehind(W2).png")
                                ],
            "idle_left":[ccircle.Image("image/AA_AmbroseSideStop.png"),
                         ],
            "idle_right":[ccircle.Image("image/AA_AmbroseCharModel(3).png"),
                          ],
            "idle_front":[ccircle.Image("image/AA_AmbroseCharModel.png"),
                            ],
            "idle_back":[ccircle.Image("image/AA_AmbroseBehind.png"),
                             ]
        }

        for anim, frames in self.image.items():
            for frame in frames:
                frame.eraseGreen()

    def draw(self, window):
        state = self.action +"_"+ self.facing
        frame = int(self.counter/0.3) % len(self.image[state])
        self.image[state][frame].draw(self.x - 65, self.y - 196, 160, 212)



    def update(self, dt):
        for obj in self.world.objects:
            if obj.getType() == "door":
               if obj.x<= self.x<= obj.x + obj.width and obj.y<= self.y<= obj.y + obj.height:
                    self.world.remove(self)
                    obj.link.add(self)
                    self.x = obj.linkx
                    self.y = obj.linky
                    break
        self.counter+=dt

        newx = self.x
        newy = self.y
        if ccircle.isKeyDown('left'):
            self.facing = "left"
            self.action = "walk"
            newx  -=self.speed*dt
        elif ccircle.isKeyDown('right'):
            self.facing = "right"
            self.action = "walk"
            newx  +=self.speed*dt
        elif ccircle.isKeyDown('up'):
            self.facing = "back"
            self.action = "walk"
            newy -=self.speed*dt
        elif ccircle.isKeyDown('down'):
            self.facing = "front"
            self.action = "walk"
            newy  +=self.speed*dt
        else:
            self.action = "idle"

        r, g, b, a = self.world.collision.getPixel(int(newx), int(newy))
        if r == 1:
            self.x = newx
            self.y = newy

    def getType(self):
        return "player"

