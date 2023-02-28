import random

def main()
    #your guess
    print('I am thinking of a 3-digit number number. Try to guess what it is.')
    print('Here are some clues:')
    print('When I say:              That means:')
    print('Pico                     One Digit is correct but in the wrong position')
    print('Fermi                    One Digit is correct and in the right position')
    print('Bagels                   No digit is correct')
    print('I have tought up a number.')
    print(' You have 10 guesses to get it.')
    bagels(input('Guess the number: '))
    


#random number chosen 
def random_num():
    x=random.randrange(0,9)
    y=random.randrange(0,9)
    z=random.randrange(0,9)
    
    random_num=str(x) + str(y) +str(z)
    
    return random_num


#prints out your guess and numbers, and compares to number chosen    
def bagels(num):
    #returns random number chosen as string
    random_number=random_num()
    #turns into list for Fermi
    random_number_list=list(random_number)
    #returns input as string
    str_num=str(num)
    #returns input string as list for Fermi
    str_num_list=list(str_num)
    
    
    try:
        while True:
            if str_num == random_number:
            return 
    
    
    
    

    







main()





if __name__ == "__main__":
    main()