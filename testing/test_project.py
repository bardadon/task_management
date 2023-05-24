import datetime
import sys

sys.path.append('/projects/task_management')

from classes.project import Project
from classes.system import System
from classes.user import User


test_user = User(name='test',email='test', password='test')
test_user.create_project(title='test', description='test', end_date=datetime.datetime(2023,1,1))
test_project = test_user.projects[0]
test_system = System()
conn = test_system.connect_to_db()
cursor = conn.cursor()


# Test: project creation
def test_project_creation():
    test_project = Project(user_id = 1, title='test@test.com', description='test', end_date=datetime.datetime(2023,1,1))
    assert type(test_project) == Project

# Test: get methods
def test_get_methods_attributes():
    test_project = Project(user_id = 1, title='test', description='test', end_date=datetime.datetime(2023,1,1))
    test_project_attributes = (test_project.user_id,test_project.title, test_project.description, test_project.end_date)
    expected_project_attributes = (1,'test', 'test', datetime.datetime(2023,1,1))

    assert test_project_attributes == expected_project_attributes

# Test: Set methods
def test_set_methods_attributes():
    test_project.title = 'test2'
    test_project.description = 'test2'
    test_project.end_date = datetime.datetime(2024,1,1)

    test_project_attributes = (test_project.title, test_project.description, test_project.end_date)
    expected_project_attributes = ('test2', 'test2', datetime.datetime(2024,1,1))

    assert test_project_attributes == expected_project_attributes

# Test: create_task
def test_create_task_appendedtolist():
    test_user = User(name='test',email='test', password='test')
    test_user.create_project(title='test', description='test', end_date=datetime.datetime(2023,1,1))

    test_project = test_user.projects[0]
    test_project.create_task(title='test', description='test', end_date=datetime.datetime(2023,1,1))
    assert len(test_project.tasks) == 1

# Test: create_task appends to database
def test_create_task_appendedtodatabase():
    test_user = User(name='test',email='test', password='test')
    test_user.create_project(title='test', description='test', end_date=datetime.datetime(2023,1,1))

    test_project = test_user.projects[0]
    test_project.create_task(title='test', description='test', end_date=datetime.datetime(2023,1,1))

    query = "SELECT * FROM tasks WHERE project_id = %s"
    cursor.execute(query, (test_project.id,))
    results = cursor.fetchall()

    assert len(results) == 1