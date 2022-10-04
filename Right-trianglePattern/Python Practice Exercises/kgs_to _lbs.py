weight = float(input("weight: "))
unit = input("(k)g or (l)bs: ")

if unit.upper == "k":
    converted = weight / 0.45
    print("weight in lbs:" + str(converted))
else:
    converted = weight * 0.45
    print("weight in kgs:" + str(converted))
