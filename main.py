from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for data in question_data:
    question_bank.append(Question(data))

quiz = QuizBrain(question_bank)

while quiz.still_have_question():
    quiz.next_question()