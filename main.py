import streamlit as st

st.write("Hello")
x = st.text_input("Your name:")
st.write(f"Name: {x}")

import pandas as pd
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df


import numpy as np

dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)