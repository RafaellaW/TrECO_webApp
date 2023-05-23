#IMPORTAR BIBLIOTECAS
import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np

def PaginaPrincipal():
    colored_header(
        label = "Dashboard",
        description="Bem Vindo",
        color_name="green-70",
        )

    tabColetaOrganica, tabColetaSeletiva, tabAprenda, tabSobreNos, tabTipoResiduos = st.tabs(["Coleta Organica", "Coleta Seletiva", "Aprenda", "Sobre Nos", "Tipo Residuos", ])
    with tabColetaOrganica:
        st.subheader(':blue[Segunda, Quarta e Sexta] :recycle:')
        st.write('* Jardim Botanico')
        st.write('* America, Nova America')
        st.write('* Washington Luis')
        st.write('* Ana, Diva, Paulo Prata')
        st.write('* Chacaras Feitoza')
        st.write('* Residencial Prata')
        st.write('* Oasis')
        st.write('* Nobre Ville')
        st.write('* Nobre Ville II')
        st.write('* Parque das Flores')
        st.write('* Chacara dos Ipes')
        st.write('* Nadir Kenan, Pedro Cavalini')
        st.write('* Conjunto Jose Feleiros')
        st.write('* Jardim Luis Spina')
        st.write('* Jardim Vale do Verde')
        st.write('* Grande Horizonte')
        st.write('* Newton Sopa, Benedito Realindo Correa, Pereira, Ibirapuera')
        st.write('* Jose Eugenio Miziara')
        st.write('* Cidade Jardim')
        st.write('* Residencial Menara')
        st.write('* City Barretos')
        st.write('* Industrial')
        st.write('* Santo Antonio')
        st.write('* Nogueira')
        st.write('* Ortega')

    with tabColetaSeletiva:
        st.subheader(':blue[Quarta Feira] :recycle:')
        st.write('* Boa esperanca')
        st.write('* Conj. Hab. Michel Jorge Naben')
        st.write('* derby Club')
        st.write('* Jardim Anastacio')
        st.write('* Jardim Anastacio II')
        st.write('* Jardim Caiçara')
        st.write('* Jardim dos Comerciarios')
        st.write('* Jardim Europa')
        st.write('* Jardim Maria Caputi')
        st.write('* Jardim Planalto')
        st.write('* Jockey Club')
        st.write('* Los Angeles')
        st.write('* Monte Alegre')
        st.write('* Residencial Jockey Club')
        st.write('* Residencial Santa Rita')
        st.write('* San Diego')
        st.write('* San Diego II')
        st.write('* Santa Cecilia')
        st.write('* Santa Terezinha')
        st.write('* Sao Francisco')
        st.write('* Tambore')

    with tabAprenda:
       st.header("Videos Interessantes sobre processos de Reciclagem")
       video_file = open('midia/LixoOrganicoSAAE.mp4', 'rb')
       video_bytes = video_file.read()
       st.video(video_bytes)
       st.write("Voce pode encontrar esse video e muitos outros no canal oficial do SAAE Barretos/Sp")
       st.write('https://www.youtube.com/@SAAEBarretosSP')

    with tabTipoResiduos:
        expanderPlasticos = st.expander("Plasticos")
        expanderPlasticos.write("""Plasticos Reciclaveis""")
        expanderPlasticos.write("""
            - Papelao
            - Sulfite
            - Jornais
            - Revistas
            - Embalagens longa vida
            - Cadernos e agendas
            """)
        expanderPlasticos.write("")
        expanderPlasticos.write("""Plasticos Nao Reciclaveis""")
        expanderPlasticos.write("""
                - Papel Higienico
                - Guardanapos engordurados
                - Embalagens de salgadinhos e biscoitos
                - fotografias
                - papel celofane
                - papel carbono
                - adesivos
                - fita crepe
                - papel vegetal
                - papel de caixa eletronico
                """)

        #-------------------------------VIDROS--------------------------------
        st.write('') #PRECISA PULAR UMA LINHA PARA NAO DAR ERRO
        expanderVidro = st.expander("Vidro")
        expanderVidro.write("""Vidros Reciclaveis""")
        expanderVidro.write("""
            - Garrafas de bebidas (leite, sucos, cervejas, refrigerantes, etc)
            - Fragmentos de vidros comuns
            - Pratos, copos e tigelas
            - Potes para armazenamento de alimentos
            - Frasco (remedio e/ou perfume)
            """)
        expanderVidro.write("")
        expanderVidro.write("Vidros nao Reciclaveis")
        expanderVidro.write("""
            - Espelhos
            - Vidros temperados
            - Refratarios - Pirex
            - Porcelana
            - Tampa de microondas
            - Lampadas
            - Cristais
            - Ampolas (remedios)
            """)

        #-------------------------------METAL--------------------------------
        st.write('') #PRECISA PULAR UMA LINHA PARA NAO DAR ERRO
        expanderMetal = st.expander("Metal")
        expanderMetal.write("""Metais Reciclaveis""")
        expanderMetal.write("""
            - Latas de Aluminio (refrigerante, cerveja, etc)
            - Aço (latas de sardinha, molhos, oleo, etc)
            - Arames, pergos, parafusos
            - Fios de metal
            - Tubos de pasta
            - Panelas sem cabo
            - Arames
            - Chapas de metal
            - Objetos de aluminio (janelas, portas, portões, etc)
            - Fios e objetos de cobre
            - Ferragens
            - Canos de metal
            - Molduras de quadros
            - Tampinhas de garrafa
            - Tampas metalicas de potes de iogurtes, margarinas, queijos, etc
            - Papel aluminio
            """)
        expanderMetal.write("")
        expanderMetal.write("""Metais nao reciclaveis""")
        expanderMetal.write("""
            - Clipes
            - Grampos
            - Esponjas de aço
            - Latas de tintas
            - Latas de combustivel
            - Pilhas
            """)
        #-------------------------------PAPEL--------------------------------
        st.write('')
        expanderPapel = st.expander("Papel")
        expanderPapel.write("""Papeis Reciclaveis""")
        expanderPapel.write("""
            - Papelão
            - Revistas
            - Livros
            - Jornais
            - Listas Telefonicas
            - Cadernos
            - Cartolinas
            - Embalagens longa-vida
            - Livros
            - Etc
            """)
        expanderPapel.write("")
        expanderPapel.write("""Papeis nao reciclaveis""")
        expanderPapel.write("""
            - Carbono
            - Celofane
            - Papel Vegetal
            - Papeis encerados ou plastificados
            - Papel Higienico
            - Lenços de papel
            - Guardanapos
            - Fotografias
            - Etc 
            """)
        #-------------------------------ORGANICOS--------------------------------
        st.write('')
        expanderOrganicos = st.expander("Organicos")
        expanderOrganicos.write("""Organicos Reciclaveis""")
        expanderOrganicos.write("""
            - Resto de comida
            - Cascas de legumes
            - frutas
            - cascas de ovos
            - etc.
            """)
        expanderOrganicos.write("")
        expanderOrganicos.write("""Organicos nao reciclaveis""")
        expanderOrganicos.write("""
            - Origem que e produzido por meios nao-naturais (plasticos, metal, aluminio)
            """)

        #-------------------------------PILHAS E BATERIAS--------------------------------
        st.write('')
        expanderPilhasBaterias = st.expander("Pilhas e Baterias")
        expanderPilhasBaterias.write("""Pilhas e Baterias reciclaveis""")
        expanderPilhasBaterias.write("""
            - Pilhas e Baterias de lítio recarregáveis, íon lítio e zinco-ar
            - Encontradas em aparelhos domesticos como cameras, celulares e notebooks
            - Baterias automotivas
            """)
        # expanderPilhasBaterias.write("")
        # expanderPilhasBaterias.write("Pilhas e Baterias nao reciclaveis")
        # expanderPilhasBaterias.write("""
        #   - Lista dos nao reciclaveis
        #   """)

        #-------------------------------HOSPITALARES-------------------------------------
        st.write('')
        expanderHospitalares = st.expander("Hospitalares")
        expanderHospitalares.write("""Hospitalares Reciclaveis""")
        expanderHospitalares.write("""
            - Frascos de soro
            - Caixas de medicamento
            - Bulas
            - Embalagens Plasticas de seringa
            - Capa da agulha
            """)
        expanderHospitalares.write("")
        expanderHospitalares.write("Hospitalares nao Reciclaveis")
        expanderHospitalares.write("""
            - Seringas
            - Fraldas
            - Agulhas
            - Cateteres
            - Sondas
            - Materiais provenientes de exames
            - Curativos
            - Etc
            """)
        #-------------------------------ELETRONICO-------------------------------------
        st.write('')
        expanderEletronico = st.expander("Eletronicos")
        expanderEletronico.write("""Eletronicos Reciclaveis""")
        expanderEletronico.write("""
            - Todos os aparelhos eletrônicos podem ser reciclados e o eletrolixo muitas vezes contém metais nobres e valiosos. Um exemplo é o ouro presente nos telefones celulares. Também é possível extrair prata, cobre e zinco
            - A reciclagem de lixo eletrônico desmonta os aparelhos após seu recebimento e classifica cada material encontrado, como plástico, placas de circuitos, vidros, metais, metais pesados, elementos químicos e outros. Com isso, cada um tem uma destinação correta para que não afete o meio ambiente
            """)
    #-------------------------------FIM-------------------------------------
       