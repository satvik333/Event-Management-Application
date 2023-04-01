import pyodbc

class database:
    def connect_to_database():
        connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=ITT-SATVIK-MS;DATABASE=ISCdatabase;Trusted_Connection=yes;')
        return connection.cursor()
