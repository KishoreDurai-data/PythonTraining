#Mini Project

#MP1: Employee Management System:

employees = []

def add_employee():
    name = input("Name: ")
    age = int(input("Age: "))
    role = input("Role: ")
    salary = float(input("Salary: "))
    employees.append({"name": name, "age": age, "role": role, "salary": salary})

def display_employees():
    for emp in employees:
        print(emp)

def update_employee():
    name = input("Enter name to update: ")
    for emp in employees:
        if emp["name"] == name:
            emp["age"] = int(input("New Age: "))
            emp["role"] = input("New Role: ")
            emp["salary"] = float(input("New Salary: "))

def delete_employee():
    name = input("Enter name to delete: ")
    for emp in employees:
        if emp["name"] == name:
            employees.remove(emp)


# MP2: Student Report Card

def report_card():
    name = input("Name: ")
    mark1 = int(input("Mark1: "))
    mark2 = int(input("Mark2: "))
    mark3 = int(input("Mark3: "))
    total = mark1 + mark2 + mark3
    avg = total / 3

    if avg >= 90:
        grade = "O"
    elif avg >= 80:
        grade = "A"
    elif avg >= 50:
        grade = "B"
    else:
        grade = "Fail"

    print(f"Name: {name}, Total: {total}, Avg: {avg:.2f}, Grade: {grade}")


# MP3: Shopping Cart System

cart = []

def add_product():
    name = input("Product: ")
    price = float(input("Price: "))
    qty = int(input("Quantity: "))
    cart.append({"name": name, "price": price, "qty": qty})

def remove_product():
    name = input("Enter product to remove: ")
    for item in cart:
        if item["name"] == name:
            cart.remove(item)

def show_cart():
    total = 0
    for item in cart:
        cost = item["price"] * item["qty"]
        total += cost
        print(item["name"], item["qty"], cost)
    print("Total:", total)


# MP4: Login & User Validation

userdetails = {"admin": "1234", "user": "pass"}

def login():
    a = input("Username: ")
    i = input("Password: ")
    if a in userdetails  and userdetails[a] == i:
        print("Login Successful")
    else:
        print("Login Failed")


# MP5: Unique Visitor Counter

visitors = set()

def add_visitor():
    name = input("Visitor name: ")
    visitors.add(name)

def show_visitors():
    print("Total Visitors:", len(visitors))


# MP6: String Formatter Tool

def formatter():
    name = input("Name: ")
    product = input("Product: ")
    print(f"{name} bought {product}")
    print(name.ljust(10, '*'))
    print(name.rjust(10, '*'))
    print(name.center(10, '*'))


# MP7: Bank Account System

account = {"name": "", "balance": 0}

def create_account():
    account["name"] = input("Name: ")
    account["balance"] = float(input("Initial Balance: "))

def deposit():
    amt = float(input("Amount: "))
    account["balance"] += amt

def withdraw():
    amt = float(input("Amount: "))
    if amt <= account["balance"]:
        account["balance"] -= amt

def check_balance():
    print(account)


# MP8: Voting System

votes = {}

def add_vote():
    name = input("CandidateName: ")
    votes[name] = votes.get(name, 0) + 1

def display_winner():
    winner = max(votes, key=votes.get)
    print("Winner is:", winner)


# MP9: Course Enrollment System

students = {}

def add_student():
    name = input("Student name: ")
    courses = input("Courses (SEPERATION): ").split(",")
    students[name] = courses

def update_courses():
    name = input("Student name: ")
    if name in students:
        courses = input("LiveCourses: ").split(",")
        students[name] = courses

def show_students():
    print(students)


# MP10: Number Utility Tool

def number_tool():
    num = int(input("Enter number: "))
    print(bin(num))
    print(oct(num))
    print(hex(num))
    print(f"{num:,}")
    print(f"{num:.2e}")