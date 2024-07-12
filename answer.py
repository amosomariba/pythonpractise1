answer = 30
guess = 30

if guess > answer:
    result = "You are right" 
elif guess < answer:
    result = "You are wrong"
elif guess > answer:
    result = "You are on the right track keep guessing"  
elif guess == answer:
    result = "Correct!!!" 
else:
    "You are out of option please!!"  
print(result)
    