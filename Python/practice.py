import time
start_time = time.time()


# print('Hello')

# print('Hello' * 5)

# print('hello, ' + 'world!')

# print("hello" + "5")

# firstnumber = 42
# secondnumber = 58
# print(firstnumber + secondnumber)



print('What is your name?')
myName = input()

while myName != 'Patrick':
    if myName == 'your name':
        print('Ha ha, very funny. Seriously, who are you?')
        myName = input

    else:
        print('That is not your name. Please, tell me your real name.')
        myName = input()

print('Hello, %s. That is a good name. Hold old are you?' % myName)
myAge = int(input())

if myAge < 13:
    print("Learning young, that's good.")

elif myAge == 13:
    print("You're a teenager now... that's cool, I guess")

elif myAge > 13 and myAge < 30:
    print("Still young, still learning...")

elif myAge >= 30 and myAge < 65:
    print("Now you're adulting.")

else:
    print("... you've lived a long time?")

programAge = int(time.time() - start_time)

time.sleep(3)

# print(myAge + '? That\'s funny, I\'m only a few seconds old')
print("%s? That's funny, I'm only %s seconds old." % (myAge, programAge))
print('I wish I was %s years old' % (myAge * 2))

time.sleep(3)
print("I'm tired. I go sleep sleep now.")

