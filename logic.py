import csv
from PyQt6.QtWidgets import *
from gui import *

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.csv_file = 'data.csv'
        self.start_csv()
        
        self.label_feedback.setText("INPUT VALID ID (6+ characters) AND SELECT A CANDIDATE")

        self.button_save.clicked.connect(lambda : self.submit())

    def start_csv(self):
        """ creates the csv file with proper headers"""
        with open(self.csv_file, 'w', newline='') as csvfile:
            headers = ['id', 'voteJane', 'voteJohn', 'totalVotes']
            file_exists = os.path.exists(self.csv_file)
            
            write_header = False
            if not file_exists:
                write_header = True
            else:
                with open(self.csv_file, 'r') as f:
                    first_line = f.readline().strip()
                    if first_line != ','.join(headers):
                        write_header = True
                        
            if write_header:
                with open(self.csv_file, 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(headers)
                    
    def total_votes(self):
        """ calculates total votes for each and entire total"""
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
        id = self.input_id.text().strip() if len(self.input_id.text().strip()) >= 6 else "Invalid"

        if id != "Invalid":
            id = int(id)
            with open('data.csv', 'r') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if row[0] == id:
                        self.label_feedback.setText("ID already exists")
                        return

        status = self.button_group.checkedButton() #FIXME: adapt this to Jane & John buttons
        if status is not None:
            if status == self.radio_jane:
                status = self.radio_jane.text()
                self.jane += 1
            elif status == self.radio_john:
                status = self.radio_john.text()
                self.john += 1
        else:
            status = "NA"
            
        if id != "Invalid" and status != "NA":
            with open('data.csv', 'a', newline='') as csvfile: 
                #FIXME: change this to record vote
                writer = csv.writer(csvfile)
                writer.writerow([id, status, (self.jane + self.john)])
            
        #FIXME: change this to reset things properly
            self.input_id.clear()
            self.input_id.setFocus()
            self.label_feedback.setText("")

        if self.button_group.checkedButton() is not None:
            #TODO: check if this needs fixing/adjusting
            self.button_group.setExclusive(False) 
            self.button_group.checkedButton().setChecked(False)
            self.button_group.setExclusive(True)