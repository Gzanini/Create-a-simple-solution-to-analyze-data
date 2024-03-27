import time
import tkinter as tk
import webbrowser
from tkinter import messagebox
import subprocess
import os


def abrir_pagina_inicial():
    # Inicia o script do dashboard localmente
    subprocess.Popen(['python', 'dashboard.py'], shell=True)
    url = "http://127.0.0.1:8050/"
    webbrowser.open(url)


def exibir_alerta_inicial():
    messagebox.showinfo("Alerta", "O software foi iniciado corretamente. "
                                  "Caso o dashboard não iniciar, recarregue a página!")


def fechar_programa():
    if messagebox.askokcancel("Fechar", "Tem certeza que deseja fechar o programa?"):
        os._exit(0)


def criar_tela_inicial():
    tela_inicial = tk.Tk()
    tela_inicial.title("Dashboard GZ Consultoria")
    tela_inicial.geometry("400x300")  # Ajustado para um tamanho um pouco maior
    tela_inicial.configure(background='#123456')  # Exemplo de cor de fundo

    estilo_texto = ("Arial", 12, "bold")
    estilo_titulo = ("Arial", 18, "bold")

    nome_programa = tk.Label(tela_inicial, text="Dashboard de Análise de Gastos", font=estilo_titulo, bg='#123456', fg='white')
    nome_programa.pack(pady=20)

    fechar_button = tk.Button(tela_inicial, text="Fechar Programa", command=fechar_programa, font=estilo_texto)
    fechar_button.pack(pady=10)

    consultoria = tk.Label(tela_inicial, text="GZ Consultoria: Soluções para Dados", font=estilo_texto, bg='#123456',
                           fg='white')
    consultoria.pack(pady=10)

    contato = tk.Label(tela_inicial, text="contato.gzconsultoria@gmail.com", font=estilo_texto, bg='#123456',
                       fg='white')
    contato.pack(pady=0)

    tela_inicial.mainloop()


if __name__ == "__main__":
    abrir_pagina_inicial()
    time.sleep(1)  # Dá tempo para o dashboard iniciar
    exibir_alerta_inicial()
    criar_tela_inicial()
