import pygame 


pygame.init() 
win = pygame.display.set_mode((763, 429)) 

pygame.display.set_caption("FNAF - Charles Location")


x = 60
y = 180
width = 40
height = 40
vel = 10
FPS = 60 
run = True


circus = pygame.image.load  ('Images/idle1.png')
circus2 = pygame.image.load ('Images/idle4.png')
circus3 = pygame.image.load ('Images/attack2.png')
circus4 = pygame.image.load ('Images/attack.png')

fundo = pygame.image.load('Images/SL_05_FINAL.gif')

while run: 
    
    pygame.time.delay(5) 
      
    
    for event in pygame.event.get(): 
        
      
        if event.type == pygame.QUIT: 
                  run = False
    
    keys = pygame.key.get_pressed() 
      
    
    if keys[pygame.K_a] and x>0: 
        
        x -= vel 
          
        pygame.display.flip()
        win.blit(fundo,(0, 0))
        win.blit(circus2, (x, y))

    
    if keys[pygame.K_d] and x<500-width: 
        
        x += vel 
         
        pygame.display.flip()
        win.blit(fundo,(0, 0))
        win.blit(circus, (x, y))
    
    if keys[pygame.K_s]:

        pygame.display.flip()
        win.blit(fundo,(0, 0))
        win.blit(circus3, (x, y))

    if keys[pygame.K_w]:

        pygame.display.flip()
        win.blit(fundo,(0, 0))
        win.blit(circus4, (x, y))



    pygame.display.update()  
pygame.quit() 