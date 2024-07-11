import streamlit as st
import logging
from resume_assistant import generate

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password", value="")

    if not openai_api_key:
            st.info("Please add your OpenAI API key to continue.")
            st.stop()

    st.title("💬 Resume AI Bot")
        
    company = st.text_area(label="1. 지원하려는 기업/직무 (모집공고 링크)", key="company")
    major = st.text_area(label="2. 고등학교 / 대학교 시절 각각 전공이 무엇인가요? 구체적으로 어떤 공부를 했나요?", key="major")
    activity = st.text_area(label="3. 학교를 다닐 때 기억에 남는 활동 경험이 있나요? (다양하고 상세할수록 좋습니다)", key="activity")
    intern = st.text_area(label="4. 인턴 혹은 업무 경험이 있나요? 있다면, 어떤 업무를 얼마나 담당했나요? (다양하고 상세하게)", key="intern")
    experience = st.text_area(label="5. 본인이 어필하고 싶은 성과 혹은 경험이 있나요? (다양하고 상세하게)", key="experience")
    personality = st.text_area(label="6. 본인이 생각하는 본인의 성격 (그에 맞는 적절한 사례가 있으면 적어주세요)", key="personality")
    strength = st.text_area(label="7. 자유롭게 지원하고자 하는 회사에 어필하고 싶은 강점과 경험을 작성해주세요", key="strength")
    example = st.text_area(label="입력할 질문에 대한 예시 작성해주세요", key="example")
        
    
    
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "자소서에서 작성해야할 질문을 입력해주세요."}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if question := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    st.session_state.messages.append({"role": "user", "content": question})
    st.chat_message("user").write(question)

    # result = start_gen(question, , user_id) # question에 대한 대답
    result = generate(company, major, activity, intern, experience, personality, strength, question, example)

    st.chat_message("assistant").write(result)

    st.session_state.messages.append({"role": "assistant", "content": result})

