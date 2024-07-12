# languages = ['Swift', 'Python', 'Go']

# # access elements of the list one by one
# for i in languages:
#     print(i)

# languages = ['Swift', 'Python', 'Go', 'Zoho']

# # using _ for placeholder variable
# for _ in languages:
#     print('Hi')

# marks = 80 
# #result = ""
# if marks < 30:
#    result = "Failed"
# elif marks > 75:
#    result = "Passed with distinction"
# else:
#    result = "Passed"

# print(result)

# Points scored by the competitor
points = 174

# If statement to determine the prize based on points
if 1 <= points <= 50:
    result = "Congratulations! You won a wooden rabbit!"
elif 51 <= points <= 150:
    result = "Oh dear, no prize this time."
elif 151 <= points <= 180:
    result = "Congratulations! You won a wafer-thin mint!"
elif 181 <= points <= 200:
    result = "Congratulations! You won a penguin!"
else:
    result = "Invalid points value."

print(result)

#Test with other inputs (commented out)
# points = 45
# points = 120
# points = 160
# points = 190
# points = 205
# print(result)
