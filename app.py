import streamlit as st
import base64

# Configuración de la página
st.set_page_config(
    page_title="Mello, Madre de Amor",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar con información del autor
with st.sidebar:
    st.title("Créditos")
    st.markdown("---")
    st.markdown("""
    **Javier Horacio Pérez Ricárdez**  
    **Dedicado a María de los Remedios**  
    **Desde Agua Dulce, Veracruz**
    """)
    st.markdown("---")

# CSS personalizado
st.markdown("""
<style>
    .song-header {
        background: linear-gradient(90deg, #ff9a9e, #fad0c4);
        padding: 25px;
        border-radius: 15px;
        margin-bottom: 30px;
        text-align: center;
        color: white;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    .song-title { font-size: 2.5em; margin-bottom: 0; }
    .song-subtitle { font-size: 1.2em; opacity: 0.9; }
    .verse-container, .chorus-container, .bridge-container, .final-container {
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .verse-container { background-color: #f8f9fa; }
    .chorus-container { background-color: #e3f2fd; border-left: 5px solid #1976d2; }
    .bridge-container { background-color: #fff8e1; border-left: 5px solid #ffa000; }
    .final-container { background-color: #e8f5e9; border-left: 5px solid #43a047; }
    .verse-title, .chorus-title, .bridge-title, .final-title {
        font-size: 1.3em;
        margin-bottom: 10px;
        border-bottom: 2px solid currentColor;
        padding-bottom: 5px;
    }
    .verse-title { color: #e83e8c; }
    .chorus-title { color: #1976d2; }
    .bridge-title { color: #ffa000; }
    .final-title { color: #43a047; }
    .song-line { font-size: 1.1em; line-height: 1.6; margin: 5px 0; }
    .dedication { font-style: italic; text-align: center; color: #6c757d; margin-top: 10px; }
</style>
""", unsafe_allow_html=True)

# Encabezado de la canción
st.markdown("""
<div class="song-header">
    <h1 class="song-title">🎵 Mello, Madre de Amor 🎵</h1>
    <p class="song-subtitle">Homenaje a María de los Remedios</p>
    <p class="dedication">Desde Agua Dulce, Veracruz</p>
</div>
""", unsafe_allow_html=True)

# Reproductor de audio
st.markdown("## 🎧 Escucha la canción")
st.markdown("### Versión a")
try:
    with open("Mello_Madre_de_Amor_a.mp3", "rb") as file:
        st.audio(file.read(), format="audio/mp3")
except FileNotFoundError:
    st.warning("⚠️ No se encontró el archivo 'mello_intro.mp3'. Asegúrate de que esté en la misma carpeta.")

st.markdown("### Versión b")
try:
    with open("Mello_Madre_de_Amor_b.mp3", "rb") as file:
        st.audio(file.read(), format="audio/mp3")
except FileNotFoundError:
    st.warning("⚠️ No se encontró el archivo 'mello_completa.mp3'. Asegúrate de que esté en la misma carpeta.")

# Letra de la canción
st.markdown("""
<div class="verse-container">
    <div class="verse-title">Verso 1</div>
    <p class="song-line">En Agua Dulce floreció una flor,</p>
    <p class="song-line">con manos fuertes y un alma de amor.</p>
    <p class="song-line">María de los Remedios, a ti canto hoy,</p>
    <p class="song-line">madre valiente, ejemplo y sol.</p>
</div>

<div class="verse-container">
    <div class="verse-title">Verso 2</div>
    <p class="song-line">Junto a Salvador formaste un hogar,</p>
    <p class="song-line">con seis estrellas que aprendiste a guiar.</p>
    <p class="song-line">Salvador y Fabián ya están en paz,</p>
    <p class="song-line">pero su luz contigo siempre va.</p>
</div>

<div class="chorus-container">
    <div class="chorus-title">Coro</div>
    <p class="song-line">Mello, dulce madre, mujer sin igual,</p>
    <p class="song-line">te amamos en cada gesto, en cada señal.</p>
    <p class="song-line">Eres raíz, eres cielo, eres canción,</p>
    <p class="song-line">nuestro refugio, nuestra bendición.</p>
</div>

<div class="verse-container">
    <div class="verse-title">Verso 3</div>
    <p class="song-line">María Eugenia, Adriana de Jesús,</p>
    <p class="song-line">Javier que escribe y a ti da su luz.</p>
    <p class="song-line">Aracelio aún recuerda tu voz,</p>
    <p class="song-line">que calma tristezas y habla con Dios.</p>
</div>

<div class="bridge-container">
    <div class="bridge-title">Puente</div>
    <p class="song-line">Tu historia es fuerza, ternura y valor,</p>
    <p class="song-line">te debemos todo, madre de amor.</p>
    <p class="song-line">Aunque algunos ya no estén aquí,</p>
    <p class="song-line">tú los llevas dentro, viven en ti.</p>
</div>

<div class="chorus-container">
    <div class="chorus-title">Coro (Repetición)</div>
    <p class="song-line">Mello, dulce madre, mujer sin igual,</p>
    <p class="song-line">te amamos en cada gesto, en cada señal.</p>
    <p class="song-line">Eres raíz, eres cielo, eres canción,</p>
    <p class="song-line">nuestro refugio, nuestra bendición.</p>
</div>

<div class="final-container">
    <div class="final-title">Final</div>
    <p class="song-line">Hoy es tu día, mamá corazón,</p>
    <p class="song-line">gracias por darnos la vida y el amor.</p>
    <p class="song-line">¡Mello querida, siempre serás…</p>
    <p class="song-line">nuestra más hermosa eternidad!</p>
</div>
""", unsafe_allow_html=True)

# Sección adicional
st.markdown("---")
expander = st.expander("🌸 Sobre esta canción")
with expander:
    st.markdown("""
    <div style="background-color: #f8f9fa; padding: 20px; border-radius: 10px;">
        <h3 style="color: #e83e8c;">Un homenaje musical</h3>
        <p>Esta canción es un tributo a María de los Remedios, conocida cariñosamente como "Mello", 
        una madre ejemplar de Agua Dulce, Veracruz.</p>
        
        <div style="display: flex; justify-content: center; margin: 20px 0;">
            <img src="https://cdn.pixabay.com/photo/2017/08/06/12/06/people-2591874_640.jpg" 
                 style="width: 100%; max-width: 400px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
        </div>
        
        <h4 style="color: #1976d2; margin-top: 20px;">Elementos destacados:</h4>
        <ul style="font-size: 1.1em;">
            <li>💖 Un reconocimiento al amor maternal</li>
            <li>👨‍👩‍👧‍👦 La importancia de la familia</li>
            <li>🌹 La fortaleza y ternura de una madre</li>
            <li>🕊️ El recuerdo de los seres queridos que ya partieron</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Efectos visuales
st.balloons()
