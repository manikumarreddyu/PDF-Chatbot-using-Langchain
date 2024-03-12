# Chatbot-using-Langchain

## Chat with PDFs using OpenAI and Langchain


## Table of Contents
- Introduction
- Project Overview
- Features
- Installation
- Usage
- How it works
- Acknowledgements
- License

## Introduction
Welcome to the Chat with PDFs project! This project utilizes the power of OpenAI's language model and Langchain to enable users to interactively chat and extract information from multiple PDF documents. The goal is to make it easier for users to get quick insights from various PDF files without the need to read each document manually.

## Project Overview
The Chat with PDFs project is built on top of two powerful technologies: OpenAI and Langchain.

### OpenAI
OpenAI provides state-of-the-art language models like GPT-3.5, which allows us to generate human-like responses and hold natural conversations with the system. By leveraging OpenAI's API, our project can understand user queries, analyze the content of PDFs, and provide relevant responses.

### Langchain
Langchain is a powerful library designed for processing and extracting information from various types of documents. It allows us to convert PDFs into machine-readable text, perform document summarization, and extract key information. Langchain serves as a valuable backend tool for our project to handle the complexity of dealing with PDFs.

## Features
- Chat with the system and ask questions related to the content of multiple PDF documents.
- Extract key information and summaries from the PDFs.
- Support for a wide range of topics and document types.

## Installation
To get started with the Chat with PDFs project, follow these installation steps:

### Clone the repository:
```
git clone https://github.com/yourusername/Chat-with-PDFs.git
cd Chat-with-PDFs
```
### Install the required dependencies:
```
pip install -r requirements.txt
```
### Set up the OpenAI API key
To use the OpenAI language model, you'll need to obtain an API key from OpenAI. Once you have the API key, create a file named .env in the root of the project and add the following line:
```
OPENAI_API_KEY=your_openai_api_key_here
Replace your_openai_api_key_here with your actual API key.
```

### Run the application:
```
streamlit run app.py
```

## Usage
After installing the project and running the application, you can interact with the system using the command-line interface or a web-based UI. The system will prompt you to ask questions related to the PDF documents you want to analyze.

## How it works
The application follows these steps to provide responses to your questions:

- PDF Loading: The app reads multiple PDF documents and extracts their text content.

- Text Chunking: The extracted text is divided into smaller chunks that can be processed effectively.

- Language Model: The application utilizes a language model to generate vector representations (embeddings) of the text chunks.

- Similarity Matching: When you ask a question, the app compares it with the text chunks and identifies the most semantically similar ones.

- Response Generation: The selected chunks are passed to the language model, which generates a response based on the relevant content of the PDFs.

![Project Architecture](https://github.com/Sakalya100/Chatbot-using-Langchain/assets/70064084/ef84a6ae-63c1-41d7-8cf0-78c2c7e9447f)


## Video Demo
https://github.com/Sakalya100/Chatbot-using-Langchain/assets/70064084/26fc8e1d-33e1-4ed1-9e55-ea01e08d3726


## Acknowledgements
We would like to express our gratitude to the developers and maintainers of OpenAI and Langchain for providing the tools and technologies that made this project possible.

## License
This project is licensed under the MIT License.

Thank you for using the Chat with PDFs project! If you have any questions or feedback, please don't hesitate to reach out to me [Sakalya](https://github.com/Sakalya100/). Happy document chatting!

