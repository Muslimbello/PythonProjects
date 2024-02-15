from cryptography.fernet import Fernet


def Key_gen():
    key = Fernet.generate_key()

    with open("key.key", "wb") as key_file:
        key_file.write(key)


with open("key.key", "rb") as file:
    if file.read():
        pass
    else:
        Key_gen()


def load_key():
    with open("key.key", "rb") as file:
        key = file.read()
    return key


key = load_key()
print(key)
fer = Fernet(key)


def create():
    name = input("Account Name: ")
    pwd = input("Password: ")
    with open("password.txt", "a") as f:
        encrypt_pass = fer.encrypt(pwd.encode()).decode()
        f.write(name + "|" + encrypt_pass + "\n")


def view():
    with open("password.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            decrypt_passw = fer.decrypt(passw.encode()).decode()
            print(f"User: {user}, | Password:{decrypt_passw}")


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
        print("invalid mode")
        continue
