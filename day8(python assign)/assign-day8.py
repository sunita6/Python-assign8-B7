#Day8:
#Assignment1

def decorator_with_arguments(function):
    def wrapper_accepting_arguments(arg1, arg2):
        print("My arguments are: {0}, {1}".format(arg1,arg2))
        function(arg1, arg2)
    return wrapper_accepting_arguments


@decorator_with_arguments
def cities(city_one, city_two):
    print("Cities I love are {0} and {1}".format(city_one, city_two))

cities("Pune", "Goa")


#Assignment 2

try:
  f = open("simple.txt", 'r')
  data = f.read()
  print("Trying\n")
except:
  print("Fiddlesticks! Failed")
finally:
  print("Finally!")
  print("All Done")
  
#output
'''Trying
Hiiiiiiiiiiiii Everyone!
saikiran sir teach us very good.
I m very thankful of sir that he started this free course,and
spreading the knowledge to everyone.
The way u teach us,we lyk very much.
Thanku sir!
Finally!
All Done
'''