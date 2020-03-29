import itertools
import drawer
import pygame as pg

def generate_ruleset(rule):
    '''
    create ruleset as a dictionary
    :param rule: number of CA rule as a decimal
    :return: ruleset - dict of k-v pairs representing CA ruleset
    '''

    k = [i for i in itertools.product([0,1], repeat=3)]  # 2^3 keys representing all possible combinations of 0 or 1
    bin_rule = '{0:08b}'.format(rule)   # convert decimal to 8-bit binary as a string
    v = [n for n in bin_rule]    # decompose binary into list
    ruleset = {}
    for n, key in enumerate(k):  # combine keys and values into dict
        ruleset[key] = int(v[n])
    return ruleset

def new_gen(old_gen):
    '''
    Return a list of the same size with new generation based on the old generation.
    '''

    new = []
    for n, bit in enumerate(old_gen):
        old_gen.append(0)   # To resolve boundaries TODO come up with something better

        # Surrounding is the number to the left, right and the number itself
        surrounding = (old_gen[n-1], bit, old_gen[n+1])
        old_gen.pop()   # To stay iterating over the same data

        # pass the surrounding into ruleset dict which returns value for this surrounding
        new.append(ruleset[surrounding])
    return new

if __name__ == '__main__':
    # Size of the window
    width = 500
    height = 250    
    # Size of the 'pixel'
    rect_size = 5

    # Create and display black window of a specified size
    window = pg.display.set_mode((width,height))
    window.fill((0,0,0))
    pg.display.update()

    # initiate clock, grid, font
    clock = pg.time.Clock()
    grid = drawer.Grid(window, rectsize=rect_size)
    pg.font.init() # you have to call this at the start,
    font = pg.font.SysFont('Consolas', 20)

    # if we want to go over just one rule:
    # data = [int(i) for i in '{0:0100b}'.format(1)]

    # specify what rules to to go through
    start_rule = 89
    finish_rule = 255

    for rule in range(start_rule, finish_rule):

        # if we want to go over just one rule - reverse commented:
        # ruleset = generate_ruleset(90)
        ruleset = generate_ruleset(rule)    # generate ruleset for this rule
        data = [int(i) for i in '{0:055b}'.format(1)]   # reset data, starting with 55 bits binary 1

        # write number of rule to the window
        t = font.render(str(rule) + '({0:08b})'.format(rule), 1, (255,255,255))
        window.blit(t, (300, 0))

        for _ in range(height // rect_size):
            clock.tick(20)

            # grid draws current generation
            grid.addline(data)
            # new generation generated based on the old one and current ruleset
            data = new_gen(data)

            # if all cells become 0 - break
            if sum(data) == 0:
                break
            # TODO break if all cells become 1
            # TODO message if repetition occurs

            # if exit is pressed - quit
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()

        # reset window and grid object
        window.fill((0,0,0))
        grid.reset_y()