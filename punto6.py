futbolistasTup = [(1, "Casillas"), (15, "Ramos"), (3, "Pique"), (5, "Puyol"), (11, "Capdevila"),
(14, "Xabi Alonso"), (16, "Busquets"), (8, "Xavi Hernandez"), (18, "Pedrito"), (6, "Iniesta"), (7, "Villa")]

futbolistasTup.sort(key=lambda futbolista: futbolista[0])
print(futbolistasTup)

# A) al aplicar el método .sort la lista de tuplas se organiza de la siguiente forma:
# [(1, 'Casillas'), (3, 'Pique'), (5, 'Puyol'), (6, 'Iniesta'), (7, 'Villa'), (8, 'Xavi Hernandez'),
#  (11, 'Capdevila'), (14, 'Xabi Alonso'), (15, 'Ramos'), (16, 'Busquets'), (18, 'Pedrito')]

# B) Gracias al parámetro (key=lambda futbolista: futbolista[0]) se especifica que la lista de
# debe ser organizada tomando en cuenta el primer parámetro de cada tupla, en este caso los números
# de los jugadores. Así, es como se organizan de menor a mayor por el parámetro de su número.

## C) No se puede aplicar este parámetro ya que las listas de los puntos 1,3,4 nos son listas de tuplas.

#Lista de tuplas mejores inventos del 2019
print("#################################################################")
inventosTup = [(70, "Oculus Quest"), (90, "Osso VR"), (60, "SmartHalo 2"), (55, "Bose Frames"), 
(47, "WAVE"), (65, "ECONcrete"), (73, "Roli Lumi"), (79, "Kano PC"), (91, "AeroFrams"), (87,"TytoHome")]

inventosTup.sort(key=lambda inventos: inventos[0])
print(inventosTup)