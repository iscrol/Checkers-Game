import pygame


WIDTH, HEIGHT = 800, 800
pygame.init()
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Checkers")

#colors
BEIGE = (245,245,220)
BLACK = (0,0,0)
BROWN = (102,51,0)
GREEN = (118,150,86)
RED = (200,0,0)

#FPS
FPS = 60

#Board size
squares_per_row = 8
squares_per_column = 8

#Font
FONT = pygame.font.Font('freesansbold.ttf',64)

'''def func():
    x = []
    x.insert(0,((range(100,200),range(300,400)),((3,5),(0,0),(0,0))))
    x.insert(1, ((range(500, 600), range(600, 700)), ((4,4),(4,3),(0,0))))
    x.insert(2, ((range(200, 300), range(0, 100)), ((1, 1),(2,2),(3,3))))
    return x

for i in func():
    for j in i[1]:
        if j[0] != 0 and j[1] != 0:
            print(j)


for i in range(len(func())):
    print(i)'''


'''def recursive(n,bool):
    coords = []
    def recursive_help(n,bool):
        if bool == True:
            return coords
        else:
            if n > 3:
                bool = True
                #coords.append(n)
                #return coords
            else:
                coords.append(n)
                recursive_help(n+1,bool)
                return coords
    return recursive_help(n,bool)

def countdown(n):
    blah = []
    def countdown_aux(n):
        if n != 1:
            blah.append(n)
            countdown_aux(n-1)
            return blah
    return countdown_aux(n)

l1 = [1,2,4,5,6,7,9]
l2 = l1
l2.remove(4)
print(l2)'''

#this is a test
