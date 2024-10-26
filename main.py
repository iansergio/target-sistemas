# 1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
def verificaEmFibonnaci(n):
    primeiroValor = 0
    segundoValor = 1
    # print(primeiroValor)
    while segundoValor < n:
        # print(segundoValor)
        # Atribuindo a um valor auxiliar a soma dos dois valores
        aux = primeiroValor + segundoValor
        # Atribuindo o valor do segundo valor ao primeiro e o do valor auxiliar ao segundo 
        primeiroValor = segundoValor
        segundoValor = aux
        if segundoValor == n:
            print(f"O número {n} faz parte da sequência de Fibonacci.")
        elif segundoValor > n and segundoValor != n:
            print(f"O número {n} não pertence à sequência de Fibonacci.")    
print("1) Fibonacci")
verificaEmFibonnaci(7778742049)

# 2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.
def verificaString(letra, texto):
    return "Sim" if letra.lower() in texto.lower() else "Não"

print("2 Verificar existência da letra 'a')")
print(verificaString("O", "Sou uma string a ser verificada"))

# 3) Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1; enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);
print("3) Trecho de código")
# Resposta
print("O valor será 77") 