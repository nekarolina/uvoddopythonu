# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Hz4fSWHRw1NLFLUeG_H_ReFZ608FRNFT
"""

1256983 % 28

(12**52 % 15 < 8) or (3**5 > 100)

5*3**3 != 900/ 75

'[[]]' [0:2:] + 'PYTHON' + '[[]]' [2:4:]

'Python'[4:6:] * 4

'Perl' [2:3] * 6

"python".upper() [0:3] + "python" [3:7]

'Python'[0:1:] * len('python')

print(7+3*2)
 print('7' + str(3*2))
 print('7' + '3*2')
 print('7' + 3*2)
#last command is causing error because it tries to add integer with string

hobby = 'painting'

'Hello, my hobby is {0}'.format(hobby)

'2018-11-01'.format

myhobbies = []
myhobbies.insert (0,"photography")
myhobbies.append ("painting")
myhobbies.append ("videogames")
myhobbies.insert (3,"exercising")
print (myhobbies[0]) 
print (myhobbies[3])
del myhobbies[3]

cities = ['Prague', 'Brno', 'Ostrava', 'Plzen', 'Liberec',
'Olomouc', 'Usti nad Labem', 'Hradec Kralove', 'Ceske Budejovice', 'Pardubice']
cities.sort()
print(cities)

cities = ['Prague', 'Brno', 'Ostrava', 'Plzen', 'Liberec',
'Olomouc', 'Usti nad Labem', 'Hradec Kralove', 'Ceske Budejovice', 'Pardubice']
s = "*"
s.join(cities)

alphabet = 'abcdefghijklmnopqrstuvwxyz'
zen = """
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
set(alphabet) - set(zen)

d = {'payton':'An interpreted, object-oriented programming language'}
d['payton']
d['python'] = d['payton']
#d.pop('payton')
del d['payton']
d

info = {'name':'Anna', 'surname': 'Prijmeni'}
info['phone'] = 728856347
info

info = {('Name', 'Surname'):('John', 'Doe')}
info.values()
["_".join(a) for a in info.values()]
#"_".join(['John','Doe'])