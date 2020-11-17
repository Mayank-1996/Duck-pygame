import pygame as pg
import sys
import random,time

pg.init()
# Start the game
screen = pg.display.set_mode((1280,720))

land = pg.image.load("Land_BG.png")
water = pg.image.load("Water_BG.png")
wood = pg.image.load("Wood_BG.png")

cloud1=pg.image.load("Cloud1.png")
cloud2=pg.image.load("Cloud2.png")
duck = pg.image.load("duck.png")
crosshair=pg.image.load("crosshair.png")
yes=pg.image.load("yes.png")
no=pg.image.load("no.png")
score=0

# font

play_again=pg.font.Font(None,80)
game_over = pg.font.Font(None,40)
myscore=pg.font.Font(None,60)
game_message=game_over.render('Game Over !!',True,(0, 102, 255))
play_again_text=play_again.render("Do You want to Play Again ??",True,(255,201,10))
message_rect=game_message.get_rect(center=(640,360))


pg.mouse.set_visible(False)

ducks=[]

water_position=600
water_velocity=1.5
duck_velocity=[2]*20
duck_images=[duck]*20

for i in range(20):
    duck_x=random.randint(50,1200)
    duck_y=random.randint(300,600)
    duck_new=duck.get_rect(center=(duck_x,duck_y))
  
    ducks.append(duck_new)

yes_rect=yes.get_rect(center=(430,320))
no_rect=no.get_rect(center=(820,320))

def getScore():
    game_score=myscore.render('Score '+str(score),True,(252, 3, 32))
    score_rect=game_score.get_rect(center=(90,70))
    screen.blit(game_score,score_rect)

start_time = pg.time.get_ticks()
print(start_time)
running = True


def new_game():
    screen.blit(play_again_text,(250,200))
    screen.blit(yes,yes_rect)
    screen.blit(no,no_rect)

    if yes_rect.collidepoint(event.pos):
        reset()
    elif no_rect.collidepoint(event.pos):
        running=False

while running:

    current_time=pg.time.get_ticks()
    duration=(current_time-start_time)/1000
    
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type==pg.MOUSEMOTION:
            crosshair_rect=crosshair.get_rect(center=event.pos)
        if event.type==pg.MOUSEBUTTONDOWN:
            for index,duck1 in enumerate(ducks):
                # if crosshair_rect.colliderect(duck1):
                #     del ducks[index]
                
                if duck1.collidepoint(event.pos):
                    del ducks[index]
                    del duck_images[index]
                    del duck_velocity[index]
                    score+=1
                    break
    
               
                    
                

    

    screen.blit(wood,(0,0))
    screen.blit(land,(0,550))
    screen.blit(water,(0,water_position))

    getScore()

      
        
    for index,duck_rect in enumerate(ducks):
        screen.blit(duck_images[index],duck_rect)

    
    ## Game end Logic
    if len(ducks)<=0 or duration>=100:
        #screen.blit(game_message,message_rect)

        new_game()
        


    screen.blit(crosshair,crosshair_rect)
    
    screen.blit(cloud1,(150,100))
    screen.blit(cloud2,(750,100))
    screen.blit(cloud1,(1050,150))
    screen.blit(cloud2,(550,100))

    water_position+=water_velocity

    if water_position>=680 or water_position<=600:
        water_velocity*=-1

    
 
    for index,evry_duck in enumerate(ducks):
        evry_duck[0]+=duck_velocity[index]
        
   
    for index,every_duck in enumerate(ducks):
        if every_duck[0]>1170 or every_duck[0]<5:
            duck_velocity[index]*=-1
            duck_images[index]=pg.transform.flip(duck_images[index],True,False)
        


        
    
    pg.display.update()
    
