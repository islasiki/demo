import streamlit as st

# markdown
st.markdown('Streamlit Demo')

# 设置网页标题
st.title('The fatest way to built a python webpage -- streamlit')

# 展示一级标题
st.header('1. install')

st.text('It is easy to install,just need one commend')
code1 = '''pip3 install streamlit'''
st.code(code1, language='bash')


# 展示一级标题
st.header('2. use')

# 展示二级标题
st.subheader('2.1 generate Markdown ')

# 纯文本
st.text('after importing streamlit，just use st.markdown() initialize')

# 展示代码，有高亮效果
code2 = '''import streamlit as st
st.markdown('Streamlit Demo')'''
st.code(code2, language='python')


