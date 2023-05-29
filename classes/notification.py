import datetime
import sys
sys.path.append('/projects/task_management')

from classes.system import System

class Notification:

    # Create a system instance
    system = System()

    # Create a Comment constructor
    def __init__(self, task_id: int, content: str, created_date = datetime.datetime.today(), notify_date = datetime.datetime.today() + datetime.timedelta(days=30)  ,last_update_date = datetime.datetime.today()) -> None:
        self._notification_id = Notification.system.grab_max_object_id(object = 'notification') + 1
        self._task_id = task_id
        self._content = content
        self._created_date = created_date
        self._notify_date = notify_date
        self._last_update_date = last_update_date
        
        # Insert comment to db
        Notification.system.insert_notification(self._notification_id, task_id, content, created_date, notify_date, last_update_date)

    # Get methods for id, name, email and password
    @property
    def notification_id(self):
        return self._notification_id
    
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
    def notify_date(self):
        return self._notify_date
    
    @property
    def last_update_date(self):
        return self._last_update_date
    
    # Set methods for content
    @content.setter
    def content(self, new_content):
        if isinstance(new_content, str):
            Notification.system.update_notification_attributes(self.notification_id, self.task_id, new_content, self.created_date, self.notify_date,datetime.datetime.today())
            self._content = new_content
        else:
            raise TypeError("Content must be a text!")
        
    @notify_date.setter
    def notify_date(self, new_notify_date):
        if isinstance(new_notify_date, datetime.datetime):
            Notification.system.update_notification_attributes(self.notification_id, self.task_id, self.content, self.created_date, new_notify_date,datetime.datetime.today())
            self._notify_date = new_notify_date
        else:
            raise TypeError("Notify date must be a datetime!")
    
        






