"""
comentário...
fiz um pip install simplekml e no pypi pra fazer rodar o import
"""
import simplekml
longitude=input("Enter longitude: ")
latitude=input("Enter longitude: ")
kml=simplekml.Kml()
kml.newpoint(name="Sample",coords=[(longitude,latitude)])
kml.save("C:\\Cursos\\Python\\Python_udemy\\Python_for_begginers\\Points.kml")