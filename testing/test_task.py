import sys
import datetime
sys.path.append('/projects/task_management')
from classes.task import Task
from classes.system import System
from classes.user import User
from classes.project import Project

test_user = User(name='test', email='test@test.com', password='test')
test_project = Project(user_id = test_user.id, title='test@test.com', description='test', end_date=datetime.datetime(2023,1,1))
test_task = Task(project_id=test_project.id, title='test', description='test')
test_system = System()
conn = test_system.connect_to_db()
cursor = conn.cursor()

# Test: creating a task
def test_create_task():
    test_task = Task(project_id=test_project.id, title='test', description='test')
    assert isinstance(test_task, Task)

# Test: creating a task, status = active
def test_createtask_defaultstatusisactive():
    assert test_task.status == 'active'


# Test: task inserted to db. 
# Test: Check if new task is insered to db with max id + 1
def test_createtask_insertedtodb():
    test_task = Task(project_id=test_project.id, title='task_title_test123', description='test')

    # Verify in db
    task_id = test_system.grab_max_object_id(object='task')
    query = "select title from tasks where task_id = %s"
    cursor.execute(query, (task_id,))
    test_title = cursor.fetchall()[0][0]
    expected_title = 'task_title_test123'

    assert test_title == expected_title

# Test: modifying task, updated in backend
def test_updatingtitle():
    old_title = test_task.title
    test_task.title = 'new_title'

    assert test_task.title != old_title

# Test: modifying task, updated in db
def test_updatingtitle_updatedindb():
    # Change title
    test_task.title = 'another_new_title'

    # Verify change in db
    query = "select title from tasks where task_id = %s"
    cursor.execute(query, (test_task.task_id,))
    test_title = cursor.fetchall()[0][0]
    expected_title = 'another_new_title'

    assert test_title == expected_title



