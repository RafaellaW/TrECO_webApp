from datetime import datetime
import streamlit as st
import sqlite3
import time
from PIL import Image
import pandas as pd


# IMPORTAR PÁGINA COM AS ABAS DOS MENUS
import pages.perfil.principal as Dashboard

# Configurar conexão com o banco de dados SQLite
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        bairro TEXT,
        login_usuario TEXT,
        senha TEXT,
        pergunta_seguranca TEXT,
        resposta TEXT
    )
''')



# Configurar a barra lateral
st.sidebar.image('midia/PI-I-TrECO2.png', width=300)



acao = st.sidebar.radio("",("Login", "Cadastro"))

if acao == "Login":
    # Lógica para o botão de login
    login = st.sidebar.text_input('Informe o login')
    senha = st.sidebar.empty()
    senha = senha.text_input('Informe a senha', type='password')

    if st.sidebar.button('Entrar'):
        if login and senha:  # Verificar se os campos não estão vazios
            # Autenticar usuário
            comandoAutenticarUsuario = f"SELECT login_usuario, senha FROM usuario WHERE login_usuario = ? AND senha = ?"
            cursor.execute(comandoAutenticarUsuario, (login, senha))
            resultado = cursor.fetchone()

            if resultado is not None:
                # Usuário autenticado
                st.sidebar.success("Login bem-sucedido!")
                time.sleep(2)  # Simular um atraso de 5 segundos

                # Chamar a página principal
                Dashboard.PaginaPrincipal()
            else:
                st.sidebar.error("Credenciais inválidas.")
        else:
            st.sidebar.error("Informe o login e a senha.")

elif acao == "Cadastro":
    nomeCompleto = st.sidebar.text_input('Nome Completo')
    bairro = st.sidebar.selectbox(label="Bairro", options=["Aeroporto", "Alpa", "Alto Sumaré", "América"])
    login_usuario = st.sidebar.text_input('Usuário')
    senha_usuario = st.sidebar.empty()
    senha_usuario = senha_usuario.text_input('Senha', type='password')
    perguntaSeguranca = st.sidebar.selectbox(label="Pergunta de segurança", options=["Nome do primeiro pet", "Marca do seu primeiro carro", "Cor Favorita"])
    respostaPerguntaSeguranca = st.sidebar.text_input('Resposta')

    if st.sidebar.button('Criar minha conta'):
        if nomeCompleto and bairro and login_usuario and senha_usuario and perguntaSeguranca and respostaPerguntaSeguranca:
            # Inserir novo usuário no banco de dados
            comandoInserirUsuario = "INSERT INTO usuario (nome, bairro, login_usuario, senha, pergunta_seguranca, resposta) VALUES (?, ?, ?, ?, ?, ?)"
            cursor.execute(comandoInserirUsuario, (nomeCompleto, bairro, login_usuario, senha_usuario, perguntaSeguranca, respostaPerguntaSeguranca))
            conn.commit()
