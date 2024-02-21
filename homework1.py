#Date: 7/2/2024
#Lesson no:9 Galaga Game
#Make a game similar to Gallaga using your own characters/ creativity
import pgzrun
import random
WIDTH=600
HEIGHT=600
cat=Actor("cat")
cat.x=300
cat.y=400
bowl=Actor("bowl")
bowl.x=300
bowl.y=100
score=0
fishes=[]
def draw():
    screen.fill("paleturquoise")
    cat.draw()
    bowl.draw()
    for b in fishes:
        b.draw()
        screen.draw.text(str(score),color="lime green",topleft=(15,15))
def update():
    if keyboard.w:
        cat.y-=10
    if keyboard.s:
        cat.y+=10
    if keyboard.d:
        cat.x+=10
    if keyboard.a:
        cat.x-=10
    if keyboard.space:
        fish=Actor("fish")
        fish.x=cat.x
        fish.y=cat.y-320
        fishes.append(fish)    
    global score
    for fish in fishes:
        if fish.colliderect(bowl):
            fishes.remove (fish)
            bowl.x=random.randint(50,475)
            score=score+1
        else:
            score=score-1
            screen.draw.text("you lost the fishes!",color="black",center=(250,250))
            bones=Actor("bones")
            bones.x=300
            bones.y=110
            bones.draw()

#https://imageresizer.com/
#https://www.remove.bg/
#Continue making your game with resize images and apply the concepts that we did in todays lesson