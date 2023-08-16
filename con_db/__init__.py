# -*- coding: utf-8 -*-
import os
import sqlite3

"""
Verifica ao iniciar o software se existe o banco de dados e executa a crição do mesmo.
"""

_CAMINHO_DB = 'banco_dados'
if not os.path.exists(_CAMINHO_DB):
    os.mkdir(_CAMINHO_DB)
    con = sqlite3.connect(_CAMINHO_DB + '/ml.db')
    cursor = con.cursor()
    cursor.execute(
        """
    CREATE TABLE usuarios(
        Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Usermane TEXT NOT NULL UNIQUE,
        Email TEXT NOT NULL,
        Password TEXT NOT NULL,
        ConfiPassoword TEXT NOT NULL);
    """
    )
    con.commit()
    con.close()
