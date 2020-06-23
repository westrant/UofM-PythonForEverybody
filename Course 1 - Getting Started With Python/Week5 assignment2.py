score = input("Enter Score: ")

try:
    scorefloat = float(score)
except:
    print("Did not receive a proper score, please ensure you enter a numeric score")
    quit()

if scorefloat > 1.0:
    print("you entered a score over 1.0")
    quit()
elif scorefloat < 0.0:
    print("you entered a score below 0.0, please try again")
    quit()
else:
    if scorefloat >= 0.9:
        grade = "A"
    elif scorefloat >= 0.8:
        grade = "B"
    elif scorefloat >= 0.7:
        grade = "C"
    elif scorefloat >= 0.6:
        grade = "D"
    elif scorefloat < 0.6:
        grade = "F"

print(grade)
