import streamlit as st
import time
import os

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(
    page_title="BAREL VOX - IA Éthique BTP",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- STYLES CSS PERSONNALISÉS ---
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #E85D04; /* Orange Barel/Ethan */
        text-align: center;
        font-weight: bold;
        margin-bottom: 1rem;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 3rem;
    }
    /* Cadre propre autour des avatars */
    .stChatMessage .stChatMessageAvatar {
        border: 2px solid #f0f2f6;
        border-radius: 50%;
        background-color: white;
    }
</style>
""", unsafe_allow_html=True)

# --- GESTION DES AVATARS ---
def get_avatar(filename, fallback_emoji):
    if os.path.exists(f"assets/{filename}"):
        return f"assets/{filename}"
    return fallback_emoji

AVATARS = {
    "user": "👤",
    "avenor": get_avatar("avenor.png", "👑"),
    "roy": get_avatar("roy.png", "👀"),
    "liorah": get_avatar("liorah.png", "⚖️"),
    "aurivna": get_avatar("aurivna.png", "💎"),
    "ethan": get_avatar("ethan.png", "🛡️"),
}

# --- INITIALISATION SESSION STATE ---
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Message d'accueil Avenor
    st.session_state.messages.append({
        "role": "assistant",
        "name": "Avenor",
        "avatar": AVATARS["avenor"],
        "content": "Bonjour Stéphane. L'équipe du Conseil OEE est au complet et prête à analyser. Veuillez déposer le DCE pour lancer la session."
    })

if "analysis_done" not in st.session_state:
    st.session_state.analysis_done = False

# --- SIDEBAR (IDENTITÉ BAREL) ---
with st.sidebar:
    # LOGO BAREL (En haut à gauche)
    if os.path.exists("assets/barel.png"):
        st.image("assets/barel.png", width=180) # Ajuste la taille si besoin
    else:
        st.title("🏗️ BAREL VOX")
    
    st.markdown("---")
    st.markdown("### 🧬 LE CONSEIL OEE")
    
    # Indicateurs de statut (pour faire pro)
    cols = st.columns([1, 4])
    with cols[0]: st.write("👀")
    with cols[1]: st.caption("**Roy** (Vision & OCR)")
    
    cols = st.columns([1, 4])
    with cols[0]: st.write("⚖️")
    with cols[1]: st.caption("**Liorah** (Juridique)")
    
    cols = st.columns([1, 4])
    with cols[0]: st.write("💎")
    with cols[1]: st.caption("**Aurivna** (Data & Structure)")
    
    cols = st.columns([1, 4])
    with cols[0]: st.write("🛡️")
    with cols[1]: st.caption("**Ethan** (Risques)")
    
    cols = st.columns([1, 4])
    with cols[0]: st.write("👑")
    with cols[1]: st.caption("**Avenor** (Synthèse)")
    
    st.markdown("---")
    if st.button("🔄 Nouvelle Analyse"):
        st.session_state.messages = []
        st.session_state.analysis_done = False
        st.rerun()

# --- HEADER PRINCIPAL ---
# On peut mettre le logo Barel ici aussi si tu veux, mais Sidebar c'est mieux
st.markdown('<div class="main-header">BAREL VOX</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Analyse Augmentée de DCE par Intelligence Artificielle Distribuée</div>', unsafe_allow_html=True)

# --- AFFICHAGE DE L'HISTORIQUE CHAT ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"], avatar=msg["avatar"]):
        st.markdown(f"**{msg['name']}**")
        st.write(msg["content"])

# --- INPUT UTILISATEUR (UPLOAD) ---
uploaded_file = st.file_uploader("📂 Déposez le dossier de consultation (PDF, ZIP)...", type=['pdf', 'zip'], disabled=st.session_state.analysis_done)

# --- LE COEUR DU RÉACTEUR (SCÉNARIO) ---
if uploaded_file and not st.session_state.analysis_done:
    
    # 1. Stéphane parle
    user_msg = f"Voici le dossier **{uploaded_file.name}**. Lancez l'analyse complète."
    st.session_state.messages.append({"role": "user", "name": "Stéphane", "avatar": AVATARS["user"], "content": user_msg})
    with st.chat_message("user", avatar=AVATARS["user"]):
        st.write(user_msg)

    # 2. Séquence d'analyse (Ralentie pour le réalisme)
    # On utilise un conteneur vide pour afficher les étapes de chargement
    status_placeholder = st.empty()
    
    with status_placeholder.status("🚀 Initialisation du protocole OEE...", expanded=True) as status:
        
        # --- PHASE 1 : ROY (Vision) ---
        status.write("👀 Roy : Lecture OCR et extraction des plans...")
        # Pause réaliste (Lecture du fichier)
        time.sleep(4) 
        
        msg_roy = "Scan terminé. J'ai extrait 45 pages de texte brut et isolé 3 plans techniques (RDC, R+1, Coupes). La résolution est optimale (300 DPI). Je dispatch les données aux experts."
        st.session_state.messages.append({"role": "assistant", "name": "Roy (Vision)", "avatar": AVATARS["roy"], "content": msg_roy})
        # Affichage du message dans le chat
        with st.chat_message("assistant", avatar=AVATARS["roy"]):
            st.markdown("**Roy (Vision)**")
            st.write(msg_roy)
            
        # --- PHASE 2 : LIORAH (Juridique) ---
        status.write("⚖️ Liorah : Analyse contractuelle (CCAP/CCTP)...")
        # Pause plus longue (Analyse complexe)
        time.sleep(5)
        
        msg_liorah = """**Rapport Juridique :**
- ✅ **Conformité** : Les assurances décennales requises sont standards.
- ⚠️ **Point de Vigilance** : L'article 4.2 du CCAP mentionne des pénalités de retard **non plafonnées**. C'est un risque financier illimité pour l'entreprise.
- ℹ️ **Indexation** : Clause de révision BT01 validée."""
        st.session_state.messages.append({"role": "assistant", "name": "Liorah (Juridique)", "avatar": AVATARS["liorah"], "content": msg_liorah})
        with st.chat_message("assistant", avatar=AVATARS["liorah"]):
             st.markdown("**Liorah (Juridique)**")
             st.write(msg_liorah)

        # --- PHASE 3 : AURIVNA (Data) ---
        status.write("💎 Aurivna : Vérification des métrés et normes...")
        # Pause longue (Calculs)
        time.sleep(5)
        
        msg_aurivna = """**Analyse Technique & Data :**
- 🏗️ **Incohérence Détectée** : Le CCTP Lot Gros Œuvre indique une dalle de 20cm, mais le Plan R+1 mentionne 18cm. À clarifier avant chiffrage.
- 📏 **Métrés Automatiques** :
    - Béton B25 : ~450 m³
    - Acier HA : ~12.5 tonnes
- 💾 **Export** : Tableau des quantitatifs généré (Excel)."""
        st.session_state.messages.append({"role": "assistant", "name": "Aurivna (Data)", "avatar": AVATARS["aurivna"], "content": msg_aurivna})
        with st.chat_message("assistant", avatar=AVATARS["aurivna"]):
             st.markdown("**Aurivna (Data)**")
             st.write(msg_aurivna)

        # --- PHASE 4 : ETHAN (Risques) ---
        status.write("🛡️ Ethan : Audit des risques et planning...")
        time.sleep(4)
        
        msg_ethan = "Je prends le relais. Analyse Logique : Le planning prévisionnel (6 mois) est trop tendu. Il ne tient pas compte des délais de séchage en période hivernale (Zone B). **Risque critique de glissement : +3 semaines.**"
        st.session_state.messages.append({"role": "assistant", "name": "Ethan (Risques)", "avatar": AVATARS["ethan"], "content": msg_ethan})
        with st.chat_message("assistant", avatar=AVATARS["ethan"]):
             st.markdown("**Ethan (Risques)**")
             st.write(msg_ethan)

        status.update(label="✅ Analyse du Conseil terminée", state="complete", expanded=False)

    # --- PHASE 5 : AVENOR (Synthèse) ---
    # Petite pause avant la conclusion du chef
    time.sleep(2)
    
    msg_avenor = """🟠 **SYNTHÈSE DU CONSEIL : VIGILANCE REQUISE**

Stéphane, l'analyse croisée révèle un dossier techniquement solide mais contractuellement risqué.

1.  **Risque Financier (Liorah)** : Il faut impérativement négocier le plafond des pénalités.
2.  **Incertitude Technique (Aurivna)** : L'épaisseur de dalle (20cm vs 18cm) impacte le prix du béton.
3.  **Risque Planning (Ethan)** : Le délai est irréaliste en hiver.

**Ma Recommandation :** Ne pas chiffrer sans avoir envoyé une demande de précision (Q/R) au Maître d'Ouvrage sur ces 3 points. Je prépare le brouillon ?"""
    
    st.session_state.messages.append({"role": "assistant", "name": "Avenor (Le Chef)", "avatar": AVATARS["avenor"], "content": msg_avenor})
    with st.chat_message("assistant", avatar=AVATARS["avenor"]):
        st.markdown("**Avenor (Le Chef)**")
        st.write(msg_avenor)

    st.session_state.analysis_done = True
    # Pas de rerun ici pour laisser l'utilisateur lire tranquillement
    # st.rerun() 

# --- INPUT UTILISATEUR APRÈS ANALYSE ---
if st.session_state.analysis_done:
    if prompt := st.chat_input("Votre ordre au Conseil ?"):
        st.session_state.messages.append({"role": "user", "name": "Stéphane", "avatar": AVATARS["user"], "content": prompt})
        with st.chat_message("user", avatar=AVATARS["user"]):
            st.write(prompt)
        
        # Réponse de fin de démo
        st.write("Avenor : Bien reçu Stéphane. Dossier clôturé.")