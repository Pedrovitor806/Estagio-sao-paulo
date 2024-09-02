def inverter_string(s):
    string_invertida = ""
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]
    return string_invertida

# Você pode usar esta linha para definir a string diretamente no código:
# string = "Exemplo de string"

# Ou pedir para o usuário inserir a string:
string = input("Informe uma string: ")

# Invertendo a string
resultado = inverter_string(string)

print(f"String invertida: {resultado}")