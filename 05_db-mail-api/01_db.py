import mysql.connector
# pip install mysql-connector-python
def connect_to_mariadb(host, database, user, password, port=3306):
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port
        )
        return conn
    except mysql.connector.Error as e:
        print(f"MariaDB connection error: {e}")
        return None

def fetch_data(conn, query):
    try:
        cursor = conn.cursor(dictionary=True) 
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result
    except mysql.connector.Error as e:
        print(f"Query error: {e}")
        return None

def calculate_statistics(data, column):
    if not data or not column:
        return None
    
    values = [row[column] for row in data if column in row and row[column] is not None]

    if not values:
        return None
    
    return {
        "count": len(values),
        "sum": sum(values),
        "avg": sum(values) / len(values),
        "min": min(values),
        "max": max(values)
    }

if __name__ == "__main__":
    db_config = {
        "host": "localhost",        
        "database": "employees",   
        "user": "employees",             
        "password": "employees",     
        "port": 3306               
    }
    conn = connect_to_mariadb(**db_config)
  
    if conn:
        try:
            query = "SELECT * FROM employees"
            results = fetch_data(conn, query)
            # print(results)
            stats = calculate_statistics(results, "yearly_salary")
            print(stats)
        finally:
            conn.close()