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

    def grab_max_object_id(self, object):
        '''
        Grab the max object id from the database
        Args:
            None
        Returns:
            max_id: max object id
        '''
        conn = self.connect_to_db()
        cursor = conn.cursor()

        if object == 'user':
            cursor.execute("SELECT MAX(user_id) FROM users")
        if object == 'project':
            cursor.execute("SELECT MAX(project_id) FROM projects")
        if object == 'task':
            cursor.execute("SELECT MAX(task_id) FROM tasks")

        max_id = cursor.fetchone()[0]
        return max_id
    

    ## User Related Methods ##
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

    def delete_user(self, user_id):
        '''
        Delete user from database
        Args:
            user_id: user id

        Returns:
            None
        '''
        conn = self.connect_to_db()
        cur = conn.cursor()
        cur.execute("DELETE FROM users WHERE user_id = %s", (user_id,))
        conn.commit()
        cur.close()
        conn.close()

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

    ## Project Related Methods ##

    def insert_project(self, id, user_id, title, description, create_date, update_date, end_date):
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
        cur.execute("INSERT INTO projects (project_id, user_id, title, description, create_date, update_date, end_date) VALUES (%s, %s, %s, %s, %s, %s, %s)", (id, user_id, title, description, create_date, update_date, end_date))
        conn.commit()
        cur.close()
        conn.close()

    def delete_project(self, project_id):
        '''
        Delete project from database
        Args:
            project_id: project id

        Returns:
            None
        '''
        conn = self.connect_to_db()
        cur = conn.cursor()
        cur.execute("DELETE FROM projects WHERE project_id = %s", (project_id,))
        conn.commit()
        cur.close()
        conn.close()

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
        cursor.close()
        conn.close

    ## Task Related Methods ##
    def insert_task(self, task_id, project_id, title, description, status, due_date, start_date, last_update_date):
        '''
        Insert task to database to tasks table
        Args:
            task_id: task id
            project_id: project id
            title: task title
            description: task description
            status: task status
            due_date: task due date
            start_date: task start date
            last_update_date: task last update date
        
        Returns:
            None
        ''' 
        conn = self.connect_to_db()
        cursor = conn.cursor()
        query = '''
        insert into tasks(task_id, project_id, title, description, status, due_date, start_date, last_update_date) 
        values
        (%s, %s,%s,%s,%s,%s,%s, %s)
        '''
        cursor.execute(query,(task_id, project_id, title, description, status, datetime.datetime.today() + datetime.timedelta(days=365), datetime.datetime.today(), datetime.datetime.today()))
        conn.commit()
        cursor.close()
        conn.close

    def update_task_attributes(self, project_id, task_id, title, description, status, due_date, start_date, last_update_date):
        '''
        Update task attributes
        Args:
            project_id: project id
            task_id: task id
            title: task title
            description: task description
            status: task status
            due_date: task due date
            start_date: task start date
            last_update_date: task last update date
        Returns:
            None
        '''
        conn = self.connect_to_db()
        cursor = conn.cursor()
        query = "update tasks set project_id = %s, task_id = %s, title = %s, description = %s, status = %s, due_date = %s, start_date = %s, last_update_date = %s where task_id = %s"
        cursor.execute(query,(project_id, task_id, title, description, status, due_date, start_date, last_update_date, task_id))
        conn.commit()
        cursor.close()
        conn.close

    def delete_task(self, task_id):
        '''
        Delete task from database
        Args:
            task_id: task id

        Returns:
            None
        '''
        conn = self.connect_to_db()
        cur = conn.cursor()
        cur.execute("DELETE FROM tasks WHERE task_id = %s", (task_id,))
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