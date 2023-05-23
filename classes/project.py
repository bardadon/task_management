import datetime
import sys
sys.path.append('/projects/task_management')
from classes.system import System

class Project:

    # insert user to database
    system = System(host = '192.168.1.193', user='postgres', password=1365, port=5432, database='task_management')
    conn = system.connect_to_db()
    cursor = conn.cursor()

    def __init__(self, title: str, description: str, create_date = datetime.datetime.today(), update_date = datetime.datetime.today(), end_date = datetime.datetime.today() + datetime.timedelta(days=365)) -> None:
        self._title = title
        self._description = description
        self._end_date = end_date
        self.create_date = create_date
        self.update_date = update_date

        # Grab the last id from the database and add 1 to it
        Project.cursor.execute("SELECT MAX(project_id) FROM projects")
        last_id = Project.cursor.fetchone()[0]
        id = last_id + 1
        
        # Insert project to db
        Project.system.insert_project(id, title, description, create_date, update_date, end_date)
        self._id = id

    # Get methods for id, name, email and password
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
        
    
    

if __name__ == '__main__':
    project = Project('Project 1', 'This is a project')
    print(project.id)

