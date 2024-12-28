import html


class QuizBrain:

    def __init__(self, q_list):
        self.question_number: int = 0
        self.score: int = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self) -> bool:
        """ Check if there are more questions in the quiz."""
        return self.question_number < len(self.question_list)

    def next_question(self) -> str:
        """ Get the next question in the quiz.
        Returns:
            str: Next question in the quiz.
        """
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        ques_test = html.unescape(self.current_question.text)
        question = f"Q.{self.question_number}: {ques_test} (True/False): "
        return question

    def check_answer(self, user_answer: str) -> bool:
        """ Check the answer provided by the user.
        Returns:
            bool: True if answer is correct, False otherwise
        """
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        return False
