
import mysql.connector
from tkinter import messagebox

# Establish connection once and reuse
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Bhumi1408",
        database="heart_data"
    )
    mycursor = mydb.cursor()
    print("✅ Connection established!!")
except mysql.connector.Error as err:
    messagebox.showerror("Connection", f"Database connection not established: {err}")
    mydb = None

def Save_Data_MySql(B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R):
    if not mydb:
        messagebox.showerror("Connection", "No database connection. Check credentials.")
        return

    try:
        query = """INSERT INTO data (Name,Date,DOB,age,sex,Cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,Result) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        values = (B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R)

        mycursor.execute(query, values)
        mydb.commit()
        print("✅ Data saved successfully!")

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error inserting data: {err}")
