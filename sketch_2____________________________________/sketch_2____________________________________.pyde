h=150
mode=1
def setup():
    size(600,600)
    background(0)
    
def draw(): 
    global h,mode
    fill(255) 
    translate(300,300)
    ellipse(0,0,h,h)
    if h>600 or h<0 :
        mode=-mode
    h+=mode
    
def mouseClicked():
    global h
    h=150
    background(0)
