import streamlit as st
from openai import OpenAI

st.title("😀인공지능(Artificial Intelligence)")

# 탭 생성 : 첫번째 탭의 이름은 Tab A 로, Tab B로 표시합니다.
tab1, tab2, tab3 = st.tabs(['인공지능 역사','머신러닝', '챗GPT'])

with tab1:
    # tab A 를 누르면 표시될 내용
    st.write("")
    st.subheader('1. 😀인공지능이란?')
    st.markdown("인공지능이란 문제 해결을 위해 대상을 **인식**하고 필요한 부분을 **학습**하며, 논리적인 "
                " **판단**과 **추론**하는 능력을 말한다. ")
    st.markdown("인공지능(Ari Intelligenc)이란 용어는 1956년 다트머스 컨퍼런스에서 **존 매카시**가 최초로 주장하였다.")

    st.subheader('2. 인공지능의 역사')
    st.markdown(':red[**① 인공지능의 탄생**]: 인공지능이라는 용어는 1956년 다트머스 회의에서 존 매카시가 최초로 주장하였으며,'
                '1950년대 전후로 컴퓨터가 등장하고 **앨런 튜링**이 생각하는 기계에 대한 아이디어를 발표하면서 인공지능 기술이 주목받기 시작하였다. ')
    

with tab2:
    # tab B를 누르면 표시될 내용
    st.write("")
    st.subheader('1.인공지능&머신러닝&딥러닝')
    
    
    
with tab3:
    # tab B를 누르면 표시될 내용
    st.title("💬 Chatbot")
    st.caption("🚀 A Streamlit chatbot powered by OpenAI")
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input():
    #if not openai_api_key:
    #    st.info("Please add your OpenAI API key to continue.")
    #    st.stop()

        client = OpenAI(api_key='sk-proj-OUdVkViMxKBaQnp2GnIWT3BlbkFJzY9CHGiBlP9w6pniUQde')
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
        msg = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": msg})
        st.chat_message("assistant").write(msg)



