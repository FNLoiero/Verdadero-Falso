class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_have_question(self):
        if self.question_number < len(self.question_list):
            return True
        print("The game is over")
        print(f"Your final score was: {self.score}")
        return False


    def next_question(self):
        user_answer = input(f"Q.{self.question_number+1}: {self.question_list[self.question_number].text} (True/False): ")
        self.check_answer(user_answer, self.question_list[self.question_number].answer)
        self.question_number += 1

    def check_answer(self,user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("you got it right")
            self.score +=1
        else:
            print("that's wrong")
            print(f"the correct answer was: {correct_answer}")
        print(f"your score is: {self.score}/{self.question_number}\n")