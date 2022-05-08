"""
This database is going to store task by User

You can Update hours on task, insert more task, or delete a task
"""

import sqlite3


#connect to database
connection = sqlite3.connect('task_manager.db')
cursor = connection.cursor()


#create table if not already exist
cursor.execute("CREATE TABLE IF NOT EXISTS `User` (`User_id` INT UNSIGNED AUTO_INCREMENT NOT NULL , `User_fname` VARCHAR(45) NOT NULL, `User_lname` VARCHAR(45) NOT NULL, PRIMARY KEY (`User_id`))")
cursor.execute("CREATE TABLE IF NOT EXISTS `Task` (`Task_id` INT UNSIGNED AUTO_INCREMENT NOT NULL, `Task_name` VARCHAR(45) NOT NULL, PRIMARY KEY (`Task_id`))")
cursor.execute("CREATE TABLE IF NOT EXISTS `User_Task` ( `User_id` INT UNSIGNED NOT NULL, `Task_id` INT UNSIGNED NOT NULL, `Hours_task` INT NOT NULL, PRIMARY KEY (`User_id`, `Task_id`), CONSTRAINT `fk_User_has_Task_User` FOREIGN KEY (`User_id`) REFERENCES `User` (`User_id`) ON DELETE NO ACTION ON UPDATE NO ACTION, CONSTRAINT `fk_User_has_Task_Task1` FOREIGN KEY (`Task_id`) REFERENCES `Task` (`Task_id`) ON DELETE NO ACTION ON UPDATE NO ACTION)")

choice = None

while choice != "5":
    print("1) Display ")
    print("2) Add ")
    print("3) Update ")
    print("4) Delete ")
    print("5) Quit")
    choice = input("> ")
    print()
    if choice == "1":
        print("1) Dispay User")
        print("2) Display Task")
        print("3) Display User Task")
        choice = input("> ")
        if choice == "1":
            # Display User
            cursor.execute("SELECT * FROM User ")
            print("{:>10}  {:>10}  {:>10}".format("User_id", "User_fname", "User_lname"))
            for record in cursor.fetchall():
                print("{:>10}  {:>10}  {:>10}".format(record[0], record[1], record[2]))

        elif choice == "2":
            # Display Task
            cursor.execute("SELECT * FROM task ORDER BY task_name DESC")
            print("{:>10}  {:>10}".format("Task Id", "Task Name"))
            for record in cursor.fetchall():
                print("{:>10}  {:>10}".format(record[0], record[1]))
        elif choice == "3":
            # Display User Task for Hour
            cursor.execute("SELECT * FROM user_task ORDER BY hours_task DESC")
            print("{:>10}  {:>10}  {:>10}".format("User_Id", "Task Id", "Hours Worked"))
            for record in cursor.fetchall():
                print("{:>10}  {:>10}  {:>10}".format(record[0], record[1], record[2]))         
    elif choice == "2":
        print("1) Add User")
        print("2) Add Task")
        print("3) Add User Task")
        choice = input("> ")
        if choice == "1":
            # Add New User
            try:
                user_id = input("User_id: ")
                user_fname = input("First Name: ")
                user_lname = input("Last Name: ")
                values = (user_id, user_fname, user_lname)
                cursor.execute("INSERT INTO user VALUES (?,?,?)", values)
                connection.commit()
            except ValueError:
                print("Invalid pay!")

        elif choice == "2":
            # Add New Task
            try:
                task_id = int(input("Task_id: "))
                task = input("Task: ")
                values = (task_id,task)
                cursor.execute("INSERT INTO task VALUES (?,?)", values)
                connection.commit()
            except ValueError:
                print("Invalid pay!")
        
        elif choice == "3":
            # Add New Hours Works
            try:
                #print out user so it's easier to pick
                cursor.execute("SELECT * FROM User ")
                print("{:>10}  {:>10}  {:>10}".format("User_id", "User_fname", "User_lname"))
                for record in cursor.fetchall():
                    print("{:>10}  {:>10}  {:>10}".format(record[0], record[1], record[2]))
                user_id = int(input("User Id: "))

                #print out task so it's easier to pick
                cursor.execute("SELECT * FROM task ORDER BY task_name DESC")
                print("{:>10}  {:>10}".format("Task Id", "Task Name"))
                for record in cursor.fetchall():
                    print("{:>10}  {:>10}".format(record[0], record[1]))
                task_id = int(input("Task Id: "))


                hours_task = int(input("Hours Worked: "))
                values = (user_id, task_id, hours_task)
                cursor.execute("INSERT INTO user_task VALUES (?,?,?)", values)
                connection.commit()
            except ValueError:
                print("Invalid pay!")
    elif choice == "3":
        print("1) Update User")
        print("2) Update Task")
        print("3) Update Hours Worked")

        choice = input("> ")

        if choice == "1":
            print("1) Change First Name")
            print("2) Change Last Name")

            choice = input("> ")
            
            if choice == "1":
                try:
                    #Update user first name
                    user_id = int(input("User Id: "))
                    user_fname = input("User First Name: ")
                    values = (user_fname, user_id) # Make sure order is correct
                    cursor.execute("UPDATE user SET user_fname = ? WHERE user_id = ?", values)
                    connection.commit()
                    if cursor.rowcount == 0:
                        print("Invalid name!")
                except ValueError:
                    print("Invalid")
            
            elif choice == "2":
                try:
                    #Update user lname name
                    user_id = int(input("User Id: "))
                    user_lname = input("User Last Name: ")
                    values = (user_lname, user_id) # Make sure order is correct
                    cursor.execute("UPDATE user SET user_lname = ? WHERE user_id = ?", values)
                    connection.commit()
                    if cursor.rowcount == 0:
                        print("Invalid name!")
                except ValueError:
                    print("Invalid")

        elif choice == "2":
                try:
                    #Update user task name
                    task_id = int(input("Task Id: "))
                    task = input("Task Name: ")
                    values = (task, task_id) # Make sure order is correct
                    cursor.execute("UPDATE task SET task_name = ? WHERE task_id = ?", values)
                    connection.commit()
                    if cursor.rowcount == 0:
                        print("Invalid name!")
                except ValueError:
                    print("Invalid")


        elif choice == "3":
            try:
                #Update user Hours worked
                task_id = int(input("Task Id: "))
                user_id = int(input("User Id:"))
                hours_worked = input("Hours Worked: ")
                values = (hours_worked,task_id, user_id) # Make sure order is correct
                cursor.execute("UPDATE user_task SET hours_task = ? WHERE task_id = ? AND user_id = ?", values)
                connection.commit()
                if cursor.rowcount == 0:
                    print("Invalid name!")
            except ValueError:
                print("Invalid")
        
    elif choice == "4":
        # Delete hours worked
        user_id = int(input("User Id: "))
        task_id = int(input("Task Id: "))
        if user_id == None:
            continue
        values = (user_id, task_id )
        cursor.execute("DELETE FROM user_task WHERE user_id = ? AND task_id = ?" , values)
        connection.commit()
    print()

# Close the database connection before exiting
connection.close()
