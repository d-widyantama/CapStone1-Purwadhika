# |---------------------------------------------------------------------------------------------------------------|
# |                              * * * * * Mini HR Management System * * * * * *                                  |
# |                 Developed by Dwika Widyantama [V.0.1b - Without pandas and tabulate - 12 August 2023]         |
# |                     For Module 1 CAPSTONE PROJECT of Purwadhika JCDS 2104 JKT Class                           |
# |---------------------------------------------------------------------------------------------------------------|

# Program Outline:
# ------------------------------------------------------------------------------------------------
# Initiate Initial Data of Employees

# Features
# 1 Show Employees data: 
    # Employee ID, First Name, Last Name, Division, Address, ASL, Join Date
# 1a Data Filtering:
    # - Filter ny Division
    # - Filter by age 
# 2. Search for employee data by name and show individual employee details
# 3. Delete Employee Data
# 4. Add Employee Details

# V.0.1
# Menu 1-3 features user input validation where it prevents the user from inputting unsupported 
# input and potentially interrupts the program mid-run

# Additional Modules & Libraries:
# -
# ---------------------------------------------------------------------------------------------------------------





# Initial Data
# ------------------------------------------------------------------------------------------------
from faker import Faker
fake = Faker('id_ID')           #Indonesian Localization with faker

from tabulate import tabulate   #Pretty Table module
# import pandas as pd             #Pandas module, used to ease table reading with dataframe


#Suppose the initial Data are already structured this way
employeesMasterData = {
   'employee1' : {
    'nama'          : 'Oni Mandala',
    'alamat'        : 'Gg. Rumah Sakit No. 1, Kota Administrasi Jakarta Pusat, NB 64796',
    'tanggalLahir'  : '1990-07-10',
    'gender'        : 'Laki-laki',
    'divisi'        : 'Finance'
   },
    'employee2' : {
    'nama'          : 'Icha Fujiati',
    'alamat'        : 'Jalan Cikutra Timur No. 100 Pasuruan, SU 52976',
    'tanggalLahir'  : '1998-01-10',
    'gender'        : 'Perempuan',
    'divisi'        : 'Marketing'
    },

    'employee3' : {
    'nama'          : 'Yusuf Pratama',
    'alamat'        : 'Gg. Kapten Muslihat No. 842 Pekalongan, AC 28047',
    'tanggalLahir'  : '2002-03-11',
    'gender'        : 'Laki-laki',
    'divisi'        : 'Marketing'
    },
    'employee4' : {
    'nama'          : 'Lulut Mulyani',
    'alamat'        : 'Jalan Antapani Lama No. 5 Singkawang, SG 19224',
    'tanggalLahir'  : '2003-10-18',
    'gender'        : 'Perempuan',
    'divisi'        : 'Operation'
    },
    'employee5' : {
    'nama'          : 'Tantri Aryani',
    'alamat'        : 'Gang Cikutra Timur No. 81 Palangkaraya, JK 18244',
    'tanggalLahir'  : '1990-08-12',
    'gender'        : 'Perempuan',
    'divisi'        : 'Marketing'}
}


# ---------------------------------------------------------------------------------------------------------------
# Main-Menu Function
# ---------------------------------------------------------------------------------------------------------------
def mainMenu():
    print("\n")
    print("****** ------------------------------------- *****")
    print("****** Welcome to Employee Management System *****")
    print("****** ------------------------------------- *****")
    print()
    print("[1] Show Employee Data" )
    print("[2] Search for Employee Data" )
    print("[3] Delete Employee Data" )
    print("[4] Add Employee Data" )
    print("[5] Exit Program \n" )


# Main Menu User Input Format Confirmation Loop
# ------------------------------------------------------------------------------------------------
def menuConfirmation():
    global userInput
    while True:
        try:
            userInput = int(input("Please select available menu by entering the menu numbers: "))
            if int(userInput) >= 1 and int(userInput) <=5: #Making sure the input is 1-5
                break      
        except :
            print("Silahkan masukkan format yang benar!") 




# ---------------------------------------------------------------------------------------------------------------
# Sub-Menu [1] Function - Show Employee Data
# ---------------------------------------------------------------------------------------------------------------
# Sub-Menu [1] Loop Function:
# ------------------------------------------------------------------------------------------------
def showEmployee():
    '''
    Show sub menu [1]
    '''
    while True:
        print("[1] Show All" )
        print("[2] Filter By DIVISI" )
        print("[3] Filter by GENDER" )
        print("[4] Exit to Main Menu \n" )
        try:
            userInput = int(input("Please select available menu by entering the menu numbers: "))
            if  int(userInput) == 1 :
                #Show Full list of Employee Data Table
                print("DAFTAR KARYAWAN")
                showEmployeeTable(employeesMasterData)

            elif int(userInput) == 2:
                #Show Full list of Employee filtered by Division
                print(' \n >>> Filter Daftar Karyawan BY DIVISION')
                divKey = input("Silahkan masukkan divisi yang ingin ditampilkan: ").capitalize()
                filterEmployeeByDiv(divKey)
                showEmployeeTable(filteredDivEmployeeDict)

            elif int(userInput) == 3:
                #Show Full list of Employee filtered by Gender
                print(' \n >>> Filter Daftar Karyawan BY GENDER')
                filterEmployeeByGender()
                
                
            elif int(userInput) == 4:
                #Break the current while loop and return to main menu loop
                break      
        except :
            print("Silahkan masukkan format yang benar!") 




# Filtering Functions for Sub-Menu [1]
# ------------------------------------------------------------------------------------------------

# [1.1] Show All Function: [ok]

def showEmployeeTable(employeeDict):
    """General function print table, parameter: Dict{key:{key:value}} """
    # f strings formatting {item:<15} are used to specify width of 15 and aligned to the left
    print("---"*50)
    showEmployeeHeaders = ["Nama",  "Tanggal Lahir", "Gender", "Divisi", "Alamat"]
    print(f'|  {"Employee id":<15}|  {showEmployeeHeaders[0]:<20} |  {showEmployeeHeaders[1]:<15}|  {showEmployeeHeaders[2]:<14}|  {showEmployeeHeaders[3]:<10}|  {showEmployeeHeaders[4]:<10}')
    print("---"*50)
    for i in employeeDict:
        print(f"|  {i:<15}|  {employeeDict[i]['nama']:<20} |  {employeeDict[i]['tanggalLahir']:<15}| {employeeDict[i]['gender']:<15}|  {employeeDict[i]['divisi']:10}| {employeeDict[i]['alamat']:10}")

# Print Transposed Employee Table
def showEmployeeTableTransposed(employeeDict):
    """General function print table but TRANSPOSED, parameter: Dict{key:{key:value}} """
    # f strings formatting {item:<15} are used to specify width of 15 and aligned to the left
    print("Employee Detail: ")
    print("---"*50)
    for i in employeeDict:
        print(f"|{'Employee id ':<15}:{i:<15} \n|{'Nama':<15}:{employeeDict[i]['nama']:<20} \n|{'Tanggal Lahir':<15}:{employeeDict[i]['tanggalLahir']:<15} \n|{'Gender':<15}:{employeeDict[i]['gender']:<15} \n|{'Divisi':<15}:{employeeDict[i]['divisi']:10} \n|{'Alamat':<15}:{employeeDict[i]['alamat']:10}")
    print("---"*50)

# [1.2] Filter by Employee Division [ok]

#Filter function for Divisi
def filterEmployeeByDiv(divisi):
    employeesMasterDataFilteredListValues = []
    employeesMasterDataFilteredListKey =[]
    global filteredDivEmployeeDict
    for i in employeesMasterData:
        if employeesMasterData[i]['divisi'] == divisi:
            employeesMasterDataFilteredListValues += [employeesMasterData[i]]
            employeesMasterDataFilteredListKey += [i]
    # zip the two lists together to create a list of key-value pairs
    key_value_pairs = zip(employeesMasterDataFilteredListKey, employeesMasterDataFilteredListValues)
    filteredDivEmployeeDict = dict(key_value_pairs)
    return filteredDivEmployeeDict

#More general filter approach
def filterEmployeeBy(innerkey,innervalues):
    employeesMasterDataFilteredListValues = []
    employeesMasterDataFilteredListKey =[]
    global filteredDivEmployeeDict
    for i in employeesMasterData:
        if employeesMasterData[i][innerkey] == innervalues:
            employeesMasterDataFilteredListValues += [employeesMasterData[i]]
            employeesMasterDataFilteredListKey += [i]
    # zip the two lists together to create a list of key-value pairs, then convert to dict with the same format as original
    key_value_pairs = zip(employeesMasterDataFilteredListKey, employeesMasterDataFilteredListValues)
    filteredDivEmployeeDict = dict(key_value_pairs)
    

# [1.3] Filter by Employee Gender [ok]
def filterEmployeeByGender():
    while True:
        genderKey = input("Silahkan masukkan gender yang ingin ditampilkan (P/L): ")
        if genderKey.upper() == 'P' :
            print(f"{genderKey} exist")
            filterEmployeeBy('gender','Perempuan')
            showEmployeeTable(filteredDivEmployeeDict)
            break
        elif genderKey.upper() == 'L' :
            print(f"{genderKey} exist")
            filterEmployeeBy('gender','Laki-laki')
            showEmployeeTable(filteredDivEmployeeDict)
            break
        else:
            print("Silahkan masukkan format yang benar!")
                           

# ---------------------------------------------------------------------------------------------------------------
# Sub-Menu [2] Function - Search for Employee Data [OK]
# ---------------------------------------------------------------------------------------------------------------
# Show Employee (Single Employee Details)
# ------------------------------------------------------------------------------------------------
# -- Declared in Main Loop    
       

# ---------------------------------------------------------------------------------------------------------------
# Sub-Menu [3] Function - Delete Employee Data [ok]
# --------------------------------------------------------------------------------------------------------------- 
# -- Declared in Main Loop


# ---------------------------------------------------------------------------------------------------------------
# Sub-Menu [4] Function - Add Employee Data [OK]
# ---------------------------------------------------------------------------------------------------------------
    
# ------------------------------------------------------------------------------------------------
def addEmployee():

    #initiate blank list
    additionEmployeeDict = {}

    #Input Employee Data
    kodeKaryawan = input("Masukkan kode baru karyawan: ")
    namaKaryawan = input("Masukkan nama baru karyawan: ")
    alamatKaryawan = input("Masukkan alamat baru karyawan: ")
    tanggalLahirKaryawan = input("Masukkan tanggal lahir baru karyawan: ")
    #Input Gender with Confirmation
    while True:
        genderKey = input("Silahkan masukkan gender yang ingin dimasukkan (P/L): ")
        if genderKey.upper() == 'P' :
            genderKaryawan = 'Perempuan'
            break
        elif genderKey.upper() == 'L' :
            genderKaryawan = 'Perempuan'
            break
        else:
            print("Silahkan masukkan format yang benar!")

    #Input Divisi with Confirmation
    while True:
        print( "\n")
        print("[F] Finance" )
        print("[M] Marketing" )
        print("[O] Operation" )
        divKey = input("Silahkan masukkan div yang ingin dimasukkan (F/M/O): ")
        if divKey.upper() == 'F' :
            divisiKaryawan = 'Finance'
            break
        elif divKey.upper() == 'M' :
            divisiKaryawan = 'Marketing'
            break
        elif divKey.upper() == 'O' :
            divisiKaryawan = 'Operation'
            break
        else:
            print("Silahkan masukkan format yang benar! (F/M/O)")

    #Update temporary dict
    additionEmployeeDict[kodeKaryawan] = {'nama':namaKaryawan, 'alamat' : alamatKaryawan, 'tanggalLahir':tanggalLahirKaryawan, 'gender' : genderKaryawan,'divisi': divisiKaryawan}
    
    #Print Temporary Dict as Details
    showEmployeeTableTransposed(additionEmployeeDict)

    while True:
            confirm = input("Yakin akan melanjutkan?")
            if confirm.upper() == 'N':
                print("CANCELED")
                break
            elif confirm.upper() == 'Y':
                #Update main Dict
                employeesMasterData[kodeKaryawan] = {'nama':namaKaryawan, 'alamat' : alamatKaryawan, 'tanggalLahir':tanggalLahirKaryawan, 'gender' : genderKaryawan,'divisi': divisiKaryawan}
                break
            else:
                print("Masukkan format yang benar! (Y/N)")
                confirm = input("Yakin akan melanjutkan?")

    
 


# ------------------------------------------------------------------------------------------------
#  -- Main Program Loop -- 
# ------------------------------------------------------------------------------------------------
while True:

    #Initiate mainMenu function --> display main menu options
    mainMenu()

    #initiate menuConfirmation function --> make sure user inputs are properly inputed
    menuConfirmation()    

    if userInput == 1:
        #1. Display sub-menu of Show employees 
        showEmployee()
            # [1] Show All
            # [2] Filter By Division
            # [3] Filter by Gender
            # [4] Exit to Main Menu
    elif userInput == 2:
        # 2. Search Employee & Show Employee Details 
        detailKey = input(" \n >>> Silahkan masukkan nama lengkap karyawan yang ingin ditampilkan : ").title()
        
        filterEmployeeBy('nama',detailKey)

        showEmployeeTableTransposed(filteredDivEmployeeDict)
        

    elif userInput == 3:
        # 3. Delete Data 
        #Show all employee
        showEmployeeTable(employeesMasterData)
        
        delKey = input("Masukkan Kode nama employee yang ingin dihapus: ")
        
        #Print Employee Details
        filterEmployeeBy('nama',employeesMasterData[delKey]['nama'])
        showEmployeeTableTransposed(filteredDivEmployeeDict)

        #Confirm Deletion 
        while True:
            confirm = input("Yakin akan melanjutkan?")
            if confirm.upper() == 'N':
                print("CANCELED")
                break
            elif confirm == 'Y':
                del employeesMasterData[delKey]
                break
            else:
                print("Masukkan format yang benar! (Y/N)")
                confirm = input("Yakin akan melanjutkan?")


    elif userInput == 4:
        # 4. Add Employee Data
        showEmployeeTable(employeesMasterData)

        addEmployee()

        showEmployeeTable(employeesMasterData)


    elif userInput == 5:
        # 5. Quit
        break


