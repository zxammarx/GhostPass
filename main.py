import os
import secrets
import string
import sqlite3
import termcolor
import pyfiglet
import base64




def encrypt_pass(password):
    encrypted_bytes = []
    for i, char in enumerate(password):
        
        key_char = secret_key[i % len(secret_key)]
        encrypted_byte = ord(char) ^ ord(key_char)
        encrypted_bytes.append(encrypted_byte)
    
    b64_bytes = base64.b64encode(bytes(encrypted_bytes))
    return b64_bytes.decode('utf-8')


def decrypt_pass(encrypted_password):

    encrypted_bytes = base64.b64decode(encrypted_password)
    
    decrypted_chars = []
    for i, byte_val in enumerate(encrypted_bytes):
        key_char = secret_key[i % len(secret_key)]
        decrypted_char = chr(byte_val ^ ord(key_char))
        decrypted_chars.append(decrypted_char)
    
    return "".join(decrypted_chars)


def database_pass():
    data_masg2 = """
        Choose What You Want:
        \t [1] Add Account
        \t [2] Update Information
        \t [3] Delet Password
        \t [4] Show One Password
        \t [5] Show All Password
        \t Else Back To Main Page
        >>>>>>>>>>>>>>>>>"""
    print(data_masg2, end=" ")
    data_choice = input()

    if data_choice not in ["1", "2", "3", "4", "5"]:
        os.system('cls||clear')
        return True
    data_masg = """
        Please Enter Database Name Followed By ( .db) Like: [database.db]
        >>>>>>>>>>>>>>>>"""
    print(data_masg, end=" ")
    data_name = input()


    db = sqlite3.connect(f"{data_name}")
    cr = db.cursor()
    cr.execute("CREATE TABLE IF NOT EXISTS PASSWORD (website TEXT, user_email TEXT, password TEXT)")


    if data_choice == "1":
        print("Please Inter Website Name >>>", end=" ")
        website_name = input()
        print("Please Inter Website Username Or Email >>>", end=" ")
        website_username = input()
        print("Please Inter Website Password >>>", end=" ")
        website_password = input()
        encrypted_password = encrypt_pass(website_password)
        cr.execute(f"INSERT INTO PASSWORD(website, user_email, password) VALUES('{website_name}', '{website_username}', '{encrypted_password}')")
        db.commit()
        db.close()
        os.system('cls||clear')
        print("-----------------------  Your Password Has Been Added  -----------------------")
        database_pass()


    elif data_choice == "2":
        print("Please Enter Website Name You Want To Update Information In It >>>>>>>", end=" ")
        website_name2 = input()
        print("What Do You Want To Update [1] Email / [2] Password", end=" ")
        update_choice = input()

        if update_choice == "1":
            print("Enter Your New Email or Username >>>>>>>>>>", end=" ")
            new_email = input()
            cr.execute(f"UPDATE PASSWORD SET user_email = '{new_email}' WHERE website = '{website_name2}'")
            db.commit()
            db.close()
            os.system('cls||clear')
            print("-----------------------  Your Email / Username Has Been Updated  -----------------------")
            database_pass()
        elif update_choice == "2":
            print("Enter Your New Password >>>>>>>>>>", end=" ")
            new_password = input()
            new_encrypted_password = encrypt_pass(new_password)
            cr.execute(f"UPDATE PASSWORD SET password = '{new_encrypted_password}' WHERE website = '{website_name2}'")
            db.commit()
            db.close()
            os.system('cls||clear')
            print("------------------  Your Password Has Been Updated  ------------------")
            database_pass()
        else:
            return True


    elif data_choice == "3":
        print("Enter Website Name >>>>>>>>>>", end="")
        delete_website = input()
        cr.execute(f"DELETE FROM password WHERE website = '{delete_website}'")
        db.commit()
        db.close()
        os.system('cls||clear')
        print("------------------  The Password Is Deleted  ------------------")
        database_pass()


    elif data_choice == "4":
        print("Enter Website You Want >>>>>>>>> ", end=" ")
        show_website = input()

        cr.execute(f"SELECT * FROM password WHERE website = '{show_website}'")
        data = cr.fetchone()
        if data:
            os.system('cls||clear')
            print("############################################")
            print(f"Website => {data[0]}")
            print(f"Email / Username => {data[1]}")
            print(f"Password => {decrypt_pass(data[2])}")
            print("############################################")
            db.close()
        else:
            os.system('cls||clear')
            print("------------------  Sorry Website You Choose Not In Database  ------------------")
            db.close()
            database_pass()
    
    elif data_choice == "5":

        cr.execute(f"SELECT * FROM password")
        data = cr.fetchall()
        os.system('cls||clear')
        print("------------------ Here Is Your Passwords  ------------------")
        
        for web in data:
            print(f"Website => {web[0]}")
            print(f"Email / Username => {web[1]}")
            print(f"Password => {decrypt_pass(web[2])}")
            print("#" * 20)
        db.close()
        database_pass()

    else:
        return True


secret_key = "GhostPass_Secret_Key"


def generate_pass():

    masg_generate = """
        ------------------------------
        |  Generate Strong Password  |
        ------------------------------
        
        Please Enter Length For Password >>>>"""
    print(masg_generate, end=" ")
    password_length = int(input())

    chars: str = string.ascii_letters + string.digits + r"""!@$#"""
    password: str = ''.join(secrets.choice(chars) for let in range(password_length))

    print(f"Here Is Your Password: {password}")

    print("Press [1] If You Want To Save It Or [2] To Go Back To Main Page:", end=" ")
    user_choose = input()
    if user_choose == "1":
        os.system('cls||clear')
        database_pass()
        return True
    else:
        os.system('cls||clear')
        return True



def check_pass():

    masg_cheack = """
        -----------------------------------------------------------------------
        |  Check If Your Password Is Leaked in Most Famous File -rockyou.txt  |
        -----------------------------------------------------------------------
        
        Please Enter Your Pasword>>>>"""
    print(masg_cheack, end=" ")
    user_password = input()

    rockyou = open("password_manager/rockyou.txt", "r", encoding = "utf-8", errors="ignore")

    for password in rockyou:

        leaked_pass = password.strip()

        if user_password == leaked_pass:
            print("Your Password Is Leaked You Must Change It")
            print("If You Want Help Change It Press [1] Or [2] To Check Another One Or [3] To Go Main Page:", end=" ")
            rockyou.close()
            user_choose = input()
            if user_choose == "1":
                os.system('cls||clear')
                generate_pass()
            elif user_choose == "2":
                os.system('cls||clear')
                check_pass()
            else:
                os.system('cls||clear')
                return True

    else:
        print("Your Password Is Strong Don't Need To Change It")
        print("If You Want To Test Another Password Type [1] Or [2] To Go Back To Main Page")
        rockyou.close()
        user_choose2 = input()
        if user_choose2 == "1":
            os.system('cls||clear')
            generate_pass()
        else:
            os.system('cls||clear')
            return True



masg = """
    ------------------------------------------
    |  Welcome To The Best Password Manager  |
    ------------------------------------------
    
    Choose What You Want:
    \t [1] Password Database
    \t [2] Generate Password
    \t [3] Check Password
    \t [4] Exit
    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""

print(termcolor.colored(pyfiglet.figlet_format("GhostPass"), color="red"))

while True:

    print(masg, end=" ")
    user_input = input()
    
    if user_input == "1":
        os.system('cls||clear')
        database_pass()
    
    elif user_input == "2":
        os.system('cls||clear')
        generate_pass()
    
    elif user_input == "3":
        os.system('cls||clear')
        check_pass()
    
    elif user_input == "4":
        os.system('cls||clear')
        print(50 * "*")
        print("Thanks For Choosing This App")
        print(50 * "*")
        break

    else:
        os.system('cls||clear')
        print(50 * "*")
        print("Wrong Choice Choose again")
        print(50 * "*")