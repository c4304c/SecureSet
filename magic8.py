

#!/usr/bin/python3
# importing random number generator
import random

# choices that will come up
choices = ("Cannot predict now”, “Ask again later", "Yes", "No", "Why would you ask me that", "HAHA for real")

# system will dran a random number
# len counts objects in choices
# this will give you the num
# 6 choices, len command will have the generator the job to pick between 0-5
value = random.randint(0,len(choices)-1)

#This will give your user the random choice
print(choices[value])


