import streamlit as st
import joblib
import pandas as pd
import base64

# Model load function ke bahar rakh sakte ho, taaki baar-baar load na ho
model = joblib.load("spam_detection.pkl")

def run_spam_classifier():
 

    # Background set karne ka function

    st.markdown("""
        <div style="background-color:#87CEFA;border-radius:10px;text-align:center;">
            <h1>⚠️SPAM DETECTION ANALYSIS</h1>
        </div>
    """, unsafe_allow_html=True)


    # Input message
    msg = st.text_input(
        "To solve your spam protection is important for us...",
        placeholder="💬Enter your message here..."
    )

    if st.button("predict",key="detection_predict"):
        resp = model.predict([msg])
        if resp[0] == "spam":
            st.markdown("<h2 style='color:red;'>⚠️ Spam</h2>", unsafe_allow_html=True)
        else:
            st.markdown("<h2 style='color:green;'>✔️ Not Spam</h2>", unsafe_allow_html=True)
            st.balloons()

    # File upload
    left_col, right_col = st.columns([6, 1])
    with left_col:
        st.markdown("📄 **Upload CSV or TXT file**")
        path = st.file_uploader(" ", type=['csv', 'txt'], key="detection_file")

    with right_col:
        predict_clicked = st.button("Predict", key="predict_btn3")

    if path is not None:
        df = pd.read_csv(path, names=["Msg"], sep="\t")
        df_col1, df_col2 = st.columns([1, 1])

        with df_col1:
            st.markdown("### 📥 Uploaded Data")
            st.dataframe(df, width=500)

        with df_col2:
            if predict_clicked:
                df["Detection"] = model.predict(df.Msg)
                df["Detection"] = df["Detection"].map({"spam": "⚠️ Spam", "ham": "✔️ Not Spam"})
                st.markdown("### 🤖 Predicted Detection")
                st.dataframe(df, width=500)
            else:
                st.markdown("### 🤖 Predicted Detection")
                st.info("Click **Detect** to analyze messages.")
