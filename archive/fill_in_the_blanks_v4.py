
# IPND Stage 2 Final Project

# Sharon Francisco
# 24 September 2016

# Here are the quiz_string, question numbers, and answers for the Easy level.
easy_string = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___
takes by adding ___2___ separated by commas between the parentheses. ___1___s by
default return ___3___ if you don't specify the value to return. ___2___ can be
standard data types such as string, number, dictionary, tuple, and ___4___ or
can be more complicated such as objects and lambda functions.'''

easy_questions = ["1", "2", "3", "4"]
easy_answers = ["function", "arguments", "None", "list"]

# Here are the quiz_string, question numbers and answers for the Medium level.
medium_string = '''___1___ often! For every small piece of code you write, ___1___ it
immediately before moving on. Try to write the smallest ___1___able code you can
manage for each step; it's good practice for minimizing ___2___ time and for
reusing code later!
Python's ___3___ will tell you where your error is and what the error is.
When ___2___ a program, it is very useful to check the state of ___4___ at
various points in the execution of the program. Scattering ___5___ statements
to find out what the values of selected ___4___ are will show what the ___4___
is at specific points in the program. This can be used to compare what you think
the ___4___ states should be with what they actually are, allowing you to
find errors.'''

medium_questions = ["1", "2", "3", "4", "5"]
medium_answers = ["test", "debugging", "Traceback", "variable", "print"]

# Here are the quiz_string, question numbers and answers for the Hard level.
hard_string = '''___1___ are the essential construct that lets us execute a
series of instructions as many times as we want. ___1___ are a set of
instructions we program for a computer to repeat a certain number of times.
___2___ ___1___ run code until the specified condition is false.
___2___ count < n
tells the comupter to run our set of instructions n number of times.
Make sure to increment count by one at the end of the ___1___.
It is HIGHLY recommended that whenever we code a ___2___ ___1___, we
first set up the structure and make sure that our count variable increases in
value. This will help us avoid getting into ___3___ ___1___ with ___2___ ___1___.
___4___ ___1___ tell us to iterate through each element in out list, tuple, or
other iterable until we reach the end of this iterable. We do not need to worry
about incrementing any variable named count because by using this construct, we
have told the ___4___ ___1___ construct to end the ___1___ once it has reached
the end of the list.
If we simply want to iterate through a list of increasing numbers from 0 to 9,
we can use the ___5___() function. The ___5___() function can take a number and
return a list of values increasing from 0 to that number, exclusive, meaning
that the list does not include the number that we are passing into the
___5___() function.'''

hard_questions = ["1", "2", "3", "4", "5"]
hard_answers = ["loops", "While", "infinite", "For", "range"]




# Here are the dictionaries for the levels and their quiz_strings and question numbers.
string = {"Easy": easy_string, "Medium": medium_string, "Hard": hard_string}
numbers = {"Easy": easy_questions, "Medium": medium_questions, "Hard": hard_questions}
answers = {"Easy": easy_answers, "Medium": medium_answers, "Hard": hard_answers}


# Has the user input the desired game level and returns the selected level.
def get_level():
    '''This function has the user input the game level and returns the selected level.'''
    choices = ["Easy", "Medium", "Hard"]
    print "Please select a game difficulty by typing it in."
    string_choices = choices [0] + ", " + choices[1] + ", or " + choices[2]
    # Ask the player to input the level he wants to play.
    level = raw_input("Possible choices are " + string_choices + ". ")
    # If the player does not select a valid level, keep asking for input.
    while level not in choices:
        print "That is not a valid difficulty."
        level = raw_input("Possible choices are " + string_choices + ". ")
    else:
        print "You have chosen " + level + "!"
        print "You will get five guesses per problem."
        print "The current paragraph reads as such:"
        return level
    

# Function to see if numbered blank in quiz_string is a subset of the question numbers.
# If the numbered blank is in quiz_string, returns the question number as an integer and the word.
# If the word is not in question_numbers, the function returns None.
def number_in_string(word, question_numbers):
    '''Checks to see if a numbered blank in quiz_string is a subset of the question
numbers. Returns the number and the question number.'''
    for n in question_numbers:
        if n in word:
            return int(n), word
    return None


# Function to loop through the quiz_string.
# Inputs are the quiz_string for the selected level, the question_numbers,
# the correct answers, the last updated quiz_string, and the counter from the
# calling loop. The outputs are either the updated quiz string with the correct
# answer or add the word to replaced.
def loop_thru_quiz_string(quiz_string, question_numbers, quiz_answers, replaced, counter):
    '''Loops through the quiz_string and checks the answer'''
    for word in quiz_string:
        # Pass the current word and question_numbers to the number_in_string function.
        question = number_in_string(word, question_numbers)
        if question != None:
            # Get the answer based on the counter from the loop in play_game().
            answer = quiz_answers[counter]
            # Pass the word from the number_in_string() function, the answer, 
            # and the quiz_string to the input_answer() function.
            quiz_string = input_answer(question[1], answer, quiz_string)
            return quiz_string            
        else:
            replaced.append(word)

# Function for getting the first three guesses wrong.
# Takes the counter as input, and increments it by one as the output.
# Tells user the answer is incorrect and how many guesses are left.
def wrong_first_three(counter):
    '''Tells user answer is incorrect and how many guesses are left.'''
    print "That isn't the correct answer! Try again."
    print "You have " + str(5 - counter) + " tries left!"
    counter = counter + 1
    return counter
    
# Function for getting the fourth guess wrong.
# Takes the counter as input, and increments it by one as the output.
# Tells user the answer is incorrect and has one guess left.
def wrong_fourth(counter):
    '''Tells user the answer is incorrect and has one guess left'''
    print "That isn't the correct answer! You only have 1 try left! Make it count!"
    counter = counter + 1
    return counter

#Function ends the game after the fifth incorrect guess.
def end_game():
    '''Ends the game after the fifth incorrect guess.'''
    import sys
    print "You've failed too many straight guesses! Game over!"
    sys.exit()

    

# Asks the user for an answer to the question_number, then compares the user input to the
# correct answer. The user gets 5 guesses. If the user does not answer correctly after 5
# guesses, the game ends.
def input_answer(question_number, answer, quiz_string):
    '''Asks the user for his answer and compares the input to the correct answer.'''
    counter = 1
    question = "What should be substituted in for " + question_number + "? "
    while counter <= 3:
        # Ask the user to input the answer
        user_input = raw_input(question)
        if user_input == answer:
            new_quiz_string = update_quizString(quiz_string, question_number, answer)
            counter = 7
            return new_quiz_string
        else:
            counter = wrong_first_three(counter)        
    if counter == 4:
        user_input = raw_input(question)
        if user_input == answer:
            new_quiz_string = update_quizString(quiz_string, question_number, answer)
            counter = 7
            return new_quiz_string
        else:
            counter = wrong_fourth(counter)
    if counter == 5:
        user_input = raw_input(question)
        if user_input == answer:
            new_quiz_string = update_quizString(quiz_string, question_number, answer)
            counter = 7
            return new_quiz_string
        else:
            end_game()


        
# Updates the quiz_string with the correct answer, then splits it again.
# Inputs are the quiz_string for the selected level, the current question_number,
# and the correct answer. Outputs are the quiz_string updated with the correct
# answer replacing the numbered blank.
def update_quizString(quiz_string, question_number, answer):
    '''Updates the quiz_string with the correct answer.'''
    new_quiz_string = " ".join(quiz_string)
    new_quiz_string = new_quiz_string.replace(question_number, answer)
    print "Correct!"
    print('\n')
    print "The current paragraph reads as such:"
    print new_quiz_string
    print('\n')
    new_quiz_string = new_quiz_string.split()
    return new_quiz_string



# This is the function that initiates the game.
# The inputs are the dictionaries for the quiz, the numbered blanks, and the answers.
def play_game(string, numbers, answers):
    '''Function initiates the game. Inputs are the string, the question numbers,
    and the answers.'''
    # Have the user choose a game level.
    level = get_level()
    # Based on the level the user chose, display the corresponding quiz_string.
    quiz_string = string.get(level)
    print('\n')
    print quiz_string

    # Based on the level the user chose, get the corresponding question_numbers
    question_numbers = numbers.get(level)

    # Based on the level the user chose, get the corresponding answers
    quiz_answers = answers.get(level)
    count = len(quiz_answers)

    replaced = []
    quiz_string = quiz_string.split()

    counter = 0
    for num in range(1, count + 1):
        quiz_string = loop_thru_quiz_string(quiz_string, question_numbers, quiz_answers, replaced, counter)
        replaced = []
        counter = counter + 1
    else:
        replaced = " ".join(replaced)
        print replaced
        print "Congratulations! You won!"
        return


play_game(string, numbers, answers)

    
    
