from abc import ABC, abstractmethod

from util.persistable import Persistable


class BaseProgram(Persistable, ABC):

    def __init__(self, project_name, project_path, persist_path, desktop):
        """ Initializes a program.

        Args:
            project_name::str
                The name of the project
            project_path::str
                The path to the base directory of the project
            persist_path::str
                The path to the directory wherein a program will
                be persisted
            desktop::BaseDesktop
                A desktop object that supports virtual desktop ops
        """
        self.project_name = project_name
        self.project_path = project_path
        self.persist_path = persist_path
        self.desktop = desktop

    @abstractmethod
    def setup(self):
        """ Sets up the program for first use in this project.
        """
        pass

    @abstractmethod
    def start(self):
        """ Starts a brand new instance of this program
        """
        pass

    @abstractmethod
    def restart(self):
        """ Restarts the program from where it was left
        """
        pass

    @abstractmethod
    def close(self):
        """ Closes the program, persisting the state
        """
        pass