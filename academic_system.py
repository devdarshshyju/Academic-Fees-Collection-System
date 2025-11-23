import json
import os

# --- 1. Student Class: Blueprint for a single student record ---
class Student:
    """Represents a student with admission and fee details."""
    
    # Class-level counter for auto-generating Admission IDs
    next_admission_id = 1001
    
    def __init__(self, name, course, total_fee):
        self.admission_id = Student.next_admission_id
        Student.next_admission_id += 1
        self.name = name
        self.course = course
        self.total_fee = total_fee
        self.paid_fee = 0
        self.admission_status = "Admitted"

    def calculate_balance(self):
        """Calculates the outstanding fee balance."""
        return self.total_fee - self.paid_fee

    def deposit_fee(self, amount):
        """Processes a fee deposit."""
        balance = self.calculate_balance()
        if amount <= 0:
            return "Error: Deposit amount must be positive."
        elif amount > balance:
            # Prevent overpayment, adjust the amount to the remaining balance
            amount = balance
            self.paid_fee += amount
            return f"Success: Fee deposited. Adjusted amount to remaining balance. Total Paid: {self.paid_fee}. Balance: {self.calculate_balance()}"
        else:
            self.paid_fee += amount
            return f"Success: {amount} deposited. Total Paid: {self.paid_fee}. Balance: {self.calculate_balance()}"

    def to_dict(self):
        """Converts the object to a dictionary for JSON saving."""
        return {
            'admission_id': self.admission_id,
            'name': self.name,
            'course': self.course,
            'total_fee': self.total_fee,
            'paid_fee': self.paid_fee,
            'admission_status': self.admission_status
        }
    
    # This method is used for printing student details
    def __str__(self):
        return (f"\n--- Student Details (ID: {self.admission_id}) ---\n"
                f"Name: {self.name}\n"
                f"Course: {self.course}\n"
                f"Total Fee: ₹{self.total_fee:.2f}\n"
                f"Paid Fee: ₹{self.paid_fee:.2f}\n"
                f"Balance: ₹{self.calculate_balance():.2f}\n"
                f"Status: {self.admission_status}")

# --- 2. Academic System Class: Manages all students and file operations ---
class AcademicSystem:
    """Manages admissions, fee collection, and data persistence."""
    
    FILE_NAME = 'academic_records.json'

    def __init__(self):
        # Dictionary to store Student objects: {ID: Student_object}
        self.students = {}
        self.load_data()

    def load_data(self):
        """Loads student data from a JSON file."""
        if os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, 'r') as f:
                data = json.load(f)
                
                # Reconstruct Student objects from the saved dictionary data
                for student_dict in data['students']:
                    student = Student(
                        student_dict['name'], 
                        student_dict['course'], 
                        student_dict['total_fee']
                    )
                    # Manually set attributes from file
                    student.admission_id = student_dict['admission_id']
                    student.paid_fee = student_dict['paid_fee']
                    student.admission_status = student_dict['admission_status']
                    self.students[student.admission_id] = student
                
                # Update the ID counter for new admissions
                Student.next_admission_id = data['next_id']
            print(f"Data loaded successfully from {self.FILE_NAME}.")
        else:
            print("No existing data file found. Starting fresh.")

    def save_data(self):
        """Saves current student data to a JSON file."""
        # Convert all student objects to a list of dictionaries
        student_list = [student.to_dict() for student in self.students.values()]
        
        # Data structure to save
        data_to_save = {
            'next_id': Student.next_admission_id,
            'students': student_list
        }
        
        with open(self.FILE_NAME, 'w') as f:
            json.dump(data_to_save, f, indent=4)
        print(f"\nData saved successfully to {self.FILE_NAME}.")

    def add_new_admission(self, name, course, total_fee):
        """Creates a new Student and adds them to the system."""
        new_student = Student(name, course, total_fee)
        self.students[new_student.admission_id] = new_student
        print(f"\n✅ New student admitted: {new_student.name} (ID: {new_student.admission_id})")

    def find_student(self, adm_id):
        """Retrieves a student object by Admission ID."""
        try:
            adm_id = int(adm_id)
            return self.students.get(adm_id)
        except ValueError:
            print("Error: Admission ID must be an integer.")
            return None

    def collect_fee(self, adm_id, amount):
        """Handles fee collection for a student."""
        student = self.find_student(adm_id)
        if student:
            result = student.deposit_fee(amount)
            print(f"\n{result}")
        else:
            print("\n❌ Error: Student not found with this ID.")

    def view_all_students(self):
        """Prints details of all students."""
        if not self.students:
            print("\nNo student records available.")
            return

        print("\n--- ALL STUDENT RECORDS ---")
        for student in self.students.values():
            print(student)
        print("--------------------------")

    def generate_fee_report(self):
        """Calculates and prints summary report."""
        total_admitted = len(self.students)
        total_fee_due = sum(student.total_fee for student in self.students.values())
        total_fee_paid = sum(student.paid_fee for student in self.students.values())
        total_balance = total_fee_due - total_fee_paid
        
        print("\n=== FEES COLLECTION SUMMARY REPORT ===")
        print(f"Total Admitted Students: {total_admitted}")
        print(f"Total Fee Due (All Students): ₹{total_fee_due:,.2f}")
        print(f"Total Fee Collected: ₹{total_fee_paid:,.2f}")
        print(f"Total Outstanding Balance: ₹{total_balance:,.2f}")
        print("======================================")

# --- 3. Main Menu and Execution ---
def main():
    system = AcademicSystem()

    while True:
        # 
        print("\n\n--- ACADEMIC MANAGEMENT SYSTEM ---")
        print("1. New Student Admission")
        print("2. Collect Fee")
        print("3. View Student Details (by ID)")
        print("4. View All Students")
        print("5. Generate Fees Report")
        print("6. Save & Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        try:
            if choice == '1':
                name = input("Enter student name: ").strip()
                course = input("Enter course name: ").strip()
                fee = float(input("Enter total course fee: ₹"))
                system.add_new_admission(name, course, fee)
                
            elif choice == '2':
                adm_id = input("Enter Student Admission ID for fee collection: ")
                amount = float(input("Enter amount to deposit: ₹"))
                system.collect_fee(adm_id, amount)
                
            elif choice == '3':
                adm_id = input("Enter Student Admission ID to view: ")
                student = system.find_student(adm_id)
                if student:
                    print(student)
                else:
                    print(f"Student with ID {adm_id} not found.")

            elif choice == '4':
                system.view_all_students()
                
            elif choice == '5':
                system.generate_fee_report()

            elif choice == '6':
                system.save_data()
                print("Exiting system. Goodbye!")
                break
                
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
                
        except ValueError:
            print("\n🚨 Input Error: Please enter valid numbers for fee/ID.")
        except Exception as e:
            print(f"\n🚨 An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
