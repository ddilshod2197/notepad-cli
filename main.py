class NotepadCLI:
    def __init__(self):
        self.sahifa = ""

    def kirish(self):
        print("Notepad CLI")
        print("1. Yozish")
        print("2. Ko'rish")
        print("3. Saqlash")
        print("4. Chiqish")

    def yozish(self):
        self.sahifa = input("Yozing: ")
        print("Yozilgan matn: ", self.sahifa)

    def ko'rish(self):
        print("Sahifa: ", self.sahifa)

    def saqlash(self):
        with open("sahifa.txt", "w") as file:
            file.write(self.sahifa)
        print("Sahifa saqlandi.")

    def chiqish(self):
        print("Chiqish")
        exit()

def main():
    notepad = NotepadCLI()
    while True:
        notepad.kirish()
        tanlov = input("Tanlov: ")
        if tanlov == "1":
            notepad.yozish()
        elif tanlov == "2":
            notepad.ko'rish()
        elif tanlov == "3":
            notepad.saqlash()
        elif tanlov == "4":
            notepad.chiqish()
        else:
            print("Notog'ri tanlov.")

if __name__ == "__main__":
    main()
