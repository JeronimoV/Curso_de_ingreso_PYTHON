import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        suma_positivos = 0
        suma_negativos = 0
        maximo = 0 
        minimo = 0 
        cantidad_ceros = 0
        cantidad_numeros_negativos = 0
        cantidad_numeros_positivos = 0

        while True:
            numero_b = prompt("Numero", "Ingrese un numeros") 
            if numero_b == None:
                break
            if 0 < int(numero_b):
                suma_positivos += int(numero_b)
                cantidad_numeros_positivos += 1
            else:
                suma_negativos += int(numero_b)
                cantidad_numeros_negativos += 1
            if maximo < int(numero_b): 
                maximo = int(numero_b) 
            if minimo > int(numero_b): 
                minimo = int(numero_b)
            if int(numero_b) == 0:
                cantidad_ceros += 1
            

        alert("Ej10", f"Suma de positivos: {suma_positivos}, Suma negativos: {suma_negativos}, Maximo: {maximo}, Minimo: {minimo}, Cantidad de ceros: {cantidad_ceros}, Cantidad numeros negativos: {cantidad_numeros_negativos}, Cantidad numeros positivos: {cantidad_numeros_positivos}")

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
