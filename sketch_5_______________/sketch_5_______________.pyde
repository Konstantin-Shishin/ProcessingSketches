def setup():
    size(600,600)
    background(0)
    
def draw(): 
    fill(255)
    if mousePressed:
        background(0)
        translate(pmouseX,pmouseY)
        triangle(-20,0,20,0,0,-20)
