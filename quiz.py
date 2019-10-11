import xml.etree.ElementTree as ET

#creates xml file with the parameters quizname,numberofquestions,listofquestions,and options
def createquizxml(qname,qno,question,options):
    if qno>0 and qno == len(question) and qno == len(options):
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
                opt.text=options[i-1][j-1]
        myfile = open(qname+".xml", "w+")
        mydata = ET.tostring(root).decode("utf-8")
        myfile.write("<?xml version=\"1.0\"?>"+mydata)
        myfile.close()

