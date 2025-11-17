class Students():
    name=""
    age=""
    grade=""

    def __init__(self):
        print("New student being added.")

    def takedetails(self):
        self.name=input("Enter name: ")
        self.age=input("Enter age: ")
        self.grade=input("Enter grade: ")

    def showdetails(self):
        print(self.name + "details:")
        print(self.age)
        print(self.grade)

Sam=Students()
Sam.takedetails()
Sam.showdetails()

Jerry=Students()
Jerry.takedetails()
Jerry.showdetails()