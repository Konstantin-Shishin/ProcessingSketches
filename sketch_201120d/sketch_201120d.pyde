angle = -70
angleChange = 1

def setup():
    size(600,400)

def draw():
    background(100)
    global angle, angleChange
    translate(300,200) # в центр
    push()
    translate(100,-50) # а теперь правее и левее
    rotate(radians(angle))
    ellipse(20,0,60,20) # смещу центр эллипса от точки вращения на 20
    pop()
    ellipse(0,0,60,20)
    
    angle = angle + angleChange
    if angle == -70 or angle == - 20:
        angleChange = - angleChange
