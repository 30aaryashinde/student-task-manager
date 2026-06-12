import mysql.connector

def get_database_connection():
   
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password="aaryashinde@30",
        database="student_task_manager",
        port=3306
    )
   
    return connection
