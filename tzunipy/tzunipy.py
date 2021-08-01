from uni import *


"""
method-carrier/main class
"""

class TzUniPy():

    """
    method which returns all universities in Tanzania
    """
    def all_universities():
        # print(university)
        return Uni().university()


    """
    method which returns objects of all universities in a given region
    """
    def get_univeristy(region):
        uni_in_region = []
        for x in Uni().university():
            if region in x:
                uni_in_region.append(University(x))

        # print(uni_in_region)
        return uni_in_region



if __name__ == '__main__':
    TzUniPy()

