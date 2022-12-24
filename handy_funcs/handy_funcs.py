from time import sleep         
import sys         
import random          
import os                  
from pygame import mixer
import pickle        
os.system('cls')           
mixer.init()           


  

sys.path.append(os.path.abspath(os.path.dirname(__file__)))           


#print funcs


def delay_print(txt, play_sound = True):           
    for i in txt:          
        if i != "~":               
            sys.stdout.write(i)        
            sys.stdout.flush()         
            sound=mixer.Sound("{}\sys\sounds\sound{}.wav".format(get_dir(), str(random.randint(1,3))))          
            if i != " ":           
                if play_sound:         
                    sound.play()           
                sleep(0.13)        
        else:          
            sleep(0.1)         
            os.system('cls')           
            sleep(0.9)         
def ask(qustion, output = None, do_auput=False):           
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
    print(qustion)    
    isntinout = True           
    if var_output != None:         
                
        while isntinout:           
            u=input()
            if u in var_output:          
                isntinout = False          
            else:          
                print("this answer is not an option")        
                        
        return u        
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
        if var_output != []:
            print("")          
            while isntinout:           
                u=input()
                if u in var_output:          
                    isntinout = False          
                else:          
                    delay_print("this answer is not an option")        
                    print("")
        else:
            print("")          
            return input()   
            return u        
    else:          
        print("")          
        return input()         


print(__file__)
#path funcs
def get_dir():
    return os.path.abspath(os.path.dirname(__file__))    

def relative_path_to_full(rel_path, rel_path_to_handy_funcs):
    return os.path.join(get_dir().replace(f'\\{rel_path_to_handy_funcs}', ''), rel_path)


#property funcs
def int_property(item):
    properties = {}
    if (item % 2) == 0:
        properties["is_even"]=True
    else:
        properties["is_even"]=False
    properties["len"]=len(str(item))
    return properties

def str_property(item):
    properties = {}
    properties["len"]=len(item)
    properties["is_alphabetic"]=item.isalpha()
    properties["is_lower_case"]=item.islower()
    return properties

def list_properties(item):
    properties = {}
    types = []
    properties["len"]=len(item)
    for i in item:
        types.append(type(i))
    properties["types"]=types
    return properties


#file functions
def import_var(var_path, file_name, create_var=False, var=None):
    try:
        with open(var_path+"\{}.dat".format(file_name), "rb") as pickle_stream:
            item=pickle.load(pickle_stream)
            return item
    except:
        if create_var:
            with open(var_path+"\{}.dat".format(file_name), "wb") as pickle_stream:
                pickle.dump(var, pickle_stream)
                return var
        else:
            print("no file was found")
def export_var(var, var_path, file_name):
    with open(var_path+"\{}.dat".format(file_name), "wb") as pickle_stream:
        pickle.dump(var, pickle_stream)
