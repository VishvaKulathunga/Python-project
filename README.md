# QR Code Generator for St. Sebastian's College ICT Day

## 📌 Project Description
This project is a **QR Code Generator System** developed for **St. Sebastian's College ICT Day** to improve efficiency and reduce queues during event registration. The system registers student details in a MySQL database and generates a unique QR code for each student. This QR code can be used for quick identification and access during the event.

## 🚀 Features
- Connect to MySQL database
- Register student details (Name, Email, NIC, Password, School)
- Store student data in the MySQL database
- Generate unique QR codes for each student
- Save QR codes as PNG images

## 🛠️ Technologies Used
- Python
- MySQL
- QR Code Library (`qrcode`)

## 📂 Database Structure
Table Name: **student**

| Column Name | Data Type |
|-------------|----------------|
| id            | INT (Primary Key) |
| name      | VARCHAR(255) |
| email       | VARCHAR(255) |
| nic            | VARCHAR(255) |
| password | VARCHAR(255) |
| school      | VARCHAR(255) |

## 🛠️ Installation & Setup

### Step 1: Install Required Libraries
```bash
pip install mysql-connector-python qrcode[pil]
```

### Step 2: Create MySQL Database
```sql
CREATE DATABASE test;

USE test;

CREATE TABLE student (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    nic VARCHAR(255),
    password VARCHAR(255),
    school VARCHAR(255)
);
```

### Step 3: Run the Python Script
```bash
python qr_code_generator.py
```

## 🎯 How It Works
1. User inputs student details (Name, Email, NIC, Password, School).
2. The system inserts the data into the MySQL database.
3. A unique QR code is generated based on student information and saved as an image.
4. The QR code is saved with the format `user_<user_id>_qr.png`.

## 📸 Sample QR Code
```
user_4_qr.png
```

## 📎 Future Improvements
- Adding user authentication
- QR code scanning system for event check-in
- Generating QR codes for event tickets

## 👨‍💻 Author
**K.P.D. Vishva Sangeeth Kulathunga**

## 🌐 GitHub Repository
[Python Project](https://github.com/VishvaKulathunga/Python-project)

