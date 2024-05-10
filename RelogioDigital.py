from tkinter import *
from time import strftime

def executar():
# Função para atualizar o relógio
    def atualizar_relogio():
        horario_atual = strftime("%H:%M:%S %p")
        rotulo_relogio.config(text=horario_atual)
        rotulo_relogio.after(1000,atualizar_relogio)

    # Criando da janela principal
    janela = Tk()
    janela.title("Relógio Digital Simples")

    # Criação do rótulo para exibir o relógio
    rotulo_relogio = Label(
        janela,
        font=("Arial", 40, "bold"),
        background="light green",
        foreground="white"
    )


    # Posiciona o rótulo no centro da janela
    rotulo_relogio.pack(anchor="center")


    # Inicia a atualização do relógio
    atualizar_relogio()

    # Inicia o loop principal da interface gráfica
    janela.mainloop()
if(__name__ == "__main__"):
    executar()