import streamlit as st
import pandas as pd
import numpy as np

st.title('Subtraction of 2 given numbers')

x = st.number_input('x')
y = st.number_input('y')
st.write('Subtraction is', x-y)