# Assignment 3: World Cup 2026 Simulation

print("Welcome to the World Cup 2026 Simulation!")

team_name = input("Enter your country name: ")

#morale → represents how strong/confident the team is, team morale starts at 50
#match → keeps track of which match you’re playing
morale = 50   
match = 1  

# Loop through matches, 3 group + 4 knockout matches
while match <= 7:

# Shows:Current match number, Current morale
    print(f"\nMatch {match} - Current morale: {morale}")

#Gives the user options before each match, Takes input (choice), User decisions affect morale → affects match result.
    print("Choose an action:")
    print("1. Train hard (+10 morale)")
    print("2. Rest (+5 morale)")
    print("3. Skip training (no change)")
    print("4. Quit tournament")

    choice = input("Enter your choice: ")

    # Using break
    if choice == "4":
        print("You have quit the tournament.")
        break

    # Using continue
    if choice not in ["1", "2", "3"]:
        print("Invalid choice! Try again.")
        continue   # skip rest of loop and repeat

    # Using pass
    if choice == "3":
        pass   # do nothing

    elif choice == "1":
        morale += 10

    elif choice == "2":
        morale += 5

    # Simulate match result
    if morale >= 60:
        print(f"{team_name} won the match! 🎉")
    else:
        print(f"{team_name} lost the match!")
        print("You are eliminated!")
        break

    match += 1

# Final result
if match > 7:
    print(f"\n🏆 Congratulations! {team_name} has won the World Cup 2026!")
else:
    print(f"\n{team_name}'s journey has ended.")