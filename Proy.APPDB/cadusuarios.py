import tkinter
from tkinter import *

class usuario:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial","10")
        self.janela = Frame(master)
        self.janela.pack()
        self.msg = Label(self.janela, text="Informe os dados:")
        self.msg["font"] = self.fontePadrao
        self.msg.pack()

        self.janela2 = Frame(master)
        self.janela2["padx"] = 20
        self.janela2.pack()

        self.janela3 = Frame(master)
        self.janela3["padx"] = 20
        self.janela3.pack()

        self.janela4 = Frame(master)
        self.janela4["padx"] = 20
        self.janela4.pack()

        self.janela5 = Frame(master)
        self.janela5["padx"] = 20
        self.janela5.pack()

        self.janela6 = Frame(master)
        self.janela6["padx"] = 20
        self.janela6.pack()

        self.janela7 = Frame(master)
        self.janela7["padx"] = 20
        self.janela7.pack()

        self.janela8 = Frame(master)
        self.janela8["padx"] = 20
        self.janela8.pack()

        self.idLabel = Label(self.janela2, text="IdUsuario:", font=self.fontePadrao, width= 10)
        self.idLabel.pack(side=LEFT)
        self.id = Entry(self.janela2)
        self.id["width"] = 12
        self.id["font"] = self.fontePadrao
        self.id.pack(side=LEFT)

        self.bus = Button(self.janela2)
        self.bus.pack(side=RIGHT)
        self.bus["text"] = "Buscar"
        self.bus["font"] = ("Calibri", "12")
        self.bus["width"] = 10
        self.bus["command"] = self.janela2
        self.bus.pack(side=RIGHT)

        self.idLabel = Label(self.janela3, text="IdUsuario:", font=self.fontePadrao, width= 10)
        self.idLabel.pack(side=LEFT)
        self.id = Entry(self.janela3)
        self.id["width"] = 25
        self.id["font"] = self.fontePadrao
        self.id.pack(side=LEFT)

        self.telLabel = Label(self.janela4, text="Telefone:", font=self.fontePadrao, width= 10)
        self.telLabel.pack(side=LEFT)
        self.tel = Entry(self.janela4)
        self.tel["width"] = 25
        self.tel["font"] = self.fontePadrao
        self.tel.pack(side=LEFT)

        self.emailLabel = Label(self.janela5, text="E-mail:", font=self.fontePadrao, width= 10)
        self.emailLabel.pack(side=LEFT)
        self.email = Entry(self.janela5)
        self.email["width"] = 25
        self.email["font"] = self.fontePadrao
        self.email.pack(side=LEFT)

        self.usuLabel = Label(self.janela6, text="Usuário:", font=self.fontePadrao, width= 10)
        self.usuLabel.pack(side=LEFT)
        self.usu = Entry(self.janela6)
        self.usu["width"] = 25
        self.usu["font"] = self.fontePadrao
        self.usu.pack(side=LEFT)

        self.senhaLabel = Label(self.janela7, text="Senha:", font=self.fontePadrao, width= 10)
        self.senhaLabel.pack(side=LEFT)
        self.senha = Entry(self.janela7)
        self.senha["width"] = 25
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)

        self.usua = Button(self.janela8)
        self.usua.pack(side=LEFT)
        self.usua["text"] = "Inserir"
        self.usua["font"] = ("Calibri", "12")
        self.usua["width"] = 14
        self.usua["command"] = self.janela8
        self.usua.pack()

        self.cidade = Button(self.janela8)
        self.cidade.pack(side=LEFT)
        self.cidade["text"] = "Alterar"
        self.cidade["font"] = ("Calibri", "12")
        self.cidade["width"] = 14
        self.cidade["command"] = self.janela8
        self.cidade.pack()

        self.clie = Button(self.janela8)
        self.clie.pack(side=LEFT)
        self.clie["text"] = "Excluir"
        self.clie["font"] = ("Calibri", "12")
        self.clie["width"] = 14
        self.clie["command"] = self.janela8
        self.clie.pack()



root = Tk()
usuario(root)
root.state("zoomed")
root.mainloop()