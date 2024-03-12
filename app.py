import streamlit as st
# This is to load the environment tokens in my main file without using them publicly
from dotenv import load_dotenv

from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplates import css, bot_template, user_template
from langchain.llms import HuggingFaceHub 

# Function to loop through all pdfs uploaded and extract the raw text in the pdfs
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    
    return text


# To convert the entire text into chunks of text
def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator = "\n",
        chunk_size = 1000,
        chunk_overlap = 200,
        length_function = len
    )
    chunks = text_splitter.split_text(text)
    return chunks

# The vector store to store the data and embeddings
def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    # embeddings = HuggingFaceInstructEmbeddings(model_name = "hkunlp/instructor-xl")
    vectorstore = FAISS.from_texts(texts = text_chunks, embedding = embeddings)
    return vectorstore


def get_conversation_chain(vectorstore):
    llm = ChatOpenAI()
    # llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature":0.5, "max_length":512})
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages = True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm = llm,
        retriever = vectorstore.as_retriever(),
        memory = memory,
    )
    return conversation_chain


def handle_userinput(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']


    for i, message in enumerate(st.session_state.chat_history):
        if i%2 == 0:
             st.write(user_template.replace("{{MSG}}", message.content), unsafe_allow_html= True)
        else:
            st.write(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html= True)


def main():
    load_dotenv()
    st.set_page_config(page_title='PDF Chatbot', page_icon=':books:', layout='wide')
    
    st.write(css, unsafe_allow_html=True)
    if "conversation" not in st.session_state:
        st.session_state.conversation = None

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    

    st.header(" Your PDF Buddy :books:")
    user_question = st.text_input("Ask a Question :")
    if user_question:
        handle_userinput(user_question)
    # st.write(user_template.replace("{{MSG}}", "Hello Robot"), unsafe_allow_html= True)
    # st.write(bot_template.replace("{{MSG}}", "Hello Human"), unsafe_allow_html= True)
    
    # For uploading pdf document
    with st.sidebar:
        st.subheader("Your Document")
        pdf_docs = st.file_uploader("Upload your pdfs here and click on 'Process'", type=['pdf'], accept_multiple_files= True)
        if(st.button("Process")):
            with st.spinner("Processing your pdfs"): # GIves a loadig animation
                # get the pdf text
                raw_text = get_pdf_text(pdf_docs)
                
                # get the text chunks
                text_chunks = get_text_chunks(raw_text)
                # st.write(text_chunks)

                # to create our vector store with embeddings
                vectorstore = get_vectorstore(text_chunks)

                # create conversation chain
                st.session_state.conversation  = get_conversation_chain(vectorstore)




if __name__ == '__main__':
    main()