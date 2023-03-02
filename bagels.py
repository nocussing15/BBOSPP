import random
import re

def main():
    print(' You have 10 guesses to get it.')
    bagels()


#random number chosen 
def random_num():
    x=random.randrange(0,9)
    y=random.randrange(0,9)
    z=random.randrange(0,9)
    
    random_num=str(x) + str(y) +str(z)
    
    return random_num


#prints out your guess and numbers, and compares to number chosen    
def bagels():
    random_number=random_num()
    #print(random_number)
    while True:
        number_guess = 1
        game_over = False
        while number_guess <= 10:
            try:
                num = input(f'Guess {number_guess}: ')
                str_num=str(num)
                if len(num) > 3:
                    raise ValueError
                elif not re.match('[0-9][0-9][0-9]',str_num):
                    raise ValueError
                    #returns random number chosen as string
                      #turns into list for Fermi
                random_number_list=list(random_number)
                        #returns input string as list for Fermi
                str_num_list=list(str_num)
                clue_list=[]
                        
                        #eval
                if str_num == random_number:
                    print('You Got it!')
                    game_over = True 
                    break 
                    
                       
                for i in range(len(str_num_list)):
                    if str_num_list[i] == random_number[i]:
                        clue_list.append('Fermi')
                    elif str_num_list[i] in random_number_list:
                        clue_list.append('Pico')
                clues_list=' '.join(sorted(clue_list))
                if len(clue_list) == 0:
                    print('Bagel')
                elif len(clue_list) > 0:
                    print(clues_list)
                            
                number_guess+=1
                
            except ValueError:
                pass 
        if game_over:
            player_response = input('Do you want to play again?')
            if not player_response.lower().startswith('y'):
                break
        elif number_guess>10:
            print("You've lost, do you want to play again?")
            player_response = input('Do you want to play again?')
            if not player_response.lower().startswith('y'):
                break 
        
    
       










if __name__ == "__main__":
    main()
