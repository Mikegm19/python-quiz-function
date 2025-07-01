# python-quiz-function
def take_quiz():
    score=0
    print("Welcome To Our Game Show")
    print("\nI am going to be asking you 5 of questions")
    print("Your First Question is:")
    ans_1='China'
    while True:
        q1=input("\nWhat is the name of the most populous country in the world ")
        if q1.strip().lower()=='china':
            print("Correct!!")
            score+=1
            print(score)
            break
        else:
                print("Snap, its's Wrong")
                print(f"Yor score is still: {score}")
                print("The right answer is china")
                break

            
      while True:
          q2=input("\nWho is reffered to as 'the father of the modern Science' " )
          if q2.strip().lower()=='einstein':
              print("Great You Are Good at this!!")
              score+=1
              print(score)
              break
              
          elif q2.strip().lower()=='albert einstein':
              print("Great You Are Good at this!!")
              score+=1
              print(score)
              break
          else:
              print("Snap, its's Wrong")
              print(f"Your score is still: {score}")
              break
  
      
      while True:
          q3=input("\nWhat name do we give the title 'power house of the cell'   ")
          if q3.strip().lower()=='mitochondria':
              print("Correct, doing good!!")
              score+=1
              print(score)
              break
          else:
              print("Snap, its's Wrong")
              print(f"Your score is still: {score}")
              break
  
  
      while True:
          q4=input("\n'I think so therefore I am' who was popularly known for this insight, full name   ")
          if q4.strip().lower()=='rene decarte':
              print("Correct!!")
              score+=1
              print(score)
              break
          else:
              print("Oops Not quite")
              print(f"Yor score is still: {score}")
              break
  
  
      while True:
          q5=input("\nWhat state was known to be the cradle of modern civilisation   ")
          if q5.strip().lower()=='greece':
              print("Correct!!")
              score+=1
              print(score)
              break
          else:
              print("Oops Not quite")
              print(f"Yor score is still: {score} ")
              break
      if score == 5:
          print(f"\n YOUR FINAL SCORE is: {score} Your score is Excellent")
      elif score<= 2:
          print(f"\n YOUR FINAL SCORE is: {score} Your score is poor")
      else:
          print(f"\n YOUR FINAL SCORE is: {score}  Your score is good")
                





        



