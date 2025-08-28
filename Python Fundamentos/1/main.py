
import array as arr
from pickle import EMPTY_LIST
import socketserver as sockt

print("Listas\n") 
list = [1, 2, 3, 4, 5, 10, 12, 13 , 14 ,120] 

aux = 0;
for i in range (0,2,1):
    if list[i] > list[i+1]:
        aux = list[i]
        list[i] = list[i+1]
        list[i+1] = aux

print (list) 

for i in range (0,len(list)):
    if list[i] % 2 == 0:
        print("O numero :", list[i], "é par!")
        

print("Outra forma de perocrrer a lista\n")

for num in list:
    if num % 2 == 0:
        print("O numero :", num, "é par!")


print("Strings")
name = "Márcio Antonio Tavares Landim"
name.lower

for n in name:
    if n == "a" or n == "o":
        print ("Foi encontrado:", n)


name = "Márcio Antonio Tavares Landim"
name = name.lower(); #fiz isso porque as strings tais com em java sao imutaveis, ou seja depois de criadas nao podem ser alteradas
count_a = 0;
count_o = 0;
for n in name:
    if n == "a" :
        count_a +=1;
    if n == "o":
        count_o +=1;

print("Quantidade de a encontrada:", count_a)
print("Quantidade de a encontrada:",count_o, "\n")


array = [1,2,3,4,5,6]
ar = arr.array("i",array)

res = arr.array("i", [0]*len(ar))

for i in range(0, len(ar)):
    if ar[i] % 2 != 0:
        res[i] = ar[i]**2
        
print(res)

# A mesma coisa só com uso do append
array = [1,2,3,4,5,6]
ar = arr.array("i",array)

res = arr.array("i")

for i in range(0, len(ar)):
    if ar[i] % 2 != 0:
       res.append(ar[i]**2)

print(res)

#insert
list = []
list.insert(0, 100)
print(list)
print(list[0])


list = [1, 2, 3, 4, 5]
list.insert(2, 100)
print(list)


# opcoes de ordenação
my_list = [10, 1, 8, 3, 5]
 
my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]
 
print(my_list)
 


# etapa 1
beatles = []
print("Etapa 1:", beatles)

# etapa 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Etapa 2:", beatles)


# etapa 3
for i in range(0,2):
    beatles.append(str(input("Adicione os seguintes membros da banda a lista (Stu Sutcliffe e Pete Best): ")))
print("Etapa 3:", beatles)

# etapa 4# remove "Stu Sutcliffe"
del beatles[-1]
del beatles[-1] # porqeu p beatles esta na ultima posicao agora 
print("Etapa 4:", beatles)

# passo 5
beatles.insert(0, "Ringo Starr")
print("Etapa 5:", beatles)



# testando o tamanho da lista

("o fabuloso", len(beatles))




dados = ["Maria", 25, 1.75, True, [10, 20, 30]]
for item in dados:
    print(item, "->", type(item))


lst = [1, [2, 3], 4]
print(lst[1])
print(len(lst))
 

lst = [[1,1], [2, 3], 4, "Landim"]

for i in lst:
    print(i, end =" ")



my_list = [8, 10, 6, 2, 4]  # Lista para ordenar
 
for i in range(len(my_list) - 1):  # precisamos de (5 - 1) comparações
    if my_list[i] > my_list[i + 1]:  # comparar elementos adjacentes
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]  # Se acabarmos aqui, nós temos que trocar os elementos.
        
 
lst = [5, 3, 1, 2, 4]
print(lst)
 
lst.reverse()
print(lst)  # outputs: [4, 2, 1, 3, 5]
 
# Copiar a lista inteira.
list_1 = [1]
list_2 = list_1 [:]
list_1 [0] = 2
print (list_2)

# Copiando parte da lista.
my_list = [10, 8, 6, 4, 2]
new_list = my_list [1: 3]
print(new_list)

# o end não é incluido 

# Copiando a lista toda.
my_list = [10, 8, 6, 4, 2]
new_list = my_list [1: len(my_list)]
print(new_list)

# Copiando a lista toda.
my_list = [10, 8, 6, 4, 2]
new_list = my_list [1: ]
print(new_list)


# Copiando parte da lista.
my_list = [10, 8, 6, 4, 2]
new_list = my_list [1: 3]
print(new_list)
del my_list[:]


EMPTY = "❌"
board = [[EMPTY for i in range(8)] for j in range(8)]
 
for row in board:
    print(" ",row)



#def name (parametros) : funcoes 



def hi_all(name_1, name_2):
    print("Oi,", name_2)
    print("Oi,", name_1)
 
hi_all("Sebastian", "Konrad")
 

def hi_all(name_1, name_2):
    print("Oi,", name_2)
    print("Oi,", name_1)
 
hi_all(name_1="Sebastian",name_2= "Konrad")
 

def subtra(a, b):
    print(a - b)
 
subtra(5, b=2)    # saídas: 3
 
def boring_function():
    return 123
 
x = boring_function()
 
print("A aborrecimento_função retornou seu resultado. Isso é:", x)
 
dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
phone_numbers = {'chefe' : 5551234567, 'Suzy' : 22657854310}
empty_dictionary = {}

# Imprima os valores aqui.
print(dictionary["gato"])
print(phone_numbers['Suzy'])



dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
words = ['gato', 'lion', 'cavalo']
 
for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "não está no dicionário")
 
# Exemplo 1:
dictionary = {
              "gato": "chat",
              "cachorro": "chien",
              "cavalo": "cheval"
}
# Exemplo 2:
phone_numbers = {'chefe': 5551234567,
              'Suzy': 22657854310
}
 

my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elem in my_tuple:
 print(elem)



my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)

 
var = 123
 
t1 = (1, )
t2 = (2, )
t3 = (3, var)
 
t1, t2, t3 = t2, t3, t1
 
print(t1, t2, t3)
 
dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
 
for key in dictionary.keys():
    print(key, "->", dictionary[key])
 


dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
 
for english, french in dictionary.items():
    print(english, "->", french)
 




dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
 
dictionary['gato'] = 'minou'
print(dictionary)




 
#for key in sorted(dictionary.keys()):
dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
 
for french in dictionary.values():
    print(french)
 




dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
 
del dictionary['cachorro']
print(dictionary)
 




#popitem() remove o ultimo item do diciioanrio 
dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
 
dictionary.popitem()
print(dictionary)    # saídas: {'gato': 'chat', 'cachorro': 'chien'}
 
 




school_class = {}

while True:
 name = input("Digite o nome do aluno: ")
 if name == '':
  break
 
 score = int(input("Insira a pontuação do aluno (0-10): "))
 if score not in range(0, 11):
  break
 
 if name in school_class:
  school_class[name] += (score,)
 else:
  school_class[name] = (score,)
 
for name in sorted(school_class.keys()):
 adding = 0
 counter = 0
 for score in school_class[name]:
  adding += score
  counter += 1
  print(name, ":", adding / counter)


pol_eng_dictionary = {
    "kwiat": "flor",
    "woda": "água",
    "gleba": "solo"
    }
 
item_1 = pol_eng_dictionary["gleba"]    # ex. 1
print(item_1)    # saídas: solo
 
item_2 = pol_eng_dictionary.get("woda")    # ex. 2
print(item_2)    # saídas: água
 


pol_eng_dictionary = {"kwiat": "flor"}
 
pol_eng_dictionary.update({"gleba": "solo"})
print(pol_eng_dictionary)    # saídas: {'kwiat': 'flor', 'gleba': 'solo'}
 
pol_eng_dictionary.popitem()
print(pol_eng_dictionary)    # saídas: {'kwiat': 'flor'}
 
pol_eng_dictionary = {
    "zamek": "castelo",
    "woda": "água",
    "gleba": "solo"
    }
 
for item in pol_eng_dictionary:
    print(item)
 
#          woda
#          gleba
 



pol_eng_dictionary = {
    "zamek": "castelo",
    "woda": "água",
    "gleba": "solo"
    }
 
copy_dictionary = pol_eng_dictionary.copy()
 


d1 = {'Adão Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

for item in (d1, d2):
    d3.update(item)

print(d3)



tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2)

print(duplicates)    # saídas: 4


colors = (("green", "#008000"), ("blue", "#0000FF"))

colors_dictionary = dict(colors)
print(colors_dictionary)

colors = {
    "branco": (255, 255, 255),
    "cinza": (128, 128, 128),
    "vermelho": (255, 0, 0),
    "verde": (0, 128, 0)
    }
 
for col, rgb in colors.items():
    print(col, ":", rgb)
 


while True:
    try:
        number = int(input("Digite um número int: "))
        print(5/number)
        break
    except ValueError:
        print("Valor errado.")
    except ZeroDivisionError:
        print("Desculpe. Não consigo dividir por zero.")
    except:
        print("eu não sei o que fazer...")
 


texto = "123456789"
print(texto[::2])          # "13579"  (saltando de 2 em 2)
print(texto[slice(0, 9, 2)])  # "13579" (mesmo resultado)
