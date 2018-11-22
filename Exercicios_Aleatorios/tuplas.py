Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> tuplas=("Ramon","python","udemy")
>>> tuplas
('Ramon', 'python', 'udemy')
>>> print(tuplas)
('Ramon', 'python', 'udemy')
>>> tuplas[0:1]
('Ramon',)
>>> tuplas[0,2]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    tuplas[0,2]
TypeError: tuple indices must be integers or slices, not tuple
>>> tuplas[0:2]
('Ramon', 'python')
>>> len(tuplas)
3
>>> tuplas*5
('Ramon', 'python', 'udemy', 'Ramon', 'python', 'udemy', 'Ramon', 'python', 'udemy', 'Ramon', 'python', 'udemy', 'Ramon', 'python', 'udemy')
>>> "Ramon" in tuplas
True
>>> "Thaina" in tuplas
False
>>> lista=[1,2,6]
>>> lista
[1, 2, 6]
>>> tuplas2=tuple(lista)
>>> tuplas2
(1, 2, 6)
>>> 
