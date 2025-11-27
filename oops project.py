#Question and project description
'''1. Calculator project
   2. Quiz App
   3. To-Do List App
   4. Number Guessing Game
   using "oops".'''
   

#python code using oops
print("1. calculator")

class calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def product(self,a,b):
        return a*b
    def divide(self,a,b):
        return a/b

cal = calculator()

while True:
    print("calculator menu")
    print("1. addition")
    print("2. subraction")
    print("3. multiplication")
    print("4. Divison")
    print("5. exit")

    choice = int(input("enter your choice"))
    if choice == 5:
        print("thank for using calculator")
        break

    a=int(input("enter a value"))
    b=int(input("enter b value"))

    if choice == 1:
        print("add ",cal.add(a,b))
    elif choice ==2:
        print("sub ",cal.sub(a,b))
    elif choice == 3:
        print("product", cal.product(a,b))
    elif choice == 4:
        print("divide", cal.divide(a,b))
    
    else:
        print("invalid menu")


print("2. quizz game")

print("quiz question each carry 5 marks")
print("------")

class quiz:
    def ask_question(self,question_1,option_1,question_2,option_2,validation):
        self.question_1=question_1
        self.option_1=option_1
        self.question_2=question_2
        self.option_2=option_2
        self.validation=validation

    def question_1 (self,question):
        print(f"your 1st question is:{question}")
    def option_1 (self,option):
        print(f"option:{option}") 
    def question_2 (self,question):
        print(f"your 2nd question is:{question}")
    def option_2 (self,option):
        print(f"option:{option}")
    def validation (self,mark,comments):
        print(f"your mark of quizz question is : {mark} {comments}")

    
q=quiz()
q.question_1("what is the state animal of Tamil Nadu")
q.option_1("a.tiger b.lion c.nilgiri d.elephant")

print("------")

q.question_2("who is called as Father of India")
q.option_2("a.nehru b.mother terasa c.gandhi d.vallabhai pathal")

print("-------")

a=5
b=0




choice_1=input("enter your option for question 1 : ")
if choice_1 == "c":
    print("Correct answer")
else:
    print("Incorrect answer")

if choice_1!="c":
    print("correct answer is option (c) nilgiri")
else:
    print("correct answer")

print("------")

choice_2=input("enter your option  for question 2 : ")
if choice_2 == "c":
    print("correct answer")
else:
    print("Incorrect answer")
if choice_2!="c":
    print("correct answer is option (c) gandhi")
else:
    print("correct answer")

print("------")
if choice_1=="c" and choice_2=="c":
    q.validation(a+a,"**excellent**")
elif choice_1!="c" and choice_2!="c":
    q.validation(b+b,"**better luck next time**")
else:
    q.validation(a+b,"**good**")

print("3.TODO app")

class to_do:
    def __init__(self):
        pass
    def task(self,complete):
        print(f"you successfully complected your {complete}")
    def exit(self,exit):
        print(f"{exit}")

t = to_do()


a="1. Do warm up & excersise"
b="2. Have a fresh juice"
c="3. Take a bath"
d="4. exit"

while True:
    print("your respected task are:")
    print("1. Do warm up and excersise")
    print("2. Have a fresh juice")
    print("3. Take a bath")
    print("4. exit")
    
    print("------")

    menu=int(input("enter your menu number 1-4 :"))
    if menu==1:
        print(t.task("1st task"))
        print("your remaining task :")
        print(b)
        print(c)
        print(d)
        print("------")
               
    elif menu==2:
        print(t.task("2nd task"))
        print("your remaining task :")
        print(a)
        print(c)
        print(d)
        print("------")
        
    elif menu==3:
        print(t.task("3rd task"))
        print("your remaining task :")
        print(a)
        print(b)
        print(d)
        print("------")
        
    else:
        print(t.exit("thank you"))
        break

print("4. Number guessing game")

import random
class number_guessing_game:
    def __init__(self):
        self.secret_number=random.randint(1,50)
    def guess(self,number):
        if number==self.secret_number:
            return("*correct*you guessed it")
        elif number<self.secret_number:
            return("too low")
        else:
            return("too high")
game=number_guessing_game()
while True:
    user_guess=int(input("ENTER YOUR GUESSING NUMBER (1-50):"))
    result=game.guess(user_guess)
    print(result)
    if result.startswith("correct"):
        break
        
    
class question:
     def __init__(self,text,answer):
         self.text=text
         self.answer=answer
class quiz:
     def __init__(self,question):
         self.questions=questions
         self.score=0
     def start(self):
         for i in self.questions:
             user_answer=input(i.text+"(true/false)")
             if user_answer.lower()==i.answer.lower():
                 print("correct answer")
                 self.score+=1
             else:
                 print("wrong answer")
                 print(self.score,len(self.questions))
questions=[question("Python is an interpreted language.","true"),
question("The earth is a flat.","false"),
question("Oops means object oriented programming.","true")]
quiz=quiz(question)
quiz.start()
        
        











    









































        
        
#Question and project description
'''1. Calculator project
   2. Quiz App
   3. To-Do List App
   4. Number Guessing Game
   using "oops".'''
   

#python code using oops
print("1. calculator")

class calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def product(self,a,b):
        return a*b
    def divide(self,a,b):
        return a/b

cal = calculator()

while True:
    print("calculator menu")
    print("1. addition")
    print("2. subraction")
    print("3. multiplication")
    print("4. Divison")
    print("5. exit")

    choice = int(input("enter your choice"))
    if choice == 5:
        print("thank for using calculator")
        break

    a=int(input("enter a value"))
    b=int(input("enter b value"))

    if choice == 1:
        print("add ",cal.add(a,b))
    elif choice ==2:
        print("sub ",cal.sub(a,b))
    elif choice == 3:
        print("product", cal.product(a,b))
    elif choice == 4:
        print("divide", cal.divide(a,b))
    
    else:
        print("invalid menu")


print("2. quizz game")

print("quiz question each carry 5 marks")
print("------")

class quiz:
    def ask_question(self,question_1,option_1,question_2,option_2,validation):
        self.question_1=question_1
        self.option_1=option_1
        self.question_2=question_2
        self.option_2=option_2
        self.validation=validation

    def question_1 (self,question):
        print(f"your 1st question is:{question}")
    def option_1 (self,option):
        print(f"option:{option}") 
    def question_2 (self,question):
        print(f"your 2nd question is:{question}")
    def option_2 (self,option):
        print(f"option:{option}")
    def validation (self,mark,comments):
        print(f"your mark of quizz question is : {mark} {comments}")

    
q=quiz()
q.question_1("what is the state animal of Tamil Nadu")
q.option_1("a.tiger b.lion c.nilgiri d.elephant")

print("------")

q.question_2("who is called as Father of India")
q.option_2("a.nehru b.mother terasa c.gandhi d.vallabhai pathal")

print("-------")

a=5
b=0




choice_1=input("enter your option for question 1 : ")
if choice_1 == "c":
    print("Correct answer")
else:
    print("Incorrect answer")

if choice_1!="c":
    print("correct answer is option (c) nilgiri")
else:
    print("correct answer")

print("------")

choice_2=input("enter your option  for question 2 : ")
if choice_2 == "c":
    print("correct answer")
else:
    print("Incorrect answer")
if choice_2!="c":
    print("correct answer is option (c) gandhi")
else:
    print("correct answer")

print("------")
if choice_1=="c" and choice_2=="c":
    q.validation(a+a,"**excellent**")
elif choice_1!="c" and choice_2!="c":
    q.validation(b+b,"**better luck next time**")
else:
    q.validation(a+b,"**good**")

print("3.TODO app")

class to_do:
    def __init__(self):
        pass
    def task(self,complete):
        print(f"you successfully complected your {complete}")
    def exit(self,exit):
        print(f"{exit}")

t = to_do()


a="1. Do warm up & excersise"
b="2. Have a fresh juice"
c="3. Take a bath"
d="4. exit"

while True:
    print("your respected task are:")
    print("1. Do warm up and excersise")
    print("2. Have a fresh juice")
    print("3. Take a bath")
    print("4. exit")
    
    print("------")

    menu=int(input("enter your menu number 1-4 :"))
    if menu==1:
        print(t.task("1st task"))
        print("your remaining task :")
        print(b)
        print(c)
        print(d)
        print("------")
               
    elif menu==2:
        print(t.task("2nd task"))
        print("your remaining task :")
        print(a)
        print(c)
        print(d)
        print("------")
        
    elif menu==3:
        print(t.task("3rd task"))
        print("your remaining task :")
        print(a)
        print(b)
        print(d)
        print("------")
        
    else:
        print(t.exit("thank you"))
        break

print("4. Number guessing game")

import random
class number_guessing_game:
    def __init__(self):
        self.secret_number=random.randint(1,50)
    def guess(self,number):
        if number==self.secret_number:
            return("*correct*you guessed it")
        elif number<self.secret_number:
            return("too low")
        else:
            return("too high")
game=number_guessing_game()
while True:
    user_guess=int(input("ENTER YOUR GUESSING NUMBER (1-50):"))
    result=game.guess(user_guess)
    print(result)
    if result.startswith("correct"):
        break
        
    
class question:
     def __init__(self,text,answer):
         self.text=text
         self.answer=answer
class quiz:
     def __init__(self,question):
         self.questions=questions
         self.score=0
     def start(self):
         for i in self.questions:
             user_answer=input(i.text+"(true/false)")
             if user_answer.lower()==i.answer.lower():
                 print("correct answer")
                 self.score+=1
             else:
                 print("wrong answer")
                 print(self.score,len(self.questions))
questions=[question("Python is an interpreted language.","true"),
question("The earth is a flat.","false"),
question("Oops means object oriented programming.","true")]
quiz=quiz(question)
quiz.start()
        
        











    









































        
        
#Question and project description
'''1. Calculator project
   2. Quiz App
   3. To-Do List App
   4. Number Guessing Game
   using "oops".'''
   

#python code using oops
print("1. calculator")

class calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def product(self,a,b):
        return a*b
    def divide(self,a,b):
        return a/b

cal = calculator()

while True:
    print("calculator menu")
    print("1. addition")
    print("2. subraction")
    print("3. multiplication")
    print("4. Divison")
    print("5. exit")

    choice = int(input("enter your choice"))
    if choice == 5:
        print("thank for using calculator")
        break

    a=int(input("enter a value"))
    b=int(input("enter b value"))

    if choice == 1:
        print("add ",cal.add(a,b))
    elif choice ==2:
        print("sub ",cal.sub(a,b))
    elif choice == 3:
        print("product", cal.product(a,b))
    elif choice == 4:
        print("divide", cal.divide(a,b))
    
    else:
        print("invalid menu")


print("2. quizz game")

print("quiz question each carry 5 marks")
print("------")

class quiz:
    def ask_question(self,question_1,option_1,question_2,option_2,validation):
        self.question_1=question_1
        self.option_1=option_1
        self.question_2=question_2
        self.option_2=option_2
        self.validation=validation

    def question_1 (self,question):
        print(f"your 1st question is:{question}")
    def option_1 (self,option):
        print(f"option:{option}") 
    def question_2 (self,question):
        print(f"your 2nd question is:{question}")
    def option_2 (self,option):
        print(f"option:{option}")
    def validation (self,mark,comments):
        print(f"your mark of quizz question is : {mark} {comments}")

    
q=quiz()
q.question_1("what is the state animal of Tamil Nadu")
q.option_1("a.tiger b.lion c.nilgiri d.elephant")

print("------")

q.question_2("who is called as Father of India")
q.option_2("a.nehru b.mother terasa c.gandhi d.vallabhai pathal")

print("-------")

a=5
b=0




choice_1=input("enter your option for question 1 : ")
if choice_1 == "c":
    print("Correct answer")
else:
    print("Incorrect answer")

if choice_1!="c":
    print("correct answer is option (c) nilgiri")
else:
    print("correct answer")

print("------")

choice_2=input("enter your option  for question 2 : ")
if choice_2 == "c":
    print("correct answer")
else:
    print("Incorrect answer")
if choice_2!="c":
    print("correct answer is option (c) gandhi")
else:
    print("correct answer")

print("------")
if choice_1=="c" and choice_2=="c":
    q.validation(a+a,"**excellent**")
elif choice_1!="c" and choice_2!="c":
    q.validation(b+b,"**better luck next time**")
else:
    q.validation(a+b,"**good**")

print("3.TODO app")

class to_do:
    def __init__(self):
        pass
    def task(self,complete):
        print(f"you successfully complected your {complete}")
    def exit(self,exit):
        print(f"{exit}")

t = to_do()


a="1. Do warm up & excersise"
b="2. Have a fresh juice"
c="3. Take a bath"
d="4. exit"

while True:
    print("your respected task are:")
    print("1. Do warm up and excersise")
    print("2. Have a fresh juice")
    print("3. Take a bath")
    print("4. exit")
    
    print("------")

    menu=int(input("enter your menu number 1-4 :"))
    if menu==1:
        print(t.task("1st task"))
        print("your remaining task :")
        print(b)
        print(c)
        print(d)
        print("------")
               
    elif menu==2:
        print(t.task("2nd task"))
        print("your remaining task :")
        print(a)
        print(c)
        print(d)
        print("------")
        
    elif menu==3:
        print(t.task("3rd task"))
        print("your remaining task :")
        print(a)
        print(b)
        print(d)
        print("------")
        
    else:
        print(t.exit("thank you"))
        break

print("4. Number guessing game")

import random
class number_guessing_game:
    def __init__(self):
        self.secret_number=random.randint(1,50)
    def guess(self,number):
        if number==self.secret_number:
            return("*correct*you guessed it")
        elif number<self.secret_number:
            return("too low")
        else:
            return("too high")
game=number_guessing_game()
while True:
    user_guess=int(input("ENTER YOUR GUESSING NUMBER (1-50):"))
    result=game.guess(user_guess)
    print(result)
    if result.startswith("correct"):
        break
        
    
class question:
     def __init__(self,text,answer):
         self.text=text
         self.answer=answer
class quiz:
     def __init__(self,question):
         self.questions=questions
         self.score=0
     def start(self):
         for i in self.questions:
             user_answer=input(i.text+"(true/false)")
             if user_answer.lower()==i.answer.lower():
                 print("correct answer")
                 self.score+=1
             else:
                 print("wrong answer")
                 print(self.score,len(self.questions))
questions=[question("Python is an interpreted language.","true"),
question("The earth is a flat.","false"),
question("Oops means object oriented programming.","true")]
quiz=quiz(question)
quiz.start()
        
        











    





#Question and project description
'''1. Calculator project
   2. Quiz App
   3. To-Do List App
   4. Number Guessing Game
   using "oops".'''
   

#python code using oops
print("1. calculator")

class calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def product(self,a,b):
        return a*b
    def divide(self,a,b):
        return a/b

cal = calculator()

while True:
    print("calculator menu")
    print("1. addition")
    print("2. subraction")
    print("3. multiplication")
    print("4. Divison")
    print("5. exit")

    choice = int(input("enter your choice"))
    if choice == 5:
        print("thank for using calculator")
        break

    a=int(input("enter a value"))
    b=int(input("enter b value"))

    if choice == 1:
        print("add ",cal.add(a,b))
    elif choice ==2:
        print("sub ",cal.sub(a,b))
    elif choice == 3:
        print("product", cal.product(a,b))
    elif choice == 4:
        print("divide", cal.divide(a,b))
    
    else:
        print("invalid menu")


print("2. quizz game")

print("quiz question each carry 5 marks")
print("------")

class quiz:
    def ask_question(self,question_1,option_1,question_2,option_2,validation):
        self.question_1=question_1
        self.option_1=option_1
        self.question_2=question_2
        self.option_2=option_2
        self.validation=validation

    def question_1 (self,question):
        print(f"your 1st question is:{question}")
    def option_1 (self,option):
        print(f"option:{option}") 
    def question_2 (self,question):
        print(f"your 2nd question is:{question}")
    def option_2 (self,option):
        print(f"option:{option}")
    def validation (self,mark,comments):
        print(f"your mark of quizz question is : {mark} {comments}")

    
q=quiz()
q.question_1("what is the state animal of Tamil Nadu")
q.option_1("a.tiger b.lion c.nilgiri d.elephant")

print("------")

q.question_2("who is called as Father of India")
q.option_2("a.nehru b.mother terasa c.gandhi d.vallabhai pathal")

print("-------")

a=5
b=0




choice_1=input("enter your option for question 1 : ")
if choice_1 == "c":
    print("Correct answer")
else:
    print("Incorrect answer")

if choice_1!="c":
    print("correct answer is option (c) nilgiri")
else:
    print("correct answer")

print("------")

choice_2=input("enter your option  for question 2 : ")
if choice_2 == "c":
    print("correct answer")
else:
    print("Incorrect answer")
if choice_2!="c":
    print("correct answer is option (c) gandhi")
else:
    print("correct answer")

print("------")
if choice_1=="c" and choice_2=="c":
    q.validation(a+a,"**excellent**")
elif choice_1!="c" and choice_2!="c":
    q.validation(b+b,"**better luck next time**")
else:
    q.validation(a+b,"**good**")

print("3.TODO app")

class to_do:
    def __init__(self):
        pass
    def task(self,complete):
        print(f"you successfully complected your {complete}")
    def exit(self,exit):
        print(f"{exit}")

t = to_do()


a="1. Do warm up & excersise"
b="2. Have a fresh juice"
c="3. Take a bath"
d="4. exit"

while True:
    print("your respected task are:")
    print("1. Do warm up and excersise")
    print("2. Have a fresh juice")
    print("3. Take a bath")
    print("4. exit")
    
    print("------")

    menu=int(input("enter your menu number 1-4 :"))
    if menu==1:
        print(t.task("1st task"))
        print("your remaining task :")
        print(b)
        print(c)
        print(d)
        print("------")
               
    elif menu==2:
        print(t.task("2nd task"))
        print("your remaining task :")
        print(a)
        print(c)
        print(d)
        print("------")
        
    elif menu==3:
        print(t.task("3rd task"))
        print("your remaining task :")
        print(a)
        print(b)
        print(d)
        print("------")
        
    else:
        print(t.exit("thank you"))
        break

print("4. Number guessing game")

import random
class number_guessing_game:
    def __init__(self):
        self.secret_number=random.randint(1,50)
    def guess(self,number):
        if number==self.secret_number:
            return("*correct*you guessed it")
        elif number<self.secret_number:
            return("too low")
        else:
            return("too high")
game=number_guessing_game()
while True:
    user_guess=int(input("ENTER YOUR GUESSING NUMBER (1-50):"))
    result=game.guess(user_guess)
    print(result)
    if result.startswith("correct"):
        break
        
    
class question:
     def __init__(self,text,answer):
         self.text=text
         self.answer=answer
class quiz:
     def __init__(self,question):
         self.questions=questions
         self.score=0
     def start(self):
         for i in self.questions:
             user_answer=input(i.text+"(true/false)")
             if user_answer.lower()==i.answer.lower():
                 print("correct answer")
                 self.score+=1
             else:
                 print("wrong answer")
                 print(self.score,len(self.questions))
questions=[question("Python is an interpreted language.","true"),
question("The earth is a flat.","false"),
question("Oops means object oriented programming.","true")]
quiz=quiz(question)
quiz.start()
        
        











    









































        
        
#Question and project description
'''1. Calculator project
   2. Quiz App
   3. To-Do List App
   4. Number Guessing Game
   using "oops".'''
   

#python code using oops
print("1. calculator")

class calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def product(self,a,b):
        return a*b
    def divide(self,a,b):
        return a/b

cal = calculator()

while True:
    print("calculator menu")
    print("1. addition")
    print("2. subraction")
    print("3. multiplication")
    print("4. Divison")
    print("5. exit")

    choice = int(input("enter your choice"))
    if choice == 5:
        print("thank for using calculator")
        break

    a=int(input("enter a value"))
    b=int(input("enter b value"))

    if choice == 1:
        print("add ",cal.add(a,b))
    elif choice ==2:
        print("sub ",cal.sub(a,b))
    elif choice == 3:
        print("product", cal.product(a,b))
    elif choice == 4:
        print("divide", cal.divide(a,b))
    
    else:
        print("invalid menu")


print("2. quizz game")

print("quiz question each carry 5 marks")
print("------")

class quiz:
    def ask_question(self,question_1,option_1,question_2,option_2,validation):
        self.question_1=question_1
        self.option_1=option_1
        self.question_2=question_2
        self.option_2=option_2
        self.validation=validation

    def question_1 (self,question):
        print(f"your 1st question is:{question}")
    def option_1 (self,option):
        print(f"option:{option}") 
    def question_2 (self,question):
        print(f"your 2nd question is:{question}")
    def option_2 (self,option):
        print(f"option:{option}")
    def validation (self,mark,comments):
        print(f"your mark of quizz question is : {mark} {comments}")

    
q=quiz()
q.question_1("what is the state animal of Tamil Nadu")
q.option_1("a.tiger b.lion c.nilgiri d.elephant")

print("------")

q.question_2("who is called as Father of India")
q.option_2("a.nehru b.mother terasa c.gandhi d.vallabhai pathal")

print("-------")

a=5
b=0




choice_1=input("enter your option for question 1 : ")
if choice_1 == "c":
    print("Correct answer")
else:
    print("Incorrect answer")

if choice_1!="c":
    print("correct answer is option (c) nilgiri")
else:
    print("correct answer")

print("------")

choice_2=input("enter your option  for question 2 : ")
if choice_2 == "c":
    print("correct answer")
else:
    print("Incorrect answer")
if choice_2!="c":
    print("correct answer is option (c) gandhi")
else:
    print("correct answer")

print("------")
if choice_1=="c" and choice_2=="c":
    q.validation(a+a,"**excellent**")
elif choice_1!="c" and choice_2!="c":
    q.validation(b+b,"**better luck next time**")
else:
    q.validation(a+b,"**good**")

print("3.TODO app")

class to_do:
    def __init__(self):
        pass
    def task(self,complete):
        print(f"you successfully complected your {complete}")
    def exit(self,exit):
        print(f"{exit}")

t = to_do()


a="1. Do warm up & excersise"
b="2. Have a fresh juice"
c="3. Take a bath"
d="4. exit"

while True:
    print("your respected task are:")
    print("1. Do warm up and excersise")
    print("2. Have a fresh juice")
    print("3. Take a bath")
    print("4. exit")
    
    print("------")

    menu=int(input("enter your menu number 1-4 :"))
    if menu==1:
        print(t.task("1st task"))
        print("your remaining task :")
        print(b)
        print(c)
        print(d)
        print("------")
               
    elif menu==2:
        print(t.task("2nd task"))
        print("your remaining task :")
        print(a)
        print(c)
        print(d)
        print("------")
        
    elif menu==3:
        print(t.task("3rd task"))
        print("your remaining task :")
        print(a)
        print(b)
        print(d)
        print("------")
        
    else:
        print(t.exit("thank you"))
        break

print("4. Number guessing game")

import random
class number_guessing_game:
    def __init__(self):
        self.secret_number=random.randint(1,50)
    def guess(self,number):
        if number==self.secret_number:
            return("*correct*you guessed it")
        elif number<self.secret_number:
            return("too low")
        else:
            return("too high")
game=number_guessing_game()
while True:
    user_guess=int(input("ENTER YOUR GUESSING NUMBER (1-50):"))
    result=game.guess(user_guess)
    print(result)
    if result.startswith("correct"):
        break
        
    
class question:
     def __init__(self,text,answer):
         self.text=text
         self.answer=answer
class quiz:
     def __init__(self,question):
         self.questions=questions
         self.score=0
     def start(self):
         for i in self.questions:
             user_answer=input(i.text+"(true/false)")
             if user_answer.lower()==i.answer.lower():
                 print("correct answer")
                 self.score+=1
             else:
                 print("wrong answer")
                 print(self.score,len(self.questions))
questions=[question("Python is an interpreted language.","true"),
question("The earth is a flat.","false"),
question("Oops means object oriented programming.","true")]
quiz=quiz(question)
quiz.start()
        
        











    









































        
        
#Question and project description
'''1. Calculator project
   2. Quiz App
   3. To-Do List App
   4. Number Guessing Game
   using "oops".'''
   

#python code using oops
print("1. calculator")

class calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def product(self,a,b):
        return a*b
    def divide(self,a,b):
        return a/b

cal = calculator()

while True:
    print("calculator menu")
    print("1. addition")
    print("2. subraction")
    print("3. multiplication")
    print("4. Divison")
    print("5. exit")

    choice = int(input("enter your choice"))
    if choice == 5:
        print("thank for using calculator")
        break

    a=int(input("enter a value"))
    b=int(input("enter b value"))

    if choice == 1:
        print("add ",cal.add(a,b))
    elif choice ==2:
        print("sub ",cal.sub(a,b))
    elif choice == 3:
        print("product", cal.product(a,b))
    elif choice == 4:
        print("divide", cal.divide(a,b))
    
    else:
        print("invalid menu")


print("2. quizz game")

print("quiz question each carry 5 marks")
print("------")

class quiz:
    def ask_question(self,question_1,option_1,question_2,option_2,validation):
        self.question_1=question_1
        self.option_1=option_1
        self.question_2=question_2
        self.option_2=option_2
        self.validation=validation

    def question_1 (self,question):
        print(f"your 1st question is:{question}")
    def option_1 (self,option):
        print(f"option:{option}") 
    def question_2 (self,question):
        print(f"your 2nd question is:{question}")
    def option_2 (self,option):
        print(f"option:{option}")
    def validation (self,mark,comments):
        print(f"your mark of quizz question is : {mark} {comments}")

    
q=quiz()
q.question_1("what is the state animal of Tamil Nadu")
q.option_1("a.tiger b.lion c.nilgiri d.elephant")

print("------")

q.question_2("who is called as Father of India")
q.option_2("a.nehru b.mother terasa c.gandhi d.vallabhai pathal")

print("-------")

a=5
b=0




choice_1=input("enter your option for question 1 : ")
if choice_1 == "c":
    print("Correct answer")
else:
    print("Incorrect answer")

if choice_1!="c":
    print("correct answer is option (c) nilgiri")
else:
    print("correct answer")

print("------")

choice_2=input("enter your option  for question 2 : ")
if choice_2 == "c":
    print("correct answer")
else:
    print("Incorrect answer")
if choice_2!="c":
    print("correct answer is option (c) gandhi")
else:
    print("correct answer")

print("------")
if choice_1=="c" and choice_2=="c":
    q.validation(a+a,"**excellent**")
elif choice_1!="c" and choice_2!="c":
    q.validation(b+b,"**better luck next time**")
else:
    q.validation(a+b,"**good**")

print("3.TODO app")

class to_do:
    def __init__(self):
        pass
    def task(self,complete):
        print(f"you successfully complected your {complete}")
    def exit(self,exit):
        print(f"{exit}")

t = to_do()


a="1. Do warm up & excersise"
b="2. Have a fresh juice"
c="3. Take a bath"
d="4. exit"

while True:
    print("your respected task are:")
    print("1. Do warm up and excersise")
    print("2. Have a fresh juice")
    print("3. Take a bath")
    print("4. exit")
    
    print("------")

    menu=int(input("enter your menu number 1-4 :"))
    if menu==1:
        print(t.task("1st task"))
        print("your remaining task :")
        print(b)
        print(c)
        print(d)
        print("------")
               
    elif menu==2:
        print(t.task("2nd task"))
        print("your remaining task :")
        print(a)
        print(c)
        print(d)
        print("------")
        
    elif menu==3:
        print(t.task("3rd task"))
        print("your remaining task :")
        print(a)
        print(b)
        print(d)
        print("------")
        
    else:
        print(t.exit("thank you"))
        break

print("4. Number guessing game")

import random
class number_guessing_game:
    def __init__(self):
        self.secret_number=random.randint(1,50)
    def guess(self,number):
        if number==self.secret_number:
            return("*correct*you guessed it")
        elif number<self.secret_number:
            return("too low")
        else:
            return("too high")
game=number_guessing_game()
while True:
    user_guess=int(input("ENTER YOUR GUESSING NUMBER (1-50):"))
    result=game.guess(user_guess)
    print(result)
    if result.startswith("correct"):
        break
        
    
class question:
     def __init__(self,text,answer):
         self.text=text
         self.answer=answer
class quiz:
     def __init__(self,question):
         self.questions=questions
         self.score=0
     def start(self):
         for i in self.questions:
             user_answer=input(i.text+"(true/false)")
             if user_answer.lower()==i.answer.lower():
                 print("correct answer")
                 self.score+=1
             else:
                 print("wrong answer")
                 print(self.score,len(self.questions))
questions=[question("Python is an interpreted language.","true"),
question("The earth is a flat.","false"),
question("Oops means object oriented programming.","true")]
quiz=quiz(question)
quiz.start()
        
        











    









































        
        
#Question and project description
'''1. Calculator project
   2. Quiz App
   3. To-Do List App
   4. Number Guessing Game
   using "oops".'''
   

#python code using oops
print("1. calculator")

class calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def product(self,a,b):
        return a*b
    def divide(self,a,b):
        return a/b

cal = calculator()

while True:
    print("calculator menu")
    print("1. addition")
    print("2. subraction")
    print("3. multiplication")
    print("4. Divison")
    print("5. exit")

    choice = int(input("enter your choice"))
    if choice == 5:
        print("thank for using calculator")
        break

    a=int(input("enter a value"))
    b=int(input("enter b value"))

    if choice == 1:
        print("add ",cal.add(a,b))
    elif choice ==2:
        print("sub ",cal.sub(a,b))
    elif choice == 3:
        print("product", cal.product(a,b))
    elif choice == 4:
        print("divide", cal.divide(a,b))
    
    else:
        print("invalid menu")


print("2. quizz game")

print("quiz question each carry 5 marks")
print("------")

class quiz:
    def ask_question(self,question_1,option_1,question_2,option_2,validation):
        self.question_1=question_1
        self.option_1=option_1
        self.question_2=question_2
        self.option_2=option_2
        self.validation=validation

    def question_1 (self,question):
        print(f"your 1st question is:{question}")
    def option_1 (self,option):
        print(f"option:{option}") 
    def question_2 (self,question):
        print(f"your 2nd question is:{question}")
    def option_2 (self,option):
        print(f"option:{option}")
    def validation (self,mark,comments):
        print(f"your mark of quizz question is : {mark} {comments}")

    
q=quiz()
q.question_1("what is the state animal of Tamil Nadu")
q.option_1("a.tiger b.lion c.nilgiri d.elephant")

print("------")

q.question_2("who is called as Father of India")
q.option_2("a.nehru b.mother terasa c.gandhi d.vallabhai pathal")

print("-------")

a=5
b=0




choice_1=input("enter your option for question 1 : ")
if choice_1 == "c":
    print("Correct answer")
else:
    print("Incorrect answer")

if choice_1!="c":
    print("correct answer is option (c) nilgiri")
else:
    print("correct answer")

print("------")

choice_2=input("enter your option  for question 2 : ")
if choice_2 == "c":
    print("correct answer")
else:
    print("Incorrect answer")
if choice_2!="c":
    print("correct answer is option (c) gandhi")
else:
    print("correct answer")

print("------")
if choice_1=="c" and choice_2=="c":
    q.validation(a+a,"**excellent**")
elif choice_1!="c" and choice_2!="c":
    q.validation(b+b,"**better luck next time**")
else:
    q.validation(a+b,"**good**")

print("3.TODO app")

class to_do:
    def __init__(self):
        pass
    def task(self,complete):
        print(f"you successfully complected your {complete}")
    def exit(self,exit):
        print(f"{exit}")

t = to_do()


a="1. Do warm up & excersise"
b="2. Have a fresh juice"
c="3. Take a bath"
d="4. exit"

while True:
    print("your respected task are:")
    print("1. Do warm up and excersise")
    print("2. Have a fresh juice")
    print("3. Take a bath")
    print("4. exit")
    
    print("------")

    menu=int(input("enter your menu number 1-4 :"))
    if menu==1:
        print(t.task("1st task"))
        print("your remaining task :")
        print(b)
        print(c)
        print(d)
        print("------")
               
    elif menu==2:
        print(t.task("2nd task"))
        print("your remaining task :")
        print(a)
        print(c)
        print(d)
        print("------")
        
    elif menu==3:
        print(t.task("3rd task"))
        print("your remaining task :")
        print(a)
        print(b)
        print(d)
        print("------")
        
    else:
        print(t.exit("thank you"))
        break

print("4. Number guessing game")

import random
class number_guessing_game:
    def __init__(self):
        self.secret_number=random.randint(1,50)
    def guess(self,number):
        if number==self.secret_number:
            return("*correct*you guessed it")
        elif number<self.secret_number:
            return("too low")
        else:
            return("too high")
game=number_guessing_game()
while True:
    user_guess=int(input("ENTER YOUR GUESSING NUMBER (1-50):"))
    result=game.guess(user_guess)
    print(result)
    if result.startswith("correct"):
        break
        
    
class question:
     def __init__(self,text,answer):
         self.text=text
         self.answer=answer
class quiz:
     def __init__(self,question):
         self.questions=questions
         self.score=0
     def start(self):
         for i in self.questions:
             user_answer=input(i.text+"(true/false)")
             if user_answer.lower()==i.answer.lower():
                 print("correct answer")
                 self.score+=1
             else:
                 print("wrong answer")
                 print(self.score,len(self.questions))
questions=[question("Python is an interpreted language.","true"),
question("The earth is a flat.","false"),
question("Oops means object oriented programming.","true")]
quiz=quiz(question)
quiz.start()
        
        











    









































        
        
#Question and project description
'''1. Calculator project
   2. Quiz App
   3. To-Do List App
   4. Number Guessing Game
   using "oops".'''
   

#python code using oops
print("1. calculator")

class calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def product(self,a,b):
        return a*b
    def divide(self,a,b):
        return a/b

cal = calculator()

while True:
    print("calculator menu")
    print("1. addition")
    print("2. subraction")
    print("3. multiplication")
    print("4. Divison")
    print("5. exit")

    choice = int(input("enter your choice"))
    if choice == 5:
        print("thank for using calculator")
        break

    a=int(input("enter a value"))
    b=int(input("enter b value"))

    if choice == 1:
        print("add ",cal.add(a,b))
    elif choice ==2:
        print("sub ",cal.sub(a,b))
    elif choice == 3:
        print("product", cal.product(a,b))
    elif choice == 4:
        print("divide", cal.divide(a,b))
    
    else:
        print("invalid menu")


print("2. quizz game")

print("quiz question each carry 5 marks")
print("------")

class quiz:
    def ask_question(self,question_1,option_1,question_2,option_2,validation):
        self.question_1=question_1
        self.option_1=option_1
        self.question_2=question_2
        self.option_2=option_2
        self.validation=validation

    def question_1 (self,question):
        print(f"your 1st question is:{question}")
    def option_1 (self,option):
        print(f"option:{option}") 
    def question_2 (self,question):
        print(f"your 2nd question is:{question}")
    def option_2 (self,option):
        print(f"option:{option}")
    def validation (self,mark,comments):
        print(f"your mark of quizz question is : {mark} {comments}")

    
q=quiz()
q.question_1("what is the state animal of Tamil Nadu")
q.option_1("a.tiger b.lion c.nilgiri d.elephant")

print("------")

q.question_2("who is called as Father of India")
q.option_2("a.nehru b.mother terasa c.gandhi d.vallabhai pathal")

print("-------")

a=5
b=0




choice_1=input("enter your option for question 1 : ")
if choice_1 == "c":
    print("Correct answer")
else:
    print("Incorrect answer")

if choice_1!="c":
    print("correct answer is option (c) nilgiri")
else:
    print("correct answer")

print("------")

choice_2=input("enter your option  for question 2 : ")
if choice_2 == "c":
    print("correct answer")
else:
    print("Incorrect answer")
if choice_2!="c":
    print("correct answer is option (c) gandhi")
else:
    print("correct answer")

print("------")
if choice_1=="c" and choice_2=="c":
    q.validation(a+a,"**excellent**")
elif choice_1!="c" and choice_2!="c":
    q.validation(b+b,"**better luck next time**")
else:
    q.validation(a+b,"**good**")

print("3.TODO app")

class to_do:
    def __init__(self):
        pass
    def task(self,complete):
        print(f"you successfully complected your {complete}")
    def exit(self,exit):
        print(f"{exit}")

t = to_do()


a="1. Do warm up & excersise"
b="2. Have a fresh juice"
c="3. Take a bath"
d="4. exit"

while True:
    print("your respected task are:")
    print("1. Do warm up and excersise")
    print("2. Have a fresh juice")
    print("3. Take a bath")
    print("4. exit")
    
    print("------")

    menu=int(input("enter your menu number 1-4 :"))
    if menu==1:
        print(t.task("1st task"))
        print("your remaining task :")
        print(b)
        print(c)
        print(d)
        print("------")
               
    elif menu==2:
        print(t.task("2nd task"))
        print("your remaining task :")
        print(a)
        print(c)
        print(d)
        print("------")
        
    elif menu==3:
        print(t.task("3rd task"))
        print("your remaining task :")
        print(a)
        print(b)
        print(d)
        print("------")
        
    else:
        print(t.exit("thank you"))
        break

print("4. Number guessing game")

import random
class number_guessing_game:
    def __init__(self):
        self.secret_number=random.randint(1,50)
    def guess(self,number):
        if number==self.secret_number:
            return("*correct*you guessed it")
        elif number<self.secret_number:
            return("too low")
        else:
            return("too high")
game=number_guessing_game()
while True:
    user_guess=int(input("ENTER YOUR GUESSING NUMBER (1-50):"))
    result=game.guess(user_guess)
    print(result)
    if result.startswith("correct"):
        break
        
    
class question:
     def __init__(self,text,answer):
         self.text=text
         self.answer=answer
class quiz:
     def __init__(self,question):
         self.questions=questions
         self.score=0
     def start(self):
         for i in self.questions:
             user_answer=input(i.text+"(true/false)")
             if user_answer.lower()==i.answer.lower():
                 print("correct answer")
                 self.score+=1
             else:
                 print("wrong answer")
                 print(self.score,len(self.questions))
questions=[question("Python is an interpreted language.","true"),
question("The earth is a flat.","false"),
question("Oops means object oriented programming.","true")]
quiz=quiz(question)
quiz.start()
        
        











    

























#Question and project description
'''1. Calculator project
   2. Quiz App
   3. To-Do List App
   4. Number Guessing Game
   using "oops".'''
   

#python code using oops
print("1. calculator")

class calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def product(self,a,b):
        return a*b
    def divide(self,a,b):
        return a/b

cal = calculator()

while True:
    print("calculator menu")
    print("1. addition")
    print("2. subraction")
    print("3. multiplication")
    print("4. Divison")
    print("5. exit")

    choice = int(input("enter your choice"))
    if choice == 5:
        print("thank for using calculator")
        break

    a=int(input("enter a value"))
    b=int(input("enter b value"))

    if choice == 1:
        print("add ",cal.add(a,b))
    elif choice ==2:
        print("sub ",cal.sub(a,b))
    elif choice == 3:
        print("product", cal.product(a,b))
    elif choice == 4:
        print("divide", cal.divide(a,b))
    
    else:
        print("invalid menu")


print("2. quizz game")

print("quiz question each carry 5 marks")
print("------")

class quiz:
    def ask_question(self,question_1,option_1,question_2,option_2,validation):
        self.question_1=question_1
        self.option_1=option_1
        self.question_2=question_2
        self.option_2=option_2
        self.validation=validation

    def question_1 (self,question):
        print(f"your 1st question is:{question}")
    def option_1 (self,option):
        print(f"option:{option}") 
    def question_2 (self,question):
        print(f"your 2nd question is:{question}")
    def option_2 (self,option):
        print(f"option:{option}")
    def validation (self,mark,comments):
        print(f"your mark of quizz question is : {mark} {comments}")

    
q=quiz()
q.question_1("what is the state animal of Tamil Nadu")
q.option_1("a.tiger b.lion c.nilgiri d.elephant")

print("------")

q.question_2("who is called as Father of India")
q.option_2("a.nehru b.mother terasa c.gandhi d.vallabhai pathal")

print("-------")

a=5
b=0




choice_1=input("enter your option for question 1 : ")
if choice_1 == "c":
    print("Correct answer")
else:
    print("Incorrect answer")

if choice_1!="c":
    print("correct answer is option (c) nilgiri")
else:
    print("correct answer")

print("------")

choice_2=input("enter your option  for question 2 : ")
if choice_2 == "c":
    print("correct answer")
else:
    print("Incorrect answer")
if choice_2!="c":
    print("correct answer is option (c) gandhi")
else:
    print("correct answer")

print("------")
if choice_1=="c" and choice_2=="c":
    q.validation(a+a,"**excellent**")
elif choice_1!="c" and choice_2!="c":
    q.validation(b+b,"**better luck next time**")
else:
    q.validation(a+b,"**good**")

print("3.TODO app")

class to_do:
    def __init__(self):
        pass
    def task(self,complete):
        print(f"you successfully complected your {complete}")
    def exit(self,exit):
        print(f"{exit}")

t = to_do()


a="1. Do warm up & excersise"
b="2. Have a fresh juice"
c="3. Take a bath"
d="4. exit"

while True:
    print("your respected task are:")
    print("1. Do warm up and excersise")
    print("2. Have a fresh juice")
    print("3. Take a bath")
    print("4. exit")
    
    print("------")

    menu=int(input("enter your menu number 1-4 :"))
    if menu==1:
        print(t.task("1st task"))
        print("your remaining task :")
        print(b)
        print(c)
        print(d)
        print("------")
               
    elif menu==2:
        print(t.task("2nd task"))
        print("your remaining task :")
        print(a)
        print(c)
        print(d)
        print("------")
        
    elif menu==3:
        print(t.task("3rd task"))
        print("your remaining task :")
        print(a)
        print(b)
        print(d)
        print("------")
        
    else:
        print(t.exit("thank you"))
        break

print("4. Number guessing game")

import random
class number_guessing_game:
    def __init__(self):
        self.secret_number=random.randint(1,50)
    def guess(self,number):
        if number==self.secret_number:
            return("*correct*you guessed it")
        elif number<self.secret_number:
            return("too low")
        else:
            return("too high")
game=number_guessing_game()
while True:
    user_guess=int(input("ENTER YOUR GUESSING NUMBER (1-50):"))
    result=game.guess(user_guess)
    print(result)
    if result.startswith("correct"):
        break
        
    
class question:
     def __init__(self,text,answer):
         self.text=text
         self.answer=answer
class quiz:
     def __init__(self,question):
         self.questions=questions
         self.score=0
     def start(self):
         for i in self.questions:
             user_answer=input(i.text+"(true/false)")
             if user_answer.lower()==i.answer.lower():
                 print("correct answer")
                 self.score+=1
             else:
                 print("wrong answer")
                 print(self.score,len(self.questions))
questions=[question("Python is an interpreted language.","true"),
question("The earth is a flat.","false"),
question("Oops means object oriented programming.","true")]
quiz=quiz(question)
quiz.start()
        
        











    









































        
        
#Question and project description
'''1. Calculator project
   2. Quiz App
   3. To-Do List App
   4. Number Guessing Game
   using "oops".'''
   

#python code using oops
print("1. calculator")

class calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def product(self,a,b):
        return a*b
    def divide(self,a,b):
        return a/b

cal = calculator()

while True:
    print("calculator menu")
    print("1. addition")
    print("2. subraction")
    print("3. multiplication")
    print("4. Divison")
    print("5. exit")

    choice = int(input("enter your choice"))
    if choice == 5:
        print("thank for using calculator")
        break

    a=int(input("enter a value"))
    b=int(input("enter b value"))

    if choice == 1:
        print("add ",cal.add(a,b))
    elif choice ==2:
        print("sub ",cal.sub(a,b))
    elif choice == 3:
        print("product", cal.product(a,b))
    elif choice == 4:
        print("divide", cal.divide(a,b))
    
    else:
        print("invalid menu")


print("2. quizz game")

print("quiz question each carry 5 marks")
print("------")

class quiz:
    def ask_question(self,question_1,option_1,question_2,option_2,validation):
        self.question_1=question_1
        self.option_1=option_1
        self.question_2=question_2
        self.option_2=option_2
        self.validation=validation

    def question_1 (self,question):
        print(f"your 1st question is:{question}")
    def option_1 (self,option):
        print(f"option:{option}") 
    def question_2 (self,question):
        print(f"your 2nd question is:{question}")
    def option_2 (self,option):
        print(f"option:{option}")
    def validation (self,mark,comments):
        print(f"your mark of quizz question is : {mark} {comments}")

    
q=quiz()
q.question_1("what is the state animal of Tamil Nadu")
q.option_1("a.tiger b.lion c.nilgiri d.elephant")

print("------")

q.question_2("who is called as Father of India")
q.option_2("a.nehru b.mother terasa c.gandhi d.vallabhai pathal")

print("-------")

a=5
b=0




choice_1=input("enter your option for question 1 : ")
if choice_1 == "c":
    print("Correct answer")
else:
    print("Incorrect answer")

if choice_1!="c":
    print("correct answer is option (c) nilgiri")
else:
    print("correct answer")

print("------")

choice_2=input("enter your option  for question 2 : ")
if choice_2 == "c":
    print("correct answer")
else:
    print("Incorrect answer")
if choice_2!="c":
    print("correct answer is option (c) gandhi")
else:
    print("correct answer")

print("------")
if choice_1=="c" and choice_2=="c":
    q.validation(a+a,"**excellent**")
elif choice_1!="c" and choice_2!="c":
    q.validation(b+b,"**better luck next time**")
else:
    q.validation(a+b,"**good**")

print("3.TODO app")

class to_do:
    def __init__(self):
        pass
    def task(self,complete):
        print(f"you successfully complected your {complete}")
    def exit(self,exit):
        print(f"{exit}")

t = to_do()


a="1. Do warm up & excersise"
b="2. Have a fresh juice"
c="3. Take a bath"
d="4. exit"

while True:
    print("your respected task are:")
    print("1. Do warm up and excersise")
    print("2. Have a fresh juice")
    print("3. Take a bath")
    print("4. exit")
    
    print("------")

    menu=int(input("enter your menu number 1-4 :"))
    if menu==1:
        print(t.task("1st task"))
        print("your remaining task :")
        print(b)
        print(c)
        print(d)
        print("------")
               
    elif menu==2:
        print(t.task("2nd task"))
        print("your remaining task :")
        print(a)
        print(c)
        print(d)
        print("------")
        
    elif menu==3:
        print(t.task("3rd task"))
        print("your remaining task :")
        print(a)
        print(b)
        print(d)
        print("------")
        
    else:
        print(t.exit("thank you"))
        break

print("4. Number guessing game")

import random
class number_guessing_game:
    def __init__(self):
        self.secret_number=random.randint(1,50)
    def guess(self,number):
        if number==self.secret_number:
            return("*correct*you guessed it")
        elif number<self.secret_number:
            return("too low")
        else:
            return("too high")
game=number_guessing_game()
while True:
    user_guess=int(input("ENTER YOUR GUESSING NUMBER (1-50):"))
    result=game.guess(user_guess)
    print(result)
    if result.startswith("correct"):
        break
        
    
class question:
     def __init__(self,text,answer):
         self.text=text
         self.answer=answer
class quiz:
     def __init__(self,question):
         self.questions=questions
         self.score=0
     def start(self):
         for i in self.questions:
             user_answer=input(i.text+"(true/false)")
             if user_answer.lower()==i.answer.lower():
                 print("correct answer")
                 self.score+=1
             else:
                 print("wrong answer")
                 print(self.score,len(self.questions))
questions=[question("Python is an interpreted language.","true"),
question("The earth is a flat.","false"),
question("Oops means object oriented programming.","true")]
quiz=quiz(question)
quiz.start()
        
        











    


























#Question and project description
'''1. Calculator project
   2. Quiz App
   3. To-Do List App
   4. Number Guessing Game
   using "oops".'''
   

#python code using oops
print("1. calculator")

class calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def product(self,a,b):
        return a*b
    def divide(self,a,b):
        return a/b

cal = calculator()

while True:
    print("calculator menu")
    print("1. addition")
    print("2. subraction")
    print("3. multiplication")
    print("4. Divison")
    print("5. exit")

    choice = int(input("enter your choice"))
    if choice == 5:
        print("thank for using calculator")
        break

    a=int(input("enter a value"))
    b=int(input("enter b value"))

    if choice == 1:
        print("add ",cal.add(a,b))
    elif choice ==2:
        print("sub ",cal.sub(a,b))
    elif choice == 3:
        print("product", cal.product(a,b))
    elif choice == 4:
        print("divide", cal.divide(a,b))
    
    else:
        print("invalid menu")


print("2. quizz game")

print("quiz question each carry 5 marks")
print("------")

class quiz:
    def ask_question(self,question_1,option_1,question_2,option_2,validation):
        self.question_1=question_1
        self.option_1=option_1
        self.question_2=question_2
        self.option_2=option_2
        self.validation=validation

    def question_1 (self,question):
        print(f"your 1st question is:{question}")
    def option_1 (self,option):
        print(f"option:{option}") 
    def question_2 (self,question):
        print(f"your 2nd question is:{question}")
    def option_2 (self,option):
        print(f"option:{option}")
    def validation (self,mark,comments):
        print(f"your mark of quizz question is : {mark} {comments}")

    
q=quiz()
q.question_1("what is the state animal of Tamil Nadu")
q.option_1("a.tiger b.lion c.nilgiri d.elephant")

print("------")

q.question_2("who is called as Father of India")
q.option_2("a.nehru b.mother terasa c.gandhi d.vallabhai pathal")

print("-------")

a=5
b=0




choice_1=input("enter your option for question 1 : ")
if choice_1 == "c":
    print("Correct answer")
else:
    print("Incorrect answer")

if choice_1!="c":
    print("correct answer is option (c) nilgiri")
else:
    print("correct answer")

print("------")

choice_2=input("enter your option  for question 2 : ")
if choice_2 == "c":
    print("correct answer")
else:
    print("Incorrect answer")
if choice_2!="c":
    print("correct answer is option (c) gandhi")
else:
    print("correct answer")

print("------")
if choice_1=="c" and choice_2=="c":
    q.validation(a+a,"**excellent**")
elif choice_1!="c" and choice_2!="c":
    q.validation(b+b,"**better luck next time**")
else:
    q.validation(a+b,"**good**")

print("3.TODO app")

class to_do:
    def __init__(self):
        pass
    def task(self,complete):
        print(f"you successfully complected your {complete}")
    def exit(self,exit):
        print(f"{exit}")

t = to_do()


a="1. Do warm up & excersise"
b="2. Have a fresh juice"
c="3. Take a bath"
d="4. exit"

while True:
    print("your respected task are:")
    print("1. Do warm up and excersise")
    print("2. Have a fresh juice")
    print("3. Take a bath")
    print("4. exit")
    
    print("------")

    menu=int(input("enter your menu number 1-4 :"))
    if menu==1:
        print(t.task("1st task"))
        print("your remaining task :")
        print(b)
        print(c)
        print(d)
        print("------")
               
    elif menu==2:
        print(t.task("2nd task"))
        print("your remaining task :")
        print(a)
        print(c)
        print(d)
        print("------")
        
    elif menu==3:
        print(t.task("3rd task"))
        print("your remaining task :")
        print(a)
        print(b)
        print(d)
        print("------")
        
    else:
        print(t.exit("thank you"))
        break

print("4. Number guessing game")

import random
class number_guessing_game:
    def __init__(self):
        self.secret_number=random.randint(1,50)
    def guess(self,number):
        if number==self.secret_number:
            return("*correct*you guessed it")
        elif number<self.secret_number:
            return("too low")
        else:
            return("too high")
game=number_guessing_game()
while True:
    user_guess=int(input("ENTER YOUR GUESSING NUMBER (1-50):"))
    result=game.guess(user_guess)
    print(result)
    if result.startswith("correct"):
        break
        
    
class question:
     def __init__(self,text,answer):
         self.text=text
         self.answer=answer
class quiz:
     def __init__(self,question):
         self.questions=questions
         self.score=0
     def start(self):
         for i in self.questions:
             user_answer=input(i.text+"(true/false)")
             if user_answer.lower()==i.answer.lower():
                 print("correct answer")
                 self.score+=1
             else:
                 print("wrong answer")
                 print(self.score,len(self.questions))
questions=[question("Python is an interpreted language.","true"),
question("The earth is a flat.","false"),
question("Oops means object oriented programming.","true")]
quiz=quiz(question)
quiz.start()
        
        











    





















#Question and project description
'''1. Calculator project
   2. Quiz App
   3. To-Do List App
   4. Number Guessing Game
   using "oops".'''

#python code using oops
print("1. calculator")

class calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def product(self,a,b):
        return a*b
    def divide(self,a,b):
        return a/b

cal = calculator()

while True:
    print("calculator menu")
    print("1. addition")
    print("2. subraction")
    print("3. multiplication")
    print("4. Divison")
    print("5. exit")

    choice = int(input("enter your choice"))
    if choice == 5:
        print("thank for using calculator")
        break

    a=int(input("enter a value"))
    b=int(input("enter b value"))

    if choice == 1:
        print("add ",cal.add(a,b))
    elif choice ==2:
        print("sub ",cal.sub(a,b))
    elif choice == 3:
        print("product", cal.product(a,b))
    
    elif choice == 4:
        print("divide", cal.divide(a,b))
    
    else:
        print("invalid menu")


print("2. quizz game")

print("quiz question each carry 5 marks")
print("------")

class quiz:
    def ask_question(self,question_1,option_1,question_2,option_2,validation):
        self.question_1=question_1
        self.option_1=option_1
        self.question_2=question_2
        self.option_2=option_2
        self.validation=validation

    def question_1 (self,question):
        print(f"your 1st question is:{question}")
    def option_1 (self,option):
        print(f"option:{option}") 
    def question_2 (self,question):
        print(f"your 2nd question is:{question}")
    def option_2 (self,option):
        print(f"option:{option}")
    def validation (self,mark,comments):
        print(f"your mark of quizz question is : {mark} {comments}")

    
q=quiz()
q.question_1("what is the state animal of Tamil Nadu")
q.option_1("a.tiger b.lion c.nilgiri d.elephant")

print("------")

q.question_2("who is called as Father of India")
q.option_2("a.nehru b.mother terasa c.gandhi d.vallabhai pathal")

print("-------")

a=5
b=0




choice_1=input("enter your option for question 1 : ")
if choice_1 == "c":
    print("Correct answer")
else:
    print("Incorrect answer")

if choice_1!="c":
    print("correct answer is option (c) nilgiri")
else:
    print("correct answer")

print("------")

choice_2=input("enter your option  for question 2 : ")
if choice_2 == "c":
    print("correct answer")
else:
    print("Incorrect answer")
if choice_2!="c":
    print("correct answer is option (c) gandhi")
else:
    print("correct answer")

print("------")
if choice_1=="c" and choice_2=="c":
    q.validation(a+a,"**excellent**")
elif choice_1!="c" and choice_2!="c":
    q.validation(b+b,"**better luck next time**")
else:
    q.validation(a+b,"**good**")

print("3.TODO app")

class to_do:
    def __init__(self):
        pass
    def task(self,complete):
        print(f"you successfully complected your {complete}")
    def exit(self,exit):
        print(f"{exit}")

t = to_do()


a="1. Do warm up & excersise"
b="2. Have a fresh juice"
c="3. Take a bath"
d="4. exit"

while True:
    print("your respected task are:")
    print("1. Do warm up and excersise")
    print("2. Have a fresh juice")
    print("3. Take a bath")
    print("4. exit")
    
    print("------")

    menu=int(input("enter your menu number 1-4 :"))
    if menu==1:
        print(t.task("1st task"))
        print("your remaining task :")
        print(b)
        print(c)
        print(d)
        print("------")
               
    elif menu==2:
        print(t.task("2nd task"))
        print("your remaining task :")
        print(a)
        print(c)
        print(d)
        print("------")
        
    elif menu==3:
        print(t.task("3rd task"))
        print("your remaining task :")
        print(a)
        print(b)
        print(d)
        print("------")
        
    else:
        print(t.exit("thank you"))
        break

print("4. Number guessing game")

import random
class number_guessing_game:
    def __init__(self):
        self.secret_number=random.randint(1,50)
    def guess(self,number):
        if number==self.secret_number:
            return("*correct*you guessed it")
        elif number<self.secret_number:
            return("too low")
        else:
            return("too high")
game=number_guessing_game()
while True:
    user_guess=int(input("ENTER YOUR GUESSING NUMBER (1-50):"))
    result=game.guess(user_guess)
    print(result)
    if result.startswith("correct"):
        break
        
    
class question:
     def __init__(self,text,answer):
         self.text=text
         self.answer=answer
class quiz:
     def __init__(self,question):
         self.questions=questions
         self.score=0
     def start(self):
         for i in self.questions:
             user_answer=input(i.text+"(true/false)")
             if user_answer.lower()==i.answer.lower():
                 print("correct answer")
                 self.score+=1
             else:
                 print("wrong answer")
                 print(self.score,len(self.questions))
questions=[question("Python is an interpreted language.","true"),
question("The earth is a flat.","false"),
question("Oops means object oriented programming.","true")]
quiz=quiz(question)
quiz.start()















        
        















        
        
















        
        




































        
        
