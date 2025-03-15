import mysql.connector
import qrcode


def connect_to_db():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="test"
        )
        print("Connected to the database")
        return db
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


def get_student_details():
    name = input("Enter your name: ")
    email = input("Enter student email: ")
    nic = input("Enter student NIC: ")
    password = input("Enter student password: ")
    school = input("Enter your school name: ")
    return name, email, nic, password, school


def insert_student(name, email, nic, password, school):
    db = connect_to_db()
    if db is None:
        return

    try:
        cursor = db.cursor()
        sql = "INSERT INTO student (name, email, nic, password, school) VALUES (%s, %s, %s, %s, %s)"
        values = (name, email, nic, password, school)
        cursor.execute(sql, values)
        db.commit()
        print(f"Record inserted successfully, ID: {cursor.lastrowid}")
        return cursor.lastrowid 
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if db.is_connected():
            db.close()
            print("Connection closed")


def generate_qr_code(name, email, nic, password, school, user_id):

   
    user_details = f"Name: {name}\nEmail: {email}\nNIC: {nic}\nSchool: {school}\nUser ID: {user_id}"

   
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(user_details)
    qr.make(fit=True)

    # Create and save the image
    img = qr.make_image(fill="black", back_color="white")
    img.save(f"user_{user_id}_qr.png")  # Save QR code as an image
    print(f"QR code generated and saved as user_{user_id}_qr.png")

# Main execution
if __name__ == "__main__":
    student_details = get_student_details()
    user_id = insert_student(*student_details)  
    if user_id:
        generate_qr_code(*student_details, user_id)  
