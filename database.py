from dotenv import load_dotenv

load_dotenv()

from app import app, db
from app.models import Employee, Menu, MenuItem, MenuItemType, Table


with app.app_context():
    db.drop_all()
    db.create_all()

    employee = Employee(name="Margot", employee_number=1234, password="password")
    beverages = MenuItemType(name="Beverages")
    entrees = MenuItemType(name="Entrees")
    sides = MenuItemType(name="Sides")

    dinner = Menu(name="Dinner")

    fries = MenuItem(name="French fries", price=3.50, type=sides, menu=dinner)
    drp = MenuItem(name="Dr. Pepper", price=1.0, type=beverages, menu=dinner)
    jambalaya = MenuItem(name="Jambalaya", price=21.98, type=entrees, menu=dinner)

    table_data = [
        {"number": 1, "capacity": 4},
        {"number": 2, "capacity": 6},
        {"number": 3, "capacity": 2},
        {"number": 4, "capacity": 8},
        {"number": 5, "capacity": 4},
    ]

    for data in table_data:
        table = Table(number=data["number"], capacity=data["capacity"])
        db.session.add(table)

    db.session.add(employee)
    db.session.commit()
