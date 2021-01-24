"""
file: html_builder.py
description: Understanding dataclass structures, queues, and HTML/CSS code within Python
language: Python3
author: Savannah Alfaro

The intended use of this program is to create a program that processes two types of input from the user
(wizard_mode and web_mode) and outputs an html file to create a website. The purpose of this program is to
further develop an understanding of how queue structures work within Python as well as understanding how to
format a HTML/CSS file.
"""
# Import & Set Up Workspace
import sys
import web_mode as web
import wizard_mode as wiz


# Define Functions
def main():
    """
    Calls website_mode if the number of argument values is greater than 2. Calls wizard_mode
    if there are no argument values inputted from the user.
    :return: None
    """
    if len(sys.argv) > 1:
        web.web_mode()
    else:
        wiz.wizard_mode()


# Call & Test Functions
if __name__ == "__main__":
    main()
