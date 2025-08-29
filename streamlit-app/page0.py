import streamlit as st

# Interface utilisateur avec Streamlit
st.set_page_config(
    layout = "wide",
    page_title = "MovieLens Data Analysis",
    page_icon = "🎬"  # Emoji Unicode directement
)

# Conteneur pour aligner les éléments horizontalement
col1, col2, col3 = st.columns([1, 4, 1])

# Colonne gauche : Image
with col1:
    st.image(
        "https://media.licdn.com/dms/image/v2/C4D03AQHBakAcLxLASQ/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1635349619392?e=1752710400&v=beta&t=PnWBdipi1fnnssiEJ0CRtobrhh0M16-EGvwgWlDm7Nc",
        width = 80,     # Ajustez la taille si nécessaire
        use_container_width = False,
    )

# Colonne centrale : Titre
with col2:
    st.markdown(
        """
        <h1 style='text-align: center; margin-bottom: 0;'>Plateforme de recommandation de films (MovieLens)</h1>
        """,
        unsafe_allow_html = True,
    )

# Colonne droite : Nom et lien LinkedIn
with col3:
    st.markdown(
        """
        <div style='text-align: right;'>
            <a href="https://www.linkedin.com/in/desty-mpassi-matondo/" target="_blank" style='text-decoration: none; color: #0077b5;'>
                <strong>Desty MPASSI MATONDO</strong>
            </a>
        </div>
        """,
        unsafe_allow_html = True,
    )

st.write(" ")
st.write(" ")

# Titre
st.markdown("# **Phase 1 : Développeur Python & Architecte API**")

# Afficher l'image séparément
st.image(
        "https://github.com/DestyM/movie-analytics/blob/41080e2f8c53bfbead03add79888e5a227c63ef2/streamlit-app/img/archi_api.png",
         use_container_width=True
        )

st.markdown(
        """
        <a href="https://github.com/DestyM/movie-backend" target="_blank">
            <button style="background-color: #28a745; color: white; padding: 10px 20px; border: none; border-radius: 8px; font-size: 16px;">
                📦 Voir le code de la Phase 1
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )

st.write(" ")
st.write(" ")
st.write(" ")


# Titre
st.markdown("# **Phase 2 : Data Analyst - Exploration et Visualisation**")
# Afficher l'image séparément
st.image("https://github.com/DestyM/movie-analytics/blob/41080e2f8c53bfbead03add79888e5a227c63ef2/streamlit-app/img/archi_app.png", use_container_width=True)

st.markdown(
        """
        <a href="https://github.com/DestyM/movie-analytics" target="_blank">
            <button style="background-color: #28a745; color: white; padding: 10px 20px; border: none; border-radius: 8px; font-size: 16px;">
                📊 Voir le code de la Phase 2
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )