# Initially, this code mistakenly assigns everyone to the adult's travel package
age = 45  # Example age

if age < 18:
    print("You are eligible for the children's travel package.")
elif age < 60:
    print("You are eligible for the adult's travel package")
else:
    print("You are eligible for the senior citizen's travel package.")