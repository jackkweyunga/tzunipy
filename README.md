# Tzunipy

- A python package that gives information about different Universities in Tanzania.
- [tzunipy](https://pypi.org/project/tzunipy/0.3/) made by [maen08](https://github.com/maen08)



[![Made in Tanzania](https://img.shields.io/badge/made%20in-tanzania-008751.svg?style=flat-square)](https://github.com/Tanzania-Developers-Community/made-in-tanzania)
[![Generic badge](https://img.shields.io/badge/pip-python-<COLOR>.svg)](https://shields.io/)

---

### Install
Run this command to install the current stable version:

```sh
pip install tzunipy

# or using pip3

pip3 install tzunipy

```


---

### Features

- Show all universities in Tanzania
- Show all universities per region given
- Show colleges per university
- Show programms pursued per college
- Show the program-duration (if necessary)

---

### Usage

```sh
>>> from tzunipy.tzunipy import TzUniPy


# get all universities

>>> TzUniPy.all_universities()
[
   'University of Dar es Salaam UDSM (Dar es Salaam)', 
   'Sokoine University of Agriculture SUA (Morogoro)', 
   'Open University of Tanzania OUT (Dar es Salaam)', 
    ...
    ...
 
   
]


# get universities from a given region
>>> TzUniPy.get_univeristy('Dodoma')

["University of Dodoma UDOM (Dodoma)",
      "St. John's University of Tanzania SJUT (Dodoma)"]
      
>>> # to get colleges of a university
>>> single = TzUniPy.get_univeristy('Dar')[0] # returns 1 universtity in Dar
>>> print(single.name)
'University of Dar es Salaam UDSM (Dar es Salaam)'
>>> print(single.colleges)
[
   College of Social Science (CoSS), 
   College of Information and Communication Technologies (CoICT), 
   College of Engineering and Technology (CoET), 
   College of Natural and Applied Science (CoNAS),
   ...
   ...
   
   ]


```

### Contribution
- Whoever wish to contribute in this project (direct or indirect), please read 
the file [update.md](https://github.com/maen08/tzunipy/blob/master/update.md)
