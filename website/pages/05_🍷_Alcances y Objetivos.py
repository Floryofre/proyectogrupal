import streamlit as st
import pandas as pd
import pydeck as pdk
import os
from urllib.error import URLError

# Alcances y Objetivos
st.header('Alcances y Objetivos')
st.write("Vamos a tomar los datos de todos los estados de Estados Unidos como primera instancia, porque el volumen de los mismos nos ayuda para un mejor análisis...")
