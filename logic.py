import csv
from PyQt6.QtWidgets import *
from gui import *

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.button_save.clicked.connect(lambda : self.submit())

    def submit(self): 
        #TODO: adapt this to get ID and check it against other IDs in the csv
        id = self.input_id.text().strip() if len(self.input_name.text().strip()) > 8 else "Invalid"

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
            if status == self.radio_student:
                status = self.radio_student.text()
            elif status == self.radio_staff:
                status = self.radio_staff.text()
            elif status == self.radio_both:
                status = self.radio_both.text()
        else:
            status = "NA"

        with open('data.csv', 'a', newline='') as csvfile: 
            #FIXME: change this to record vote
            writer = csv.writer(csvfile)
            writer.writerow([name, age, status])
            
        #FIXME: change this to reset things properly
        self.input_name.clear() 
        self.input_age.clear()
        self.input_name.setFocus()
        self.label_feedback.setText("")

        if self.button_group.checkedButton() is not None:
            #TODO: check if this needs fixing/adjusting
            self.button_group.setExclusive(False) 
            self.button_group.checkedButton().setChecked(False)
            self.button_group.setExclusive(True)