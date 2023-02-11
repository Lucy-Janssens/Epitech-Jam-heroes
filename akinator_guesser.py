import random as rd
import akinator

heroes = ["Superman", "Batman", "Spiderman", "CatWoman"]

if __name__ == '__main__':
    print("Welcome to HELP ME REMEMBER")
    print("The point is to make the genius guess the following hero:")
    print(rd.choice(heroes), "\n")
    print("Answer with the following answers:\n\t 1. Yes \n\t 2. No \n\t 3. Don't know")
    print("\t 4. Probably \n\t 5. Probably Not")
    print("Please answer with the given numbers for the moment :) \nLet's start the game afolle !! \n")

    aki = akinator.Akinator()
    questioner = aki.start_game()

    while aki.progression <= 20:
        answer_nbr = input(questioner + "\n\t")

        try:
            answer_nbr = int(answer_nbr)
        except:
            print("Boloss it's not a number")

        if answer_nbr == 1:
            questioner = aki.answer("Yes")
        elif answer_nbr == 2:
            questioner = aki.answer("No")
        elif answer_nbr == 3:
            questioner = aki.answer("Don't know")
        elif answer_nbr == 4:
            questioner = aki.answer("Probably")
        elif answer_nbr == 5:
            questioner = aki.answer("Probably Not")
        else:
            print("This is not a supported number")

    aki.win()

    print(aki.first_guess['name'])
    print(aki.first_guess['absolute_picture_path'])

    print("got out of the loop")
