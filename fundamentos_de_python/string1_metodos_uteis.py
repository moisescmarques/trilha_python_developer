curso = "pYthON"

print(curso.upper()) #converte todas as letras para maiuscula. Ex: "PYTHON"
print(curso.lower()) #converte todas as letras para minuscula. Ex: "python"
print(curso.title()) #converte todas a letras para minuculo com execeção da primeira letra. Ex: "Python"

curso1 = "      Hello World!  "

print(curso1.strip()) #Remove todos os espaçoes em branco na esquerda e na direita. Ex: "Python"
print(curso1.lstrip()) #Remove todos os espaçoes em branco na esquerda. Ex: "Python  "
print(curso1.rstrip()) #Remove todos os espaçoes em branco na direita. Ex: "      Python"

curso2 = "Python"

print(curso2.center(10, "#")) #adiciona caracteres na esquerda e direita mantendo a string alvo no centro até dar a quantidade de caracteres do 1 parametro.
print(".".join(curso2)) #Ex: "P.y.t.h.o.n"


