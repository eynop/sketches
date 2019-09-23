from wind import Wind

wind = None

def setup():
    global wind
    size(400, 600)
    wind = Wind()
    
    
def draw():
    background(0)
    wind.display()
