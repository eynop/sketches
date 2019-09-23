from sun import Sun

sun = None

def setup():
    global sun
    size(400, 600)
    sun = Sun(width/2, height/2, 30)
    
def draw():
    background(0)
    sun.display()
    
