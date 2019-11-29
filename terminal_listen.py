# import keyboard  # using module keyboard
# while True:  # making a loop
#     # try:  # used try so that if user pressed other than the given key error will not be shown
#     if keyboard.is_pressed('Q'):  # if key 'q' is pressed 
#         print('You Pressed A Key!')
#         break  # finishing the loop


import keyboard
from subprocess import call

read = keyboard.read_key()
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZenterspace12−34.|'



def altElement(a):
    return a[::2]
def ar(a):
    return a[::1]
def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    
    # return string   
    return str1  
sentence = []
var = ''
last = ''
master = 'enterspace'
while True:
    
    
    g = keyboard.read_key()
    
    if g in alphabet:
       
        
        if g == 'enter':
            command = " ".join(sentence)
            print(command)
            call(command, shell=True)
            sentence = []     
        
        else:
            if g == '−':
                    g = '-'

            
         
            if last == g:
                last = ''
                pass 
            elif g == 'space':
                if var:

                    sentence.append(var)
                    print(sentence)
                    var = ''
            else:
                
                var = var + listToString(altElement(g))
                print(var) 
                last = g
            
            
    
    # if d in master:
     
    #     if d == 'space':
    #         print('space')
    #         sentence.append(var)
    # print(sentence)
        # if g == 'enter':
        #     sentence = []

    





