from psycopg2 import connect
import sys
import os
import datetime
sys.path.append('/projects/task_management')

class System:
    def __init__(self, host = '192.168.1.193', user = 'postgres', password = 1365, port = 5432, database = 'task_management') -> None:
        '''
        Constructor for System class
        Args:
            host: host ip address(default: my local ip address)
            user: username (default: postgres)
            password: password (default: 1365)
            port: port number (default: 5432)
            database: database name (default: task_management)
        Returns:
            None
        '''
        self.host = host
        self.user = user
        self.password = password
        self.port = port 
        self.database = database

    def connect_to_db(self):
        '''
        Connect to PostgreSQL database
        Args:
            None
        Returns:
            conn: connection to database
        '''
        try:
            conn = connect(host = self.host, user = self.user, password = self.password, port = self.port, database = self.database)
            return conn
        except:
            print("Error connecting to database")

    def grab_max_user_id(self):
        '''
        Grab the max user id from the database
        Args:
            None
        Returns:
            max_id: max user id
        '''
        conn = self.connect_to_db()
        cursor = conn.cursor()
        cursor.execute("SELECT MAX(user_id) FROM users")
        max_id = cursor.fetchone()[0]
        return max_id

    def update_user_attributes(self, user_id, name, email, password):
        '''
        Update user attributes
        Args:
            user_id: user id
            name: user name
            email: user email
            password: user password
        
        Returns:
            None
        '''
        conn = self.connect_to_db()
        cursor = conn.cursor()
        query = "update users set name = %s, email = %s,password = %s, update_date = %s where user_id = %s"
        cursor.execute(query,(name, email, password, datetime.datetime.today(), user_id))
        conn.commit()

    def update_project_attributes(self, project_id, title, description, end_date):
        '''
        Update project attributes
        Args:
            project_id: project id
            title: project title
            description: project description
            end_date: project end date

        Returns:
            None
        '''
        conn = self.connect_to_db()
        cursor = conn.cursor()
        query = "update projects set title = %s, description = %s, update_date = %s, end_date = %s where project_id = %s"
        cursor.execute(query,(title, description, datetime.datetime.today(), end_date, project_id))
        conn.commit()


    def insert_user(self, id, name, email, password, create_date, update_date):
        '''
        Insert user to database to users table
        Args:
            id: user id
            name: user name
            email: user email
            password: user password
            create_date: user create date
            update_date: user update date
        
        Returns:
            None
        '''
        conn = self.connect_to_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO users (user_id, name, email, password, create_date, update_date) VALUES (%s, %s, %s, %s, %s, %s)", (id, name, email, password, create_date, update_date))
        conn.commit()
        cur.close()
        conn.close()

    def insert_project(self, id, title, description, create_date, update_date, end_date):
        '''
        Insert project to database to projects table
        Args:
            id: project id
            title: project title
            description: project description
            create_date: project create date
            update_date: project update date

        Returns:
            None
        '''
        conn = self.connect_to_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO projects (project_id, title, description, create_date, update_date, end_date) VALUES (%s, %s, %s, %s, %s, %s)", (id, title, description, create_date, update_date, end_date))
        conn.commit()
        cur.close()
        conn.close()



    #def modify user

    # def insert_project

    # def modify project




if __name__ == '__main__':
    test_system = System(host = '192.168.1.193', user='postgres', password=1365, port=5432, database='task_management')
    conn = test_system.connect_to_db()
    print(conn.status)
    cursor = conn.cursor()

    # Creating a new user
    #test_user = User(name='test2', email='test2@test2.com', password='test2')

    # Check if System automatically inserted user
    query = "SELECT * FROM users WHERE name = 'test2'"

    cursor.execute(query)
    results = cursor.fetchall()
    print(results)