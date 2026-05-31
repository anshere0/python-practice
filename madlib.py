from ast import FloorDiv
from random import randint
import copy

print("welcome to madlib games!")

playing=input("lets play shall we?\n")
if playing.lower() != "yes":
   quit()
print("okay, lets start:\n")
noun1=input("enter your name")
noun2=input("enter your friend's name")
noun3=input("enter another friend's name")

place1=input("enter a place")

adjective1=input("enter an adjective")
adjective2=input("enter another adjective")
adjective3=input("enter another adjective")
adverb1=input("enter an adverb")
adverb2=input("enter another adverb")
exclamation1=input("enter an emotion")


#print story




print("one day, "+ noun1 + " went to " + place1 + " to meet " + noun2 + " and " + noun3 + ".")
print("they were very " + adjective1 + " to see each other after such a long time.")
print("they " + adverb1 + " greeted each other and decided to go on an adventure.")
print("as they walked through the " + adjective2 + " forest, they suddenly heard a " + adjective3 + " noise.")
print(exclamation1.capitalize() + "! they exclaimed, as they saw a group of magical creatures dancing " + adverb2 + " around a glowing tree.")
print("it was a day they would never forget!")  
   
   
  
print("thanks for playing madlib games!")   
         