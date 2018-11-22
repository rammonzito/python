Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> for x in range(0,5):
	print("Valor de x é:", x)

	
Valor de x é: 0
Valor de x é: 1
Valor de x é: 2
Valor de x é: 3
Valor de x é: 4
>>> nome="Ramon"
>>> for x in nome:
	print(x)

	
R
a
m
o
n
>>> listaNomes=["Ramon","Thainá","Thaisa","Amanda"]
>>> for valor in listaNome:
	print(valor)

	
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    for valor in listaNome:
NameError: name 'listaNome' is not defined
>>> for valor in listaNomes:
	print(valor)

	
Ramon
Thainá
Thaisa
Amanda
>>> 
