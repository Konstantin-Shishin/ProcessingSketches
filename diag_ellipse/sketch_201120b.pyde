x = 0
y = 0
mode = 1
def setup():
  size(600,400)
  
def draw():
    global mode
    global x
    global y
    background(0)
    ellipse(x,y,40,40)
    x=x+3*mode
    y=y+2*mode
    if x >=600 and y>=400 or x <=0 and y<=0 :
        mode=-mode
        
  
