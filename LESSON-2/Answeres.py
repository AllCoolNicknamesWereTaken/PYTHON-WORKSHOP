import pygame
import random
from random import randint
import argparse
# how to display a window?
# how to display a pixel and how to change its colour?
def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-color")
    parser.add_argument("-background")
    args = parser.parse_args()
    print(args.color)
    color = tuple(map(int, args.color[1:-1].split(',')))
    bgcolor = tuple(map(int, args.background[1:-1].split(',')))


    width, height = 725, 545
    size = (width, height)
    width1, height2 = (720/3), (540/3)

    screen = pygame.display.set_mode(size) #dlaczego tu sa dwa nawiasy lol
    background_colour = bgcolor #(0, 0, 0)
    running = True
    stop = True;
    pixel_ar = []
    screen.fill(background_colour)
    step = 5
    change = []
    mousePosition = pygame.mouse.get_pos()

    for (i, row) in enumerate(range(5, (height - 5), step)):
        line = []
        change_line = []
        for column in range(5, (width - 5), step):
            # line.append(randint(0, 1))
            if (row == 5 + step * 60) :
                line.append(1)
                change_line.append(1)
            else:
                line.append(0)
                change_line.append(0)

        pixel_ar.append(line)
        change.append(change_line)





    pygame.init()
    def BoardUpdate():
        for (i, row) in enumerate(pixel_ar):
            for (j, cell) in enumerate(row):
                if pixel_ar[i][j] == 0:
                    pygame.draw.rect(screen, bgcolor, ((step * j + 5), (step * i + 5), (step-5), (step-5)))

                else:
                    pygame.draw.rect(screen, color, ((step * j + 5), (step * i + 5), (step-5), (step-5)))
        pygame.display.flip()

    BoardUpdate()
    pygame.display.set_caption('moje okienko')

    while running:
        for event in pygame.event.get():
            if pygame.mouse.get_pressed().index(0) and stop == True:
                mousePosition = pygame.mouse.get_pos()
                print(" {}, {}".format(int(True), bool(0)))
                pixel_ar[int(mousePosition[1] / step)][int(mousePosition[0] / step)]= \
                (int(not bool(pixel_ar[int(mousePosition[1] / step)][int(mousePosition[0] / step)])))

                BoardUpdate()


            if event.type == pygame.QUIT or (event.key == pygame.K_ESCAPE if event.type == pygame.KEYDOWN else False) :
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    stop = not stop;
        if pygame.time.get_ticks() % 100 == 0 and stop == False:
            for (i, row) in enumerate(pixel_ar):
                for (j, cell) in enumerate(row):
                    bottom = pixel_ar[i + 1][j] if len(pixel_ar) > i+1 else 0
                    top = pixel_ar[i - 1][j] if i > 0 else 0
                    right = row[j + 1] if len(row) > j+1 else 0
                    left = row[j - 1] if j > 0 else 0
                    bottom_right = pixel_ar[i + 1][j + 1] if (len(pixel_ar) > i+1 and len(row) > j+1) else 0
                    bottom_left = pixel_ar[i + 1][j - 1] if (len(pixel_ar) > i+1 and j > 0) else 0
                    top_right = pixel_ar[i - 1][j + 1] if (i > 0 and len(row) > j+1) else 0
                    top_left = pixel_ar[i - 1][j - 1] if (i > 0 and j > 0) else 0

                    neighbours = bottom + top + right + left + bottom_right + bottom_left + top_left + top_right
                    if cell == 0 and neighbours == 3:
                        change[i][j] = 1;
                    elif cell == 1 and (neighbours == 1 or neighbours == 0 or neighbours > 3):
                        change[i][j] = 0
                    else:
                        if cell > 0:
                            change[i][j] = cell


            for (i, row) in enumerate(pixel_ar):
                for (j, cell) in enumerate(row):
                    pixel_ar[i][j] = change[i][j]
                    # change[i][j] = 0

            BoardUpdate()


            pygame.display.update()

if __name__ == '__main__':
    Main()
