# -*- coding: utf-8 -*-
import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
from con_db.ml_db import MLDB


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.conf_inicial()
        self.tela_de_login()
        self.ml_db = MLDB()
        self.protocol('WM_DELETE_WINDOW', self.fechar_mlsytem)

    # Configurando a janela principal
    def conf_inicial(self):
        self.geometry('700x400')
        self.title('Mlcoder System')
        self.resizable(False, False)
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')

    def verifica_login(self):
        username_login = self.username_login_entry.get()
        senha_login = self.senha_login_entry.get()
        existe = self.ml_db.consultar_existencia_usuario(
            username_login, senha_login
        )
        if existe:
            messagebox.showinfo(
                title='Mlcoder System',
                message=f'Parabéns {username_login}\nLogin feito com sucesso',
            )
            # se for para tela após não limpar apenas destruir a tela de login
            self.limpa_entry_login()
        else:
            messagebox.showerror(
                title='Mlcoder Syatema',
                message='Erro!!!\nDados não localizado',
            )

    def cadastrar_usuario(self):
        username_cadastro = self.username_cadastro_entry.get()
        email_cadastro = self.email_cadastro_entry.get()
        senha_cadastro = self.senha_cadastro_entry.get()
        conifirma_senhaa_cadastro = self.confirma_senha_entry.get()
        erro = self.ml_db.cadastrar_usuario(
            username_cadastro,
            email_cadastro,
            senha_cadastro,
            conifirma_senhaa_cadastro,
        )
        if erro is None:
            messagebox.showinfo(
                title='Mlcoder System',
                message=f'Parabéns {username_cadastro}\nOs seus dados foram cadastrados',
            )
        else:
            messagebox.showwarning(title='Mlcoder System', message=erro)

    def tela_de_login(self):

        # trabalhando com a imagem
        self.img = PhotoImage(file='jg.png')
        self.lb_img = Label(image=self.img, bg='#000000', fg='#FFFFFF')
        self.lb_img.grid(row=1, column=0, padx=10)
        self.iconbitmap('officedatabase_103574.ico')

        # texto
        self.title = ctk.CTkLabel(
            self,
            text='Faça sem Login ou\nCadastre-se na nossa plataforma!',
            font=('Century Gothic bold', 14),
        )
        self.title.grid(row=0, column=0, pady=10)

        # criação do frame do formulario de login
        self.frame_login = ctk.CTkFrame(self, width=350, height=380)
        self.frame_login.place(x=350, y=10)

        # colocando Wedgests dentro do frame - formulario de login
        self.lb_title = ctk.CTkLabel(
            self.frame_login,
            text='faça seu Login',
            font=('Century Gothic bold', 22),
        )
        self.lb_title.grid(row=0, column=0, padx=10, pady=10)

        # entry
        self.username_login_entry = ctk.CTkEntry(
            self.frame_login,
            width=300,
            placeholder_text='Seu nome de Usuário..',
            font=('Century Gothic bold', 16),
            corner_radius=15,
            border_color='red',
        )
        self.username_login_entry.grid(row=1, column=0, padx=10, pady=10)

        self.senha_login_entry = ctk.CTkEntry(
            self.frame_login,
            width=300,
            placeholder_text='Senha do Usuário..',
            font=('Century Gothic bold', 16),
            show='*',
            corner_radius=15,
            border_color='red',
        )
        self.senha_login_entry.grid(row=2, column=0, padx=10, pady=10)

        self.ver_senha = ctk.CTkCheckBox(
            self.frame_login,
            text='Clique para ver a senha',
            font=('Century Gothic bold', 12),
            corner_radius=20,
        )
        self.ver_senha.grid(row=3, column=0, padx=10, pady=10)

        self.btn_login = ctk.CTkButton(
            self.frame_login,
            width=300,
            fg_color='red',
            text='Login'.upper(),
            font=('Century Gothic bold', 16),
            corner_radius=15,
            command=self.verifica_login,
        )
        self.btn_login.grid(row=4, column=0, padx=10, pady=10)

        self.spa = ctk.CTkLabel(
            self.frame_login,
            text='Se não tens conta, clique no botão abaixo',
            font=('Century Gothic', 10),
        )
        self.spa.grid(row=5, column=0, padx=10, pady=10)

        self.btn_cadastro = ctk.CTkButton(
            self.frame_login,
            width=300,
            fg_color='green',
            text='Cadastre-se'.upper(),
            font=('Century Gothic bold', 16),
            corner_radius=15,
            command=self.tela_de_cadastro,
        )
        self.btn_cadastro.grid(row=6, column=0, padx=10, pady=10)

        # tela de cadastro

    def tela_de_cadastro(self):
        # remover formulario de login
        self.frame_login.place_forget()

        # frame de cadastro
        self.frame_cadastro = ctk.CTkFrame(self, width=350, height=380)
        self.frame_cadastro.place(x=350, y=10)

        # colocando Wedgests dentro do frame - formulario de cadastro
        self.lb_title = ctk.CTkLabel(
            self.frame_cadastro,
            text='faça seu Login',
            font=('Century Gothic bold', 22),
        )
        self.lb_title.grid(row=0, column=0, padx=10, pady=10)

        # criar os nossos widgets da tela de cadastro
        self.username_cadastro_entry = ctk.CTkEntry(
            self.frame_cadastro,
            width=300,
            placeholder_text='Seu nome de Usuário..',
            font=('Century Gothic bold', 16),
            corner_radius=15,
            border_color='red',
        )
        self.username_cadastro_entry.grid(row=1, column=0, padx=10, pady=5)

        self.email_cadastro_entry = ctk.CTkEntry(
            self.frame_cadastro,
            width=300,
            placeholder_text='e_mail de Usuário..',
            font=('Century Gothic bold', 16),
            corner_radius=15,
            border_color='red',
        )
        self.email_cadastro_entry.grid(row=2, column=0, padx=10, pady=5)

        self.senha_cadastro_entry = ctk.CTkEntry(
            self.frame_cadastro,
            width=300,
            placeholder_text='Senha do Usuário..',
            font=('Century Gothic bold', 16),
            show='*',
            corner_radius=15,
            border_color='red',
        )
        self.senha_cadastro_entry.grid(row=3, column=0, padx=10, pady=5)

        self.confirma_senha_entry = ctk.CTkEntry(
            self.frame_cadastro,
            width=300,
            placeholder_text='confirmar a senha..',
            font=('Century Gothic bold', 16),
            corner_radius=15,
            border_color='red',
            show='*',
        )
        self.confirma_senha_entry.grid(row=4, column=0, padx=5, pady=5)

        self.ver_senha = ctk.CTkCheckBox(
            self.frame_cadastro,
            text='Clique para ver a senha',
            font=('Century Gothic bold', 12),
            corner_radius=20,
        )
        self.ver_senha.grid(row=5, column=0, padx=10, pady=5)

        self.btn_cadastrar_user = ctk.CTkButton(
            self.frame_cadastro,
            width=300,
            fg_color='green',
            text='Cadastre-se'.upper(),
            font=('Century Gothic bold', 16),
            corner_radius=15,
            command=self.cadastrar_usuario,
        )
        self.btn_cadastrar_user.grid(row=6, column=0, padx=10, pady=5)

        self.btn_login_back = ctk.CTkButton(
            self.frame_cadastro,
            width=300,
            text='voltar'.upper(),
            font=('Century Gothic bold', 14),
            corner_radius=15,
            fg_color='#444',
            hover_color='#333',
            command=self.tela_de_login,
        )
        self.btn_login_back.grid(row=7, column=0, pady=5, padx=10)

    def fechar_mlsytem(self):
        self.ml_db.fechar_con()
        self.destroy()

    # backend
    def limpa_entry_cadastro(self):
        self.username_cadastro_entry.delete(0, END)
        self.email_cadastro_entry.delete(0, END)
        self.senha_cadastro_entry.delete(0, END)
        self.confirma_senha_entry.delete(0, END)

    def limpa_entry_login(self):
        self.username_login_entry.delete(0, END)
        self.senha_login_entry.delete(0, END)


# chamando o APP
if __name__ == '__main__':
    app = App()
    app.mainloop()
