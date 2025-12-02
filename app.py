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
        color: #E85D04; /* Orange Barel */
        text-align: center;
        font-weight: bold;
        margin-bottom: 0.5rem;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .sub-header {
        font-size: 1.4rem;
        color: #444;
        text-align: center;
        margin-bottom: 3rem;
        font-weight: 300;
    }
    /* Cadre propre autour des avatars */
    .stChatMessage .stChatMessageAvatar {
        border: 2px solid #f0f2f6;
        border-radius: 50%;
        background-color: white;
    }
    /* Style pour le statut des agents en sidebar */
    .agent-status {
        font-size: 1rem;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# --- GESTION INTELLIGENTE DES AVATARS (FIX LINUX/MAC) ---
def get_avatar(base_name, fallback_emoji):
    # Le serveur Linux est sensible à la casse (Majuscules/Minuscules)
    # On teste toutes les combinaisons possibles pour trouver l'image
    possible_names = [
        base_name,                      # ex: avenor.png
        base_name.capitalize(),         # ex: Avenor.png
        base_name.upper(),              # ex: AVENOR.PNG
        base_name.replace(".png", ".PNG"), # ex: avenor.PNG
        base_name.capitalize().replace(".png", ".PNG") # ex: Avenor.PNG
    ]
    
    for name in possible_names:
        if os.path.exists(f"assets/{name}"):
            return f"assets/{name}"
            
    # Si aucune image n'est trouvée, on renvoie l'émoji
    return fallback_emoji

# Dictionnaire de la Team
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
        "content": "Bonjour Stéphane. L'équipe du Conseil OEE est prête pour l'audit MOE avant publication. Veuillez déposer le DCE pour lancer le contrôle qualité."
    })

if "analysis_done" not in st.session_state:
    st.session_state.analysis_done = False

# --- SIDEBAR (PANNEAU DE CONTRÔLE) ---
with st.sidebar:
    # LOGO BAREL (Test variantes aussi)
    logo_path = None
    for name in ["barel.png", "Barel.png", "Barel.PNG", "barel.PNG"]:
        if os.path.exists(f"assets/{name}"):
            logo_path = f"assets/{name}"
            break
            
    if logo_path:
        st.image(logo_path, width=150)
    else:
        st.title("🏗️ BAREL VOX")
    
    st.markdown("---")
    st.markdown("### 🧬 L'ÉQUIPE ACTIVE")
    
    st.markdown("**Roy** (Vision) : 🟢 Prêt")
    st.markdown("**Liorah** (Juridique) : 🟢 Prêt")
    st.markdown("**Aurivna** (Data) : 🟢 Prêt")
    st.markdown("**Ethan** (Risques) : 🟢 Prêt")
    st.markdown("**Avenor** (Synthèse) : 🟢 En ligne")
    
    st.markdown("---")
    
    if st.button("🔄 Nouvelle Analyse"):
        st.session_state.messages = []
        st.session_state.analysis_done = False
        st.rerun()

    st.caption("Mode : Simulation Démo v1.0")

# --- HEADER PRINCIPAL ---
st.markdown('<div class="main-header">BAREL VOX</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">L\'Intelligence Augmentée Multi-Agents au service des Professionnels</div>', unsafe_allow_html=True)

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

    # 2. Séquence d'analyse
    status_placeholder = st.empty()
    
    with status_placeholder.status("🚀 Initialisation du protocole OEE...", expanded=True) as status:
        
        # --- PHASE 1 : ROY (Vision) ---
        status.write("👀 Roy : Lecture OCR et extraction des plans...")
        time.sleep(8) 
        
        msg_roy = "Scan terminé. J'ai extrait 45 pages de texte brut et isolé 3 plans techniques (RDC, R+1, Coupes). La résolution est optimale (300 DPI). Je dispatch les données aux experts."
        st.session_state.messages.append({"role": "assistant", "name": "Roy (Vision)", "avatar": AVATARS["roy"], "content": msg_roy})
        with st.chat_message("assistant", avatar=AVATARS["roy"]):
            st.markdown("**Roy (Vision)**")
            st.write(msg_roy)
            
        # --- PHASE 2 : LIORAH (Juridique) ---
        status.write("⚖️ Liorah : Analyse de conformité administrative...")
        time.sleep(10)
        
        msg_liorah = """**Rapport Juridique :**
- ✅ **Conformité** : Les assurances décennales requises sont standards.
- ⚠️ **Point de Vigilance** : L'article 4.2 du CCAP mentionne des pénalités de retard **non plafonnées**. C'est un risque financier illimité pour l'entreprise. **Faire valider par MOA.**
- ℹ️ **Indexation** : Clause de révision BT01 validée."""
        st.session_state.messages.append({"role": "assistant", "name": "Liorah (Juridique)", "avatar": AVATARS["liorah"], "content": msg_liorah})
        with st.chat_message("assistant", avatar=AVATARS["liorah"]):
             st.markdown("**Liorah (Juridique)**")
             st.write(msg_liorah)

        # --- PHASE 3 : AURIVNA (Data) ---
        status.write("💎 Aurivna : Croisement Plans vs CCTP...")
        time.sleep(12)
        
        msg_aurivna = """**Analyse Technique & Data :**
- 🏗️ **Incohérence Détectée** : Le CCTP Lot Gros Œuvre indique une dalle de 20cm, mais le Plan R+1 mentionne 23cm. **À clarifier avant envoi.**
- 📏 **Métrés Automatiques** :
    - Béton C25/30 : ~450 m³
    - Acier HA : ~12.5 tonnes
- 💾 **Export** : Tableau des quantitatifs généré (Excel)."""
        st.session_state.messages.append({"role": "assistant", "name": "Aurivna (Data)", "avatar": AVATARS["aurivna"], "content": msg_aurivna})
        with st.chat_message("assistant", avatar=AVATARS["aurivna"]):
             st.markdown("**Aurivna (Data)**")
             st.write(msg_aurivna)

        # --- PHASE 4 : ETHAN (Risques) ---
        status.write("🛡️ Ethan : Simulation planning et aléas...")
        time.sleep(8)
        
        msg_ethan = "Je prends le relais. Analyse Logique : Le planning prévisionnel (6 mois) est trop tendu. Il ne tient pas compte des délais de séchage en période hivernale (Zone B). **Risque critique de glissement : +3 semaines.**"
        st.session_state.messages.append({"role": "assistant", "name": "Ethan (Risques)", "avatar": AVATARS["ethan"], "content": msg_ethan})
        with st.chat_message("assistant", avatar=AVATARS["ethan"]):
             st.markdown("**Ethan (Risques)**")
             st.write(msg_ethan)

        status.update(label="✅ Audit du Conseil terminé", state="complete", expanded=False)

    # --- PHASE 5 : AVENOR (Synthèse) ---
    time.sleep(3)
    
    msg_avenor = """🟠 **SYNTHÈSE DU CONSEIL : VIGILANCE REQUISE**

Stéphane, l'analyse croisée révèle un dossier techniquement solide mais contractuellement risqué.

1.  **Risque Financier (Liorah)** : Il faut impérativement clarifier le plafond des pénalités avec MOA.
2.  **Incertitude Technique (Aurivna)** : L'épaisseur de dalle (20cm vs 23cm) impacte le prix du béton.
3.  **Risque Planning (Ethan)** : Le délai est irréaliste en hiver.

**Ma Recommandation :** Ne pas lancer la publication sans avoir envoyé une demande de précision (Q/R) au Maître d'Ouvrage sur ces 3 points. Je prépare le brouillon ?"""
    
    st.session_state.messages.append({"role": "assistant", "name": "Avenor (Le Chef)", "avatar": AVATARS["avenor"], "content": msg_avenor})
    with st.chat_message("assistant", avatar=AVATARS["avenor"]):
        st.markdown("**Avenor (Le Chef)**")
        st.write(msg_avenor)

    st.session_state.analysis_done = True

# --- INPUT UTILISATEUR APRÈS ANALYSE ---
if st.session_state.analysis_done:
    if prompt := st.chat_input("Votre ordre au Conseil ?"):
        st.session_state.messages.append({"role": "user", "name": "Stéphane", "avatar": AVATARS["user"], "content": prompt})
        with st.chat_message("user", avatar=AVATARS["user"]):
            st.write(prompt)
        
        # Réponse de fin
        st.write("Avenor : Bien reçu Stéphane. Je génère le document Q/R pour le MOA.")