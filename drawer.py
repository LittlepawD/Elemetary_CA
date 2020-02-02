from pygame import display, draw
import os


def drawline(surface, data, y=0, x=0, a=20):
    '''Draws an array of squares with size "a" on "surface" based on binary array of given data.
    Starts at coordinates x,y
    To be only called by the Grid methods!
    '''
    for bit in data:
        if bit == 1:
            draw.rect(surface, (255,255,255), (x,y,a,a))
        x += a

class Grid():
    def __init__(self,surface,rectsize = 20):
        self.surface = surface  # Name of the window we are drawing to
        self.last_y = 0
        self.no_lines = 0
        self.rect_size = rectsize # Change to be a fraction of window size or data

    def reset_y(self):
        self.last_y = 0

    def addline(self, data):
        drawline(self.surface, data, self.last_y, a=self.rect_size)
        self.last_y += self.rect_size
        self.no_lines += 1
        display.update()


if __name__ == '__main__':
    data = [1,0,0,0,1,1,0,1]

    window = display.set_mode((250,250))
    window.fill((0,0,0))

    grid = Grid(window)
    grid.addline(data)
    grid.addline(data)
    data.append(1)
    grid.addline(data)

    os.system('pause')