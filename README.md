# 🚖 Taxi Booking System 

A desktop-based **Taxi Booking System** designed using **Python, Tkinter**, and **SQLite3**. This system allows users to create accounts, log in securely, and book taxi rides between various campus locations. It calculates fare based on distance, car type, journey type, and other selected options.

---

## 📌 Features

- ✅ **Login & Registration System** (with SQLite)
- ✅ **GUI-based Interface** using `Tkinter`
- ✅ **Distance Calculation** between LPU locations
- ✅ **Car Type Selection** – Standard, Prime Sedan, Premium Sedan
- ✅ **Journey Type Options** – Single, Return, Special Needs
- ✅ **Fare Calculation** with Base Tax, Insurance, Luggage
- ✅ **Receipt Generation**
- ✅ **Reset and Exit Functionalities**

---

## 🎯 Functional Modules

### 🔐 User Authentication
- Register with a new username and password
- Login securely using SQLite3 for credential storage

### 📋 Booking Options
- Select pickup & drop location (CampusCafe, BoysHostel, GirlsHostel, AdmissionBlock)
- Choose journey type & car type
- Enable options like:
  - Travelling Insurance
  - Extra Luggage
  - Base Taxi Tax

### 💵 Cost Computation
- Calculates:
  - Distance-based fare
  - Tax (9%)
  - Travel insurance and luggage cost
- Total cost is displayed in real-time

### 🧾 Receipt
- Generates a formatted receipt with user and trip details
- Two-pane design: label and corresponding value

---

