'''def main(): #TODO: Adapt all of this to pyqt6
    john = 0
    jane = 0
    while True:
        choice = vote_menu()
        if choice == "x":
            print("-" * 30)
            print(f"John - {john}, Jane - {jane}, Total - {john + jane}")
            print("-" * 30)
            break
        elif choice == "v":
            person = candidate_menu()
            if person == 1:
                john += 1
            elif person == 2:
                jane += 1
        
def vote_menu():
    string = None
    print("-" * 20)
    print("VOTE MENU")
    print("-" * 20)
    print("v: Vote")
    print("x: Exit")
      
    option = input("Option: ").lower().strip()
    while option != "v" and option != "x":
        option = input("Invalid (v/x): ").strip().lower()
        
    if option == "x":
        string = option
        return string
    elif option == "v":
        string = option
        return string

def candidate_menu():
    print("-" * 20)
    print("CANDIDATE MENU")
    print("-" * 20)
    print("1: John")
    print("2: Jane")
      
    vote = input("Candidate: ").strip()
    while vote != "1" and vote != "2":
        vote = input("Invalid (1/2): ").strip()
        
    if vote == "1":
        print("Voted John")
        return int(vote)
    elif vote == "2":
        print("Voted Jane")
        return int(vote)'''
from logic import *

def main():
    application = QApplication([])
    window = Logic()
    window.show()
    application.exec()

if __name__ == "__main__":
    main()