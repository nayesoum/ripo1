# mon commentaire

ma_variable ='je suis'
print(ma_variable)

#print cest pour afficher mon résultat dans ma console

MON_NUMERO_CARTE = 1111111111

#la j'ai déclaré ma constante si on la voix
# comme ca on sait qu'elle a deja déclarer une contante'

is_connected = False
for i in range(11):
    print(i)

some_latters ="je m'appelle sacha"

a_figure = 5

print(a_figure)

all_countries = ["france","Mali"]
"""ceci est une list
pas de virgule pour le dernier élément"""

print(all_countries)

all_figure = [1, 2, 3, 4, 5]

print(all_figure)

many_thing = [1, 'hello', True, False]#on peut mettre plusieur element different
#dans un tableau

print(many_thing[-1])#ici ca prend que le dernier element donc false
#
print(many_thing[:-1])#ici ca affichera tous sauf le dernier avec :

print(many_thing[0:3])# ici je vais afficher seulement les 3 premier élément
#sans le 3 eme inclu

first_tuple = ('axa','air france' 'adidas',)

print(first_tuple[0])

print(first_tuple[-1])

many_thing = [ ] #ici ca va clear mon tableau many_things

print(many_thing) # ici mon tableau sera vide

# un tuple est comme une constante on ne peut pas le changer 
#on l'utilise si au cas ou on ne veux pas que quelquun change 

# comment differencier un tuple d'une list
#le tuple s'ecrit avec des ()parentese et une list avec []

#le = va ecraser ma valeur précedente si au cas ou je veux réafecter une valeur

for i in 'hello':
    print(i) #ici jai fait une boucle sur la chaine de caractere elle va 
    #me mettre tous les 

# for ca veut dire une boucle
#in ca veut dire dans
# 'hello' dans quoi hello
for lala in 'hello':
    print(lala) #ceci est une contraction de ce qui est en dessous

print('hello'[0]) #ici ca va m'afficher le h
print('hello'[1]) #ici ca va m'afficher le e
print('hello'[2]) #ici ca va m'afficher le l
print('hello'[3]) #ici ca va m'afficher le l
print('hello'[4]) #ici ca va m'afficher le o

my_firstname= 'sacha'

my_firstname == "sacha"
your_firstname= "nayé"

if my_firstname== your_firstname:
    print('oui')

else:
    print('non')

my_age=70

if my_age >= 70:
    print('trop vieux')
elif my_age < 70 and my_age >=40:
    print('ca se rapproche')

else:
    print('la jeunesse!')    


def message_aleatoire ():
    messages = [
        'salut, comment ca va',
        'bienvenue sur notre site!',
        'aujourdhui est une belle journée qui commence'
    ]


    print(messages[randint (0,2)])

    def get_net_value (raw_price):
        return raw_price * 1.2

            print(get_net_value(50))


def get_net_value (raw_price):

    net_price = 0

    if type == 'food':
        net_price = raw_price * 1.05
    elif type == 'service':
        net_price = raw_price * 1.20

    return net_price

            print(get_net_value(50))








#ici cest les exercices
SON_NOM = '50 cent'
print(SON_NOM)
SON_AGE = 46

print(SON_AGE)

