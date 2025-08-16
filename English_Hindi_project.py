import streamlit as st
import joblib
import pandas as pd
import base64

model=joblib.load("eng_Hi_pred.pkl")

def run_language_classifier():
    
    st.markdown("""
        <div style="background-color:burlywood;border-radius:10px;text-align:center;">
            <h1 style="color:black;">English Hindi Language Prediction</h1>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <style>
        .stTextInput input {
            width: 100%;
            padding: 20px;
            font-size: 16px;
            font-weight: bold;
            text-align:left;
            border-radius: 10px;
            border: none;
            background:burlywood;
            color: black;
        }
        .stTextInput input::placeholder {
            color: black;
            opacity: 0.7;
        }
        </style>
    """, unsafe_allow_html=True)
    msg = st.text_input("To solve your lanugage problam is important for us", placeholder="💬Enter your Language here...")

    if st.button("predict",key="language_predict"):
        resp = model.predict([msg])
        if resp == "ENGLISH":
            st.markdown("<h2 style='color:red;'>ENGLISH</h2>", unsafe_allow_html=True)
        else:
            st.markdown("<h2 style='color:green;'>HINDI</h2>", unsafe_allow_html=True)
            st.balloons()

    left_col, right_col = st.columns([6, 1])  # Wider left column to push uploader to extreme left

    with left_col:
        st.markdown("📄 **Upload CSV or TXT file**")
        path = st.file_uploader(" ", type=['csv', 'txt'], key="language_file")  # empty label for cleaner look

    with right_col:
        predict_clicked = st.button("Predict", key="language_pred")

    # If file is uploaded
    if path is not None:
        df = pd.read_csv(path, names=["Msg"])
        
        # Layout for side-by-side DataFrames
        df_col1, df_col2 = st.columns([1, 1])

        with df_col1:
            st.markdown("### 📥 Uploaded Data")
            st.dataframe(df, width=500)

        with df_col2:
            if predict_clicked:
                # Add your actual model prediction here
                df["Language"] = model.predict(df.Msg)
                df["Language"] = df["Language"].map({"ENGLISH": "ENGLISH", "HINDI": "HINDI"})

                st.markdown("### 🤖 Predicted Language")
                st.dataframe(df, width=500)
            else:
                st.markdown("### 🤖 Predicted Languaget")
                st.info("Click **Predict** to analyze Language.")