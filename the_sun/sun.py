def _get_cos(angle):
    return cos(radians(360 - angle))


def _get_sin(angle):
    return sin(radians(360 - angle))


class Sun:
    
    COLOR = "#FFB476"
    
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.sunlight = Sunlight(self.x, self.y, self.radius)
        
    def display(self):
        noStroke()
        fill(Sun.COLOR)
        ellipseMode(RADIUS)
        circle(self.x, self.y, self.radius)

        self.sunlight.display()

        ellipseMode(CENTER) # reset the mode


class Sunlight:

    OPENING_ANGLE = 8
    CLOSING_ANGLE = 13
    
    def __init__(self, x, y, sun_radius):
        self.x = x
        self.y = y
        self.sun_radius = sun_radius
        
    def display(self):
        for angle in range(0, 360, 90):
            self.beam(angle)
        
        for angle in range(45, 360, 90):
            self.beam(angle, 0.7) 
        
    def beam(self, angle, strength=1):
        beam_offset = self.sun_radius * 1.33
        beam_length = self.sun_radius * 2.83 * strength
        
        x1 = self.x + _get_cos(angle - Sunlight.OPENING_ANGLE/2) * beam_offset
        x2 = self.x + _get_cos(angle + Sunlight.OPENING_ANGLE/2) * beam_offset
        x3 = self.x + _get_cos(angle + Sunlight.CLOSING_ANGLE/2) * beam_length
        x4 = self.x + _get_cos(angle - Sunlight.CLOSING_ANGLE/2) * beam_length
        
        y1 = self.y + _get_sin(angle - Sunlight.OPENING_ANGLE/2) * beam_offset
        y2 = self.y + _get_sin(angle + Sunlight.OPENING_ANGLE/2) * beam_offset
        y3 = self.y + _get_sin(angle + Sunlight.CLOSING_ANGLE/2) * beam_length
        y4 = self.y + _get_sin(angle - Sunlight.CLOSING_ANGLE/2) * beam_length
        
        quad(x1,y1,x2,y2,x3,y3,x4,y4)
        
