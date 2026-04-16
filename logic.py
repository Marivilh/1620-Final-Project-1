import csv
import os
from PyQt6.QtWidgets import *
from gui import *

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.csv_file = 'data.csv'
        self.start_csv()
        
        self.label_feedback.setText("INPUT VALID ID AND SELECT A CANDIDATE")

        self.button_save.clicked.connect(lambda : self.submit())

    def start_csv(self):
        """ creates the csv file with proper headers"""
        headers = ['id', 'voteJane', 'voteJohn', 'totalVotes']
        if not os.path.exists(self.csv_file) or os.stat(self.csv_file).st_size == 0:
            with open(self.csv_file, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(headers)
                    
    def total_votes(self):
        """calculates total votes in teh csv file"""
        count = 0
        if os.path.exists(self.csv_file):
            with open(self.csv_file, 'r') as csvfile:
                reader = csv.reader(csvfile)
                next(reader, None) #skips the header
                for row in reader:
                    if row:
                        count += 1
        return count
                        
    def submit(self): 
        #TODO: adapt this to get ID and check it against other IDs in the csv
        id = self.input_id.text().strip()
        
        if not id: #check if there is an ID and promts for one if not
            self.label_feedback.setText("Enter an ID")
            self.label_feedback.setStyleSheet("color: red;") 
            return
        
        if not id.isdigit(): #chekc if id is numbers
            self.label_feedback.setText("ID must be numeric")
            self.label_feedback.setStyleSheet("color: red;") 
            return
        
        if len(id) < 6: #check id lenght
            self.label_feedback.setText("ID must be at least 6 characters")
            self.label_feedback.setStyleSheet("color: red;") 
            return
        
        if os.path.exists(self.csv_file): #check if id already is in the data file
             with open(self.csv_file, 'r') as csvfile:
                reader = csv.reader(csvfile)
                next(reader, None) #skips the header
                for row in reader:
                    if row and row[0] == id:
                        self.label_feedback.setText("ID already exists")
                        self.label_feedback.setStyleSheet("color: red;") 
                        return
                    
        selected_vote = self.button_group.checkedButton()
        if selected_vote is None: #check if a candidate is selected
            self.label_feedback.setText("Select a candidate")
            self.label_feedback.setStyleSheet("color: red;") 
            return
        
        vote_Jane = None
        vote_John = None
        
        if selected_vote == self.radio_jane:
            vote_Jane = 'x'
        elif selected_vote == self.radio_john:
            vote_John = 'x'
            
        # get totatl votes
        total_votes = self.total_votes() + 1
        
        # send data to the csv
        with open(self.csv_file, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([id, vote_Jane if vote_Jane else '', vote_John if vote_John else '', total_votes])
            
        self.label_feedback.setText("Vote submitted.")
        self.input_id.clear()
        self.input_id.setFocus()
        
        self.button_group.setExclusive(False)
        selected_vote.setChecked(False)
        self.button_group.setExclusive(True)