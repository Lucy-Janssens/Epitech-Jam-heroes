import random as rd
import akinator
import sys
from PySide6 import QtCore, QtWidgets, QtGui

aki = None
first_question = None

heroes = ["Superman", "Batman", "Spiderman", "CatWoman"]

# TODO: add super villain qui stoppe le jeu avec une certaine probabilité
# TODO: add a retry button
# TODO: add a button to show the picture of the hero
# TODO: add a leaderboard
class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.counter = 0

        self.game_title = QtWidgets.QLabel("Make It Remember!",
                                     alignment=QtCore.Qt.AlignCenter)
        self.hero_name = QtWidgets.QLabel("Make me guess : " + rd.choice(heroes),
                                          alignment=QtCore.Qt.AlignCenter)
        self.display_counter = QtWidgets.QLabel("Number of questions answered: " + str(self.counter),
                                                alignment=QtCore.Qt.AlignCenter)
        self.current_question = QtWidgets.QLabel(first_question, alignment=QtCore.Qt.AlignCenter)

        self.btn_yes = QtWidgets.QPushButton("Yes")
        self.btn_no = QtWidgets.QPushButton("No")
        self.btn_dk = QtWidgets.QPushButton("I Don't know")
        self.btn_prob = QtWidgets.QPushButton("Probably")
        self.btn_prob_no = QtWidgets.QPushButton("Probably Not")
        self.btn_finish = QtWidgets.QPushButton("Show me the prediction")

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.game_title)
        self.layout.addWidget(self.hero_name)
        self.layout.addWidget(self.display_counter)
        self.layout.addWidget(self.current_question)

        self.layout.addWidget(self.btn_yes)
        self.layout.addWidget(self.btn_no)
        self.layout.addWidget(self.btn_dk)
        self.layout.addWidget(self.btn_prob)
        self.layout.addWidget(self.btn_prob_no)
        self.layout.addWidget(self.btn_finish)

        self.btn_yes.clicked.connect(self.on_click_yes)
        self.btn_no.clicked.connect(self.on_click_no)
        self.btn_dk.clicked.connect(self.on_click_dk)
        self.btn_prob.clicked.connect(self.on_click_prob)
        self.btn_prob_no.clicked.connect(self.on_click_prob_no)
        self.btn_finish.clicked.connect(self.on_click_finish)

        self.setWindowTitle("Make It Remember")

    def update_counter(self):
        self.counter += 1
        self.display_counter.setText("Number of questions answered: " + str(self.counter))

    @QtCore.Slot()
    def on_click_finish(self):
        aki.win()
        to_show = "The genius has guessed the following hero: " + aki.first_guess['name']

        self.counter = -1
        self.update_counter()
        self.hero_name.setText("Make me guess: " + rd.choice(heroes))

        self.current_question.setText(to_show)

    @QtCore.Slot()
    def on_click_yes(self):
        question = aki.answer("yes")
        self.current_question.setText(question)
        self.update_counter()

    @QtCore.Slot()
    def on_click_no(self):
        question = aki.answer("no")
        self.current_question.setText(question)
        self.update_counter()

    @QtCore.Slot()
    def on_click_dk(self):
        question = aki.answer("idk")
        self.current_question.setText(question)
        self.update_counter()

    @QtCore.Slot()
    def on_click_prob(self):
        question = aki.answer("probably")
        self.current_question.setText(question)
        self.update_counter()

    @QtCore.Slot()
    def on_click_prob_no(self):
        question = aki.answer("probably not")
        self.current_question.setText(question)
        self.update_counter()


if __name__ == '__main__':

    app = QtWidgets.QApplication([])

    aki = akinator.Akinator()
    first_question = aki.start_game()

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())

    # print("Welcome to HELP ME REMEMBER")
    # print("The point is to make the genius guess the following hero:")
    # print(rd.choice(heroes), "\n")
    # print("Answer with the following answers:\n\t 1. Yes \n\t 2. No \n\t 3. Don't know")
    # print("\t 4. Probably \n\t 5. Probably Not")
    # print("Please answer with the given numbers for the moment :) \nLet's start the game afolle !! \n")
