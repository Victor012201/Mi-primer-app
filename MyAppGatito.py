import streamlit as st
st.title("Mi primer app")
click=st.button("SI")
st.write("el valor de click es:",click)
if click==True:
    st.image("gato.jpg")
st.button("NO")
num1=st.slider("elige el numero 1",0.0,100.0,25.0)
num2=st.slider("elige el numero 2",0.0,100.0,25.0)
suma=num1+num2
st.write("la suma de",num1,"y",num2,"es :",suma)
st.write("ahora multipliquemos")
nn1=st.number_imput("dame n1")
nn2=st.number_imput("dame n2")
mult=nn1*nn2
st.write("la multiplicacion de",nn1,"y",nn2,"es :",mult)
#import pandas as pd
#df = pd.read_csv("https://raw.githubusercontent.com/quantum-apps/mapa/main/data.csv")
#st.write(df)
#st.map(df)
#st.write("Hola tengo hambre")
#st.text("Hola tengo hambre")
#st.latex("C_6H_6+CH_3COCl-C_6H_5COCH_3+HCl")
#st.latex("\int_1^6 sin(x)dx")
#st.markdown("#titulo")
