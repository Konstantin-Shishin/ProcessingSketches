value = 0
def draw(): 
    fill(value)
    rect(25, 25, 50, 50)

def mouseClicked(): 
    global value
    if value == 0:
        value = 255
    else:
        value = 0
