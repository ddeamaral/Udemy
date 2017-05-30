# Date Time examples
r"""
This script creates an empty file
"""
# You import the datetime module
import datetime


#Example datetime functions

#datetime.datetime.now()


#file_name = "sample.txt"
file_name = datetime.datetime.now()


def create_file():
    """ This function creates an empty file"""
    with open(str(file_name.strftime("%Y")), "w") as file:
        file.write("")

create_file()
