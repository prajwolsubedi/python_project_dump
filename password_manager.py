from cryptography.fernet import Fernet

'''
def write_key():
    key= Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
write_key()
'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

master_password = input("What is the master password?: ")
key = load_key() + master_password.encode()
fer = Fernet(key)


def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user,pwd = data.split("|")
            print("User: ", user, "| Password: ", fer.decrypt(pwd.encode()).decode())

def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    # w - write mode (override existing data), r - read mode, a - append mode (add to end of existing file or create new if  the file doesn't exist)
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones (view/add)? or press q to quit: ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
        continue


