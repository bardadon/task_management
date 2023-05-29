import datetime
import sys

sys.path.append('/projects/task_management')

from classes.project import Project
from classes.user import User
from classes.system import System

test_system = System()
conn = test_system.connect_to_db()
cursor = conn.cursor()

test_user = User(name='test', email='test@test.com', password='test')
test_project = test_user.create_project(title = 'test', description='test')


# Test: user creation
def test_user_creation():
    test_user = User(name='test', email='test@test.com', password='test')
    assert type(test_user) == User

# Test: get methods
def test_get_methods_attributes():
    test_user_attributes = (test_user.name, test_user.email, test_user.password)
    expected_user_attributes = ('test', 'test@test.com', 'test')

    assert test_user_attributes == expected_user_attributes

# Test: Set methods
def test_modifyattributes_changeoccuredindb():
    test_user = User(name='modifyingtest',
                     email='modifyingemail',
                     password='modifyingpassword')
    
    # Change the attributes of the user
    test_user.name = 'modifyingtest2'
    test_user.email = 'modifyingemail2'
    test_user.password = 'modifyingpassword2'

    # extract the name from the database
    query = "SELECT * FROM users WHERE user_id = %s"
    cursor.execute(query, (test_user.id,))
    results = cursor.fetchall()

    # check if the name in the database is the same as the one we set
    assert results[0][1] == test_user.name
    assert results[0][2] == test_user.email
    assert results[0][3] == test_user.password
 
def test_changingattributes_changesupdatetime():
    # grab old update time
    test_user = User(name='update_time',
                    email='update_time',
                    password='update_time')
    old_update_time = test_user.update_date

    # modify an attribute
    test_user.name = 'new_update_time'

    # grab new update time
    query = "select update_date from users where user_id = %s"
    cursor.execute(query, (test_user.id,))
    new_update_date = cursor.fetchall()[0][0]

    # assert new updatetime == today 
    assert new_update_date > old_update_time


# Test: create project method
def test_create_project():
    # Creating a project using a User, and collecting its attributes
    test_project = test_user.create_project(title='test_project', description='test')

    # Verifying the attributes of the project from the database
    query = "SELECT * FROM projects WHERE project_id = %s"
    cursor.execute(query, (test_project.id,))
    results = cursor.fetchall()

    # Collecting the attributes of the project from the database
    project_attributes = (results[0][2], results[0][3])

    # Expected attributes of the project
    expected_project_attributes = (test_project.title, test_project.description)  

    # Verifying the attributes of the project from the database
    assert project_attributes == expected_project_attributes


# Test: can update project attributes
def test_update_project():
    # Creating a project using a User, and collecting its attributes
    test_project = test_user.create_project(title='test_project', description='test')

    # Updating the project attributes
    test_project.title = 'updated_project'
    test_project.description = 'updated_project'

    # Verifying the attributes of the project from the database
    query = "SELECT * FROM projects WHERE project_id = %s"
    cursor.execute(query, (test_project.id,))
    results = cursor.fetchall()

    # Collecting the attributes of the project from the database
    project_attributes = (results[0][2], results[0][3])

    # Expected attributes of the project
    expected_project_attributes = (test_project.title, test_project.description)  

    # Verifying the attributes of the project from the database
    assert project_attributes == expected_project_attributes


# Test: deleting a project, deletes from both db and User.project list
def test_deletecomment_deletedfromUserprojectlist():
    # Creating a user and a project, and counting the number of projects
    test_user3 = User(name='test3', email='test3', password='test3')
    test_user3.create_project(title='test_project3', description='test_project3')
    test_user3.create_project(title='test_project4', description='test_project4')
    test_number_of_projects = len(test_user3.projects)

    # Deleting project from User.project list
    test_user3.delete_project(project_title='test_project3')

    # Expected number of projects
    expected_number_of_projects = len(test_user3.projects) + 1

    # Verify that project is deleted from list
    assert test_number_of_projects == expected_number_of_projects

def test_deletecomment_deletedfromdb():
    # Creating a user and a project, and counting the number of projects
    test_user3 = User(name='test3', email='test3', password='test3')
    test_user3.create_project(title='test_project3', description='test_project3')
    test_user3.create_project(title='test_project4', description='test_project4')
    
    # Grab num of projects from db
    query = "select count(*) from projects where user_id = %s"
    cursor.execute(query, (test_user3.id,))
    test_number_of_projects = cursor.fetchall()[0][0]

    # Deleting project 
    test_user3.delete_project(project_title='test_project3')

    # Grab number of projects from db
    query = "select count(*) from projects where user_id = %s"
    cursor.execute(query, (test_user3.id,))
    expected_test_number_of_projects = cursor.fetchall()[0][0] + 1

    # Verify that project is deleted from list
    assert test_number_of_projects == expected_test_number_of_projects 
    
    




if __name__ == '__main__':
    test_deleteproject_deletedfromdb()