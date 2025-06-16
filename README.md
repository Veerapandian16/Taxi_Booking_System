Taxi Booking System in LPU
Overview
The Taxi Booking System in LPU is a Python-based desktop application built using Tkinter and SQLite3. It provides a user-friendly interface for managing taxi bookings within a university campus (Lovely Professional University - LPU). The application includes a login system for user authentication and a comprehensive booking system to calculate fares based on distance, car type, and additional services.
Features

User Authentication:
Login and registration system with SQLite database to store usernames and passwords.
Secure password entry with masked input.


Taxi Booking:
Select pickup and drop-off locations within the campus (e.g., CampusCafe, BoysHostel, GirlsHostel, AdmissionBlock).
Choose car types: Standard, PrimeSedan, or PremiumSedan.
Select journey types: Single, Return, or SpecialNeeds.
Additional options: Taxi Tax, Travel Insurance, and Extra Luggage.
Calculate total fare based on distance, car type, and selected services.


Receipt Generation:
Generate a detailed receipt with booking details, customer information, and cost breakdown.


Reset and Exit:
Reset the booking form to start a new booking.
Exit the application with a confirmation prompt.



Prerequisites
To run this application, you need:

Python 3.x (tested with Python 3.8+)
Tkinter: Included with standard Python installations.
SQLite3: Included with standard Python installations.

Installation

Clone the Repository:
git clone https://github.com/your-username/taxi-booking-system-lpu.git
cd taxi-booking-system-lpu


Verify Python Installation:Ensure Python 3.x is installed by running:
python --version


Run the Application:Execute the main script:
python taxi_booking_system.py

This will create a Users.db SQLite database file in the project directory to store user credentials.


Usage

Launch the Application:
Run the script to open the login window.


Login or Register:
Login: Enter your username and password to access the booking system.
Create Account: If you don't have an account, click "Create Account" to register a new username and password.


Booking a Taxi:
Enter customer details (Firstname, Surname, Address, Postcode, Telephone, Mobile, Email).
Select pickup and drop-off locations from the dropdown menus.
Choose the number of passengers (Pooling).
Select a car type (Standard, PrimeSedan, PremiumSedan) and journey type (Single, Return, SpecialNeeds).
Check optional services (Taxi Tax, Distance, Travel Insurance, Extra Luggage) as needed.
Click Total to calculate the fare.
Click Receipt to generate a detailed receipt.
Click Reset to clear the form or Exit to close the application.



Project Structure

taxi_booking_system.py: Main Python script containing the application logic.
Users.db: SQLite database file (created automatically) to store user credentials.

Screenshots
(You can add screenshots of the login screen and booking interface here. Use GitHub's image hosting or link to an external source.)
Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes and commit (git commit -m "Add feature").
Push to the branch (git push origin feature-branch).
Create a Pull Request.

License
This project is licensed under the MIT License. See the LICENSE file for details.
Contact
For issues or suggestions, please open an issue on GitHub or contact [your-email@example.com].

Built with Python, Tkinter, and SQLite3 for efficient taxi booking management at LPU.
