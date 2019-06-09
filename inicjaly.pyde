def setup():
    size(700,700)
    frameRate(60)
    textAlign(CENTER)
    background(200)
    textSize(200)
    fill(255,0,255)
    text("W" , width/2-50 , height/2 )
    text("J" , width/2 +50 , height/2)
    
    
    
def draw():
    
    if keyPressed:
        if key=='w' or keyCode ==37:  # bardzo dobre rozwiązanie, by spiąć to razem
            background(200)
            textSize(300)
            fill(255,0,255)
            text("w" , width/2 - 100 , height/2)
            textSize(250)
            fill(40,10,30)
            text("j" , width/2+ 100 , height/2 )
        if key=='j' or keyCode ==39: 
            background(200)
            textSize(300)
            fill(255,0,255)
            text("j" , width/2 +100 , height/2)
            textSize(250)
            fill(40,10,30)
            text("w" , width/2- 100 , height/2 )   
            
            # brakuje obsługi najechania myszą
    
    tr = createShape()
    tr.beginShape()
    tr.fill(70,70,70)
    tr.noStroke()
    tr.vertex(100,600)
    tr.vertex(500,600)
    tr.vertex(300,700)
    tr.vertex(200,300)
    tr.vertex(200,700)
    tr.endShape(CLOSE)
    shape(tr,0,0)
    
    
    
    
    
