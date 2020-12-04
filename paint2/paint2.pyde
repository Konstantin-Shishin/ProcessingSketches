def setup():
    size(500, 500)
    background(126)
    noStroke()

def draw():
    if mousePressed and (mouseButton == LEFT):
        fill(126)
    elif mousePressed and (mouseButton == RIGHT):
        fill(random(0,255), random(0,255), random(0,255))
    else:
        rect(mouseX, mouseY, 50, 50)
