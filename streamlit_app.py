import openai
import streamlit as st

# 🔑 INSERISCI LA TUA API KEY QUI
openai.api_key = os.getenv("OPENAI_API_KEY") 
# 🔹 Titolo dell'app
st.title("👩‍⚕️ Chatbot AI per Caregiver (GPT-4)")

# 🔹 Lista delle malattie disponibili
malattie = [
    "Alzheimer", "Parkinson", "SLA", "Demenza", "Ictus", "Sclerosi Multipla",
    "Diabete", "Cancro", "Insufficienza Cardiaca", "Malattie Rare"
]

# 🔹 Selezione della malattia
malattia = st.selectbox("Seleziona la malattia:", malattie)

# 🔹 Chatbot Function
def caregiver_chatbot(user_input):
    prompt = f"Sei un AI esperto nell'assistenza ai caregiver per pazienti con {malattia}. Rispondi in modo chiaro e utile.\n"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": prompt},
                      {"role": "user", "content": user_input}],
            temperature=0.7,
            request_timeout=20
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"⚠️ Errore: {str(e)}"

# 🔹 Input Utente
user_input = st.text_input("Scrivi un messaggio:")

if st.button("INVIA"):
    if user_input:
        risposta = caregiver_chatbot(user_input)
        st.write(f"**🤖 AI ({malattia}):** {risposta}")
