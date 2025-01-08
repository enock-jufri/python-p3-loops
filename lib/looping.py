#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i=10
    while i > -1:
        if(i==0):
            print('Happy New Year!')
        else:
            print(i)
        i =i- 1
def square_integers(int_list):
    # code goes here!
    return [i**2 for i in int_list]

def fizzbuzz():
    # code goes here!
    i=1
    while i<=100:
        if(i%3==0 and i%5==0):
            print("FizzBuzz")
        elif(i%3==0):
            print("Fizz")
        elif(i%5==0):
            print("Buzz")
        else:
            print(i)
        i+=1
fizzbuzz()