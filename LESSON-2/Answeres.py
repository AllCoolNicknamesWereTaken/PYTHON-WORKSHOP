import pygame
import random
from random import randint
# how to display a window?
# how to display a pixel and how to change its colour?
width, height = 725, 545
size = (width, height)
width1, height2 = (720/3), (540/3)

screen = pygame.display.set_mode(size) #dlaczego tu sa dwa nawiasy lol
background_colour = (0, 0, 0)
running = True
pixel_ar = []
screen.fill(background_colour)
step = 30
change = []

for row in range(5, (height - 5), step):
    line = []
    change_line = []
    for column in range(5, (width - 5), step):
        # line.append(randint(0, 1))
        line.append(0)
        change_line.append(0)

    pixel_ar.append(line)
    change.append(change_line)

# pixel_ar[5][5] = 1
# pixel_ar[6][5] = 1
# pixel_ar[7][5] = 1
# pixel_ar[6][6] = 1
# pixel_ar[6][7] = 1
pixel_ar[5][15] = 1
pixel_ar[6][14] = 1
pixel_ar[6][13] = 1
pixel_ar[5][13] = 1
pixel_ar[4][13] = 1
# change[5][15] = 1
# change[6][14] = 1
# change[6][13] = 1
# change[5][13] = 1
# change[4][13] = 1

pygame.init()
for (i, row) in enumerate(pixel_ar):
    for (j, cell) in enumerate(row):
        if pixel_ar[i][j] == 0:
            pygame.draw.rect(screen, (225, 225, 255), ((step * j + 5), (step * i + 5), (step-5), (step-5)))
            # print(pygame.time.get_ticks() + 1)
        else:
            # print((step * j + 5), (step * i + 5), (step-5), (step-5))
            pygame.draw.rect(screen, (0, 225, 255), ((step * j + 5), (step * i + 5), (step-5), (step-5)))


pygame.display.flip()
pygame.display.set_caption('moje okienko')

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # if pygame.time.get_ticks() % 100 == 0:
            #     for i in range(len(pixel_ar) - 1 ):
            #         for j in range(len(pixel_ar[i]) - 1):
            #             if pixel_ar[i][j] == 0 and (pixel_ar[i+1][j] + pixel_ar[i - 1][j]
            #             + pixel_ar[i][j + 1] + pixel_ar[i][j - 1]) == 3 :
            #                 pixel_ar[i][j] = 1
            #                 pygame.draw.rect(screen, (0, 225, 255), ((step * j + 5), (step * i + 5), (step-5),(step-5)))
            #
            #
            #
            #                     # pygame.draw.rect(screen, (225, 225, 255), ((step * j + 5), (step * i + 5), (step-5),(step-5)))
            #
            #             else :
            #                 pygame.draw.rect(screen, (0, 225, 255), ((step * j + 5), (step * i + 5), (step-5),(step-5)))
            running = False
    if pygame.time.get_ticks() % 500 == 0:
        # print(pixel_ar)
        # print(len(pixel_ar[0]))
        # for i in range(1, len(pixel_ar) - 1):
        #     for j in range(1, len(pixel_ar[i]) - 1):
        for (i, row) in enumerate(pixel_ar):
            for (j, cell) in enumerate(row):

                # if i == 0:
                #     if j == 0:
                #         neighbours = pixel_ar[i+1][j] + pixel_ar[i][j + 1]
                #     else:
                #     neighbours = pixel_ar[i+1][j] + pixel_ar[i][j + 1] + pixel_ar[i][j - 1]
                # if
                # print("e")
                # print("%d, %d", i, j)
                # print("ELO", i, j)

                bottom = pixel_ar[i + 1][j] if len(pixel_ar) > i+1 else 0
                top = pixel_ar[i - 1][j] if i > 0 else 0
                right = row[j + 1] if len(row) > j+1 else 0
                left = row[j - 1] if j > 0 else 0
                bottom_right = pixel_ar[i + 1][j + 1] if (len(pixel_ar) > i+1 and len(row) > j+1) else 0
                bottom_left = pixel_ar[i + 1][j - 1] if (len(pixel_ar) > i+1 and j > 0) else 0
                top_right = pixel_ar[i - 1][j + 1] if (i > 0 and len(row) > j+1) else 0
                top_left = pixel_ar[i - 1][j - 1] if (i > 0 and j > 0) else 0

                neighbours = bottom + top + right + left + bottom_right + bottom_left + top_left + top_right

                if neighbours > 0:
                    # print(bottom, top, right, left)
                    print(i, j, neighbours)

                if cell == 0 and neighbours == 3:
                    change[i][j] = 1;
                    # pixel_ar[i][j] = 1
                    # pygame.draw.rect(screen, (255, 0, 255), ((step * j + 5), (step * i + 5), (step-5),(step-5)))
                        # pygame.draw.rect(screen, (225, 225, 255), ((step * j + 5), (step * i + 5), (step-5),(step-5)))

                elif cell == 1 and (neighbours == 1 or neighbours == 0 or neighbours == 4):
                    change[i][j] = 0

                else:
                    if cell > 0:
                        print("ZOSTAJE", cell)
                    change[i][j] = cell

                    # pixel_ar[i][j] = 0
                    # pygame.draw.rect(screen, (255, 255, 255), ((step * j + 5), (step * i + 5), (step-5),(step-5)))

        for (i, row) in enumerate(pixel_ar):
            for (j, cell) in enumerate(row):
                pixel_ar[i][j] = change[i][j]
                # change[i][j] = 0

        for (i, row) in enumerate(pixel_ar):
            for (j, cell) in enumerate(row):
                if cell == 0:
                    pygame.draw.rect(screen, (225, 225, 255), ((step * j + 5), (step * i + 5), (step-5),(step-5)))
                    # print(pygame.time.get_ticks() + 1)
                else:
                    pygame.draw.rect(screen, (0, 225, 255), ((step * j + 5), (step * i + 5), (step-5),(step-5)))


        pygame.display.update()
