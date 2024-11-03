import mysql.connector

#  Establish a connection to the database
def create_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='mobilecomparison'
    )
    
def login_data(email, password):
        result = False
        connection = create_connection()
        cursor = connection.cursor()
        query1 = f"""
                CREATE TABLE IF NOT EXISTS Accounts (
                Username VARCHAR(50) NOT NULL,
                Email VARCHAR(100) primary key,
                passwords VARCHAR(100) NOT NULL
                );
                """
        query2 = f"""SELECT passwords FROM Accounts WHERE Email='{email}';"""
        cursor.execute(query1)
        cursor.execute(query2)
        results = cursor.fetchall()
        if results:
            for passwd in results:
                if passwd[0] == password:
                    result = True
                else:
                    result = False
        else:
            result ="no user"
        cursor.close()
        connection.close()
        return result
    
def upload_data(username,email, password):
    connection = create_connection()
    cursor = connection.cursor()
    query1 = f"""
                CREATE TABLE IF NOT EXISTS Accounts (
                Username VARCHAR(50) NOT NULL,
                Email VARCHAR(100) primary key,
                passwords VARCHAR(100) NOT NULL
                );
                """
    query2 = """
                    insert into Accounts(Username,Email,passwords) values(%s,%s,%s);
            """
    cursor.execute(query1)
    cursor.execute(query2,(username,email, password))
    
    cursor.close()
    connection.commit()
    connection.close()