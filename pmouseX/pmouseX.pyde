# Быстро перемещайте мышь, чтобы увидеть разницу
# между текущей и предыдущей позицией
def draw(): 
    background(204)
    line(mouseX, 20, pmouseX, 80)
    print("%d : %d" % (mouseX, pmouseY))
