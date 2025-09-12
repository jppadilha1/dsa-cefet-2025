# Dado uma string de expressão x. 
# Verifique se os pares e a ordem de ‘{’ , ‘}’ , ‘(’ , ‘)’ , ‘[’ , ‘]’ estão corretos.
# Por exemplo, a função deve retornar:
# ‘True’ para exp = “[()]{}{()()}” e 
# ‘False’ para exp = “[(])”.

from stack import Stack

def is_balanced(expression):
    """
    Verifica se a expressão possui parênteses balanceados.
    Usa a pilha implementada em stack.py.
    """
    pilha = Stack()

    map = {"]":"[", ")":"(", "}":"{"}

    for char in expression:
        if char == "[" or char == "(" or char == "{":
            pilha.push(char)
        else:
            if pilha.is_empty():
                return False
            elif map.get(char) != None and map.get(char) != pilha.peek():
                return False
            elif map.get(char) == pilha.peek():
                pilha.pop()

    if pilha.is_empty():
        return True
    else:
        return False
    


# Teste
print(is_balanced("[{}(2+2)]{}")) #Esperado True
print(is_balanced("[{}(2+2))]{}")) #Esperado False
print(is_balanced("[{}])")) #Esperado False
print(is_balanced("[{}]")) #True
print(is_balanced("[{]}")) #False