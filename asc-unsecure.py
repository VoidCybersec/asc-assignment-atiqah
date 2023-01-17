import subprocess
import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="1101", database="asc_unsecure2")
cursor = db.cursor()

def bash_clear():
    subprocess.run("clear")

def add_dish():
    bash_clear()
    dish_name = input("Enter the name of the dish          : ")
    dish_type = input("Enter the type of the dish          : ")
    dish_origin = input("Enter the the origin of the dish    : ")
    
    cursor.execute(f"INSERT INTO dishes (dish_name, dish_type, dish_origin) VALUES ('{dish_name}', '{dish_type}', '{dish_origin}');")
    db.commit()

    admin_dashboard()    


def view_dish_admin():
    bash_clear()
    print(" ________________________________________________________")
    print("|                                                        |")
    print("| These are the yummy dishes found in the system! Enjoy! |")
    print("|________________________________________________________|")
    
    db = mysql.connector.connect(host="localhost", user="root", password="1101", database="asc_unsecure2")
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM dishes;")
    all_dishes = cursor.fetchall()

    for dish in all_dishes:
        print (f"{dish[1]}, a {dish[2]} type dish, originating from {dish[3]}")

    while True:
        choice = input("\nBack to main page? (y/n)")
        match choice:
            case "y":
                admin_dashboard()
                break
            case "n":
                view_dish_admin()
                break
            case _:
                print("\nInvalid choice! Pick again:")

    admin_dashboard()



def admin_dashboard():
    bash_clear()
    print(" _____________________________________________________")
    print("|                                                     |")
    print("| Welcome to the Dish Managment System Administrator! |")
    print("|_____________________________________________________|")
    print("\n1. Add Dish\n2. View Dishes\n3. Exit")

    while True:
        choice = input("\nChoice: ")
        match choice:
            case "1":
                add_dish()
                break
            case "2":
                view_dish_admin()
                break
            case "3":
                exit()
            case _:
                print("Invalid choice! Pick again: ")

def view_dish_user():
    bash_clear()
    print(" __________________________________________________")
    print("|                                                  |")
    print("| These are the dishes found in the system! Enjoy! |")
    print("|__________________________________________________|")
    
    cursor.execute(f"SELECT * FROM dishes;")
    all_dishes = cursor.fetchall()

    for dish in all_dishes:
        print (f"{dish[1]}, by {dish[2]} from the year {dish[3]}")

    while True:
        choice = input("Back to main page? (y/n)")
        match choice:
            case "y":
                user_dashboard()
            case "n":
                view_dish_user()
            case _:
                print("\nInvalid choice! Pick again:")

def user_dashboard():
    bash_clear()
    print(" ____________________________________________")
    print("|                                            |")
    print("| Welcome to the Dish Managment System User! |")
    print("|____________________________________________|")
    print("\n1. View Dishes\n2. Exit")

    while True:
        choice = input("\nChoice: ")
        match choice:
            case "1":
                view_dish_user()
            case "2":
                exit()
            case _:
                print("Invalid choice! Pick again: ")

def login():

    in_user_name = input("Username: ")
    in_user_password = input("Password: ")
    print("\n")

    cursor.execute(f"SELECT user_name FROM credentials WHERE user_name='{in_user_name}';")
    db_out_un = cursor.fetchall()

    if len(db_out_un) == 0:
        print("Incorrect username or password!")
    else:
        db_username = db_out_un[0][0]

        cursor.execute(f"SELECT user_password FROM credentials WHERE user_name='{db_username}';")
        db_out_pass = cursor.fetchall()

        if len(db_out_pass) == 0:
            print("Incorrect usernmae or password!")
        else:
            db_password = db_out_pass[0][0]

            if (in_user_name == db_username) and (in_user_password == db_password):
                if (in_user_name == "admin"):
                    admin_dashboard()
                else:
                    user_dashboard()
            else:
                print("Incorrect usernmae or password!")
        
def begin():
    bash_clear()
    print(" _________________________________________________________________")
    print("|                                                                 |")
    print("| Welcome to the Dish Managment System! Please log in to proceed! |")
    print("|_________________________________________________________________|")
    
    login()

begin()
