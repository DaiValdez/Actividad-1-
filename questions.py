import random 


# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
        "// Esto es un comentario",
        "/* Esto es un comentario */",
        "-- Esto es un comentario",
        "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

questions_to_ask = random.choices(list(zip(questions,
answers, correct_answers_index)), k=3)

# zip(questions, answers, correct_answers_index): 
# Combina las tres listas en tuplas donde cada tupla contiene una pregunta, 
# sus respuestas posibles y el índice correcto.
# list(zip(...)): Convierte ese objeto en una lista de tuplas
# random.choices(..., k=3): Selecciona aleatoriamente 3 de esas tuplas para usarlas en el juego.

points = 0

# El usuario deberá contestar 3 preguntas
for question, answer,correct_index in questions_to_ask:
    
    # Se muestra la pregunta y las respuestas posibles
    print(question)
    for i, ans in enumerate(answer):
        print(f"{i + 1}. {ans}")

    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = input("Respuesta: ") 
        # Comprobar si lo que se ingreso es un digito
        if not user_answer.isdigit():
           print("Respuesta no valida")
           exit(1)
        #si es un numero lo convierte en entero
        user_answer = int(user_answer)-1
        # Se verifica si la respuesta es correcta
        if user_answer == correct_index:
            print("¡Correcto!")
            points += 1   # Sumar un punto por acierto
            break 
        else:
           points -= 0.5
    
    else: 
        # Si el usuario no responde correctamente después de 2 intentos,
        # se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(answer[correct_index])


    # Se imprime un blanco al final de la pregunta

    print()
print("El puntaje del jugad@r es: ", points)