# IPND Stage 2 Final Project

# Sharon Francisco
# 11 September 2016


# Function to see if numbered blank in quiz_string is a subset of the question numbers.
def number_in_string(word, question_numbers):
    '''Checks to see if a numbered blank in quiz_string is a subset of the question numbers. Returns the number and the question number.'''
    for n in question_numbers:
        if n in word:
            return int(n), word
    return None


def update_quizString(quiz_string, question_number, answer):
    new_quiz_string = " ".join(quiz_string)
    new_quiz_string = new_quiz_string.replace(question_number, answer)
    print "Correct!"
    print('\n')
    print new_quiz_string
    new_quiz_string = new_quiz_string.split()
    print new_quiz_string
    return new_quiz_string



# Function to ask the user to input his answer.
def input_answer(question, quiz_answers, quiz_string):
        # Ask the user to input the answer.
        user_input = raw_input("What should be substituted in for " + question[1] + "? ")
        # Pass the question number, the user's answer, and the correct answers to the
        # check_answer function. If the answer is correct, the function returns True.
        response = check_answer(question[0], user_input, quiz_answers)
        if response == True:
            print "2nd if loop"
            new_quiz_string = " ".join(quiz_string)
            new_quiz_string = new_quiz_string.replace(question[1], user_input)
            print "Correct!"
            print('\n')
            print new_quiz_string
            quiz_string = new_quiz_string.split()
            print quiz_string
            return quiz_string
        else:
            i = 1
            counter = 5
            for i in range(counter):
                guesses_left = "You have " + str(counter) + " guesses left!"
                print "Incorrect! Try again." + guesses_left
                user_input = raw_input("What should be substituted in for " + question[1] + "? ")
                counter = counter - 1
            else:
                print "You've failed too many straight guesses! Game over!"
                # I need to end the game here
                return;





# Function to check validity of user's answer
def check_answer(number, guess, answer):
    '''Checks the answer input by user. Inputs are question number, raw_input, and the answer key.'''
    if guess == answer[number - 1]:
        return True
    else:
        return False




# Function to loop through the quiz_string
def loop_thru_quiz_string(quiz_string, question_numbers, quiz_answers, replaced):
    for word in quiz_string:
        print "1st for loop: " + word

        # Pass the current word and question_numbers to the number_in_string function.
        # If the word is in the question_numbers, the function returns the question_number
        # as an integer and the word. If the word is not in question_numbers, the
        # function returns None.
        question = number_in_string(word, question_numbers)
        if question != None:
            print "1st if loop: " + question[1]
            quiz_string = input_answer(question, quiz_answers, quiz_string)

        else:
            replaced.append(word)
    




# Use the madlibs generator code as a starting point

def play_game():
    choices = ["Easy", "Medium", "Hard"]
    print "Please select a game difficulty by typing it in."
    string_choices = choices [0] + ", " + choices[1] + ", or " + choices[2]
    level = raw_input("Possible choices are " + string_choices + ". ")
    # If the player does not select a valid level, keep asking for input.
    while level not in choices:
        print "That is not a valid difficulty."
        level = raw_input("Possible choices are Easy, Medium, and Hard. ")
    else:
        print "You have chosen " + level + "!"

    # based on level, print the right string.
    # that string needs to become quiz_string (see below)
    # I need to work on the formatting of the quiz_strings

    # Here are the quiz_string, question numbers, and answers for the Easy level.
    easy_string = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___
takes by adding ___2___ separated by commas between the parentheses. ___1___s by default
return ___3___ if you don't specify the value to return. ___2___ can be standard data
types such as string, number, dictionary, tuple, and ___4___ or can be more complicated
such as objects and lambda functions.'''

    easy_questions = ["1", "2", "3", "4"]
    easy_answers = ["function", "arguments", "None", "list"]

    # Here are the dictionaries for the levels and their quiz_strings and question numbers.
    string = {"Easy": easy_string, "Medium": "placeholder1", "Hard": "placeholder2"}
    numbers = {"Easy": easy_questions, "Medium": "later", "Hard": "tomorrow"}
    answers = {"Easy": easy_answers, "Medium": "not now", "Hard": "some other time"}
    
    # Based on the level the user chose, display the corresponding quiz_string.
    quiz_string = string.get(level)
    print('\n')
    print quiz_string

    # Based on the level the user chose, get the corresponding question_numbers
    question_numbers = numbers.get(level)

    # Based on the level the user chose, get the corresponding answers
    quiz_answers = answers.get(level)

    replaced = []
    quiz_string = quiz_string.split()

    quiz_string = loop_thru_quiz_string(quiz_string, question_numbers, quiz_answers, replaced)

    replaced = " ".join(replaced)
    print replaced
    return;

play_game()
            

