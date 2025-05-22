#modules for web and langchain
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
# api load
load_dotenv()
#api model
app=ChatOpenAI(model="gpt-4o-mini",temperature=1.5)
#web designing
st.header("Mini SearchEngine")
st.subheader("Welcome Everyone ! This is a LLM model(GenAI) developed from ChatGpt using Langchain Technology.")
st.sidebar.header("Introduction")
st.sidebar.text("This is a LLM model developed from Langchain Technology.It Was build by using api key of chatgpt.Whatever question you ask to this model ,it gives the question on the basis of chatgpt answer.")
st.sidebar.header("About Developer")
st.sidebar.text("This model is build by Mr Suraj Kumar Jha.He is a Student with curiosity to learn new technology.He learnt python programming a lot.")
st.sidebar.subheader("Developer Contact\nEmail:-Zhasuraj31@gmail.com")
question=st.text_input("Ask Questions")

result=app.invoke(question)
st.write(result.content)
