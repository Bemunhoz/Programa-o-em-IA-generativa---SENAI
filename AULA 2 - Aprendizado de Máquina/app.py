import streamlit as st

#st.title('Calculadora')
#st.caption ('colocar um numero depois outro numero e escolher a operacao e ver o resutado')

#n1 = st.number_input('primeiro número')
#n2 = st.number_input('segundo número')
#valor = n1 + n2
#st.caption (valor)

#escolha = st.selectbox ('escolha a operação:', ['+','-','*','/'])

#if st.button('calcular'):
 #   if escolha == '+':
  #      soma = n1 + n2
   #     resultado = soma
    #elif escolha == '-':
     #  sub = n1 - n2
      # resultado = sub   
    #elif escolha == '*':
     #   mult = n1 * n2
      #  resultado = mult  
    #elif escolha == '/':
     #   div = n1 / n2
      #  resultado = div  

#st.success(resultado)

#----------------------ignorar
 
st.title ('Calculo do IMC')

n1 = st.number_input ('Coloque seu peso em kg')
n2 = st.number_input ('Coloque sua altura em metros', value = 0.01)
imc = n1 / (n2*n2)


if st.button('calcular IMC'):
    if imc:
        st.success(imc)
if imc >= 40:
  st.write ('obesidade grau 3')
elif imc > 35:
    st.write ('obesidade grau 2')
elif imc > 30:
    st.write ('obesidade grau 1')
elif imc > 25:
    st.write ('sobrepeso')
elif imc >18.5:
    st.write ('peso ideal')
elif imc <18.5:
    st.write ('abaixo do peso')      

# ------------------------------------------------
# exc 3
# Formulario

st.title ('Casdastro Simples')

nome = st.text_input('Nome: ')
idade = st.number_input('Idade: ')
email = st.text_input('E-mail: ')
altura = st.number_input('Altura: ')

if st.button ('Cadastrar'):
    st.success ('Cadastro feito com sucesso')

#----------------------------------------------------
# exc 4
# tabuada
st.title ('Tabuada')
numero = st.number_input('numero: ')

if st.button('Calcular'):
 for x in range(0,11): #o loop para no 11, entao vai ate o 10 somente 
    calculo = x * numero
   
    #st.write(x,'X', numero, '-', calculo) e uma forma de fazer ou desse outro jeito q ta embaixo
    
    st.write(f'{x} x {numero} = {calculo}')


#-----------------------------------------------------
# exc 5
#
