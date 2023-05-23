import datetime
import sys

sys.path.append('/projects/task_management')
from classes.project import Project
from classes.system import System


class User:

    # insert user to database
    system = System(host = '192.168.1.193', user='postgres', password=1365, port=5432, database='task_management')

    # User projects
    projects = []

    # User constructor
    def __init__(self, name: str, email: str, password: str, create_date = datetime.datetime.today(), update_date = datetime.datetime.today()) -> None:
        self._name = name
        self._email = email
        self._password = password
        self.create_date = create_date
        self.update_date = update_date

        # Grab the last id from the database and add 1 to it
        id = User.system.grab_max_user_id() + 1
        
        # Insert user to db
        User.system.insert_user(id, name, email, password, create_date, update_date) 
        self._id = id       

    # Get methods for id, name, email and password
    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    @property
    def email(self):
        return self._email
    
    @property
    def password(self):
        return self._password
    
    # Set methods for name, email and password
    # Each set method updates the database as well
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            User.system.update_user_attributes(self.id, new_name, self.email, self.password)
            self._name = new_name
        else:
            raise TypeError("Name must be a text!")
        
    @email.setter
    def email(self, new_email):
        if isinstance(new_email, str):
            User.system.update_user_attributes(self.id, self.name, new_email, self.password)
            self._email = new_email
        else:
            raise TypeError("Email must be a text!")
        
    @password.setter
    def password(self, new_password):
        if isinstance(new_password, str):
            User.system.update_user_attributes(self.id, self.name, self.email, new_password)
            self._password = new_password
        else:
            raise TypeError("Password must be a text!")
        

    # Create Project
    def create_project(self, title: str, description: str, create_date = datetime.datetime.today(), update_date = datetime.datetime.today(), end_date = datetime.datetime.today() + datetime.timedelta(days=365)):
        User.projects.append(Project(title=title, description=description, create_date=create_date, update_date=update_date, end_date=end_date))
        return User.projects[-1]

    # Update project
    def update_project_title(self, project_id, new_title, new_description, new_end_date, update_date = datetime.datetime.today()):
        # get a project id and modify it in the database using the System class
        User.system.update_project(project_id, new_title, new_description, new_end_date, update_date)
        



if __name__ == "__main__":
    user = User(name="John", email="doe", password="123")
    print(user.name)

    user.create_project(title="Project 1", description="Description 1")
    user.create_project(title="Project 2", description="Description 2")

    print(user.projects[0].title)
    print(user.projects[1].title)

    print(user.projects[0].id)

    user.update_project_title(1, "New title", "New description", datetime.datetime.today() + datetime.timedelta(days=365))