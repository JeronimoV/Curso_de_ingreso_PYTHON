import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por alert

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        max_votado_nombre = None
        max_votado_cantidad = None
        min_votado_nombre = None
        min_votado_edad = None
        min_votado_cantidad = None
        edad_suma = 0
        total_votos = 0
        contador = 1

        while True:
            candidato_nombre = prompt("Nombre", "Ingrese el nombre")
            if candidato_nombre == None:
                break
            candidato_edad = int(prompt("Edad", "Ingrese la edad"))
            if candidato_edad == None:
                break
            while candidato_edad < 25:
                candidato_edad = int(prompt("Edad", "Ingrese la edad"))
            candidato_votos = int(prompt("Votos", "Ingrese la cantidad de votos"))
            if candidato_votos == None:
                break
            while candidato_votos < 0:
                candidato_votos = int(prompt("Votos", "Ingrese la cantidad de votos"))
            if max_votado_cantidad == None or candidato_votos > max_votado_cantidad:
                max_votado_nombre = candidato_nombre
                max_votado_cantidad = candidato_votos
            if min_votado_cantidad == None or candidato_votos < min_votado_cantidad:
                min_votado_cantidad = candidato_votos
                min_votado_nombre = candidato_nombre
                min_votado_edad = candidato_edad
            edad_suma += candidato_edad
            total_votos += candidato_votos
            respuesta = prompt("Quieres seguir?", " ¿Quieres seguir? Si/No")
            if respuesta == "Si":
                contador += 1
            else:
                break
        
        promedio = edad_suma / contador
        
        alert("Resultados", f"Candidato mas votado: {max_votado_nombre} con {max_votado_cantidad} votos")
        alert("Resultados", f"Candidato menos votado: {min_votado_nombre} con {min_votado_cantidad} votos de {min_votado_edad} de edad")
        alert("Resultados", f"Datos adicionales: Promedio edad: {promedio}, Total votos: {total_votos}")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
