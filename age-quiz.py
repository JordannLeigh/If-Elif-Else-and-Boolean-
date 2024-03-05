"""

start

if the user is 40 <=, output "You're over the hill"
ask user to input "age" then store users input under variable 'age'
assume the oldest one can be is 100 - if user enters higher number output "Sorry, you're dead"
if the user is 65 <=, output "Enjoy your retirment"
is the user is 13>, output "You qualify for the kiddie discount"
if the user = 21, output "Congrats on your 21st!"
for any other age output "Age is but a number"
use if-elif-else structure 
ensure order is logical

stop

"""

age = int(input("Kindly enter your age: "))
if age > int(100):
    print ("Sorry, you're dead")
elif age >= int(65):
    print ("Enjoy your retirment")
elif age >= int(40):
    print ("You're over the hill")
elif age == int(21):
    print ("Congrats on your 21st!")
elif age < int(13):
    print ("You qualify for the kiddie discount")
else:
    print ("Age is but a number")