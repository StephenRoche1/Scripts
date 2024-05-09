from _datetime import datetime


def Visit():
    return 1


def SiteVisit():
    return 1


def EditFile(fileName):
    now = datetime.now()
    with open(fileName + '.txt', 'a') as file:
        file.write("UPDATE ON: " + str(
            datetime.now()) + "\n\n\n\n\n----------------------------------------------------------\n")
        print("Do you need to update the point of contact")
        upPoc = input()
        if upPoc == '1':
            print("Enter the point of contact")
            inpoc = input()
            POC = "Client Point of Contact: " + inpoc + "\n"
            file.write(POC)
        print("Do you need to update the phone number")
        upPhone = input()
        if upPhone == '1':
            print("Enter the phone number")
            inphone = input()
            phone = "Client Contact Phone Number: " + inphone + "\n\n\n\n\n----------------------------------------------------------\n"
            file.write(phone)
        inputNote = True
        notes = []
        while inputNote == True:

            choice = input("Would you like to add a note input 1 for Yes or 0 for No")
            if choice == '1':
                note = input("Please input your note")
                notes.append(str(now.strftime("%m/%d/%Y, %H:%M")) + "|x|" + note + "\n")
                continue
            elif choice == '0':
                inputNote = False
            else:
                print('Invalid entry please input 1 to input a note or 0 to continue')
            print(notes)
            if len(notes) > 0:
                for i in range(len(notes)):
                    file.write(notes[i])
                inputNote = False
            file.close()

    return 1


class Template:
    def handover(self, inname, indb, indate, intime, incompany, inpoc, inphone, inproduct, notes):
        filename = incompany + "_" + indate + ".txt"
        with open(filename, 'w+') as file:
            name = "Implementor name: " + inname + "\n\n\n--------------------------------------------------------\n"
            file.write(name)
            Database = "Database Name: " + indb + "\n\n"
            file.write(Database)
            date = "Completion Date: " + indate + "\n\n"
            file.write(date)
            time = "Completion Time: " + intime + "\n\n\n----------------------------------------------------------\n"
            file.write(time)
            company = "Client Company Name: " + incompany + "\n\n"
            file.write(company)
            POC = "Client Point of Contact: " + inpoc + "\n\n"
            file.write(POC)
            phone = "Client Contact Phone Number: " + inphone + "\n\n\n----------------------------------------------------------\n"
            file.write(phone)
            product = "Client Device Purchased for installation: " + inproduct + "\n\n\n----------------------------------------------------------\n"
            file.write(product)
            if len(notes) > 0:
                for i in range(len(notes)):
                    file.write(notes[i])
            file.close()


print("Welcome to the template writer")
method = None
now = datetime.now()
while method != 'q':
    print("Please select an option or q to exit")
    structure = Template()
    print("1) Handover Document\n2) Site visit documentation\n3) Site visit specifics\n4) Update a file")
    method = input()
    if method == '1':
        name = input("Please input your full name\n")
        database = input("Please input the name of the initial database\n")
        date = input("Please input the date of completion in format ddmmyyyy \n")
        time = input("Please input the time of completion\n")
        company = input("Please input the client company name\n")
        poc = input("Who is the point of contact in the business?\n")
        product = input("What is the product the client has purchased from DEM?\n")
        phonenum = input("Point of contact Phone number input 0 if no number given\n")
        inputNote = True
        notes = []
        while inputNote:
            choice = input("Would you like to add a note input 1 for Yes or 0 for No")
            if choice == '1':
                note = input("Please input your note")
                notes.append(str(now.strftime("%m/%d/%Y, %H:%M")) + "|x|" + note + "\n")
            elif choice == '0':
                inputNote = False
            else:
                print('Invalid entry please input 1 to input a note or 0 to continue')

        structure.handover(str(name), str(database), str(date), str(time), str(company), str(poc), phonenum,
                           str(product), notes)
        continue
    elif method == '2':
        print("Site Visit")
        continue
    elif method == '3':
        print("Site Visit Specifics")
        continue
    elif method == '4':
        filename = input("Input the filename")
        EditFile(filename)
        continue
    elif method == 'q':
        print("Goodbye!!!")
        break
    else:
        print("Invalid input please try again")
        continue
