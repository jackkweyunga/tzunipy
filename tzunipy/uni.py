
'''
@author jack kweyunga

This file carries code to be used to load universities data from the json files.

Objects of type University, College and Course are used to access the actual data. 

'''

import json
import os
from pathlib import Path

# resolved base dir 
base_dir = Path(__file__).resolve().parent

# path to the uni folder
uni_dir = os.path.join(base_dir, 'uni')

class Uni:
    """
    A class to load the list of universities
    :: Uni().university() -> returns the list not objects
    """

    def university(self):
        with open(os.path.join(uni_dir, 'universities.json'), 'r') as f:
            return json.load(f)


class College():
    """
    College class for constructing college objects

    properties:: name, courses, university

    """
    
    def __init__(self, university, name, courses=[]) -> None:
        self.name = name
        self.courses = courses
        self.university = university

        if self.load_colleges() is not None:
            for i in self.load_colleges():
                if (self.name == i['name']) and (i['types'] != []):
                    self.courses = [k for k in i['types']]

    def load_colleges(self):
        fname = os.path.join(uni_dir, f'{self.university.name}.json')
        # print(fname)
        try:
            with open(fname, 'r') as f:
                return json.load(f)
        except:
            return None

    def __repr__(self) -> str:
        return f"{self.name}"


class University():

    """
    University class for constructing University objects

    properties:: name, colleges, get_colleges
    """

    def __init__(self, name, colleges=[]):
        self.name = name
        self.colleges = colleges

        if self.load_colleges() is not None:
            self.colleges = [College(self, i['name']) for i in self.load_colleges()]

    def load_colleges(self):
        fname = os.path.join(uni_dir, f'{self.name}.json')
        # print(fname)
        try:
            with open(fname, 'r') as f:
                return json.load(f)
        except:
            return None

    def __repr__(self) -> str:
        return f"{self.name}"

    @property
    def get_colleges(self):
        if self.colleges == []:
            return "colleges not available for this university."
        return self.colleges

    






