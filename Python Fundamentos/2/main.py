# Introdução aos modulos 
from math import pi


import math
def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


pi = 3.14
print(sin(pi/2))
print(math.sin(math.pi/2))



from math import pi
print(math.e)


from math import sin, pi
print(sin(pi/2))



from math import sin, pi
print(sin(pi / 2))
pi = 3.14





def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None
    
print(sin(pi / 2))



#Uma forma mais agressiva que seleciona 
# a lista de entidades em vez de um por um 
from math import *




#Aliasing - Observação: após a execução bem-sucedida de
#uma importação com alias, o nome do módulo original se torna 
#inacessível e não deve ser usado.
import math as m
print(m.sin(m.pi/2))



#Formas de fazer importação
#import mod1
#mport mod2, mod3, mod4


#mport my_module  
#esult = my_module.my_function(my_module.my_data)


#Como ver nomes dentro de um modulo (funcoes, variaveis, classes, objetos,metodos)
dir(math)

import math 
for name in dir(math):
  print(name, end=" ")

  



from math import pi, radians, degrees, sin, cos, tan, asin

ad = 90
ar = radians(ad)
ad = degrees(ar)

print(ad == 90.)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar) 
print(pow(2,2))




from math import e, exp, log
print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0))



from platform import platform
print(platform())
print(platform(1))
print(platform(0, 1))



from platform import machine
print(machine())




from platform import processor
print(processor())




from platform import system
print(system())

print(dir(platform))




import platform, inspect
funcoes = inspect.getmembers(platform, inspect.isfunction)
for nome, _ in funcoes:
    print(nome)





import pygame

run = True
width = 400
height = 100
pygame.init()
screen = pygame.display.set_mode((width, height))
font = pygame.font.SysFont(None, 48)
text = font.render("Welcome to pygame", True, (255, 255, 255))
screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))
pygame.display.flip()
while run:
  for event in pygame.event.get():
   if event.type == pygame.QUIT\
   or event.type == pygame.MOUSEBUTTONUP\
   or event.type == pygame.KEYUP:
    run = False


#pip install name_packe
#pip help 
#pip  install -U 
#pip list
#pip show packeg_name
#pip uninstall nome_pacote



from random import randint
  
for i in range(2):
   print(randint(1, 2), end='')
    



#Metódos usados para strings


# Demonstrando o método capitalize():
print('aBcD'.capitalize())
print("Alpha".capitalize())
print('ALPHA'.capitalize())
print(' Alpha'.capitalize())
print('123'.capitalize())
print("αβγδ".capitalize())
    

# Demonstrando o método center():
print('[' + 'alpha'.center(10) + ']')
print('[' + 'Beta'.center(2) + ']')
print('[' + 'Beta'.center(4) + ']')
print('[' + 'Beta'.center(6) + ']')
print('[' + 'gamma'.center(20, '*') + ']')


# Demonstrando o método endswith():
if "epsilon".endswith("on"):
    print("yes")
else:
    print("no")


t = "zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("et"))
print(t.endswith("eta"))


# Demonstrando o método find():
print("Eta".find("ta"))
print("Eta".find("mma"))



t = 'theta'
print(t.find('eta'))
print(t.find('et'))
print(t.find('the'))
print(t.find('ha'))

print('kappa'.find('a', 2))


the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = the_text.find('the')
while fnd != -1:
    print(fnd)
    fnd = the_text.find('the', fnd + 1)
    #fnd + 1


#O segundo argumento sera o indice de incio da procura e 
# o terceiro será o final que nao será incluido na procura
print('kappa'.find('a', 1, 4))
print('kappa'.find('a', 2, 4))



# Demonstrando o método isalnum():
#O método sem parâmetros chamado isalnum() verifica se a string 
# contém apenas dígitos ou caracteres alfabéticos
# (letras) e retorna True ou False de acordo com o resultado.

print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())


t = 'Six lambdas'
print(t.isalnum())

t = '&Alpha;&beta;&Gamma;&delta;'
print(t.isalnum())

t = '20E1'
print(t.isalnum())





# Exemplo 1: Demonstrando o método isapha():
print("Moooo".isalpha())
print('Mu40'.isalpha())
    

# Exemplo 2: Demonstrando o método isdigit():
print('2018'.isdigit())
print("Year2019".isdigit())


# Exemplo: Demonstrando o método islower():
print("Moooo".islower())
print('moooo'.islower())
    

# Exemplo: Demonstrando o método isspace():
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())


# Exemplo: Demonstrando o método isupper():
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())
    


# Demonstrando o método join():

#O método join() é bastante complicado, então iremos guiá-lo a cada passo:

#como o nome sugere, o método executa uma junção, ele espera um argumento como uma lista; 
# deve-se assegurar
# que todos os elementos
# da lista sejam strings, caso contrário o método irá causar uma exceção TypeError ;
#todos os elementos da lista serão unidos em uma string, mas...
#...a string a partir da qual o método foi chamado será usada como separador, colocado entre as strings;
#a string criada será retornada como resultado.
#print(",".join(["omicron", "pi", "rho"]))




# Demonstrando o método lstrip():
#Funciona como trim() mas so para espços iniciais
print("[" + " tau ".lstrip() + "]")
    
# esta versão com argumentos remove o caractere passado como argumento
# Atenção : Os caracteres tem que ser iniciais
print("www.cisco.com".lstrip("w."))



# Demonstrando o método replace():
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))


# Demonstrando o método rfind(): faz a procura a partir do fim (right -r)
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))
    


# Demonstrando o método rstrip(): funciona com o strip mas retiraos espços do fim para o inicio 
print("[" + " upsilon ".rstrip() + "]")
print("cisco.com".rstrip(".com"))
    
# Demonstrando o método split():
print("phi       chi\npsi".split())
print("phiuf f8f       chi\npsi".split())

# Demonstrando o método startswith():
print("omega".startswith("meg"))
print("omega".startswith("om"))
print()


# Demonstrando o método strip(): o famoso trim() do python (retira os espaços iniciais e finais)
#rstrip() -+lstrip()
print("[" + "   aleph   ".strip() + "]")


# Demonstrando o método swapcase():
#O método swapcase() cria uma nova string ao inverter as letras maiúsculas 
# para minúsculas e vice-versa.
print("I know that I know nothing.".swapcase())
print()


# Demonstrando o método title():
#O método title() realiza uma função ligeiramente similar, ele transforma a primeira letra de cada palavra em 
# maiúscula e todas as outras letras em minúsculas.
print("I know that I know nothing. Part 1.".title())
print()


#1. Alguns dos métodos oferecidos por strings são:
#capitalize() – altera todas as letras da string para maiúsculas;
#center() – centraliza a string no campo de um comprimento conhecido;
#count() – conta as ocorrências de um determinado caractere; # type: ignore
#join() – une todos os itens de uma tupla/lista em uma string; # type: ignore
#lower() – converte todas as letras da string para minúsculas;
#lstrip() – remove os caracteres em branco do início da string;
#replace() – substitui uma determinada substring com outra;
#rfind() – encontra uma substring a partir do fim da string;
#rstrip() – remove os espaços em branco do final da string;
#split() – divide a string em uma substring usando um delimitador específico;
#strip() – remove os espaços em branco iniciais e finais;
#swapcase() – transforma as letras maiúsculas em minúsculas e vice-versa
#title() – transforma a primeira letra de cada palavra em maiúscula;
#upper() – converte todas as letras de uma string em maiúsculas.

#2. O conteúdo da string pode ser determinado por meio dos métodos a seguir (todos retornam valores Booleanos):

#endswith() – a string termina com uma determinada substring?
#isalnum() – a string é composta apenas por letras e dígitos?
#isalpha() – a string é composta apenas por letras?
#islower() – a string é composta somente por letras minúsculas?
#isspace() – a string é composta apenas por espaços em branco?
#isupper() – a string é composta apenas por letras maiúsculas?
#startswith() – a string começa com uma substring específica?




def mysplit(strng):
    i = 0
    word =""
    palavras_list = []
    
 
    while i < len(strng):
        if strng[i] !=" " :
            word += strng[i]
            
        else:
            palavras_list.append(word)
            word =""
        
        i+=1
    
    return palavras_list
            
          



print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))



# Demonstrando o método sort():
second_greek = ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)

second_greek.sort()
print(second_greek)
   


# Demonstrando a função sorted():
first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)

print(first_greek)
print(first_greek_2)

print()




itg = 13
flt = 1.3
si = str(itg)
sf = str(flt)

print(si + ' ' + sf)
    




digitos = {
    "0": ["###",
          "# #",
          "# #",
          "# #",
          "###"],
    "1": ["  #",
          "  #",
          "  #",
          "  #",
          "  #"],
    "2": ["###",
          "  #",
          "###",
          "#  ",
          "###"],
    "3": ["###",
          "  #",
          "###",
          "  #",
          "###"],
    "4": ["# #",
          "# #",
          "###",
          "  #",
          "  #"],
    "5": ["###",
          "#  ",
          "###",
          "  #",
          "###"],
    "6": ["###",
          "#  ",
          "###",
          "# #",
          "###"],
    "7": ["###",
          "  #",
          "  #",
          "  #",
          "  #"],
    "8": ["###",
          "# #",
          "###",
          "# #",
          "###"],
    "9": ["###",
          "# #",
          "###",
          "  #",
          "###"]
}

# O 5 é o número de linhas 
def desenhar_numero(numero):
    linhas = [""] * 5  
    for digito in numero:
        if digito.isdigit():  
            padrao = digitos[digito]

        else:  
            padrao = ["   "] * 5
       
        for i in range(5):
            linhas[i] += padrao[i] + " "
    
    return "\n".join(linhas)



n = input("Digite um número: ")
print(desenhar_numero(n))





# Cifra de César.
text = input("Enter your message: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)
    



# Cifra de César - descriptografando uma mensagem.
cipher = input('Enter your cryptogram: ')
text = ''
for char in cipher:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)

print(text)




# Processador de números.

line = input("Enter a line of numbers - separate them with spaces: ")
strings = line.split()
total = 0
try:
    for substr in strings:
        total += float(substr)
    print("The total is:", total)
except:
    print(substr, "is not a number.")
    



# Validador IBAN.

iban = input("Enter IBAN, please: ")
iban = iban.replace(' ','')

if not iban.isalnum():
    print("You have entered invalid characters.")
elif len(iban) < 15:
    print("IBAN entered is too short.")
elif len(iban) > 31:
    print("IBAN entered is too long.")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ''
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A'))
    iban = int(iban2)
    if iban % 97 == 1:
        print("IBAN entered is valid.")
    else:
        print("IBAN entered is invalid.")
    

    
def eh_palindromo(texto):
    # remover espaços e colocar tudo em minúsculas
    texto = texto.lower()
   
    return texto == texto[::-1]


print(eh_palindromo("arara"))          
print(eh_palindromo("radar"))          
print(eh_palindromo("python"))         
print(eh_palindromo("Socorram me subi no onibus em Marrocos"))  



def eh_anagrama(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    return sorted(s1) == sorted(s2)


print(eh_anagrama("amor", "roma"))       
print(eh_anagrama("arco", "caro"))       
print(eh_anagrama("python", "typhon"))   
print(eh_anagrama("python", "java"))     


# Este código não pode ser finalizado
# pressionando Ctrl-C.

from time import sleep

seconds = 0

while True:
    try:
        print(seconds)
        seconds += 1
        sleep(1)
    except KeyboardInterrupt:
        print("Não faça isso!")

