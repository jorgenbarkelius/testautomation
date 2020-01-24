#!/usr/bin/env python3

import pytest
from EHS.automation import IElement, IButton, IField, IExecutionTool
#from seleniumbase import BaseCase


class TestEHSAutomation(object):

    def __init__(self):
        self.interface_exec_tool = IExecutionTool()
        self.interface_field = IField()
        self.interface_button = IButton()

    def test_list_all_products(self):
        """Story 1: As an administrator of the EHS system I want to be able to see all the available products so that
            I can make faster decisions."""

        self.interface_exec_tool.start_application()
        self.interface_exec_tool.wait_for_appliaction_idle()

        field_dict = {}
        button_dict = {}
        field_dict = self.interface_exec_tool.get_all_fields()
        button_dict = self.interface_exec_tool.get_all_buttons()

        for field in button_dict.keys():
            if self.interface_field.read() == 'List all items':
                if self.interface_button.click():
                    num = 0
                    for element in field_dict.keys():
                        num += 1
                        assert field_dict.keys() == f'EHS item {num}'

    def test_detailed_product_info(self):
        """Story 2: As an administrator of the EHS system I want to se detailed information about a specific
        product so that I know that the system is up to date."""
        pass



    def test_search_products(self):
        """Story 3: As an administrator of the EHS system I want to be able to search for a specific product so that
        I can get faster access to its product details."""
        pass
