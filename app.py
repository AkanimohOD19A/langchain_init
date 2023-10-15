from langchain.llms import OpenAI
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.chat_models import ChatOpenAI

from langchain.callbacks import StreamlitCallbackHandler
import streamlit as st

st_callback = StreamlitCallbackHandler(st.container())

llm = OpenAI(openai_api_key=st.secrets["OPENAI_API_KEY"],
             temperature=0, streaming=True)
tools = load_tools(["ddg-search"])
agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)
# chat_model = ChatOpenAI(openai_api_key="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")


if prompt := st.chat_input():
    st.chat_message("user").write(prompt)
    with st.chat_message("assistant"):
        st_callback = StreamlitCallbackHandler(st.container())
        response = agent.run(prompt, callbacks=[st_callback])
        st.write(response)

st.write("Made with ❤️‍🔥| AfroLogicInsect")