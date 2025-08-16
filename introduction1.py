import streamlit as st
import base64

def run_introduction1_classifier():
    st.markdown("""
            <div style="text-align:center;">
                <h1 style="color:black;">ML PROJECT HUB</h1>
            </div>
        """, unsafe_allow_html=True)

        # ---------- CSS Styling ----------
    st.markdown("""
            <style>
            .project-button {
                padding: 1.5rem 1.5rem;
                margin: 0rem ;
                border: none;
                background-color: #1f77b4;
                color: white;
                font-size: 0.1 rem;
                border-radius: 8px;
                cursor: pointer;
                text-align: center;
                transition: background-color 0.3s ease;
                width: 100%;
            }
            .project-button:hover {
                background-color: #135b87;
            }
            .title {
                font-size: 3rem;
                font-weight: bold;
                color: black;
                margin-bottom: o.5rem;
            }
            .subtitle {
                font-size: 1.3rem;
                color: #555;
                margin-bottom: 2rem;
            }
            </style>
        """, unsafe_allow_html=True)

        # ---------- Layout ----------
    left_col, right_col = st.columns([1, 2])

        # ---------- Left Column (Image) ----------
    with left_col:
            st.image("rishu.jpg", use_container_width=True)

        # ---------- Right Column (Text + Buttons) ----------
    with right_col:
            st.markdown('<div class="title">Rishabh Kumar Verma</div>', unsafe_allow_html=True)         
            st.markdown('<div class="subtitle">Welcome to the ML Projects Hub.</div>', unsafe_allow_html=True)
        # Add some descriptive text
    st.markdown("""
        Welcome to the **Machine Learning Projects Portal**! 🚀  
        Here, you can explore and interact with various ML models like:

        - 🛡️ **Spam Detection**
        - 🎬 **Movie Recommendation**
        - 🍔 **Food Sentiment Analysis**
        - 🌐 **English-Hindi Text Classifier**

        Choose a project from above to get started.  
        Let the learning begin! 🎓💡
        """)
        

