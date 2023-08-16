# -*- coding: utf-8 -*-
import sqlite3


class MLDB:
    """
    Classe que manipula o banco de dados.
    """

    def __init__(self):
        caminho_db = 'banco_dados/ml.db'
        self.con = sqlite3.connect(caminho_db)
        self.cursor = self.con.cursor()

    def cadastrar_usuario(
        self, usermane: str, email: str, password: str, confipassoword: str
    ) -> str | None:
        """
        Cadastra um novo usuário.
        :param usermane: Nome do usuário.
        :param email: E-mail do usuário.
        :param password: Senha do usuário.
        :param confipassoword: Confirmação de senha do usuário.
        :return: Mensagem com o erro ocorrido ou None se a operação for bem sucedida.
        """
        if (
            usermane == ''
            or email == ''
            or password == ''
            or confipassoword == ''
        ):
            return 'ERRO\nPreencha os Campos vazios!'
        elif len(usermane) < 4:
            return 'O nome de Usuário deve\nter pelo menos 4 caracteres!'
        elif len(password) < 4:
            return 'A Senha deve\nter pelo menos 4 caracteres!'
        elif password != confipassoword:
            return 'Senha incorreta'
        else:
            self._cadastrar_usuario(usermane, email, password, confipassoword)
            return None

    def consultar_existencia_usuario(
        self, username: str, password: str
    ) -> bool:
        """
        Consulta a existência do usuário informado.
        :param username: Nome do usuário.
        :param password: Senha do usuário.
        :return: Retorna se o usuário existe no banco de dados.
        """
        if username == '' or password == '':
            return False
        else:
            resultado = self._consultar_existencia_usuario(username, password)
            return resultado

    def _cadastrar_usuario(
        self, usermane: str, email: str, password: str, confipassoword: str
    ) -> None:
        """
        Cadastra um novo usuário no banco de dados.
        :param usermane: Nome do usuário.
        :param email: E-mail do usuário.
        :param password: Senha do usuário.
        :param confipassoword: Confirmação de senha do usuário.
        """
        try:
            self.cursor.execute(
                f"""
            INSERT INTO usuarios (Usermane, Email, Password, ConfiPassoword)
            VALUES ('{usermane}', '{email}', '{password}', '{confipassoword}')
            """
            )
            self.con.commit()
        except sqlite3.IntegrityError:
            raise f'Usuário já existe'

    def _consultar_existencia_usuario(
        self, username: str, password: str
    ) -> bool:
        """
        Método privado que consulta a existência do usuário informado no banco de dados.
        :param username: Nome do usuário.
        :param password: Senha do usuário.
        :return: Retorna se o usuário existe no banco de dados.
        """
        resultado_consulta = self.cursor.execute(
            f"""SELECT * FROM usuarios
            WHERE (Usermane = '{username}' AND Password = '{password}')"""
        )
        if len(resultado_consulta.fetchall()) == 0:
            return False

        else:
            return True

    def fechar_con(self):
        """
        Fecha a conexão com o banco de dados.
        """
        self.con.close()
