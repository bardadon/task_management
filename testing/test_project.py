import datetime
import sys

sys.path.append('/projects/task_management')

from classes.project import Project


test_project = Project(user_id = 1, title='test', description='test', end_date=datetime.datetime(2023,1,1))

# Test: project creation
def test_project_creation():
    test_project = Project(user_id = 1, title='test@test.com', description='test', end_date=datetime.datetime(2023,1,1))
    assert type(test_project) == Project

# Test: get methods
#def test_get_methods_attributes():
#    test_project_attributes = (test_project.id,test_project.title, test_project.description, test_project.end_date)
#    expected_project_attributes = (1,'test', 'test', datetime.datetime(2023,1,1))

 #   assert test_project_attributes == expected_project_attributes

# Test: Set methods
#def test_set_methods_attributes():
 #   test_project.id = 2
  #  test_project.title = 'test2'
   # test_project.description = 'test2'
    #test_project.end_date = datetime.datetime(2024,1,1)

    #test_project_attributes = (test_project.id,test_project.title, test_project.description, test_project.end_date)
    #expected_project_attributes = (2,'test2', 'test2', datetime.datetime(2024,1,1))

    #assert test_project_attributes == expected_project_attributes