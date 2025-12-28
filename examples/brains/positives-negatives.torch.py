"""
Red Neuronal Simple - Clasificador de Signo
Propósito académico: clasificar un número como positivo (1), cero (0), o negativo (-1)
"""

# Importamos PyTorch y algunos componentes útiles para redes neuronales
import torch
import torch.nn as nn
import torch.optim as optim


# Definir la arquitectura de la red neuronal que aprenderá a reconocer el signo
class SignClassifier(nn.Module):
    def __init__(self):
        super(SignClassifier, self).__init__()
        # Capa de entrada: 1 neurona (el número a clasificar)
        # Capa oculta: 8 neuronas para aprender patrones simples
        # Capa de salida: 3 neuronas (una por cada clase: negativo, cero, positivo)
        self.layer1 = nn.Linear(1, 8)
        self.layer2 = nn.Linear(8, 3)
        self.activation = nn.ReLU()  # Función de activación

    def forward(self, x):
        current = x
        # Pasamos la entrada por la primera capa y aplicamos la función de activación
        current = self.activation(self.layer1(current))
        # La segunda capa produce los logits de las 3 clases
        current = self.layer2(current)
        return current  # No usamos softmax porque CrossEntropyLoss lo aplica internamente


# Función para convertir etiqueta numérica a clase entera comprensible por la red
def label_to_class(num):
    """Convierte un número a su clase: 0=negativo, 1=cero, 2=positivo"""
    if num < 0:
        return 0  # negativo
    elif num == 0:
        return 1  # cero
    else:
        return 2  # positivo


# Función para convertir predicción de la red (clase) a resultado final (-1, 0, 1)
def class_to_result(class_idx):
    """Convierte índice de clase a resultado: -1, 0, o 1"""
    mapping = {0: -1, 1: 0, 2: 1}
    return mapping[class_idx]


# Crear datos de entrenamiento que la red utilizará para aprender
def create_training_data(n_samples):
    # Generar números aleatorios entre -100 y 100 (distribución normal escalada)
    numbers = torch.randn(n_samples, 1) * 100

    # Agregar algunos ceros explícitamente para que la red los vea con frecuencia
    numbers[0:10] = 0

    # Agregar algunos decimales cercanos a cero
    numbers[10:110] = torch.randn(100, 1) * 1

    # Crear etiquetas transformando cada número a su clase
    labels = torch.tensor([label_to_class(n.item()) for n in numbers])

    return numbers, labels


# Entrenar el modelo para que aprenda de los datos
def train_model(model, epochs):
    criterion = nn.CrossEntropyLoss()  # Función de pérdida para clasificación multiclase
    optimizer = optim.Adam(model.parameters(), lr=0.01)  # Algoritmo que ajusta los pesos

    X_train, y_train = create_training_data(1000)  # Obtenemos datos y etiquetas

    print("Entrenando la red neuronal...")
    for epoch in range(epochs):
        # Forward pass: obtener predicciones de la red
        outputs = model(X_train)
        loss = criterion(outputs, y_train)  # Comparar predicciones vs etiquetas

        # Backward pass y optimización
        optimizer.zero_grad()      # Reiniciar gradientes acumulados
        loss.backward()            # Calcular gradientes mediante retropropagación
        optimizer.step()           # Actualizar pesos con los gradientes calculados

        if (epoch + 1) % 100 == 0:
            print(f"Época [{epoch+1}/{epochs}], Pérdida: {loss.item():.4f}")

    print("¡Entrenamiento completado!")


# Función para hacer predicciones sobre nuevos números
def predict(model, number):
    model.eval()  # Ponemos el modelo en modo evaluación (sin dropout/batchnorm)
    with torch.no_grad():  # Desactivamos el cálculo de gradientes para ahorrar memoria
        input_tensor = torch.tensor([[float(number)]])  # Convertimos el número a tensor 2D
        output = model(input_tensor)  # Obtenemos los logits de las clases
        predicted_class = torch.argmax(output, dim=1).item()  # Clase con mayor probabilidad
        return class_to_result(predicted_class)  # Convertimos a -1, 0 o 1


# Programa principal: solo se ejecuta si abrimos el archivo directamente
if __name__ == "__main__":
    # Crear el modelo (instancia de nuestra red)
    modelo = SignClassifier()

    # Entrenar el modelo con los datos generados
    train_model(modelo, epochs=1000)

    # Probar con algunos números manuales para ver cómo responde
    print("\n--- Pruebas ---")
    test_numbers = [5, -3, 0, 100, -50, 0.5, -0.1]

    for num in test_numbers:
        resultado = predict(modelo, num)  # Obtener la predicción de la red
        # Mostrar en pantalla la predicción junto con el valor esperado
        print(f"Número: {num:>6} → Predicción: {resultado:>2} (esperado: {1 if num > 0 else (0 if num == 0 else -1)})")