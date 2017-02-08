# -*- coding: utf-8 -*-
print ("Hello World")

#collections and comments

#List
fruits=['Banana','Strawberry','Apple','Grapes']
print(fruits[0])
print(fruits[-1])
print(fruits[-3])

#List slicing
numbers=[0,1,2,3,4,5,6,7,8,9,10]
from_2to7=numbers[2:7]
print from_2to7
geatherThan3=numbers[3:]
print geatherThan3
pairsNumbers=numbers[::2]
print pairsNumbers
notpairNumbers=numbers[1::2]
print notpairNumbers

print (4 in numbers)

#dictionaries and None value
city={"name":'Granada',"place":"south","population":"12414112"}
print city["name"]#not a good way to acces dictionaries
print city.get("name")#GOOD WAY: return name or none if not found that key


#functions, brackets, :,;
#one instruction per line
#good code indent practice

def print_fruits(fruits):
    for fruit in fruits:
        print fruit


print_fruits(fruits)


#python 2 reads ASCII code by default
#print("Hola mundo rotísimo)" #syntax error: non-ASCII
#we can solve this by typing one of the "magic codification line":

# coding=utf-8
print("Hola mundo rotísimo")
#python interprets comments also!

