# Empty lists to store people in different age groups
kids = []      # 0-12
teens = []     # 13-19
adults = []    # 20-59
seniors = []   # 60+

# Ask how many people to input
num_people = int(input("How many people you wanna add, bruh? "))

# Loop to get names and ages
for i in range(num_people):
    name = input(f"Enter name #{i+1}: ")
    age = int(input(f"Enter {name}'s age: "))
    
    # Sort them into groups based on age
    if age <= 12:
        kids.append(name)
    elif age <= 19:
        teens.append(name)
    elif age <= 59:
        adults.append(name)
    else:
        seniors.append(name)

# Print the results
print("\nHere’s the breakdown, bruh:")
print("Kids (0-12):", kids)
print("Teens (13-19):", teens)
print("Adults (20-59):", adults)
print("Seniors (60+):", seniors)
