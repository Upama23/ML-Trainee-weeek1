from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.models import Employee


SQLALCHEMY_DATABASE_URL = "sqlite:///./data.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# employee_data = [
#     {"id": "094", "name": "Upama","department":"AI Services" },
#     {"id":"023", "name": "Samyam", "department":"AI Services"},
#     {"id":"064", "name":"Sadichhya", "department":"Data"}
# ]


def create_employee_data():
    db = SessionLocal()
    try:
        employee_data = [
            {"name": "Upama", "department": "AI Services"},
            {"name": "Samyam", "department": "AI Services"},
            {"name": "Sadichhya", "department": "Data"}
        ]

        for data in employee_data:
            employee = Employee(**data)
            db.add(employee)

        db.commit()

    finally:
        db.close()