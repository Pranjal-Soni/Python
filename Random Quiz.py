#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 13:37:25 2019

@author: pranjal
"""

import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 
'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier',
 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

    
# Create the Quiz File and Suffle the Question Order
    
for quizNum in range(35):
    # Create the quiz and answer key files.
    quizFile = open('capitalsquiz%s' % (quizNum+1),'w')
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')
    
    # Write out the header for the quiz
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((" "*20)+'State Capital Quiz (Form %s)'%(quizNum+1) )
    quizFile.write('\n\n')
    
    #Suffle the order of the states
    states = list(capitals.keys())
    random.shuffle(states)
    
    #Create the Answer Options
    for questionNum in range(50):
        
        correctAns = capitals[states[questionNum]]
        wrongAnsers = list(capitals.values())
        del wrongAnsers[wrongAnsers.index(correctAns)]
        wrongAnsers = random.sample(wrongAnsers,3)
        answersOptions = wrongAnsers + [correctAns]
        random.shuffle(answersOptions)
        
        # Write Contant to Quiz and Answer Key files
        quizFile.write('%s. What is the capital of %s?\n' % (questionNum+1,states[questionNum]))
        for i in range(4):
            quizFile.write('    %s. %s\n' %('abcd'[i],answersOptions[i]))
        quizFile.write('\n')
        #write answer key to a file 
        answerKeyFile.write('%s. %s\n' % (questionNum+1,'abcd'[answersOptions.index(correctAns)]))
    

quizFile.close()
answerKeyFile.close()
