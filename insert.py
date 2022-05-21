import pyodbc

try:
    connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Denzel\OneDrive\Documents\Database1.accdb;')
    record = connection.cursor()

    record.execute("INSERT INTO Table1 (ID,Inventors,Invention,DateOfInvention,Description) VALUES ('11','Ezekiel L. Betchayda, Brendon Gio C. Campaña, Dwight Matthew G. David, Adriane B. Dollisen, Denzel Rafael K. Donato, Dwayne Marel C. Palcon, John Rey N. Pateno, Nicole Shaira A. Tabligan','Lab9','05/22/2022','It helps to insert a certain record to MS Access Database using connecting and inserting functions. The needed data were inserted in ID 11')")
    connection.commit()
    print('Database inserted')

except pyodbc.Error as e:
    print("Connection Error")
