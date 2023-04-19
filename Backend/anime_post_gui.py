import tkinter as tk
import requests
import json


def submit():
    # Obtener los valores de los campos de entrada
    name = name_entry.get()
    description = description_entry.get()
    episodes = int(episodes_entry.get())
    season = season_entry.get()
    genres = genres_entry.get()
    image_url = image_url_entry.get()

    # Crear un diccionario con los valores ingresados por el usuario
    anime_dict = {
        "name": name,
        "description": description,
        "episodes": episodes,
        "season": season,
        "genres": genres,
        "image_url": image_url
    }

    # Convertir los datos en formato JSON
    anime_json = json.dumps(anime_dict)

    # Definir la URL del endpoint de la solicitud POST
    url = "https://fastapi-1-v7692141.deta.app/animes/"

    # Definir los encabezados de la solicitud POST
    anime_headers = {
        "Content-Type": "application/json"
    }

    # Enviar la solicitud POST con los datos en formato JSON y los encabezados adicionales
    response = requests.post(url, data=anime_json, headers=anime_headers)

    # Imprimir la respuesta de la solicitud POST
    print(response.text)

    # Agregar mensaje si la respuesta es 201 created
    if response.status_code == 201:
        response_message = tk.Label(
            window, text="Anime added successfully!", font=("Arial", 16), fg="green")
        response_message.pack()

    # Agregar mensaje si el código de estado es 422 Validation Error
    elif response.status_code == 422:
        response_message = tk.Label(
            window, text="Validation Error. Please check your data!", font=("Arial", 16), fg="red")
        response_message.pack()


def clear():
    # Borrar contenido de todas las cajas de texto
    name_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)
    episodes_entry.delete(0, tk.END)
    season_entry.delete(0, tk.END)
    genres_entry.delete(0, tk.END)
    image_url_entry.delete(0, tk.END)


# Crear una ventana
window = tk.Tk()
window.title("Anime Post - Full Stack Team API")
window.geometry("500x500")
window.attributes('-topmost', True)


def focus_on_window():
    window.attributes('-topmost', True)
    window.after(100, focus_on_window)


focus_on_window()

# Crear campos de entrada de texto para cada clave en el diccionario de anime
name_label = tk.Label(window, text="Name:", font=("Arial", 16))
name_label.pack()
name_entry = tk.Entry(window, font=("Arial", 16))
name_entry.pack(ipadx=100)

description_label = tk.Label(window, text="Description:", font=("Arial", 16))
description_label.pack()
description_entry = tk.Entry(window, font=("Arial", 16))
description_entry.pack(ipadx=100)

episodes_label = tk.Label(window, text="Episodes:", font=("Arial", 16))
episodes_label.pack()
episodes_entry = tk.Entry(window, font=("Arial", 16))
episodes_entry.pack(ipadx=100)

season_label = tk.Label(window, text="Season:", font=("Arial", 16))
season_label.pack()
season_entry = tk.Entry(window, font=("Arial", 16))
season_entry.pack(ipadx=100)

genres_label = tk.Label(window, text="Genres:", font=("Arial", 16))
genres_label.pack()
genres_entry = tk.Entry(window, font=("Arial", 16))
genres_entry.pack(ipadx=100)

image_url_label = tk.Label(window, text="Image URL:", font=("Arial", 16))
image_url_label.pack()
image_url_entry = tk.Entry(window, font=("Arial", 16))
image_url_entry.pack(ipadx=100)

submit_button = tk.Button(window, text="Submit",
                          command=submit, font=("Arial", 16))
submit_button.pack()

clear_button = tk.Button(window, text="Clear",
                         command=clear, font=("Arial", 16))
clear_button.pack()

# Iniciar el bucle principal de la ventana
window.mainloop()
