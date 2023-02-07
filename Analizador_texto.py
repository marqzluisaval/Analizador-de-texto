texto = input(f"Ingresa el texto que quieres analizar: ")
texto = texto.lower()
letra1 = input(f"Ingresa la primera letra: ").lower()
letra2 = input(f"Ingresa la segunda letra: ").lower()
letra3 = input(f"Ingresa la tercera letra: ").lower()
letras = [letra1,letra2,letra3]

print()
veces_letra1 = texto.count(letra1)
veces_letra2 = texto.count(letra2)
veces_letra3 = texto.count(letra3)

print(f"VECES QUE APARECE UNA LETRA EN EL TEXTO")
print(f"La letra {letra1} aparece {veces_letra1} veces dentro del texto")
print(f"La letra {letra2} aparece {veces_letra2} veces dentro del texto")
print(f"La letra {letra3} aparece {veces_letra3} veces dentro del texto")

print()
texto_separado = texto.split(" ")
palabras = len(texto_separado)

print(f"NUMERO DE PALABRAS QUE TIENE TU TEXTO")
print(f"tu texto tiene {palabras} palabras")

print()
primera_letra = texto[0]
ultima_letra = texto[-1]

print(f"PRIMERA Y ULTIMA LETRA DEL TEXTO")
print(f"La primera letra de tu texto es la {primera_letra}")
print(f"La ultima letra de tu texto es la {ultima_letra}")

print()
texto_separado.reverse()
texto_invertido = " ".join(texto_separado)
print(f"TEXTO INVERTIDO")
print(f"Si invertimos las palabras de tu texto, queda asi: '{texto_invertido}'")

print()
buscar_palabra = "python" in texto
dic = {True:'si',False:'no'}
print(f"¿LA PALABRA PYTHON APARECE EN EL TEXTO?")
print(f"La palabra 'python' {dic[buscar_palabra]} se encuentra en el texto")
