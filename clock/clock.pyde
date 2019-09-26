clock_radius = 400


def _get_cos(angle):
    return cos(radians(360 - angle))


def _get_sin(angle):
    return sin(radians(360 - angle))


def setup():
    size(900, 900)
    font = createFont("font/ShareTechMono-Regular.ttf", 120);
    textFont(font)
    textAlign(CENTER, CENTER)


def draw():
    
    background(0)
    
    fill('#ff0000')
    for i in range(0, 60, 5):
        x = width/2 + (clock_radius + 15) * _get_cos(90 - (360/60) * i)
        y = height/2 + (clock_radius + 15) * _get_sin(90 - (360/60 * i))
        circle(x, y, 10)

    fill(255)
    for i in range(second() + 1):
        x = width/2 + clock_radius * _get_cos(90 - (360/60) * i)
        y = height/2 + clock_radius * _get_sin(90 - (360/60 * i))
        circle(x, y, 10)
        
    s = '{} : {}'.format(hour(), minute())
    text(s, width/2, height/2)
    
