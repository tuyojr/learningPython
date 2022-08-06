#import module
from tkinter import *

# initialize window
root = Tk()
root.geometry('300x300')
root.title('Mad Libs Generator(DataFlair)')
Label(root, text= 'Mad Libs Generator \n Have Fun!' , font = 'arial 20 bold').pack()
Label(root, text = 'Click Any One :', font = 'arial 15 bold').place(x=40, y=80)


################Stories##############

def madlib1():

    animals= input('enter a animal name : ')
    profession = input('enter a profession name: ')
    cloth = input('enter a piece of cloth name: ')
    things = input('enter a thing name: ')
    name= input('enter a name: ')
    place = input('enter a place name: ')
    verb = input('enter a verb in ing form: ')
    food = input('food name: ')
    print('say ' + food + ', the photographer said as the camera flashed! ' 
    + name + ' and I had gone to ' + place +
    ' to get our photos taken today. The first photo we really wanted was a picture of us dressed as ' 
    + animals + ' pretending to be a ' + profession + 
    ' .when we saw the second photo, it was exactly what I wanted. We both looked like ' 
    + things + ' wearing ' + cloth + ' and ' + verb + ' --exactly what I had in mind')



def madlib2():
   
    adjective = input('enter an adjective : ')
    color = input('enter a color: ')
    thing = input('enter the name of a thing:')
    place = input('enter the name of a place: ')
    person= input('enter a person\'s name: ')
    adjective1 = input('enter an adjective : ')
    insect= input('enter the name of an insect: ')
    food = input('enter the name of a food: ')
    verb = input('enter a verb: ')

    print('Last night I dreamt I was a ' + adjective + ' butterfly with ' + color + 
    ' wings that looked like '+ thing + '. I flew to ' + place + 
    ' with my best friend and '+ person + ' who was a '+ adjective1 + ' ' 
    + insect +'. We ate some ' + food + ' when we got there and then decided to ' 
    + verb + ' and the dream ended when I said; lets ' + verb + '.')
    


def madlib3():
    person = input('enter a person\'s name: ')
    color = input('enter a color: ')
    foods = input('enter the name of a food: ')
    adjective = input('enter an adjective : ')
    thing = input('enter the name of a thing: ')
    place = input('enter the name of a place: ')
    verb = input('enter a verb: ')
    adverb = input('enter an adverb: ')
    food = input('enter the name of another food: ')
    things = input('enter a thing name : ')

   
    print('Today we picked an apple from '+ person + 
    "'s Orchard. I had no idea there were so many different varieties of apples. I ate " 
    + color + ' apples straight off the tree that tasted like '+ foods + 
    '. Then there was a '+ adjective + ' apple that looked like a ' + thing + 
    '. When our bags were full, we went on a free way ride to '+ place + 
    ' and back. We ended up with a huge sack of apples ' + verb + ' ' + adverb + 
    '. I can\'t wait to get back home and cook something nice with the apples. We are going to make apple '
    + food + ' and '+ things +' pies!.')  



######buttons   
Button(root, text= 'The Photographer', font ='arial 15', command= madlib1, bg = 'ghost white').place(x=60, y=120)
Button(root, text= 'The Tasty Apples', font ='arial 15', command = madlib3 , bg = 'ghost white').place(x=70, y=180)
Button(root, text= 'The Butterfly', font ='arial 15', command = madlib2, bg = 'ghost white').place(x=80, y=240)

root.mainloop()
