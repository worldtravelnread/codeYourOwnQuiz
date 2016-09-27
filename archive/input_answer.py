


question_number = "__1__"
answer = "one"

def input_answer(question_number, answer):
    counter = 1
    question = "What should be substituted in for " + question_number + "?"
    while counter <= 4:
        # Ask the user to input the answer
        user_input = raw_input(question)
        if user_input == answer:
            print "Correct!"
            return answer
        else:
            print "That isn't the correct answer! Try again."
            print "You have " + str(6 - counter) + " tries left!"
            print counter
            counter = counter + 1
    if counter == 5:
        user_input = raw_input(question)
        if user_input == answer:
            print "Correct"
            return answer
        else:
            print "That isn't the correct answer! You only have 1 try left! Make it count!"
            counter = counter + 1
    if counter == 6:
        user_input = raw_input(question)
        if user_input == answer:
            print "Correct"
            return answer
        else:
            print "You've failed too many straight guesses! Game Over!"
            
        
    
input_answer(question_number, answer)
