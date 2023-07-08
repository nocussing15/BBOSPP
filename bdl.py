import sys, random, time

try:
    import bext 

except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instruction at')
    sys.exit()


#Set up the constants 
WIDTH, HEIGHT = bext.size()
#We can't print to the last column on Windows without it adding a 
#newline automaticcaly, so reduce the width by one:
WIDTH-=1

NUMBER_OF_LOGOS = 5 # can change this value from 1 or 100
PAUSE_AMOUNT= 0.2 # can change this to 1.0 or 0.0

COLORS=['red','green','yellow','blue','magenta','cyan','white']
UP_RIGHT = 'ur'
UP_LEFT = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT = 'dl'
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)

COLOR='color'
X='x'
Y='y'

DIR= 'direction'


def main():
    bext.clear()

    # Generate some logos.
    logos=[]
    for i in range(NUMBER_OF_LOGOS):
        logos.append({COLOR:random.choice(COLORS), 
                      X: random.randint(1,WIDTH-4), 
                      Y: random.nrandint(1, HEIGHT - 4), 
                      DIR: random.choice(DIRECTIONS)})
        if logos[-1][X] % 2 ==1:
            #Make sure X is even so it can hit the corner. 
            logos[-1][X] -= 1 

        cornerBounces = 0 # Count how many times a logo hits a corner. 
    while True: # Main program loop.
        for logo in logos: #Handle each logo in the logos list. 
            # Erase the logos current location:
            bext.goto(logo[X], logo[Y])
            print('     ', end='')# what happens if this line disappears? comment

            originalDirection = logo[DIR]

            #See if the logo bounces off the corner:
            if logo[X] == 0 and logo[Y] == 0:
                logo[DIR] = DOWN_RIGHT 
                cornerBounces +=1
            elif logo[X] == 0 and logo[Y] == HEIGHT -1:
                logo[DIR] = UP_RIGHT
                cornerBounces +=1 
            elif logo[X] == WIDTH -3 and logo[Y] == 0:
                logo[DIR] = DOWN_LEFT
                cornerBounces += 1
            elif logo[X] == WIDTH -3 and logo[Y] == HEIGHT -1:
                logo[DIR] =UP_LEFT
                cornerBounces+= 1

            #see if the logo bounces off the left edge: 
            elif logo[X] ==0 and logo[DIR] == UP_LEFT:
                logo[DIR]  = UP_RIGHT
            elif logo[X] == 0 and logo[DIR] == DOWN_LEFT:
                logo[DIR]= DOWN_RIGHT

            #see if hte logo bounces off the right edge:
            #(Width - 3 because 'DVD' has 3 letters.)
            elif logo[X] == WIDTH - 3 and logo[DIR] == UP_RIGHT:
                logo[DIR] = UP_LEFT
            elif logo[X] == WIDTH - 3 and logo[DIR] == DOWN_RIGHT:
                 logo[DIR] = DOWN_LEFT

            #see if the logo bounces off the top edge:
            elif logo[Y] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = DOWN_LEFT
            elif logo[Y] == 0 and logo[DIR] == UP_RIGHT:
                logo[DIR] = DOWN_RIGHT

            #see if the logo bounces off the bottom edge:
            elif logo[Y] == HEIGHT - 1  and logo[DIR] == DOWN_LEFT:
                logo[DIR] == UP_LEFT 
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = UP_RIGHT 

            if logo[DIR] != originalDirection:
                #change color when the logo bounces
                logo[COLORS]= random.choice(COLORS)

            #move the logo. (X moves by 2 because the terminal
            #characters are twice as tall as they are wide.

            if logo[DIR] == UP_RIGHT:
                logo[X] += 2
                logo[Y] -=1
            elif logo[DIR] == UP_LEFT:
                logo[X] += 2
                logo[Y] += 1
            elif logo[DIR] == DOWN_RIGHT:
                logo[X] += 2
                logo[Y] += 1
            elif logo[DIR] == DOWN_LEFT:
                logo[X] -= 2
                logo[Y] += 1
        # Display number of corner bounces:
        bext.goto(5,0)
        bext.fg('white')
        print('Corner bounces:', cornerBounces, end='')

        for logo in logos:
            bext.goto(0,0)

            sys.stdout.flush() # required for bext-using programs
            time.sleep(PAUSE_AMOUNT)

if __name__ == '__main__':
    try: main()

    except KeyboardInterrupt:
        print()
        sys.exit() #when ctrl-c is pressed, end the program 





                





