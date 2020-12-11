x=10
y=250  #координаты квадрата
flag=0 #Если flag == 0 значит обычная прорисовка, если flag == 1 значит прыжок
def setup():
    background(0)
    size(1000,400)
def draw():
    global x,y,flag
    global temp # переменная для прыжка
    background(0)
    rect(x, y, 10, 10)    
    if flag==1 and temp>=5: # квадрат поднимается
        x+=1
        y-=9
        temp-=1
    if flag==1 and temp <5: # квадрат опускается
        x+=1
        y+=9
        temp-=1
    if flag==1 and temp < 0: # конец прыжка, теперь обычная прорисовка
        flag=0       
    else: # обычная прорисовка
        if mousePressed and mouseButton == (RIGHT):
            x+=10
        if mousePressed and mouseButton == (LEFT):
            x-=10
                
def keyPressed(): # выполняется при нажатии любой клавиши
    global x,y,flag,temp
    flag=1
    temp=9
    
        
        
    
        
