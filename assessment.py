"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

2. What is a class?

3. What is an instance attribute?

4. What is a method?

5. What is an instance in object orientation?

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

#### See about_OOP.txt (Laurel)

"""


# Parts 2 through 5:
# Create your classes and class methods

# Student class


class Student_Info(object):
    """Information about students including first name, last name, and address"""

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = "{} {}".format(first_name, last_name)
        self.address = address


class Questions(object):
    """A dictionary of question/answer pairs"""

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def ask_and_evaluate(self):
        student_answer = raw_input("{} >".format(self.question))
        if student_answer == self.answer:
            return True
        else:
            return False


class Exam(object):
    "A list of questions and correct answers"

    def __init__(self, exam_name):
        self.exam_name = exam_name
        self.all_exam_questions = []

    def add_question(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer
        exam_question = Questions(question, correct_answer)
        self.all_exam_questions.append(exam_question)

        def administer_exam(self):
            score = 0.0
            question_count = 0.0

            for question in self.all_exam_questions:
                if Questions.ask_and_evaluate() is True:
                    score += 1.0
                    question_count += 1.0
                else:
                    question_count += 1.0

            final_score = (score / question_count) * 100
            return final_score


def take_test(exam_name, first_name, last_name):
    student_score = Exam.administer_exam()
    print "On {} {} {} got a score of {}".format(exam_name, first_name, last_name, student_score)


def example():


    # Instantiate student
    jessica = Student_Info("Jessica", "Rabbit", "123 Main St., Anytown, CA, 94105")

    # Instantiate exam
    exam1 = Exam("Midterm")

    # Create exam question list

    ##### Artificial case where I'm hard-coding a list of questions rather than
    # prompting the teacher for them.
    possible_questions = [
        ("What are the first 3 digits of pi?", "3.14"),
        ("What is Newton's 2nd law?", "F =ma")
        ]

    for question in possible_questions:
        exam1.add_question(question[0], question[1])

    # Take test & report score
    take_test(exam1.name, jessica.first_name, jessica.last_name)

example()
