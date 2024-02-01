from Network import Network

print("This is game...")

name = input("Write your name: ")
print()

balance = 0

network = Network()
while True:
    print("What is your selection(Cooperation or Defect)?")
    while True:
        SelectionPleyer1 = input("Wrire C or D:").lower()
        if  SelectionPleyer1 == "d" or SelectionPleyer1 == "c":
            break
        print("C or D was not entered. Try again")
    
    SelectionPleyer2 = network.SendDate(SelectionPleyer1)

    print("The second player chose", SelectionPleyer2.upper())
    if SelectionPleyer1 == "c" and SelectionPleyer2 == "c":
        balance += 3
    elif SelectionPleyer1 == "d" and SelectionPleyer2 == "c":
        balance += 5
    elif SelectionPleyer1 == "c" and SelectionPleyer2 == "d":
        balance += 0
    elif SelectionPleyer1 == "d" and SelectionPleyer2 == "d":
        balance += 1
    print("Your balance:", balance , end = "\n\n")
    
