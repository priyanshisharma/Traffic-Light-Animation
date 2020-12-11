'''
This program displays a traffic light animation
wherein the traffic light turns amber followed by
green on pressing any key on the keyboard.
'''

import time # This will be used to maintain time difference between amber and green light
        
class lights:
    def __init__(self):
        self.ch = 'R' #This contains which light is on
        
    def display(self):
        '''Displaying the traffic light'''
        fill(77,72,72) #RGB Colour inside the figure
        strokeWeight(0) #Border-width
        rect(545, 220, 15, 110) #Bottom thinner rectangle of the light
        rect(527, 142, 50, 127) #Upper wider rectangle of the light
        
        #Turning the light on and off by appropriate RGB colour
        if self.ch=='R': #Red
            fill(255,0,0)
        else:
            fill(203,32,32)
        circle(553, 165, 40) #circular traffic light
        
        if self.ch=='A': #Amber
            fill(255,213,0)
        else:
            fill(219,146,0)
        circle(553, 207, 40);
        
        if self.ch=='G': #Green
            fill(0,255,94)
        else:
            fill(94,216,139)
        circle(553, 248, 40);
        
class Car:
    def __init__(self):
        self.x=20 #x-coordinate of car
        self.y=300 #y-coordinate of car
        self.vx=5 #velocity of car in horizontal direction
    
    def update(self,tr_l):
        if(tr_l.ch=='R' or tr_l.ch=='A'): #If the light is amber or red
            if (self.x+self.vx)<300: #Stop at the traffic light
                self.x += self.vx
        else:
            if (self.x+self.vx)<1200: #If car is within the frame
                self.x += self.vx
    
    def display(self):
        #Display the car image at the car object's position
        global img
        img = loadImage("car.png")
        image(img, self.x,self.y)


tl = lights() #traffic light object
c = Car() #Car object

def setup():
    size(1100,400) #Making the Canvas
        
def draw():
    background(92,207,255) #Sky in backround
    
    #Writing my name and roll number
    fill(0);
    textSize(20);
    text("Roll: 18115060",width/2+310,50);
    text("Priyanshi Sharma",width/2+310,80);
    
    #Sun
    fill(255, 170, 0);
    ellipse(225, 60, 100, 100);
    
    # Clouds 
    fill(255, 255, 255)
    
    # Left cloud
    ellipse(195, 115, 126, 97)
    ellipse(195+62, 115, 70, 60)
    ellipse(195-62, 115, 70, 60)
    
    # Right Cloud
    ellipse(330, 70, 126, 97)
    ellipse(330+62, 70, 70, 60)
    ellipse(330-62, 70, 70, 60)
    
    #Drawing the road
    fill(120,128,131)
    strokeWeight(0)
    rect(0, 330, 1100, 70)
    
    #Drawing the markings on the road
    strokeWeight(5)
    stroke(201)
    for i in range(0,1100,50):
        line(i, 375, i+10, 375)
        
    #Displaying the traffic light    
    tl.display()
    
    #Updating and Displaying the car according to the traffic light
    c.update(tl)
    c.display()
    
    #Change colours once key is pressed
    if keyPressed:
        if tl.ch=='R': #If red change to amber
            tl.ch='A'
            tl.display()
        else: #If amber change to green
            time.sleep(2) #Change to green after 2 seconds (of Amber)
            tl.ch='G'
    else: #Display, click to make it green
        if tl.ch!='G':
            fill(0)
            text("Click to make the light green",width/2-70,50);
            
