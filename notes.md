///python notes///
Day 1 variables and data types:                             git commands:      
*******************************************                 **git init, git status, git add .
variables is a name given to memory location in program     git commit -m "notes", git log,
//name="hp"                                                 git push origin main.**  
//age="45"                                                        
//amoutn=50$                                                remove a file or folder commands:              
print("my name is :",name)                                   mkdir notes > used for to create a files     
print("my age is :",age)                                     rmdir notes > user for remove folder or file in repo.
print("my amoutn is :",amout)//

key words are reserved in python they are 33 types are present in python.
set data_type:
              set is an unorder collection of unique items.set is defined by values seperated by commas inside braces{}.
//student_id={556,557,535}
  print(student_id)
  print(type(student_id))//
dict:
     Python dictionary is an ordered collection of items. It stores elements in key/value pairs.
//food_city={'icecream':'turkey','ramens' : 'japan','biryanis':'india'}
  print(food_city)//
operators:
          1.arithematic operators(+*/-)2.relational(==,!=,>,<)3.assignment(=,+=,-=)4.logical(not,and,or)
type casting:
    this method convert the python varaiable datatype into a certain datatype in order to perform operations by users.
input:
  most programs need to collect user data such as name,age,number it is done using input()function

day 2:
string: 
      string is a data type that store a sequence of characters.
contatination:
    using string + operation and replace them using * opertinos.
slicing: 
  is a way to extreat a portion of string by specify start and end indexes.
format():
 another way to format string using format_method.
  name="hp"
  age=45
  amout=50
  print("my name is {} my age is {} my amout is {}".format(name,age,amout))//

list: is also mutable it not be change
 list are order collections of items that allows for easy use of set of data.list value are place in square brackets[].
//fruits=["apple","banana","mango","grapes"]
  print(fruits)
  print(type(fruits))//
types in list:
append():
 add an element to end of a list.
//fruits.append("orange")
  print(fruits)//
sort():
 sorts the list in ascending order default.
//fruits.sort()
  print(fruits)//
reverse():
 reverse the order of the element in a list.
//fruits.reverse()
  print(fruits)//
index():
 return the index of the first occurance of a specific elements.
//print(fruits.index("mango"))//
remove():
 remove the first occurance of a specific elements.
//fruits.remove("banana")
  print(fruits)//

Tuples: is immutalbe it can be change any values by using this"()" paranthesis.tuple can hold elements of diff data types.
//colors=("red","green","blue","yellow")
  print(colors)
  print(type(colors))//

day 3:
dictionary:
dict is a data structure that stores value in key pair.value in a data dict can be any data type can be duplicate.
//student={'name':'hp','age':45,'amout':50}
  print(student)
  print(type(student))//

  accessing dict:
   we can access a value from a dict by using the key with in the square bracket or get method().

   iteration in dict:
    we can iterate through a dict using for loop to get keys and values.

  sets:
  set is an unordered collection of unique items.it is defined by values seperated by commas inside braces{}.
//student_id={556,557,535}
 methods():
 
 adding elements to sets: the set is done through the set.add() function, where an appropriate record value is created to store in the hash table.
//student_id.add(558)
  print(student_id)//

union:
 Union() method in Python is an inbuilt function provided by the set data type. It is used to combine multiple sets into a single set, containing all unique elements from the given sets.

 intersection:
 The intersection of two given sets is the largest set, which contains all the elements that are common to both sets. given sets A and B is a set which consists of all the elements which are common to both A and B.
  
day 4:loops:
 pass: the pass statement in python is placeholder that does nothing when executed.
 
 continue: the continue statement in python is used to skip the current iteration of a loop and move to the next iteration.
 
 break: the break statement in python is used to terminate the loop prematurely when a certain condition is met.
 
 for loop: a for loop is used for iterating over a sequence.
 
 while loop: a while loop is used to repeatedly execute a block of code as long as a specified condition is true.
 
 nested loop:they are two types of loop which are for loop and while loop by using we can created nested loop in python nested loop means loops inside a loop.

day 5: funtions and recursion

function: are using by def keywords,followed by function name,parathasis(),and colon .
//def greet():
  print("hello world")//
  greet()//

parameters and arguments:
  function can accept input value is know has parameters during their definition.when funtion is know as actual values passes an arguments.

return values:
a function can return values by using return keyword.if no retrun statement  is mention the funtion implicity none.

recursion:
 it is program technigue where a function call itself either directly or indirectly to solve a problem by breaking into a small simpler sub problems.

 factorial :
  defines a recursive function to calculate factorial of a number, where function repeatedly calls itself with smaller values until it reaches the base case.

  fibonacci:
   defines a recursive function to calculate nth Fibonacci number, where each number is the sum of the two preceding ones, starting from 0 and 1.

day 6: I/O functions 
   the process of performing operations on a file, such as creating, opening, reading, writing and closing it through a programming interface.

  opening a file:
  to open a file in python we use the built-in open() function which takes the file name and mode as arguments.    

  







 







  
