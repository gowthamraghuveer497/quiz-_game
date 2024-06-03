print("WELCOME TO LAKSHIT'S 17TH BDAY PARTY")
print("lets see who knows laks the best by answering these simple questions")
answers = input("so lets begin....yes or no ??")

scores = 0
total_questions = 5

if answers.lowerr == ("yes"):
    answers = input("question 1 : what is laks fav anime ??")
    if answers.lower == ("one peice"):
        scores = +1
    else:
        print("wrong!!!!")

    
    answers = input("question 2 : what is laks eye power ??(answer eg : 1-2 r/L respectively)")
    if answers.lower == ("6-8"):
        scores = +1
    else:
        print("wrong!!!!")

   
    answers = input("question 3 : what is laks fav h-anime ??")
    if answers.lower == ("lolicon"):
        scores = +1
    else:
        print("wrong!!!!")

    
    answers = input("question 4 : what is laks fav car company ??")
    if answers.lower == ("konisegg"):
        scores = +1
    else:
        print("wrong!!!!")

    
    answers = input("question 5 : when did laks get his braces ?? (year-month)")
    if answers.lower == ("2023-june"):
        scores = +1
    else:
        print("wrong!!!!")

print("THANK YOU FOR PLAYING!! APNE BUFFET ENJOY KARE :) ") 
marks = (scores/total_questions) * 100
print ("marks obtained" , marks)
print("khana tuso saab abh hehe")


    


