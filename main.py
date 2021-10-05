'''Author: Pallav'''

#Open Terminal(ctrl+alt+t, on linux)/powershell on windows, and type 'pip install gtts'!


#Importing library
from gtts import gTTS 
import os

#Main code!

language = "en" #Language 
myobj = input("Enter the TEXT that you want to convert to AUDIO!!:- ")

nameoffile = input("Enter the name by which you want to save the audio file:- ")

audio = gTTS(text=myobj, lang=language,)

audio.save(nameoffile + ".mp3") #The Audio file will be saved in same folder as this!!

os.system(nameoffile + ".mp3") #This line of code May/MayNot work

#Note
#1] 'os.system(nameoffile + ".mp3")', This is used to autoplay the converted audio file!
#2] This May/MayNot work!! [Not that Important!!]



