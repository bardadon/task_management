import datetime
import sys
sys.path.append('/projects/task_management')
from classes.system import System

class Project:

    # Create a system instance
    system = System(host = '192.168.1.193', user='postgres', password=1365, port=5432, database='task_management')

    def __init__(self, user_id, title: str, description: str, create_date = datetime.datetime.today(), update_date = datetime.datetime.today(), end_date = datetime.datetime.today() + datetime.timedelta(days=365)) -> None:
        '''
        Constructor for Project class
        Args:
            title: project title
            description: project description
            create_date: project create date (default: today)
            update_date: project update date (default: today)
            end_date: project end date (default: today + 365 days)
        Returns:
            None
        Notes:
            - This constructor will insert the project to the database.
            - Only User class can create a project.
        '''
        self._title = title
        self._description = description
        self._end_date = end_date
        self.create_date = create_date
        self.update_date = update_date
        self.user_id = user_id

        # Grab the last id from the database and add 1 to it
        last_id = Project.system.grab_max_object_id(object='project')
        id = last_id + 1
        
        # Insert project to db
        Project.system.insert_project(id, user_id, title, description, create_date, update_date, end_date)
        self._id = id

    # Get methods for name, email and password
    @property
    def id(self):
        return self._id
    
    @property
    def title(self):
        return self._title
    
    @property
    def description(self):
        return self._description
    
    @property
    def end_date(self):
        return self._end_date
    
    # Set methods for name, email and password
    # Each set method updates the database as well
    @title.setter
    def title(self, new_title):
        if isinstance(new_title, str):
            Project.system.update_project_attributes(self.id, new_title, self.description, self.end_date)
            self._title = new_title
        else:
            raise TypeError("Title must be a text!")
        
    @description.setter
    def description(self, new_description):
        if isinstance(new_description, str):
            Project.system.update_project_attributes(self.id, self.title, new_description, self.end_date)
            self._description = new_description
        else:
            raise TypeError("Description must be a text!")
        
    @end_date.setter
    def end_date(self, new_end_date):
        if isinstance(new_end_date, datetime.datetime):
            Project.system.update_project_attributes(self.id, self.title, self.description, new_end_date)
            self._end_date = new_end_date
        else:
            raise TypeError("End date must be a date!")
        
    def __str__(self) -> str:
        return f'Project: {self.title}\nDescription: {self.description}\nEnd date: {self.end_date}\nCreate date: {self.create_date}\nUpdate date: {self.update_date}\n'
        
    
    

if __name__ == '__main__':
    project = Project(1, 'Project 1', 'This is a project')
    print(project)

