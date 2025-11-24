Project Title : Python Academic Fees Collection and Admission System

Project Overview

This Python-based Academic Fees Collection and Admission System addresses the challenge of managing student admissions and financial records in an academic institution effectively. It allows users to register new students, track fee deposits against a total course fee, and instantly calculate the outstanding balance. The project applies Object-Oriented Programming (OOP) and JSON file handling to ensure robust data persistence, providing an efficient and accurate digital solution to replace manual financial ledgers.

Structured Development Process

1. Problem Definition : - (Identify a real-world problem)

Problem:- The reliance on manual processes for managing student admissions and fee payments, leading to increased administrative effort, potential human error in balancing accounts, and difficulty generating quick financial reports.

Goal:- To develop a functional, user-friendly command-line utility that utilizes Object-Oriented Programming (OOP) to model data, provides accurate, real-time tracking of fees, ensures data persistence, and promotes efficient, error-free academic finance management.

2. Requirement Analysis : - 

Functional Requirements

The application must allow users to Add New Admissions (name, course, total fee) and assign a unique, auto-generated ID.

The application must allow users to Collect Fee Deposits for an existing student ID.

The application must Calculate and Display the Remaining Balance for any student.

The application must display a Summary Report (Total Admitted, Total Fee Collected, Total Outstanding Balance).

The application must use JSON file handling to save and load all student records from the academic_records.json file.

The application must include validation to prevent overpayment and handle non-numeric input gracefully.

3. Top-Down Design / Modularization:-

The project uses modular design based on Object-Oriented Programming (OOP), defining two main classes for clear separation of concerns:

Student Class: Encapsulates all data related to a single student (ID, name, total fee, paid fee). It contains methods like calculate_balance() and deposit_fee().

AcademicSystem Class: The central controller. It manages the collection of all Student objects (stored in a dictionary for efficiency) and handles global operations like the main menu flow, file I/O, and report generation.

Key Functions: load_data(), save_data(), add_new_admission(), and collect_fee() are key methods within the central system.

4. Algorithm Development:-

The core financial logic is managed by the Fee Collection Algorithm, ensuring accurate accounting and preventing overpayment.

*Data Structure: All student records are stored as a Dictionary of Student Objects in the AcademicSystem class, keyed by the unique Admission ID.
*Fee Collection Algorithm:
    1. Locate student using ID.
    2. Calculate Remaining Balance = Total Fee - Paid Fee.
    3. Check if Deposit Amount > Remaining Balance.
    4. IF True: Adjust Deposit Amount = Remaining Balance.
    5.Update Paid Fee = Paid Fee + Deposit Amount.
    6.Report new balance.

5. ImplementationLanguage:

 Python 3.13.5
Tools/Libraries: Standard Python Library 
Concepts Applied: Object-Oriented Programming (OOP), JSON File 

6. Testing and Refinement

The program was tested against crucial scenarios focusing on financial accuracy and data integrity:

Test Case 1 (Persistence):
 Verified that records and the next available Admission ID are correctly loaded from academic_records.json upon program restart.

Test Case 2 (Overpayment): 
Confirmed that attempting to deposit an amount greater than the remaining balance results in the deposit being adjusted to the exact remaining balance (e.g., balance of 1000, attempt to deposit 1500; only 1000 is accepted).

Test Case 3 (Input Validation):
 Tested entering letters for ID and amount; the program correctly caught the ValueError and reprompted the user, preventing a crash.

Test Case 4 (Report Accuracy): 
Confirmed the Summary Report's totals (Collected Fee, Outstanding Balance) accurately reflected the sum of all individual student records.

Submission and Access Details
Submission Details
Clone the Repository: 'git clone https://github.com/devdarshshyju/Academic-Fees-Collection-System.git'

Navigate to Directory: cd Academic-Fees-Collection-System

Run the Script: python academic_system.py

Visual Demonstration
Screenshots of the program's output demonstrating its functionality (menu, fee collection, summary report) are provided in the screenshots directory.

Licensing

This project is distributed under the MIT License.
