import streamlit as st

# from langchain_openai import OpenAI

from langchain_openai import ChatOpenAI

# from langchain_core import PromptTemplate, LLMChain

from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage,
)

from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="Chatbot",
    page_icon="🤖"
)

st.subheader(
    "You can ask me anything about the company and I will try to answer your questions."
)

chat = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.5,
    max_tokens=150
)

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:

    system_message = st.text_input(
        label="System role",
        value="You are a helpful assistant."
    )

    user_prompt = st.text_input(
        label="User prompt",
        value="You are a helpful assistant."
    )

    if system_message:

        if not any(
            isinstance(x, SystemMessage)
            for x in st.session_state.messages
        ):
            st.session_state.messages.append(
                SystemMessage(content=system_message)
            )

        if user_prompt:

            st.session_state.messages.append(
                HumanMessage(content=user_prompt)
            )

            with st.spinner("Thinking..."):

                response = chat.invoke(
                    st.session_state.messages
                )

                st.session_state.messages.append(response)


# Display messages

if len(st.session_state.messages) > 1:

    if not isinstance(
        st.session_state.messages[0],
        SystemMessage
    ):
        st.session_state.messages.insert(
            0,
            SystemMessage(content=system_message)
        )

    for x in st.session_state.messages[1:]:

        if isinstance(x, HumanMessage):

            with st.chat_message("user"):
                st.write(x.content)

        elif isinstance(x, AIMessage):

            with st.chat_message("assistant"):
            with st.spinner("Thinking…"):
                answer = chain.invoke(question)
                st.markdown(answer)

                # Show the retrieved chunks for transparency
                with st.expander("🔍 Sources (retrieved chunks)"):
                    for doc in retriever.invoke(question):
                        page = doc.metadata.get("page", "?")
                        st.markdown(f"**Page {page + 1 if isinstance(page, int) else page}**")
                        st.text(doc.page_content[:500])
                        st.divider()

        st.session_state.messages.append({"role": "assistant", "content": answer})
else:
    st.info("👆 Upload a PDF to get started.")