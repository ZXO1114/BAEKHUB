name, age, weight = input().split()
age, weight = int(age), int(weight)

while name != "#":
    if age <= 17 and weight < 80:
        print(name, 'Junior')
    else:
        print(name, 'Senior')
    name, age, weight = input().split()
    age, weight = int(age), int(weight)
