def setup():
    size(500, 500)
    
def draw():
    if mousePressed:
        strokeWeight(25)
        stroke(random(0,255),random(0,255),random(0,255))
        line(mouseX, mouseY, pmouseX,pmouseY)
