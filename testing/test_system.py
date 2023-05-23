
import sys
from classes.project import Project
from classes.user import User
from classes.system import System
sys.path.append('/projects/task_management')



test_system = System(host = '192.168.1.193', user='postgres', password=1365, port=5432, database='task_management')
conn = test_system.connect_to_db()
cursor = conn.cursor()

def test_connect_to_db():
    test_system = System(host = '192.168.1.193', user='postgres', password=1365, port=5432, database='task_management')
    conn = test_system.connect_to_db()

    assert conn.status == 1 

def test_insert_user():
    
    # Creating a new user
    test_user = User(name='test2', email='test2@test2.com', password='test2')

    # Check if System automatically inserted user
    query = "SELECT * FROM users WHERE name = 'test2'"

    cursor.execute(query)
    results = cursor.fetchall()

    assert results[0][1] == 'test2'


def test_insert_project():
    
    # Creating a new user
    test_project = Project(title='test2', description='test2')

    # Check if System automatically inserted user
    query = "SELECT * FROM projects WHERE title = 'test2'"

    cursor.execute(query)
    results = cursor.fetchall()

    assert results[0][1] == 'test2'
