import tkinter
from tkinter import *

class tabela:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial","12")
        self.janela = Frame(master)
        self.janela.pack()
        self.msg = Label(self.janela, text="Sistema de cadastro")
        self.msg["font"] = self.fontePadrao
        self.msg.pack()

        self.janela2 = Frame(master)
        self.janela2["padx"] = 20
        self.janela2.pack()

        self.usua = Button(self.janela)
        self.usua.pack(side=LEFT)
        self.usua["text"] = "Usuário"
        self.usua["font"] = ("Calibri", "12")
        self.usua["width"] = 14
        self.usua["command"] = self.janela
        self.usua.pack()

        self.cidade = Button(self.janela)
        self.cidade.pack(side=LEFT)
        self.cidade["text"] = "Cidades"
        self.cidade["font"] = ("Calibri", "12")
        self.cidade["width"] = 14
        self.cidade["command"] = self.janela
        self.cidade.pack()

        self.clie = Button(self.janela)
        self.clie.pack(side=LEFT)
        self.clie["text"] = "Clientes"
        self.clie["font"] = ("Calibri", "12")
        self.clie["width"] = 14
        self.clie["command"] = self.janela
        self.clie.pack()

        self.fechar = Button(self.janela)
        self.fechar.pack(side=LEFT)
        self.fechar["text"] = "Fechar"
        self.fechar["font"] = ("Calibri", "12")
        self.fechar["width"] = 14
        self.fechar["command"] = self.janela
        self.fechar.pack()



root = Tk()
tabela(root)
root.state("zoomed")
root.mainloop()
