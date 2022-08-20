    
from time import sleep         
import sys         
import random          
import os                  
from pygame import mixer           
os.system('cls')           
mixer.init()           
dir = os.path.abspath(os.path.dirname(__file__)) + "\sys"          
sys.path.append(dir)           
def delay_print(txt, play_sound = True):           
    for i in txt:          
        if i != "~":               
            sys.stdout.write(i)        
            sys.stdout.flush()         
            sound=mixer.Sound("{}\sound{}.wav".format(dir, str(random.randint(1,3))))          
            if i != " ":           
                if play_sound:         
                    sound.play()           
                sleep(0.13)        
        else:          
            sleep(0.1)         
            os.system('cls')           
            sleep(0.9)         
def ask(qustion, output = None):           
    print(qustion)         
    isntinout = True           
    if output != None:         
        print("")          
        while isntinout:           
            if input() in output:          
                isntinout = False          
            else:          
                print("this answer is not an option")          
        return output          
    else:          
        print("")          
        return input()         
def delay_ask(qustion, output = None, play_sound = True, do_auput=True):          
    var_output = output
    line_loc = []
    line_locc = []
    auto_output = []
    for i in range(len(qustion)):
        if qustion[i] == "|":
            line_loc.append(i)
    for i in range(len(line_loc)):
            if (i % 2) == 0:
                line_locc.append([line_loc[i],line_loc[i+1]])

    for i in line_locc:
        auto_output.append(qustion[i[0]:i[1]])
    for i in range(len(auto_output)):
        auto_output[i] = auto_output[i][1:]
    if do_auput:
        var_output = auto_output
    delay_print(qustion, play_sound)       
    isntinout = True           
    if var_output != None:         
        print("")          
        while isntinout:           
            u=input()
            if u in var_output:          
                isntinout = False          
            else:          
                delay_print("this answer is not an option")        
                print("")          
        return u        
    else:          
        print("")          
        return input()         
