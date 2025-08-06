import math,pygame,sys

SCHWARZ = (0,0,0)
BLAU    = (17,69,126)
ROT     = (255,0,0)
ROT2    = (215,20,26)
ROT3    = (238,0,0)
WEISS   = (255,255,255)
GRUEN   = (46,139,87)
GELB    = (255,215,0)
GOLD    = (255,206,0)

def pentagramm(cx,cy,cr):
    punkte = []
    r = math.sqrt((25-11*math.sqrt(5))/10)
    R = math.sqrt((5-math.sqrt(5))/10)
    for i in range(5):
        x1 = cx+cr*R*math.sin(2*i*math.pi/5)
        y1 = cy-cr*R*math.cos(2*i*math.pi/5)
        punkte.append((x1,y1))
        x2 = cx+cr*r*math.sin((2*i+1)*math.pi/5)
        y2 = cy-cr*r*math.cos((2*i+1)*math.pi/5)
        punkte.append((x2,y2))
    return(punkte)

width = 900
height = 600
pygame.init()
screen = pygame.display.set_mode((width,height),pygame.RESIZABLE)
pygame.display.set_caption("Flaggen")

P = pentagramm(3*height/10,3*height/10,height/3)

while True:
    pygame.event.wait()

    for event in pygame.event.get():
        # Wurde das Fenster geschlossen?
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.VIDEORESIZE:
            (width,height) = screen.get_size()
            P = pentagramm(3*height/10,3*height/10,height/3)

    # Japan
    # screen.fill(WEISS)
    # pygame.draw.circle(screen,ROT,(450,300),180)

    # Deutschland
    # R = pygame.Rect(0,0,900,200)
    # pygame.draw.rect(screen,SCHWARZ,R)
    # R = pygame.Rect(0,200,900,200)
    # pygame.draw.rect(screen,ROT,R)
    # R = pygame.Rect(0,400,900,200)
    # pygame.draw.rect(screen,GOLD,R)

    # Tschechien
    # pygame.draw.polygon(screen,BLAU,[(0,0),(450,300),(0,600)])
    # pygame.draw.polygon(screen,WEISS,[(0,0),(900,0),(900,300),(450,300)])
    # pygame.draw.polygon(screen,ROT2,[(450,300),(900,300),(900,600),(0,600)])

    # Togo

    for i in range(3):
        R = pygame.Rect(0,2*i*height/5,width,height/5)
        pygame.draw.rect(screen,GRUEN,R)
    for i in range(2):
        R = pygame.Rect(0,(2*i+1)*height/5,width,height/5)
        pygame.draw.rect(screen,GELB,R)

    R = pygame.Rect(0,0,3*height/5,3*height/5)
    pygame.draw.rect(screen,ROT3,R)

    pygame.draw.polygon(screen,WEISS,P)

    pygame.display.update()


