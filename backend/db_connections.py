import mysql.connector

def get_connection():
    """
    Returns a MySQL database connection
    """
    return mysql.connector.connect(
        host="localhost",          
        user="root",               
        password="2202",
        database="voting_db"       
    )
