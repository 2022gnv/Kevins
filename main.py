print("hola,bienvenido a mi trivia sobre los simpsom\n")

edad = input("ingresa tu edad:")

print("\n tienes", edad, " buena edad para que realizes esta trivia.\n")

nombre = input("ingresa tu nombre: ")

print("\n Hola", nombre, "podremos a prueba tu conocimiento simpsoniano")

print( "Responde las siguientes preguntas escribiendo la letra de la alternativa y presionando *enter* para enviar tu respuesta:\n")

print("1)¿Quien andaba en patineta?")
print("a)Lisa simpsom")
print("b)Ned flanders")
print("c)Bart simpsom")
print("d)Ralph")

respuesta_1 = input("\ntu respuesta:")
if respuesta_1 == "c": print("parece que tuvistes suerte,jajajaja\n")
else: print("fallastes estupido fladers\n ")

while respuesta_1 not in ("a", "b", "c", "d"):
  respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta o eres milhouse: ")

print("2)¿quien era el conductor del bus escolar?")
print("a)Otto mann")
print("b)Homero simpsom")
print("c)Apu")
print("d)krusty el payaso")
respuesta_2 = input("\ntu respuesta: ")
if respuesta_2 == "a": print("Ooo eres bueno\n")
else: print("incorrecton\n")

while respuesta_2 not in ("a", "b", "c", "d"):
  respuesta_2 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta o eres milhouse: ")

a = "Muy bien"
b = " simpsoniano vamos por mas.\n"
c = a + b
print(c)
