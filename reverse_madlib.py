#-*-coding: utf-8-*-
quiz_ques = ["HTML stand for 1_____ text markup language. \nIn HTML, we have 2_____ heading tags for writing heading. \nHTML tags are used to mark-up HTML 3_____ . \nHTML documents imply a structure of 4_____ HTML elements.",
"HTML is used to create 1_____ documents (called pages) that are displayed on the World Wide Web. \nAttributes usually consist of 2 parts : An attribute name and its 2_____ . \nHTML consists of a set of elments, which define the 3_____ meaning of their content. \nNamed character 4_____ are used to print characters that have a special meaning in HTML.",
"HTML has a mechanism for embedding 1_____ that are not displayed when the page is rendered in a browser. \nTags are enclosed by 2_____ brackets, and the closing tag begins with a forward slash in HTML. \nThe 3_____ declaration refers to a Document Type Definition(DTD). \nThe browser collapses the multiple white spaces into a 4_____ white space in HTML."]

ans = [["hyper","six","elements","nested"],["electronic","value","semantic","references"],["comments","angle","doctype","single"]]

def right(ques,ans,index):
    # fn has 3 inputs and executes when ans is correct to inform user and prints the statements with correct answers
    print("\nYippee...you entered correct answer...  ^ __ ^ \n")
    ques = replace_it(ques,ans,index)
    return ques

def wrong():
    # fn executes when ans is wrong and prints that to inform user
    print("\nOhhh...you entered wrong option...Plz try again...  ^ __ ^ \n")

def replace_it(ques,ans,index):
    # fn has 3 inputs and replaces blank with correct answer in the statement and returns that statements
    final_statement = []
    initial_statement = ques.split()
    for word in initial_statement:
        if word != str(index) + "_____":
            final_statement.append(word)
        else:
            final_statement.append(ans)
    ques=" ".join(final_statement)
    return ques


def check_my_ans(ques,ans):
    # fn has 2 inputs and checks whether the ans entered is correct or not and therby printing the questions again
    for ans_index in xrange(0,4):
        questionNo = ans_index + 1
        while(1):
            answer = raw_input("\nenter the answer for ques " + str(questionNo) + " is :-  ").lower()
            if answer == ans[ans_index]:
                ques = right(ques,answer,questionNo)
                show_quiz(ques)
                break
            else:
                wrong()
                show_quiz(ques)
    print "\nCongrats...you are a genius...you did it...keep it up...  ^ __ ^ \n"

def show_quiz(ques):
    # takes ques as input and this fn prints the ques
    print ques

def choose_level():
    # has no input, asks user to enter leve and returns the value
    print("Select the level of the quiz...  ^ __ ^ ")
    user_input = int(raw_input("Enter 1 for Level 1   ^ __ ^ \n" + "Enter 2 for Level 2   ^ __ ^ \n" + "Enter 3 for Level 3   ^ __ ^ \n" + "So the level is :-  "))
    print("\nSo, now be calm and concentrate on your level " + str(user_input) + " quiz   ^ __ ^ \n")
    return user_input - 1

def quiz(ques,ans):
    # takes 2 inputs and calls another fn to print the quiz questions, to chec kans and to continue quiz
    show_quiz(ques)
    check_my_ans(ques,ans)
    continuing()


def continuing():
    # takes no input and ask user whether he want to continue the quiz or not
    user_input = raw_input("So, would you like to take the challange again...???   ^ __ ^ \nEnter yes to continue or no to quit   ^ __ ^ \nSo what's your decision :- ").lower()
    if user_input == 'yes':
        play_it(quiz_ques,ans)
    else:
        print("\nThnx for playing the quiz...You did well...Keep it up...  ^ __ ^ \n")

def play_it(quiz_ques,ans):
    # fn takes two variables as inputs and calls other fn to choose level and to play quiz further
    print("\nWelcome...to the WORLD of QUESTIONS...  ^ __ ^ \n")
    level = choose_level()
    questions = quiz_ques[level]
    answers = ans[level]
    quiz(questions,answers)


play_it(quiz_ques,ans)
