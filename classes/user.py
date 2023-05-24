import datetime
import sys

sys.path.append('/projects/task_management')
from classes.project import Project
from classes.system import System


class User:

    # insert user to database
    system = System(host = '192.168.1.193', user='postgres', password=1365, port=5432, database='task_management')

    # User constructor
    def __init__(self, name: str, email: str, password: str, create_date = datetime.datetime.today(), update_date = datetime.datetime.today()) -> None:
        '''
        Constructor for User class
        Args:
            name: user name
            email: user email
            password: user password
            create_date: user create date (default: today)
            update_date: user update date (default: today)
        Returns:
            None
        Notes:
            This constructor will insert the user to the database
        '''
        self._name = name
        self._email = email
        self._password = password
        self.create_date = create_date
        self.update_date = update_date

        # Grab the last id from the database and add 1 to it
        id = User.system.grab_max_object_id(object='user') + 1
        
        # Insert user to db
        User.system.insert_user(id, name, email, password, create_date, update_date) 
        self._id = id   

        # Create an empty list for projects
        self.projects = []


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
    def create_project(self, user_id, title: str, description: str, create_date = datetime.datetime.today(), update_date = datetime.datetime.today(), end_date = datetime.datetime.today() + datetime.timedelta(days=365)):
        '''
        Create a new project for the user
        Args:
            title: project title
            description: project description
            create_date: project create date (default: today)
            update_date: project update date (default: today)
            end_date: project end date (default: today + 365 days)
        Returns:
            project_id
        Notes:
            - This method will insert the project to the database
            - This method will append the project to the User.projects list
        '''
        self.projects.append(Project(user_id = self.id, title=title, description=description, create_date=create_date, update_date=update_date, end_date=end_date))
        return self.projects[-1]
    
    # delete project
    def delete_project(self, project_title):
        '''
        Delete a project from the user
        Args:
            project_title: project title
        Returns:
            None
        Notes:
            - This method will delete the project from the database
            - This method will delete the project from the User.projects list
        '''
        for project in self.projects:
            if project.title == project_title:
                self.projects.remove(project)
                User.system.delete_project(project.id)
                break

    
    
        



if __name__ == "__main__":
    user = User(name="John", email="doe", password="123")
    print(user.name)

    user.create_project(title="Project 1", description="Description 1")
    user.create_project(title="Project 2", description="Description 2")

    print(user.projects[0].title)
    print(user.projects[1].title)

    print(user.projects[0].id)

    user.update_project_title(1, "New title", "New description", datetime.datetime.today() + datetime.timedelta(days=365))