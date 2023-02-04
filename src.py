import dbm
import pickle
import os
import time


class DB:

    def __init__(self, DB_SEARCH, DB_NAME, db, cwd, dirList, ID, DATA):
        self.db_search = DB_SEARCH
        self.db_name = DB_NAME
        self.db = db
        self.cwd = cwd
        self.dirList = dirList
        self.ID = ID
        self.DATA = DATA

    def DB_MESSAGES(self):

        time.sleep(3)
        db_welcome = """
                        Plese hold Database is loading. . .
        """
        print(db_welcome)
        time.sleep(3)


    def SYSTEM(self):
        
        self.cwd = os.getcwd()
        self.dirList = os.listdir(self.cwd)
        self.db_search = str(input("[+] Search Database Name y/n: "))
        print('\n')

        if self.db_search == 'y':
            for i in self.dirList:
                time.sleep(1)
                print("- - - - -  - - ")
                print(i)
                print("- - - - -  - - ")

            print('\n')
            print("[+] Total Amount of files found: %s" % len(self.dirList))
            self.NEW_DB()    

        elif self.db_search == 'n':
            while self.db_search == 'n':
                time.sleep(2)
                print("[+] Program Termination Complete!")
                break
             

    def NEW_DB(self):

        new_db_message = """
                            [-] Do you want to create a new database? (y/n)
                            [-] Type the name of existing database to contuinue 
                            Example: store
        
        """
        print(new_db_message)
        new_db = input("[=] y/n:_ ")
        if new_db == 'y':
            time.sleep(2)
            db_message = """
                            Database Creating. . .        
            """
            print(db_message)
            time.sleep(1)
            self.DATA_INFORMATION()
        else:
            print('Waiting!')



    def DATA_INFORMATION(self):
        time.sleep(2)
        self.db_name = input("[=] Enter Database name:_ ")

        #Need fixing----------------
        if self.db_name == int:
            print("[-] Name of database must be string.")
            self.DATA_INFORMATION()

        elif self.db_name == "" or self.db_name == False:
            time.sleep(2)
            print("""           Database Name Error.
                                Enter a valid name to contuinue.
            
            """)
            self.DATA_INFORMATION()

        else:
            self.db = dbm.open(self.db_name, 'c')
            db_message = """
                            New database created successfully. . .        
            """
            print(db_message)
            time.sleep(1)
            print("[-] Database name is: %s" % self.db_name)


            time.sleep(2)
            self.ID = input("[=] Enter a unique key:_ ")
            self.DATA = input("[=] Enter Data:_ ")

            # ---------   Security   ----------------   - --------------- 

            ID_SECURITY = pickle.dumps(self.ID)
            DATA_SECURITY = pickle.dumps(self.DATA)

            # ---------   Security   ----------------   - ---------------  
            self.db[ID_SECURITY] = DATA_SECURITY
            db_message = """
                            Data save successfully.
            """
            print(db_message)
            time.sleep(2)

            menu =("""
                                            Menu
                                ---------------------------
                                [1] Add content to Database
                                [2] Show contents in Database
                                [3] Return to main screen
            """)
            print(menu)
            time.sleep(2)
            db_menu = int(input("[=]_ "))

            if db_menu == 1:
                self.DATA_INFORMATION()
            elif db_menu == 2:
                self.DB_CONTENT()
            elif db_menu == 3:
                self.DB_MESSAGES()



    def DB_CONTENT(self):
        time.sleep(2)
        db_message = """
                        Showing content in Database. . .
        """
        print(db_message)

        for j in self.db.keys():
            print(self.db[j])


if __name__=="__main__":
    DATABASE = DB("DB_SEARCH", "DB_NAME", "db", "cwd", "dirList", "ID", "DATA")
    DATABASE.DB_MESSAGES()
    DATABASE.SYSTEM()
    # DATABASE.DATA_INFORMATION()

