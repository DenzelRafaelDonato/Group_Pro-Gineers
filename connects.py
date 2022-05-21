import pyodbc

try:
    connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Denzel\OneDrive\Documents\Database1.accdb;')
    print("Database1 is connected")



except pyodbc.Error as e:
    print("Connection Error")