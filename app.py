import streamlit as st  # biblioteca para criar aplicativos web apenas com python
import pandas as pd  # manipulação de dados
from sklearn.linear_model import LinearRegression  # criar e treinar o modelo de regressão linear.


# Lê os dados do arquivo CSV pizzas.csv e os carrega em um DataFrame df.
df = pd.read_csv("pizzas.csv")  

modelo = LinearRegression()  # instância do modelo de regressão linear.
x = df[["diametro"]]
y = df[["preco"]]

#  Treina o modelo com os dados disponíveis.
modelo.fit(x, y)  

# app web -> streamlit run app.py
st.title("Preço da pizza conforme diâmetro")
st.divider()

diametro = st.number_input("Digite o tamanho do diâmetro da pizza em cm: ")

# Usa o modelo treinado para prever o preço da pizza com base no diâmetro inserido pelo usuário.
if diametro:
    preco_previsto = modelo.predict([[diametro]])[0][0]
    st.write(f"O valor da pizza com diâmetro de {diametro:.2f}cm é de R${preco_previsto:.2f}.")
