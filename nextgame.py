#do Ctrl A then Ctrl C the paste into idle. Do not look at the code, just run it!!!!





















































questionOneCorrect = 0
print("Welcome back. let's test your memory.") 
print("First question.")
while questionOneCorrect == 0:
    print("How many puzzles were there in the original game?")
    questionOneAnswer = raw_input()
    questionOneAnswer = str(questionOneAnswer)
    if str.lower(questionOneAnswer) == "four":
        print("Correct!")
        questionOneCorrect = 1
    elif questionOneAnswer == "4":
        print("Correct!")
        questionOneCorrect = 1
    else:
        print("Incorrect!")
questionTwoCorrect = 0
print("Second question.")
while questionTwoCorrect == 0:
    print("Who was the famous figure you put in the anagram generator?")
    questionTwoAnswer = raw_input()
    questionTwoAnswer = str(questionTwoAnswer)
    if str.lower(questionTwoAnswer) == "william shakespeare":
        print("Correct!")
        questionTwoCorrect = 1
    else:
        print("Incorrect!")
questionThreeCorrect = 0
print("Third question.")
while questionThreeCorrect == 0:
    print("What are we?")
    questionThreeAnswer = raw_input()
    questionThreeAnswer = str(questionThreeAnswer)
    if str.lower(questionThreeAnswer) == "the eye":
        print("Correct!")
        questionThreeCorrect = 1
    else:
        print("Incorrect!")
print("Fourth question.")
questionFourCorrect = 0
while questionFourCorrect == 0:
    print("What social media cite did you use?")
    questionFourAnswer = raw_input()
    questionFourAnswer = str(questionFourAnswer)
    if str.lower(questionFourAnswer) == "instagram":
        print("Correct!")
        questionFourCorrect = 1
    else:
        print("Incorrect!")
print("Fifth question. Are you sure you want to continue?")
questionFiveCorrect = 0
while questionFiveCorrect == 0:
    print("You are not safe... in the last game what was the quiz about?")
    questionFiveAnswer = raw_input()
    questionFiveAnswer = str(questionFiveAnswer)
    if str.lower(questionFiveAnswer) == "dantes inferno":
        print("Correct!")
        questionFiveCorrect = 1
    else:
        print("Incorrect!")
print("Sixth question.")
questionSixCorrect = 0
while questionSixCorrect == 0:
    print("Do you beleive in hell?")
    questionSixAnswer = raw_input()
    if str.lower(questionSixAnswer) == "yes":
        print("Correct!")
        questionSixCorrect = 1
    elif str.lower(questionSixAnswer) == "of course":
        print("Correct!")
        questionSixCorrect = 1
    else:
        print("Incorrect!")
print("Seventh question")
questionSevenCorrect = 0
while questionSevenCorrect == 0:
    print("You have gone too far, there is no turning back. Do not blame us for what is to come. Are you ready?")
    questionSevenAnswer = raw_input()
    if str.lower(questionSevenAnswer) == "yes":
        print("Correct!")
        questionSevenCorrect = 1
    elif str.lower(questionSevenAnswer) == "of course":
        print("Correct!")
        questionSevenCorrect = 1
    else:
        print("You may leave now")
print("Eighth qustion")
questionEightCorrect = 0
while questionEightCorrect == 0:
    print("Im glad you stayed, it would be no fun if you left.... What's Our name")
    questionEightAnswer = raw_input()
    if str.lower(questionEightAnswer) == "beta":
        print("Correct!")
        questionEightCorrect = 1
    elif str. lower(questionEightAnswer) == "beta2332":
        print("Correct!")
        questionEightCorrect = 1
    else:
        print("Incorrect!")
print("Ninth question")
questionNineCorrect = 0
while questionNineCorrect == 0:
    print("Your mother and father have been kidnapped. The person says,'pick one, and the other dies.' What do you say?")
    questionNineAnswer = raw_input()
    if str.lower(questionNineAnswer) == "":
          print("Correct!")
          questionNineCorrect = 1
    else:
          print("Incorrect!")

for count in range(100):
          print("")
print("You made it... i'm surprised... Beware, for he bites.  They bite; in the frostbite, the freezing plight.  A murderous plight, a band of wagon wheels screeching in the snow, they begin to slow, not grow. A murderous party indeed. What is our name? what is the devil's number? Where are you? put all three together to find the last part let's just hope... you wont die first.")
