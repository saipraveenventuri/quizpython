import os
from datetime import datetime
import pickle

#provides log functionality for debugging
#2 Modes have been provided log and err.
def log(logtext,mode="log"):
    if not os.path.exists("logs/"):
        os.mkdir("logs")
    if mode == "err":
        file = open("logs/error.log","a")
    else:
        file = open("logs/app.log","a")
    file.write(str(datetime.now())+"------------"+logtext+"\n")
    file.close()
    
#quiz-class
class quiz:
    def __init__(self,qname="",questions=[],options=[]):
        self.qname = qname
        self.questions = questions
        self.options = options
    def __str__(self):
        return 'quiz(name='+self.qname+', numberof questions='+str(len(self.questions))+ ')'
    def is_valid(self):
        if self.qname != "" and len(self.questions) != 0 and len(self.questions) == len(self.options):
            return True
        return False
    # returns -1 if file already exists,-2 for unable to create and 1 to success
    def store(self):
        if self.is_valid():
            if not os.path.exists("obj/"):
                os.mkdir("obj")
            if os.path.exists("obj/"+self.qname+".pkl"):
                log("Quiz with same file exists","err")
                return -1
            with open("obj/"+self.qname+".pkl", 'wb') as output:
                pickle.dump(self, output, pickle.HIGHEST_PROTOCOL)
                return 1
        else:
            log("invalid/null object cannot store","err")
            return -2

#fetches quiz object
def fetch(qname):
    if os.path.exists("obj/"+qname+".pkl"):
        with open("obj/"+qname+'.pkl', 'rb') as input:
            quiz = pickle.load(input)
            return quiz
    return None
    
#creates necessary directories
def initialize():
    logger("Application Initialization Started")
    if not os.path.exists("qxml/"):
        os.mkdir("qxml")
        logger("qxml directory created")        

#Command line function to create a quiz object
def createQuiz():
    try:
        quizName = input("Enter the quiz name:")
        numberOfQuestions = input("Enter number of questions:")
        questions_list = []
        options_list = []

        for i in range(0,int(numberOfQuestions)):
            question = input("Enter " + str((i+1)) + " question:")
            questions_list.append(question)
            option1= input("Enter 1st option")
            option2= input("Enter 2nd option")
            option3= input("Enter 3rd option")
            option4= input("Enter 4th option")
            options = [option1,option2,option3,option4]
            options_list.append(options)

        q = quiz(quizName, questions_list, options_list)

        if q.is_valid()and q.store() == 1 :
            return q
        else :
            return None
    except:
        log("Some problem in creating the Quiz",mode="err")
        return None


if __name__ == "__main__":
    q = createQuiz()
    if q is not None:
        print(q);
        
    
