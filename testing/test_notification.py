import datetime
import sys
sys.path.append('/projects/task_management')

from classes.system import System
from classes.notification import Notification
from classes.user import User
from classes.project import Project
from classes.task import Task

# Test: create_notification
def test_create_notification():
    test_user = User(name = 'test', email='test', password='test')
    test_user.create_project(title='test', description='test')
    test_project = test_user.projects[0]

    test_project.create_task(title='test', description = 'test')
    test_tasks = test_project.tasks[0]

    # Create a notification using Task
    test_notification = test_tasks.create_notification('test123')
    assert isinstance(test_notification, Notification)

# Test: create notification using Task
# Test: get method for title
def test_createnotification_usingTask():
    test_user = User(name = 'test', email='test', password='test')
    test_user.create_project(title='test', description='test')
    test_project = test_user.projects[0]

    test_project.create_task(title='test', description = 'test')
    test_tasks = test_project.tasks[0]

    # Create a notification using Task
    test_notification = test_tasks.create_notification('test123')
    assert test_notification.content == 'test123'

# Test: create_notification inserted to notifications list
def test_createnotification_appendedToList():
    test_user = User(name = 'test', email='test', password='test')
    test_user.create_project(title='test', description='test')
    test_project = test_user.projects[0]

    test_project.create_task(title='test', description = 'test')
    test_tasks = test_project.tasks[0]

    # Create a notification using Task
    assert len(test_tasks.notifications) == 0
    test_notification = test_tasks.create_notification('test123')
    assert len(test_tasks.notifications) == 1

# Test: create_notification inserted notification to db
def test_createnotification_appendedTodb():
    test_user = User(name = 'test', email='test', password='test')
    test_user.create_project(title='test', description='test')
    test_project = test_user.projects[0]

    test_project.create_task(title='test', description = 'test')
    test_tasks = test_project.tasks[0]
    test_notification = test_tasks.create_notification('test123')
    
    system = System()
    conn = system.connect_to_db()
    cursor = conn.cursor()
    query = "select content from notifications where notification_id = %s"
    cursor.execute(query, (test_notification.notification_id,))
    assert cursor.fetchone()[0] == 'test123'


def test_setmethods():
    test_user = User(name = 'test', email='test', password='test')
    test_user.create_project(title='test', description='test')
    test_project = test_user.projects[0]

    test_project.create_task(title='test', description = 'test')
    test_tasks = test_project.tasks[0]
    test_notification = test_tasks.create_notification('test123')

    test_notification.content = 'test1234'
    assert test_notification.content == 'test1234'

def test_setmethods_updatesdb():
    test_user = User(name = 'test', email='test', password='test')
    test_user.create_project(title='test', description='test')
    test_project = test_user.projects[0]

    test_project.create_task(title='test', description = 'test')
    test_tasks = test_project.tasks[0]
    test_notification = test_tasks.create_notification('test123')

    test_notification.content = 'test1234'
    system = System()
    conn = system.connect_to_db()
    cursor = conn.cursor()
    query = "select content from notifications where notification_id = %s"
    cursor.execute(query, (test_notification.notification_id,))
    assert cursor.fetchone()[0] == 'test1234'

