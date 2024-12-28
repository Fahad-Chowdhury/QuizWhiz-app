THEME_COLOR = "#375362"

from quiz_brain import QuizBrain
from tkinter import *
import os


class QuizInterface():

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = None
        self.score_label = None
        self.canvas = None
        self.quote_text = None
        self.true_button = None
        self.false_button = None
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.setup_ui()
        self.get_next_question()
        self.window.mainloop()

    def setup_ui(self) -> None:
        """ Setup the User Interface. """
        self._setup_window()
        self._setup_label()
        self._setup_canvas()
        self._setup_buttons()

    def _setup_window(self) -> None:
        """ Setup the window. """
        self.window = Tk()
        self.window.title("QuizWhiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

    def _setup_label(self) -> None:
        """ Setup Label for Score. """
        self.score_label = Label(text="Score: 0", fg="white", font=("Arial", 15), bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

    def _setup_canvas(self) -> None:
        """ Setup Canvas with the question text. """
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.quote_text = self.canvas.create_text(150,
                                                  125,
                                                  width=280,
                                                  text="Some question text",
                                                  font=("Arial", 15, "italic"),
                                                  fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

    def _setup_buttons(self) -> None:
        """ Setup True and False buttons. """
        true_img_path = os.path.join(self.current_dir, "images/true.png")
        self.true_img = PhotoImage(file=true_img_path)
        self.true_button = Button(image=self.true_img, highlightthickness=0,
                                  command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_img_path = os.path.join(self.current_dir, "images/false.png")
        self.false_img = PhotoImage(file=false_img_path)
        self.false_button = Button(image=self.false_img, highlightthickness=0,
                                   command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

    def get_next_question(self) -> None:
        """ Get the next question from the quiz brain. """
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quote_text, text=question_text)
        else:
            self.canvas.itemconfig(self.quote_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self) -> None:
        """ Check if the answer is True. """
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self) -> None:
        """ Check if the answer is False. """
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_correct: bool) -> None:
        """ Give feedback to the user whether the answer is right or wrong,
        by changing the background color to red or green. Then updating the
        next question and score after 1 second.
        """
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
