**Schnell Energy Chatbot - RAG (Retrieve-Augment-Generate)**
This repository contains the codebase for the Schnell Energy Chatbot, designed to assist in the installation, maintenance, and monitoring of smart lighting devices for the Luminator 3.7.0 application. The chatbot uses a Retrieve-Augment-Generate (RAG) architecture and is powered by LangChain, FAISS, and OpenAI GPT-4.


**The chatbot provides answers to maintenance-related questions by retrieving relevant documents stored in a FAISS (Facebook AI Similarity Search) index. The system is designed to:**

1,Retrieve relevant text and table data from indexed documents.
2,Augment the user query with the retrieved context.
3,Generate an appropriate response using the GPT-4 model.

**Folder Structure**
├── app.py                     # Main FastAPI application
├── Dockerfile                 # Docker configuration for deployment
├── requirements.txt           # Python dependencies
├── faiss_index/               # FAISS index files
│   ├── index.faiss
│   └── index.pkl
├── templates/                 
│   └── index.html             # Web interface template
├── .env                       # Environment variables
├── README.md                  # Project documentation

**Setup and Installation**
**Prerequisites**
Python 3.12+
Docker (for containerized deployment)

1. Clone the Repository(check with correct URL)
   git clone https://github.com/username/RAG-chatbot.git
cd schnell-chatbot

2. Set Up a Virtual Environment
   python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install Dependencies
   pip install -r requirements.txt

4. Set Environment Variables
   OPENAI_API_KEY=sk-your-openai-api-key

**Running the Application**

uvicorn app:app --host 0.0.0.0 --port 9000
(Run the FastAPI application using uvicorn:)

**Docker Deployment**
1. Build the Docker Image

docker build -t myfastapi-app .

2. Run the Docker Container

docker run -d -p 9000:9000 --name myfastapi-container myfastapi-app

3. Stop and Remove the Container

docker stop myfastapi-container
docker rm myfastapi-container




