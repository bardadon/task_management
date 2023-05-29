import datetime
import sys
sys.path.append('/projects/task_management')

from classes.system import System
from classes.user import User
from classes.project import Project
from classes.task import Task
from classes.comment import Comment

system = System()
conn = system.connect_to_db()
cursor = conn.cursor()

# Test: create_comment
def test_create_comment():
    test_comment = Comment(1, 1, 'test')
    assert isinstance(test_comment, Comment)

# Test: create comment using Task
# Test: get method for title
def test_createcomment_usingTask():
    test_user = User(name = 'test', email='test', password='test')
    test_user.create_project(title='test', description='test')
    test_project = test_user.projects[0]

    test_project.create_task(title='test', description = 'test')
    test_tasks = test_project.tasks[0]

    # Create a comment using Task
    test_comment = test_tasks.create_comment('test123')
    assert test_comment.content == 'test123'
    

# Test: create_comment inserted to comments list
def test_createcomment_appendedToList():
    test_user = User(name = 'test', email='test', password='test')
    test_user.create_project(title='test', description='test')
    test_project = test_user.projects[0]

    test_project.create_task(title='test', description = 'test')
    test_tasks = test_project.tasks[0]

    # Create a comment using Task
    assert len(test_tasks.comments) == 0
    test_comment = test_tasks.create_comment('test123')
    assert len(test_tasks.comments) == 1

# Test: create_comment inserted comment to db
def test_createcomment_appendedTodb():
    test_user = User(name = 'test', email='test', password='test')
    test_user.create_project(title='test', description='test')
    test_project = test_user.projects[0]

    test_project.create_task(title='test', description = 'test')
    test_tasks = test_project.tasks[0]
    test_comment = test_tasks.create_comment('test123')
    
    query = "select content from comments where comment_id = %s"
    cursor.execute(query, (test_comment.comment_id,))
    test_result = cursor.fetchall()[0][0]
    expected_result = 'test123'

    assert test_result == expected_result

# Test: set method for content
def test_setMethod_content():
    test_user = User(name = 'test', email='test', password='test')
    test_user.create_project(title='test', description='test')
    test_project = test_user.projects[0]

    test_project.create_task(title='test', description = 'test')
    test_tasks = test_project.tasks[0]
    test_comment = test_tasks.create_comment('test123')

    test_comment.content = 'new_content'
    assert test_comment.content == 'new_content'

# Test: update comment in db
def test_updatecomment_updatedindb():
    test_user = User(name = 'test', email='test', password='test')
    test_user.create_project(title='test', description='test')
    test_project = test_user.projects[0]

    test_project.create_task(title='test', description = 'test')
    test_tasks = test_project.tasks[0]
    test_comment = test_tasks.create_comment('test123')

    test_comment.content = 'new_content'

    # Check if comment updated in db
    query = "select content from comments where comment_id = %s"
    cursor.execute(query, (test_comment.comment_id,))
    test_result = cursor.fetchall()[0][0]
    expected_result = 'new_content'

    assert test_result == expected_result

# Test: 

    

if __name__ == '__main__':
    test_createcomment_usingTask()