from cryptography.fernet import Fernet

master_pwd = input("What is the master password")

""" uncomment and run this code ones to get your unique key """
# def Key_gen():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)
# Key_gen()


def load_key():
    with open("key.key", "rb") as file:
        key = file.read()
    return key


key = load_key() + master_pwd.encode()
fer = Fernet(key)


def create():
    name = input("Account Name: ")
    pwd = input("Password: ")
    with open("password.txt", "a") as f:
        f.write(name + "|" + str(fer.encrypt(pwd.encode())) + "\n")


def view():
    with open("password.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print(f"user:{user}, password:{passw}")


while True:
    mode = input(
        " would you like to add a password or view all existing passwords(view/create) type 'q' to quit "
    ).lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "create":
        create()
    else:
        pass
