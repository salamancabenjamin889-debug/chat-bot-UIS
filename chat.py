import random

# Diccionario de intenciones (Tu código original)
intents = {
    "saludo": [
        "¡Hola! ¿Cómo estás?",
        "¡Buen día! ¿En qué puedo ayudarte?",
        "Hola, soy tu asistente virtual"
    ],
    "despedida": [
        "¡Hasta luego!",
        "Que tengas un gran día",
        "Adiós, fue un gusto ayudarte"
    ],
    "horario": [
        "Nuestro horario es de lunes a viernes de 8am a 6pm.",
        "Abrimos de 8 a 6 de lunes a viernes."
    ],
    "carreras": [
        "Ofrecemos Ingeniería, Medicina, Derecho y más programas.",
        "Puedes estudiar Ingeniería, Ciencias Sociales, Medicina, etc."
    ],
    "default": [
        "Lo siento, no entendí tu pregunta",
        "¿Podrías reformular eso?",
        "No tengo información sobre eso, pero puedo ayudarte en otra cosa."
    ]
}

keywords = {
    "saludo": ["hola", "buenas", "qué tal"],
    "despedida": ["adiós", "chao", "hasta luego"],
    "horario": ["horario", "hora", "abren", "cierran"],
    "carreras": ["carrera", "programa", "estudio", "universidad"]
}

def clasificar_intencion(user_input):
    texto = user_input.lower()
    for intent, palabras in keywords.items():
        if any(p in texto for p in palabras):
            return intent
    return "default"

# --- MENÚ DE OPCIONES DEL HTML SIMULADO ---
menu_opciones = [
    "1. Matemáticas Avanzadas",
    "2. Historia Universal",
    "3. Programación en Python",
    "4. Inglés de Negocios",
    "5. Diseño Gráfico",
    "6. Biología Molecular"
]

def mostrar_menu_elegante_simulado():
    """Simula la presentación del menú de opciones en la consola."""
    print("\n" + "="*40)
    print("✨ ¡Excelente! Es hora de elegir tus cursos de interés. ✨")
    print("="*40)
    for opcion in menu_opciones:
        print(f"| {opcion:<36} |")
    print("="*40 + "\n")
    print("Por favor, introduce el número de las opciones (separadas por comas).")

def chatbot_con_transicion():
    print("Chatbot universitario. Escribe 'salir' para terminar.")
    
    # 1. SALUDO INICIAL
    print(f"Chatbot: {random.choice(intents['saludo'])}")
    
    conversacion_terminada = False
    while not conversacion_terminada:
        user_input = input("Tú: ")
        
        if user_input.lower() == "salir":
            print("Chatbot: ¡Hasta pronto!")
            return
        
        intent = clasificar_intencion(user_input)
        
        if intent == "default":
            # Si el chatbot no entiende, sigue la conversación normal
            respuesta = random.choice(intents[intent])
            print(f"Chatbot: {respuesta}")
            
        else:
            # Si el chatbot responde algo útil (ej. 'carreras' o 'horario')
            respuesta = random.choice(intents[intent])
            print(f"Chatbot: {respuesta}")
            
            # 2. TRANSICIÓN DESPUÉS DE LA INTERACCIÓN
            pregunta_menu = input("\nChatbot: ¿Hemos resuelto tu duda principal? (s/n): ")
            if pregunta_menu.lower() == 's':
                print("Chatbot: Perfecto. Para continuar con tu inscripción, veamos tus intereses:")
                conversacion_terminada = True
            else:
                print("Chatbot: Entiendo, ¿en qué más puedo ayudarte?")

    # 3. MOSTRAR EL MENÚ (Simulación)
    mostrar_menu_elegante_simulado()
    
# Ejecutar chatbot con la nueva lógica
chatbot_con_transicion()