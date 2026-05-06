import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI Code Assistant", page_icon="💻", layout="wide")

st.markdown("""
<style>
    .stTextArea textarea {
        font-family: 'Courier New', monospace;
        font-size: 14px;
        background-color: #1e1e1e;
        color: #d4d4d4;
    }
</style>
""", unsafe_allow_html=True)

st.title("💻 AI Code Assistant")
st.caption("Code likho — AI real-time help karega!")

@st.cache_resource
def get_client():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        st.error("GROQ_API_KEY nahi mili! .env file mein daalo.")
        st.stop()
    return Groq(api_key=api_key)

client = get_client()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ── Layout: Editor + AI side by side ─────────────────────────
left, right = st.columns(2)

with left:
    st.subheader("📝 Code Editor")
    language = st.selectbox("Language:", ["Python", "JavaScript", "Java", "C++", "C", "TypeScript"])
    code = st.text_area(
        "Code likho yahan:",
        height=450,
        placeholder="Yahan code likhna shuru karo...",
        label_visibility="collapsed"
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        suggest_btn = st.button("💡 Suggest karo", use_container_width=True, type="primary")
    with col2:
        error_btn = st.button("🐛 Errors dhundo", use_container_width=True)
    with col3:
        complete_btn = st.button("✅ Complete karo", use_container_width=True)

with right:
    st.subheader("🤖 AI Suggestions")

    def ask_ai(prompt):
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an expert coding assistant like GitHub Copilot. "
                        "Help the user write better code. "
                        "Explain in Hinglish (Hindi + English mix). "
                        "Always show code in proper code blocks."
                    )
                },
                {"role": "user", "content": prompt}
            ],
            max_tokens=2048,
            temperature=0.1,
        )
        return response.choices[0].message.content

    if not code.strip():
        st.info("👈 Pehle code editor mein kuch likho!")

    # 💡 Suggest button
    if suggest_btn:
        if not code.strip():
            st.warning("Pehle code likho!")
        else:
            with st.spinner("AI soch raha hai..."):
                result = ask_ai(
                    f"Yeh {language} code dekho aur improvements suggest karo:\n```{language}\n{code}\n```"
                )
            st.markdown(result)

    # 🐛 Error button
    if error_btn:
        if not code.strip():
            st.warning("Pehle code likho!")
        else:
            with st.spinner("Errors dhundh raha hoon..."):
                result = ask_ai(
                    f"Yeh {language} code mein saare errors, bugs aur warnings dhundo. "
                    f"Line number bhi batao aur fixed code bhi do:\n```{language}\n{code}\n```"
                )
            st.markdown(result)

    # ✅ Complete button
    if complete_btn:
        if not code.strip():
            st.warning("Pehle code likho!")
        else:
            with st.spinner("Code complete kar raha hoon..."):
                result = ask_ai(
                    f"Yeh {language} code incomplete lagta hai — isko complete karo aur "
                    f"poora working code do:\n```{language}\n{code}\n```"
                )
            st.markdown(result)

# ── Chat Section ──────────────────────────────────────────────
st.divider()
st.subheader("💬 AI se Seedha Pucho")

for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if question := st.chat_input("Code ke baare mein kuch bhi pucho..."):
    st.session_state.chat_history.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Soch raha hoon..."):
            context = f"User ka current code:\n```{language}\n{code}\n```\n\n" if code.strip() else ""
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are an expert coding assistant. "
                            "Answer in Hinglish (Hindi + English mix). "
                            f"{context}"
                        )
                    },
                    *[{"role": m["role"], "content": m["content"]} for m in st.session_state.chat_history],
                ],
                max_tokens=2048,
                temperature=0.1,
            )
            answer = response.choices[0].message.content
            st.markdown(answer)

    st.session_state.chat_history.append({"role": "assistant", "content": answer})
