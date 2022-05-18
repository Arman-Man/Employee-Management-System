import csv
import pickle

def main():
    employeeDict = dict()
    userInput = ''
    filename = 'employee.dat'

    print('Welcome to Employee Management System (EMS)')

    employeeDict = load(filename)

    while userInput != '10':
        #menu
        print('Main Menu:')
        print('1.\tAdd Employee')
        print('2.\tFind Employee by EID')
        print('3.\tFind Employee by Name')
        print('4.\tDelete Employee')
        print('5.\tDisplay Statistics')
        print('6.\tDisplay All Employees')
        print('7.\tBackup Database')
        print('8.\tRestore Database')
        print('9.\tPurge Database')
        print('10.\tExit')

        #checks if userInput can be converted to an int, then checks if userInput is in range
        found = False
        while found == False:
            userInput = input('Enter your selection (1..10):\n')
            try:
                intVar = int(userInput)
                if intVar >= 1 and intVar <= 10:
                    found = True
                else:
                    print('Invalid selection.')
            except:
                print('Invalid selection.')

        if userInput == '1':
            #add entry to dictionary using addEmployee()
            addEmployee(employeeDict)

        elif userInput == '2':
            userInput = input('Enter an Employee ID or QUIT to stop:\n')
            if userInput.upper() != 'QUIT':
                findEmployeeEID(employeeDict,userInput)

        elif userInput == '3':
            userInput = input('Enter an employee name or QUIT to stop:\n')
            if userInput.upper() != 'QUIT':
                findEmployeeName(employeeDict,userInput)

        elif userInput == '4':
            userInput = input('Enter an Employee ID or QUIT to stop:\n')
            if userInput.upper() != 'QUIT':
                deleteEmployee(employeeDict,userInput)

        elif userInput == '5':
            displayStatistics(employeeDict)

        elif userInput == '6':
            displayEmployees(employeeDict)

        elif userInput == '7':
            backupDatabase(employeeDict)

        elif userInput == '8':
            restoreDatabase(employeeDict)

        elif userInput == '9':
            purgeDatabase(employeeDict)

        elif userInput == '10':
            print('Thank you for using Employee Management System (EMS)')

        else:
            print('Invalid selection.')

    save(employeeDict, filename)


#'1'
def addEmployee(database):
    employeeEID = input('Enter an Employee ID or QUIT to stop:\n')
    for key in database: #input validaiton for non-duplicate EID, this works because the key for our dict is the EID
        while employeeEID == key:
            print('Invalid. EID already exists.')
            employeeEID = input('Enter an Employee ID or QUIT to stop:\n')

    if str(employeeEID).upper() != 'QUIT':
        employeeName = input('Enter employee name:\n')
        employeeDept = input('Enter employee department:\n')
        employeeTitle = input('Enter employee title:\n')
        employeeSalary = input('Enter employee salary:\n')
        tempList = [employeeEID, employeeName, employeeDept, employeeTitle, employeeSalary]

        #dictionary with EID as the key and a dictionary as values {a:{c:d, e:f}, a:{c:d, e:f}}
        database[tempList[0]] = {'employeeName':tempList[1], 'employeeDept':tempList[2], 'employeeTitle':tempList[3], 'employeeSalary':tempList[4]}


#'2'
def findEmployeeEID(database,EID):
    boolVar = False
    for key in database:
        if EID == key:
            boolVar = True

    if boolVar == True:
        for key in database:
            if EID == key:
                print('Employee ID:', EID)
                print('\tName:', database[EID]['employeeName'])
                print('\tDepartment:', database[EID]['employeeDept'])
                print('\tTitle:', database[EID]['employeeTitle'])
                print('\tSalary:', format(database[EID]['employeeSalary'], ',.2f'))
        return
    else:
        print('Employee ID: {} was not found in the database.'.format(EID))
            
#'3'
def findEmployeeName(database,name):
    total = 0

    for key in database:
        if database[key]['employeeName'] == name:
            total += 1

    if total != 0:
        if total == 1:
            print('Found 1 employee with that name.')
            for key in database:
                if database[key]['employeeName'] == name:
                    print('Employee ID:', key)
                    print('\tName:', database[key]['employeeName'])
                    print('\tDepartment:', database[key]['employeeDept'])
                    print('\tTitle:', database[key]['employeeTitle'])
                    print('\tSalary:', format(database[key]['employeeSalary'], ',.2f'))
            return
        else:
            print('Found {} employees with that name.'.format(total))
            for key in database:
                if database[key]['employeeName'] == name:
                    print('Employee ID:', key)
                    print('\tName:', database[key]['employeeName'])
                    print('\tDepartment:', database[key]['employeeDept'])
                    print('\tTitle:', database[key]['employeeTitle'])
                    print('\tSalary:', format(database[key]['employeeSalary'], ',.2f'))
            return
    else:
        print('Employee name: {} was not found in the database.'.format(name))

#'4'
def deleteEmployee(database,EID):

    boolVar = False
    for key in database:
        if EID == key:
            boolVar = True

    if boolVar == True:
        for key in database:
            if EID == key:
                userInput = input('Enter y/n to confirm deletion of {}\n'.format(EID))
                if userInput.upper() == 'Y':
                    database.pop(EID)
        return
    else:
        print('Employee ID: {} was not found in the database.'.format(EID))


#'5'
#this still isn't correct
def displayStatistics(database):
    totalEmployees = 0
    numDepartments = 0
    deptDict = dict()

    for key in database: #each key in database is an EID
        if deptDict != dict(): #makes sure deptDict isnt empty
            boolVar = False
            for dept in deptDict: 
                if database[key]['employeeDept'] == dept: #so the key for deptDict is the dept, but for database its EID
                    deptDict[dept] = deptDict[dept] + 1 #increasing employee number by 1
                    totalEmployees += 1
                    boolVar = True

            if boolVar == False:
                deptDict[database[key]['employeeDept']] = 1 #creates a new key-value pair
                numDepartments += 1
                totalEmployees += 1

        else: #if it is empty, add this first entry
            deptDict[database[key]['employeeDept']] = 1 #creates a new key-value pair
            numDepartments += 1
            totalEmployees += 1

    print('Department Statistics:')

    for key in deptDict:
        if deptDict[key] > 1:
            print('\tDepartment: {} - {} employees'.format(key, deptDict[key]))
        elif deptDict[key] == 1:
            print('\tDepartment: {} - 1 employee'.format(key))

    if numDepartments > 1:
        print('There are {} departments in the database.'.format(numDepartments))
    elif numDepartments == 1:
        print('There is 1 department in the database.')
    else:
        print('There are 0 departments in the database.')

    if totalEmployees > 1:
        print('There are {} employees in the database.'.format(totalEmployees))
    elif totalEmployees == 1:
        print('There is 1 employee in the database.')
    else:
        print('There are 0 employees in the database.')



#'6'
def displayEmployees(database):
    tempDatabase = dict()
    for key in database:
        tempDatabase[int(key)] = {'employeeName':database[key]['employeeName'],
                'employeeDept':database[key]['employeeDept'], 'employeeTitle':database[key]['employeeTitle'], 'employeeSalary':database[key]['employeeSalary']}

    emptyDict = dict()
    if tempDatabase != emptyDict:
        sortedByKeyDict = dict(sorted(tempDatabase.items(), key = lambda t: t[0])) #sorted by EID smallest to largest, EID must be an int/float to work
        count = 0
        for EID in sortedByKeyDict:
            print('Employee ID:', EID)
            print('\tName:', sortedByKeyDict[EID]['employeeName'])
            print('\tDepartment:', sortedByKeyDict[EID]['employeeDept'])
            print('\tTitle:', sortedByKeyDict[EID]['employeeTitle'])
            print('\tSalary:', format(float(sortedByKeyDict[EID]['employeeSalary']), ',.2f'))
            count += 1


        if count == 1:
           print('There is 1 employee in the database.')
        else:
            print('There are {} employees in the database.'.format(count))
    else:
        print('Employee database is empty.')


#'7'
def backupDatabase(database):  
    fields = ['EID', 'null', 'null', 'null', 'null'] 
    
    tempList = list()
    for key in database:
        tempList.append([key, database[key]['employeeName'], database[key]['employeeDept'], database[key]['employeeTitle'], database[key]['employeeSalary']])    

    filename = input('Enter a backup filename (should end with .csv) or QUIT to stop:\n')

    if filename.upper() == "QUIT":
        return
    
    # writing to csv file 
    with open(filename, 'w') as csvfile: 
        # creating a csv writer object 
        csvwriter = csv.writer(csvfile, lineterminator = '\n') 
        
        # writing the fields 
        csvwriter.writerow(fields) 
        
        # writing the data rows 
        csvwriter.writerows(tempList)

    print('Successfully backed up the database to CSV file backup.csv.')


#'8'
def restoreDatabase(database):
    found = False
    while found == False:
        filename = input('Enter a restore filename (should end with .csv) or QUIT to stop:\n')
        if filename.upper() == "QUIT":
            return
        try:
            input_file = open(filename)
            found = True
        except FileNotFoundError:
            print("File {} does not exist".format(filename))

    #clear before adding the new keys
    database.clear()

    reader = csv.reader(input_file)
    for row in reader:
        try:
            testVar = int(row[0])
            database[row[0]] = {'employeeName':row[1], 'employeeDept':row[2], 'employeeTitle':row[3], 'employeeSalary':row[4]}
            # row[0] is the EID, everything is the same order as the main dictionary
        except:
            pass

    print('Successfully restored the database from CSV file {}.'.format(filename))
    input_file.close()


#'9'
def purgeDatabase(database):
    if database != dict():
        userInput = input('All employees will be deleted from the database. Are you sure (y/n)?\n')
        if userInput.upper() == 'Y':
            database.clear()
            print('Employee database was purged.')
    else:
        print('Employee database is already empty.')


def load(filename):
    found = False
    try:
        input_file = open(filename,'rb')
        found = True
    except FileNotFoundError:
        print('Unable to load the database from binary file {}.'.format(filename))
        print('Creating an empty database.')

    if not found:
        return dict()
    else:
        dictVar = pickle.load(input_file)
        input_file.close()
        return dictVar


def save(database, filename):
    output_file = open(filename, 'wb')
    pickle.dump(database, output_file)
    output_file.close()


main()