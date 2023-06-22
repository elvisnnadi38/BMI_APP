import streamlit as st
from PIL import Image
st.header('MY BMI APP')
img = Image.open('bmi.jpg')
st.image(img)

weight = st.number_input('WHAT DO YOU WEIGH (KG)', step = 0.1)
height = st.number_input('HOW TALL ARE YOU(M)')

def BMI(w,h):
    bmi = round(w/h**2,2)
    return bmi


def rating(b):
    if b>25:
        st.write('you are over weight')
    elif 18.4<b<25.1:
        st.write('you are doing well keep it up')
    else:
        st.write('you are underweight')

if st.button('calculte'):
    score= BMI(weight,height)
    st.write(score)
    rate = rating(score)

