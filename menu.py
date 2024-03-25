import time
import tkinter as tk
from tkinter import messagebox
import webbrowser
import os


def abrir_pagina_inicial():
    # Função para abrir a página inicial
    url = "https://www.google.com.br/?hl=pt-BR"
    webbrowser.open(url)


def exibir_alerta_inicial():
    # Função para exibir a mensagem de alerta inicial
    messagebox.showinfo("Alerta", "O software foi iniciado corretamente. "
                                  "Caso o dachbord não iniciar, recaregar a pagina!")


def fechar_programa():
    # Função para fechar o programa
    # Exibe uma mensagem de confirmação antes de encerrar o programa
    if messagebox.askokcancel("Fechar", "Tem certeza que deseja fechar o programa?"):
        # Finaliza a execução do programa
        os._exit(0)


def criar_tela_inicial():
    # Função para criar a tela inicial
    tela_inicial = tk.Tk()
    tela_inicial.title("API Bet365 Reader")
    tela_inicial.geometry("350x200")

    # Define o estilo do texto
    estilo_texto = ("Arial", 12)  # Tipo de fonte Arial, tamanho 12

    # Define o estilo do Titulo
    estilo_titulo = ("Arial", 16)  # Tipo de fonte Arial, tamanho 12

    # Label com o nome do programa
    nome_programa = tk.Label(tela_inicial, text="API Bet365 Reader", font=estilo_titulo)
    nome_programa.pack(pady=10)

    # Botão para fechar o programa
    fechar_button = tk.Button(tela_inicial, text="Fechar Programa", command=fechar_programa, font=estilo_texto)
    fechar_button.pack(pady=10)

    consultoria = tk.Label(tela_inicial, text="GZ Consultoria: Soluções para Dados", font=estilo_texto)
    consultoria.pack(pady=10)

    contato = tk.Label(tela_inicial, text="contato.gzconsultoria@gmail.com", font=estilo_texto)
    contato.pack(pady=0)

    # Inicia o loop principal do Tkinter
    tela_inicial.mainloop()


if __name__ == "__main__":
    # Abre a página inicial
    abrir_pagina_inicial()

    # Exibe a mensagem de alerta inicial
    time.sleep(1)
    exibir_alerta_inicial()

    # Cria a tela inicial do software
    criar_tela_inicial()
