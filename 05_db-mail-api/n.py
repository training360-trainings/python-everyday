import mysql.connector
from xlsx_handler import read_xlsx


def connect_to_mariadb(host, database, user, password, port=3306):
    try:
        connection = mysql.connector.connect(
            host=host, database=database, user=user, password=password, port=port
        )
        return connection
    except mysql.connector.Error as error:
        print("MardiaDB conection error:", error)
        return None


def create_table(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        cursor.close()
    except mysql.connector.Error as error:
        print("Failed to create table:", error)


def show_tables(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        cursor.close()
        return tables
    except mysql.connector.Error as error:
        print("Failed to show tables:", error)


if __name__ == "__main__":
    mariadb_config = {
        "host": "localhost",
        "database": "employees",
        "user": "employees",
        "password": "employees",
    }
    conn = connect_to_mariadb(**mariadb_config)

    table = """CREATE TABLE IF NOT EXISTS employees(
      id INT AUTO_INCREMENT PRIMARY KEY,
      first_name VARCHAR(50) NOT NULL,
      last_name VARCHAR(50) NOT NULL,
      email_address VARCHAR(100) NOT NULL UNIQUE,
      gender VARCHAR(50) NOT NULL,
      yearly_salary INT NOT NULL,
      years_of_experience TINYINT NOT NULL,
      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
      updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    )
    """

    # create_table(conn, table)
    # print(show_tables(conn))
    print(read_xlsx("./files/employees-with-header.xlsx", skip_headers_count=1))
