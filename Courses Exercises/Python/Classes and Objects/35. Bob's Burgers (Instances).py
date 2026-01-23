class Restaurant:
    name = ""
    category = ""
    rating = 0.0
    delivery = False

bobs_burgers = Restaurant()
bobs_burgers.name =  "Bob\'s Burgers"
bobs_burgers.category = "American Diner"
bobs_burgers.rating = 4.7
bobs_burgers.delivery = False

La_Tratoria = Restaurant()
La_Tratoria.name = "La Tratoria"
La_Tratoria.category = "Italian food"
La_Tratoria.rating = 4.9
La_Tratoria.delivery = False

Nona_lola = Restaurant()
Nona_lola.name = "La Nona Lola"
Nona_lola.category = "Pizzeria"
Nona_lola.rating = 4.0
Nona_lola.delivery = False

print(vars(bobs_burgers))
print(vars(La_Tratoria))
print(vars(Nona_lola))