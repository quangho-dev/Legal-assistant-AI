import streamlit as st
import asyncio
from main import main  # your async/sync LLM pipeline

st.set_page_config(
    page_title="AI Legal Assistant",
    page_icon="⚖️",
    layout="wide"
)

st.title("⚖️ Trợ lý AI về luật")

# -----------------------------
# Session State
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# Helpers
# -----------------------------

def run_query(query: str):
    """Handle both sync and async main()"""
    try:
        if asyncio.iscoroutinefunction(main):
            return asyncio.run(main(query))
        else:
            return main(query)
    except RuntimeError:
        # fallback when event loop already running
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        return loop.run_until_complete(main(query))

# -----------------------------
# Display chat history
# -----------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -----------------------------
# Chat input
# -----------------------------
user_input = st.chat_input("Nhập câu hỏi pháp lý của bạn...")

if user_input:
    # Save user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate assistant response
    with st.chat_message("assistant"):
        with st.spinner("Đang phân tích luật..."):
            response = run_query(user_input)

            # Optional: stream effect
            placeholder = st.empty()
            full_text = ""

            for chunk in str(response):
                full_text += chunk
                placeholder.markdown(full_text + "▌")
            placeholder.markdown(full_text)

    # Save assistant message
    st.session_state.messages.append({"role": "assistant", "content": str(response)})

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.header("⚙️ Tùy chọn")

    if st.button("🧹 Xóa hội thoại"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")
    st.markdown("### 💡 Gợi ý câu hỏi")
    st.markdown("""
    - Quy định về hợp đồng dân sự là gì?
    - Tranh chấp đất đai xử lý thế nào?
    - Quyền thừa kế theo pháp luật Việt Nam?
    - Điều kiện ly hôn đơn phương?
    """)
