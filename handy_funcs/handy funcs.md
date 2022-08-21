# handy funcs
## handy funcs is a module full of handy functions. more functions will be added once a week or so.  
#
#
#
#
  
### print functions

##### delay_print(txt, play_sound=True)
this functions prints text letter by letter with typing sounds.
##### arguments:
- txt - this is the txt to print.
- play_sound - this determines if typing noises will be played.
#
#
##### delay_ask(qustion, output = None, play_sound = True, do_auput=True)
this function prints like delay_print, then will use input().
##### arguments:
- qustion - the qustion to print
- output - this is a list of posible answers. if input() is not in the ist, it will ask again. 
- play_sound - this determines if typing noises will be played.
- do_auput - a short for "do auto output". determines if an "output" list shuold generate automaticly. for example, if the qustion was "|yes| or |no|", the auto_output will be ["yes", "no"]

returns input().
#
#
##### ask(qustion, output=None, do_auput=True)
dose the same as delay_ask, but prints normally.
#
#
#
### PATH functions

##### relative_path_to_full(rel_path)
this function turns relative PATH to full PATH.
##### arguments:
- rel_path - the relative PATH you want to convert.

returns the full path.






