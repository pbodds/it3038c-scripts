from faker import Faker
import time
fake = Faker(['en_US'])

# Initial use of faker. Giving a fake name, address, email, and country.
print("Hello! Hmm. I see. You don't remember who you are... no worries! I remember everything about you:")
time.sleep(2)

print("Your name: " + fake.name())
print("Your SSN: " + fake.ssn())
print("Your address: " + fake.address())
print("Your email: " + fake.email())
print("Your country: " + fake.country())
print("\n")

# Printing 10 random names and countries assigned to each person

print("You have 10 friends who also forgot everything about themselves?? Interesting! I guess I will help you again:")
for i in range (0,10):
    print('Name->', fake.name(), 'SSN->', fake.ssn(), 'Country->', fake.country(), "\n")


# Printing out text that is randomized each time it is called. 
print("I can speak gibberish, watch this:")
print(fake.text() + '\n')

# Printing a profile without specifiying what information you want
print("You don't have the time to mess around with me? I'm being serious... fine, as fast as I can get it to ya: ")
print(fake.simple_profile())