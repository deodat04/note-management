import sqlite3 
  
try: 
    sqliteConnection = sqlite3.connect('etudiants.db')  
    print("Connected to SQLite") 
except sqlite3.Error as error: 
    print("Failed to connect with sqlite3 database", error) 
finally: 
    if sqliteConnection: 
        sqliteConnection.close() 
        print("the sqlite connection is closed")