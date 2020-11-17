import streamlit as st

st.title("Streamlit Crash course")
st.header("Simple Header")
st.sidebar.header("Example de Side Bar")
st.sidebar.text("Hello")
st.text("For a simple text")
st.markdown("#### A Markdown ")
st.success("Successful")
st.info("This is an info alert ")
st.warning("This is a warning ")
st.error("This shows an error ")
# st.help(range())
# st.write("Text with write")
# st.write("Python Range with write",range(10))
# st.text("Display JSON")
# dico={'name':'hello','age':34}
# st.json(dico)
st.button("Simple Button")
st.text("Une check box")

if st.checkbox("Show/Hide"):
    #do some action
    st.text("Some actions")


status = st.radio("Ton statut",('Active','Inactive'))
if status == 'Active':
    st.text("OK t'es Actif(ve)")
else:
    st.warning("Et un petit warning")

st.text("Petite boite de selection")

occupation = st.selectbox("Ton poste",['Data Scientist','Programmer','Doctor','Businessman'])
st.write("So, you are a ",occupation)

st.text("La selection multiple")
# MultiSelect
location = st.multiselect("Ou es tu ?",("Paris","London","New York","Accra","Kiev","Berlin","New Delhi", "Montpellier"))
st.write("You selected",len(location),"location")

salary = st.slider("Ton score aux QCM  :P  ",0,100)

@st.cache
def ma_fonction_a_garder_en_cache():
    return 0

import seaborn 

@st.cache
def load_data(name):
    """ Load dataset from seaborn
        See the available list here : https://github.com/mwaskom/seaborn-data
    """
    return seaborn.load_dataset(str(name))

#utilisation de la fonction load_data()
df = load_data('iris')


# Seaborn Plot
if st.checkbox("Correlation Plot with Annotation[Seaborn]"):
    st.write(seaborn.heatmap(df.corr(),annot=True))
    st.pyplot()