# 🧠 Quiz Game

Un simple juego de preguntas y respuestas en la terminal. ¡Pon a prueba tus conocimientos con este quiz interactivo! 📚

## 🚀 ¿Cómo funciona?

- El programa te muestra una serie de preguntas de verdadero o falso.
- Responde cada pregunta escribiendo **True** o **False**.
- Al final, el juego te dirá tu puntuación total.

### 📸 Vista previa



## 📦 Instalación

Asegúrate de tener **Python 3.x** instalado. Luego, sigue estos pasos:

```bash
# Clona el repositorio
https://github.com/tu-usuario/quiz-game.git

cd quiz-game

# Ejecuta el programa
python main.py
```

## 📋 Estructura del proyecto

```
quiz-game/
├── data.py            # Datos con las preguntas
├── main.py            # Punto de entrada del programa
├── question_model.py  # Clase Question (modelo de pregunta)
└── quiz_brain.py      # Lógica principal del juego
```

## 🛠️ Personalizar el juego

Puedes agregar más preguntas editando el archivo `data.py`.

```python
question_data = [
    {"text": "¿El sol es una estrella?", "answer": "True"},
    {"text": "¿Python fue creado en 2020?", "answer": "False"}
]
```


