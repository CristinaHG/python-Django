#python flow controls
name="Laura"
n=5
#if-else
if name=="Cristina":
    print "hola"

else:
    print "adios"


#if-elif-else
if name=="Cristina":
    print "hola"
elif name=="Laura":
    print "hola L"
else:
    print "adios"


# x if y else z
name="Cristina" if n==5 else "Laura"

#--------LOOPS-----------
#while
while n>1:
    print "hola"
    n=n-1

#for
cities=['Granada','Sevilla','Malaga','Cadiz']

for c in cities:
    print "the city is:", c


#----------FUNCTIONS--------

def sum(a,b):
    return a+b

print (sum(1,3))

#default params
def mult(a=2,b=2):
    return a*b

print (mult(1,3))

#changing params order
print (mult(b=6))
print (mult(b=6,a=3))

#variable params (*args)

def grocery(*groceries):
    for g in groceries:
        if g=="broccoli":
            return g
    return None
print(grocery("tomato","broccoli"))

#variable params as dictionarys (**args)
def grocery(*groceries):
        if "potato" in groceries:
            return "potato is present"
        return None
print(grocery("tomato","broccoli","potato"))

#in python everything is passed by reference


#functions as params
def addThree(mylist,func):
    for number in mylist:
        x=3
        summ=func(number,3)
    return summ
print(addThree([1,2],sum))

#lambda functions
exp=lambda n,m:n**m
print exp(2,3)
print exp(2,5)

#decorators: function as param and as a result

def function1(function2):
    def function3(*args,**kwargs):
        print "Arguments: %s,%s" % (args,kwargs)
        return function2(*args,**kwargs)
    return function3

# @logger
# def function1(function2)