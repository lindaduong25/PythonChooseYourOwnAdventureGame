print("Welcome to Random Guessing!")
name = input("What is your name? ")
age = int(input("What is your age? "))

points = 20

if age >= 15:
    print("You are old enough to play!")

    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("Let's begin then!")
        print("Let's start you off with 20 points, but beware, the decisions you make may cost you.... mwahahahah")

        red_or_green = input("First choice... Red or Green (red/green)? ").lower()
        if red_or_green == "red":
            ans = input("Correct! You chose the correct answer, now you come to a stop sign, do you turn left or right (left/right)? ").lower()
            if ans == "right":
                print("You have reached a dead end! You will have to be re-set on your track and therefore will lose 10 points.")
                points -= 10
            elif ans == "left":
                print("Awesome, you have made it across the road.")

            ans = input("You come to a fruit tree, do you pick the apple or the orange (apple/orange)? ").lower()
            if ans == "apple":
                print("You were poisoned by the apple, whoopsie. You lose 10 points.")
                points -= 10

                if points <=0:
                    print("You have no more points to use and have lost the game.")
                else:
                    print("You win!")

            else:
                print("Wrong choice, you have lost!")
        else:
            print("Wrong! You lose, sorry...")



    else:
        print("Goodbye!")
                          
else:
    print("You are not old enough to play...")

