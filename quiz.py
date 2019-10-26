import xml.etree.ElementTree as ET
import os
from datetime import datetime

#provides log functionality for debugging
def logger(logtext):
    if not os.path.exists("logs/"):
        os.mkdir("logs")
    log = open("logs/app.log","a")
    log.write(str(datetime.now())+"------------"+logtext+"\n")
    log.close()

#provides error logs
def error(errortext):
    if not os.path.exists("logs/"):
        os.mkdir("logs")
    log = open("logs/error.log","a")
    log.write(str(datetime.now())+"---"+errortext+"\n")
    log.close()
    
#creates necessary directories
def initialize():
    logger("Application Initialization Started")
    if not os.path.exists("qxml/"):
        os.mkdir("qxml")
        logger("qxml directory created")        

#creates xml file with the parameters quizname,numberofquestions,listofquestions,options and answers
def createquizxml(qname,qno,question,options,answers):
    if qno>0 and qno == len(question) and qno == len(options) and qno == len(answers):
        ##Making the quiz name as the base tag for the xml and the name of the xml file.
        root = ET.Element(qname)
        for i in range(1,qno+1):
            questions = ET.SubElement(root, 'questions')
            questions.set('id',str(i))
            q = ET.SubElement(questions,'q')
            q.text = question[i-1]
            for j in range(1,len(options[i-1])+1):
                opt=ET.SubElement(questions,'opt')
                opt.set('id',str(j))
                if j == answers[i-1]:
                    opt.set('correct',str(1))
                else:
                    opt.set('correct',str(0))
                opt.text=options[i-1][j-1]
        mydata = ET.tostring(root).decode("utf-8")
        mydata = mydata.replace(">",">\n")
        mydata = mydata.replace("<","\n<")
        myfile = open("qxml/"+qname+".xml", "w+")
        myfile.write("<?xml version=\"1.0\"?>\n"+mydata)
        logger("<admin> created quiz named "+qname+" with "+str(qno)+" questions")
        myfile.close()
        return 1
    return 0

#This function validates the useroptions with correct answers
def validate(useranswers,qname):
    correct=[]
    score = -1 
    if os.path.exists("qxml/"+qname+".xml"):
        tree = ET.parse("qxml/"+qname+".xml")
        root = tree.getroot()
        for child in root:
            for subchild in child:
                if subchild.tag == "opt" and subchild.attrib['correct'] == str(1):
                    correct.append(int(subchild.attrib['id']))
        if len(correct) == len(useranswers):
            score = 0
            for i in range(len(correct)):
                if correct[i] == useranswers[i]:
                    score = score +1
    else:
        error("Quiz does not Exist")
    return score
              
