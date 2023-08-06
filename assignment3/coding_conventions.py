''' Criteria: Complete all the questions
● Create a Python program that manages student records. The program should have the
following functionalities:
- Create a function that can add new students to the records with their student_id,
name, age, and grade. The records should be saved to “json” file and each time
new record is added, it should be saved to same “json” file
- Allow searching for a student by student_id or name. The data should return age
and grade from the saved file.
- Allow updating a student's information by using student_id or name(age or grade)
Ensure to follow PEP8 Coding Guidelines for following criterias:
- Proper Indentation
- Maximum Line Length
- Prescriptive Naming conventions (Package and Module Names, Class Names,
Exception Names, Global Variable Names, Function and Variable Names, Method
Names and Instance Variables, Constants)
- Source File Encoding while accessing the JSON file
- Add NumPy Docstring to each function '''

import json
import io


class StudentRecordManager:
    """
    Class for managing student records.

    Attributes:
        file_path (str): Path to the JSON file to save the records.
        records (list): List of student records.
    """

    def __init__(self, file_path='C:/Users/Upama/ML-Trainee-weeek1/assignment3/student_records.json'):
        """
        Initialize the StudentRecordManager.

        Args:
            file_path (str): Path to the JSON file to save the recirds.
        """
        self.file_path = file_path
        self.records = self._load_records()

    def _load_records(self):
        """
        Load records from the JSON file.

        Returns:
            list: List of student records
        """
        try:
            with io.open(self.file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _save_records(self):
        """Save records to the JSON file. """
        with io.open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(self.records, file, indent=4)

    def add_student(self, student_id, name, age, grade):
        """
        Add a new student record.

        Args:
            student_id (str): Student ID.
            name (str): Student name.
            age (int): Student age.
            grade (str): Student grade.
        """
        new_student = {
            'student_id': student_id,
            'name': name,
            'age': age,
            'grade': grade
        }
        self.records.append(new_student)
        self._save_records()

    def search_student(self, key, value):
        """
        Search for a student by student_id or name.

        Args:
            key (str): 'student_id' or name:
            value (str): Value to search for.

        Returns:
            dict or None: Student recor if found, otherwise None.
        """
        for student in self.records:
            if student[key] == value:
                return {'age': student['age'], 'grade': student['grade']}
        return None

    def update_student(self, key, value, new_data):
        """
        Update a student's information.

        Args:
            key (str): 'student_id or 'name.
            value (str): Value to identify the stuednts.
            new_data (dict): New daat to update (age and/or garde).

        Returns:
            bool: True if update successul, False otherwise.
        """
        for student in self.records:
            if student[key] == value:
                if 'age' in new_data:
                    student['age'] = new_data['age']
                if 'grade' in new_data:
                    student['grade'] = new_data['grade']
                self._save_records
                return True
        return False

#Example usage
if __name__ == '__main__':
    manager = StudentRecordManager()

    manager.add_student('064', 'Sadichhya', 23, 'A')
    manager.add_student('094', 'Upama', 23, 'B')
    manager.add_student('097', 'Samyam', 22, 'C')

    print(manager.search_student('student_id', '097'))
    print( manager.search_student('name', 'Upama'))

    manager.update_student('name', 'Sadichhya', {'age': 24, 'grade': 'A+'})