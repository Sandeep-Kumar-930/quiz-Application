class Question:
    def __init__(self, text, options, correct_option):
        self.text = text
        self.options = options
        self.correct_option = correct_option

    def is_correct(self, answer):
        return answer == self.correct_option

class Quiz:
    def __init__(self):
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def start(self):
        score = 0
        for question in self.questions:
            print(question.text)
            for i, option in enumerate(question.options, 1):
                print(f"{i}. {option}")
            answer = int(input("Enter the number of your answer: "))
            if question.is_correct(answer):
                score += 1
            print()

        print(f"You got {score} out of {len(self.questions)} questions correct!")

# Create questions
q1 = Question("What is 2 + 2?", ["4", "5", "6"], 1)
q2 = Question("What color is the sky on a clear day?", ["Blue", "Red", "Green"], 1)
q3 = Question("What animal says 'quack'?", ["Dog", "Cat", "Duck"], 3)
q4 = Question("which animal is known as the 'Ship of the Desert?", ["dog", "camel", "lion"], 2)
q5 = Question("How many days are there in a week?", ["9", "7", "5"], 2)

# Create a quiz and add questions
quiz = Quiz()
quiz.add_question(q1)
quiz.add_question(q2)
quiz.add_question(q3)
quiz.add_question(q4)
quiz.add_question(q5)

# Start the quiz
quiz.start()
