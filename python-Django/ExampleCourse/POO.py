#object oriented programming: excetions,modules, packets...

#class definition
class Fruit(object): #object for compatibility with python 3
    """i am delicious"""
    def __init__(self,name): #called AFTER creating the object, to initialize it
        self.name=name

    def __new__(cls, *args, **kwargs): # static method called BEFORE __init__ that construct and returns the object

    def __del__(self): # desctructor

    def __str__(self):#returns object as string (toString)

    def __cmp__(self, other):#called when using comparation methods. Return 0 if equals, negative is < and + if >

    def __len__(self):#return object 's lenght

#inheritance
class Pear(Fruit):

def __private_method(self):
    #private method
def public_method(self):
    #public method
def _protected_method(self): #protected but public really

#multiple inheritance
class Dolphin(Mamal,Animal):



class Banana(Fruit):
    #class atributes:shared byevery instacne
    skin=["green","yellow","black"]

    #static methods
    @staticmethod
    def a_static_method(args):

    #class methods
    @classmethod
    def a_class_method(clscls,args):

    #super class calls
    super(Banana,self).__init__()



#abstract classes
class Fruit(object):
    def __init__(self,name):
        self.name = name

    def peel(self):
        raise NotImplementedError


#instantiating classes
melon=Fruit("melon")
melon.peel()

#get class atributes
melon.name
def __getattr__(self,name):
    #define get
def __setattr__(self,name,value):
    #define set



#EXCEPTIONS

 try:
     #.....
except:
    print("error ocurred(it is like a catch)")


#to catch defined error classes:
try:
    #-----
except NameError:
    print "A NameError exception happened"

except ValueError:
    print "A ValueError exception happened"

except:
#any other exception


#access exception data
try:
    #....
except NameError as err:
    print "A NameError exception happened",err
except ValueError as err:
    print "A ValueError exception happened",err
except:
    print "An unknow exception happened"

#it is possible to capture various exceptions at same time:
try:
#....
except (NameError,ValueError):
    print "A NameError or ValueError exception happened"


#Except-else : execute else if any exception is catch
try:
    #....
except:
    print "an exception happened"
else:
    print "any exception happened"



#Except-Finally: execute finally ALWAYS even if an exception is catched or not
try:
#....
except:
    print "an exception happened"
finally:
    print "always displayed"


#an exception is thrown by: raise
#there are many types of exceptions:
        #1) BASE EXCEPTION: is the base class(all exceptions inherits from it)
        #2) EXCEPTION(BaseException):Super class for all exceptions which are not OUT exceptions
        #3) GENERATOREXIT(Exception): it ask to go out a generator
        #4) STANDARDERROR(Exception): Base class for all the exceptions which doesnt have nothing to see with exiting the interpeter
        #ARITHMETICERROR(StandardError): Base class for arithmetic errors



#PYTHON MODULES
#let us divide programs
# each file is a module
import <modulename> #without .py extension
#other wy of importing modules:
from <modulename> import classname,varname


#if various modules have functions with the same name:
from <modulename> import <classname> as name #we set alias




#PACKETS
#organize modules
#are directories that have a file named:__init__.py
#could be empty
#could be accesed by <packagename>.<modulename> metthod


