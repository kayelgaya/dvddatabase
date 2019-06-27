import sqlite3,time
conn = sqlite3.connect('DVDS_AT_HOME.db')

c = conn.cursor()
# c.execute("""DROP TABLE DVDS_AT_HOME""")
try:
    dvds = c.execute("""CREATE TABLE DVDS_AT_HOME(
        Titles text
    ) """)
except sqlite3.OperationalError:
    print ("You've already got a table, so I'll just ask the choices.")

def DVD(dvd_name):
    with conn:
        c.execute("INSERT INTO DVDS_AT_HOME VALUES (:Titles)", {'Titles' : dvd_name})
        return c.fetchall()

#Prompts user on what they want to do
while True: # while loop ensures that the program will keep running
    try:
        askuser = int(input("What would you like to do? \n 1. Add a new dvd \n 2. Find a Dvd \n 3. Delete a dvd \n 4. See all DVDs \n \n" ))
    except ValueError: #program only accepts integer values
        print ("I can't process that, let's try again \n")
        time.sleep(0.5)
        continue
    else:
        if askuser not in [1,2,3,4]: #program only limits to range 1-4
            print ("I can't process that, let's try again \n")
            continue

    if askuser == 1: #Prompts the user to add something
        add_disk = input("Add here! \n")
        c.execute("INSERT INTO DVDS_AT_HOME VALUES (:Titles)", {'Titles' : add_disk})
        conn.commit()
    elif askuser == 2: #Prompts user to find a title
        search_disk = input("Find your disk: \n ")
        found_disk = c.execute("SELECT Titles FROM DVDS_AT_HOME WHERE Titles = (:Titles)", {'Titles' : search_disk})
        print (c.fetchall())
    elif askuser == 3: #Prompts user to remove a title
        remove_disk = input("What do you want to remove? \n")
        c.execute("DELETE FROM DVDS_AT_HOME WHERE Titles = (:Titles)", {'Titles' : remove_disk})
        conn.commit()
    elif askuser == 4: #Shows all titles in database
        for row in c.execute("SELECT * FROM DVDS_AT_HOME ORDER BY Titles"):
            print (row)

    another = input("Anything else?")
    if another == 'Y' or another == 'y':
        continue
    else:
        print ("Thanks for using me!")
        break

# DVD() #To enter into database w/o prompts

conn.close()
