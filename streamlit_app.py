import streamlit as st
import numpy as np
import pandas as pd
# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )
    
# markdown
st.markdown('Streamlit Demo')

# title
st.title('The fatest way to built a python webpage -- streamlit')

# first level title
st.header('1. install')

st.text('It is easy to install,just need one commend')
code1 = '''pip3 install streamlit'''
st.code(code1, language='bash')


# first level title
st.header('2. use')

# second level title
st.subheader('2.1 generate Markdown ')

# text
st.text('after importing streamlit，just use st.markdown() initialize')

# code with highlight
code2 = '''import streamlit as st
st.markdown('Streamlit Demo')'''
st.code(code2, language='python')

#pandas and munpy gnerate data
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)
#generate a variable to store the value first
values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)
st.map(df)

genre = st.radio(
    "What\'s your favorite movie genre",
    ('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
    st.write('You selected comedy.')
else:
    st.write("You didn\'t select comedy.")
