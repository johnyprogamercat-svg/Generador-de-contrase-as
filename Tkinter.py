import tkinter as tk
import random as rd
caracteres = "1234567890abcdefghijklmnñopqrstuvwxyz!#$%&/()=?¡¨*][_:;,.-{+}]"
contraseña_generada = ""
def generar():
    contraseña_generada = ""
    for caracter_aleatorio in range(12):
        caracter_aleatorio = rd.choice(caracteres)
        contraseña_generada += caracter_aleatorio
    resultado.config(text= f"Nueva contraseña: {contraseña_generada}")
def copiar():
    ventana.clipboard_clear()
    ventana.clipboard_append(contraseña_generada)
ventana = tk.Tk()
ventana.geometry("600x500")

saludo = tk.Label(ventana, text="Bienvenido al generador de contraseñas segurísimas", font=("Montserrat", 14))
saludo.pack(pady=20)

resultado = tk.Label(ventana, text="N/A")
resultado.pack(pady=20)

boton = tk.Button(ventana, text="¡Haz clic aquí para generar una nueva contraseña!", command=generar, bg="lightblue")
boton.pack(pady=10)

boton2 = tk.Button(ventana, text="Copiar contraseña", command=copiar, bg="lightblue")
boton2.pack(pady=10)


ventana.mainloop()