#math practice game, with three levels of difficulty
#by Abnash Bassi

import random

def generate_question(mode):
    
    text_question = None
    solution = None
    
    if mode == 'easy':
        first_term = random.randint(0, 100)
        second_term = random.randint(0, 100)
        add_or_sub = random.randint(0,1) #endpoints are included in the integer generated
        operator = None #for use in text form of the calculation
       
        if add_or_sub == 0: #add
            solution = first_term + second_term
            operator = ' + '
        
        else: #subtract
            solution = first_term - second_term
            operator = ' - '
        
        text_question = str(first_term) + operator + str(second_term)
    
    elif mode == 'medium':
        first_term = random.randint(0, 100)
        second_term = random.randint(0, 100)
        third_term = random.randint(0, 100)
        add_or_sub_1 = random.randint(0,1) #for operator between first and second term
        add_or_sub_2 = random.randint(0,1) #for operator between second and third term
        operator_1 = None #for use in text form of the calculation
        operator_2 = None #for use in text form of the calculation
       
        if add_or_sub_1 == 0: #add first and second term
            solution = first_term + second_term
            operator_1 = ' + '
       
        elif add_or_sub_1 == 1: #subtract first and second term
            solution = first_term - second_term
            operator_1 = ' - '
            
        if add_or_sub_2 == 0: #add third term to result from first and second terms
            solution += third_term
            operator_2 = ' + '
       
        elif add_or_sub_2 == 1: #subtract third term to result from first and second terms
            solution -= third_term
            operator_2 = ' - '
        
        text_question = str(first_term) + operator_1 + str(second_term) + operator_2 + str(third_term)
    
    elif mode == 'hard':
        first_term = random.randint(0, 100)
        second_term = random.randint(0, 100)
        third_term = random.randint(0, 100)
        fourth_term = random.randint(0, 100)
        add_or_sub_1 = random.randint(0,1) #for operator between first and second term
        add_or_sub_2 = random.randint(0,1) #for operator between second and third term
        add_or_sub_3 = random.randint(0,1) #for operator between third and fourth term
        operator_1 = None #for use in text form of the calculation
        operator_2 = None #for use in text form of the calculation
        operator_3 = None #for use in text form of the calculation
       
        if add_or_sub_1 == 0: #add first and second term
            solution = first_term + second_term
            operator_1 = ' + '
       
        elif add_or_sub_1 == 1: #subtract first and second term
            solution = first_term - second_term
            operator_1 = ' - '
            
        if add_or_sub_2 == 0: #add third term to result from first and second terms
            solution += third_term
            operator_2 = ' + '
       
        elif add_or_sub_2 == 1: #subtract third term to result from first and second terms
            solution -= third_term
            operator_2 = ' - '
        
        if add_or_sub_3 == 0: #add fourth term to result
            solution += fourth_term
            operator_3 = ' + '
       
        elif add_or_sub_3 == 1: #subtract fourth term from result
            solution -= fourth_term
            operator_3 = ' - '
        
        text_question = str(first_term) + operator_1 + str(second_term) + operator_2 + str(third_term) + operator_3 + str(fourth_term) 
    
    else: #if user does not select valid mode
        text_question = 'Error. Please try again and enter valid option for question difficulty.'
    
    return [text_question, solution]

def check_answer(solution, user_ans):
    message = None
    if int(solution) == int(user_ans):
        message = 'You are correct! \n'
    else:
        message = 'You were just ' + str(abs(int(solution)-int(user_ans)))+ ' away! The correct answer is ' + str(solution) + '\n'
    return message

if __name__ == "__main__":
    print('Welcome to this math game for people who can do calculus but have forgotten arithmetic!')
    mode = input('Type \'easy\', \'medium\', or \'hard\' to select the question difficulty! \n')
    mode = mode.lower().strip() #in case user types uppercase or capitalized response, or has whitespace
    [text_question, solution] = generate_question(mode)
    print(text_question)
    if solution != None: #user typed valid option
        user_ans = input('Type the correct answer and press Enter when you\'re done!\n')
        print(check_answer(solution, user_ans))