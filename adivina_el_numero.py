import random

def jugar_adivina_el_numero():
    print("¡Bienvenido a Adivina el Número!")
    print("Estoy pensando en un número entre 1 y 50.")
    print("Tienes 5 vidas para adivinarlo.")

    numero_secreto = random.randint(1, 50)
    vidas = 5

    while True:
        try:
            print(f"\nTe quedan {vidas} vidas.")
            entrada = input("¿Qué número estoy pensando? ")
            numero_usuario = int(entrada)
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        if numero_usuario < numero_secreto:
            print("¡Frío! Mi número es más grande.")
        elif numero_usuario > numero_secreto:
            print("¡Te pasaste! Mi número es más pequeño.")
        else:
            print(f"¡Exacto! Eres un genio. El número era {numero_secreto}.")
            break

        vidas -= 1
        if vidas == 0:
            print(f"\n¡Game Over! Te quedaste sin vidas. El número era {numero_secreto}.")
            break

if __name__ == "__main__":
    jugar_adivina_el_numero()
