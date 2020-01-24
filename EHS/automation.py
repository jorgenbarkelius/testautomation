#!/usr/bin/env python3

import pyjnius


class IExecutionTool(object):
    """public interface IExecutionTool """

    def start_application(self):
        """boolean StartApplication()
        Starts the EHS application
        Returns:
            true on successful start"""
        pass

    def exit_application(self):
        """boolean ExitApplication()
        Terminates the EHS application
        Returns:
            true if application terminated without error"""
        pass

    def wait_for_appliaction_idle(self):
        """void WaitForApplicationIdle()
        Halts execution until EHS application is ready for user input"""
        pass

    def get_all_buttons(self):
        """java.util.Dictionary<java.lang.String,IButton> GetAllButtons()
        Retrieves all possible buttons from the EHS application, regardless if the buttons are visible or not.
        Returns:
            Dictionary of button identifiers and button proxy objects"""
        pass

    def get_all_fields(self):
        """java.util.Dictionary<java.lang.String,IField> GetAllFields()
        Retrieves all possible text fields from the EHS application, regardless if the fields are visible or not.
        Returns:
            Dictionary of field identifiers and field proxy objects"""
        pass


class IElement(object):

    def exist(self, timeout):
        """boolean Exists(int timeout)

        Verifies that a specific UI element is visible in the EHS application
        Parameters:
            timeout - max number of seconds to wait for element to become visible
        Returns:
            true on finding the UI element within given timeout"""
        pass


class IButton(IElement):
    """public interface IButton extends IElement"""

    def click(self):
        """boolean Click()

        Simulates a left mouse click on button UI element
        Returns:
            true on successful click"""
        pass


class IField(IElement):
    """public interface IField extends IElement"""
    def read(self):
        """java.lang.String Read()

        Reads text from a field UI element
        Returns:
            the text contained in the field UI element"""
        pass

    def write(self, text):
        """boolean Write(java.lang.String text)

        Writes text into a field UI element
        Parameters:
            text - the text to enter into the field
        Returns:
            true on successful write"""
        pass
