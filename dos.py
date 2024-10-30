palabras= "bienvenidos al curso bienvenidos al curso bienvenidos al     curso "
try:
  palabras_sep =palabras.split(" ")
  print(palabras_sep)
except NameError:
  print("no hay palabras")
  