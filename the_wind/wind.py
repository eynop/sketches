class Wind:
    
    COLOR = 217
    TRANSPARENCY = 50
    
    def __init__(self):
        self.rays = [Ray(random(width), random(height)) for i in range(20)]
    
    def display(self):
        for ray in self.rays:
            stroke(Wind.COLOR, Wind.TRANSPARENCY)
            ray.display()
            ray.x -= 3
            if ray.x < 0:
                ray.x = random(width)
                ray.y = random(height)
        

class Ray:

    HEIGHT = 3
    LENGTH = 20
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def display(self):
        strokeWeight(Ray.HEIGHT)
        strokeCap(PROJECT)
        line(self.x - Ray.LENGTH/2, self.y, self.x + Ray.LENGTH/2, self.y)
