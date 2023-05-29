import datetime
import sys
sys.path.append('/projects/task_management')

from classes.system import System

class Comment:

    # Create a system instance
    system = System()

    # Create a Comment constructor
    def __init__(self, task_id: int, content: str, created_date = datetime.datetime.today(), last_update_date = datetime.datetime.today()) -> None:
        self._comment_id = Comment.system.grab_max_object_id(object = 'comment') + 1
        self._task_id = task_id
        self._content = content
        self._created_date = created_date
        self._last_update_date = last_update_date
        
        # Insert comment to db
        Comment.system.insert_comment(self._comment_id, task_id, content, created_date, last_update_date)

    # Get methods for id, name, email and password
    @property
    def comment_id(self):
        return self._comment_id
    
    @property
    def task_id(self):
        return self._task_id
    
    @property
    def content(self):
        return self._content
    
    @property
    def created_date(self):
        return self._created_date
    
    @property
    def last_update_date(self):
        return self._last_update_date
    
    # Set methods for content
    @content.setter
    def content(self, new_content):
        if isinstance(new_content, str):
            Comment.system.update_comment_attributes(self.comment_id, self.task_id, new_content, self.created_date, datetime.datetime.today())
            self._content = new_content
        else:
            raise TypeError("Content must be a text!")
    
        






