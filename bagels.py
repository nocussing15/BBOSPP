import random

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
    print(random_number)
    while True:
        try:
            num = input('Guess the number: ')
            if len(num) > 3:
                raise ValueError
            #returns random number chosen as string
            
            #turns into list for Fermi
            random_number_list=list(random_number)
            #returns input as string
            str_num=str(num)
            #returns input string as list for Fermi
            str_num_list=list(str_num)
            
            
            if str_num == random_number:
                print('You Got it!')
                break
            elif str_num != random_number:
                for i in range(len(str_num_list)):
                    for j in range(len(random_number_list)):
                        if i == j:
                            if str_num_list[i] == random_number_list[j]:
                                print('Fermi')
                            elif str_num_list[i] != random_number_list[j]:
                                if str_num_list[i] in random_number_list:
                                    print('Pico')
                                
                                
                          

        except ValueError:
            pass 











if __name__ == "__main__":
    main()
