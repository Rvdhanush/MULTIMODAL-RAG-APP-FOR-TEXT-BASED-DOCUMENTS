# **Schnell Energy Chatbot - RAG (Retrieve-Augment-Generate)**

This repository contains the codebase for the **Schnell Energy Chatbot**, designed to assist in the installation, maintenance, and monitoring of smart lighting devices for the **Luminator 3.7.0** application. The chatbot leverages a **Retrieve-Augment-Generate (RAG)** architecture, powered by **LangChain**, **FAISS**, and **OpenAI GPT-4**.

## **System Overview**
The chatbot provides answers to maintenance-related questions by retrieving relevant documents stored in a FAISS (Facebook AI Similarity Search) index. The system is designed to:

1. **Retrieve** relevant text and table data from indexed documents.  
2. **Augment** the user query with the retrieved context.  
3. **Generate** an appropriate response using the GPT-4 model.

## **Folder Structure**

```
├── app.py                     # Main FastAPI application
├── Dockerfile                 # Docker configuration for deployment
├── requirements.txt           # Python dependencies
├── faiss_index/               # FAISS index files
│   ├── index.faiss
│   └── index.pkl
├── templates/                 # Web interface template
│   └── index.html
├── .env                       # Environment variables
├── README.md                  # Project documentation
```

## **Setup and Installation**

### **Prerequisites**
- Python 3.12+
- Docker (for containerized deployment)

### **1. Clone the Repository**  
Replace `https://github.com/username/RAG-chatbot.git` with the correct URL.

```bash
git clone https://github.com/username/RAG-chatbot.git
cd RAG-chatbot
```

### **2. Set Up a Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### **3. Install Dependencies**

```bash
pip install -r requirements.txt
```

### **4. Set Environment Variables**  
Create a `.env` file in the root directory and add your OpenAI API key:

```bash
OPENAI_API_KEY=sk-your-openai-api-key
```

## **Running the Application Locally**

Run the FastAPI application using **Uvicorn**:

```bash
uvicorn app:app --host 0.0.0.0 --port 9000
```

Access the chatbot at: [http://localhost:9000](http://localhost:9000)

## **Docker Deployment**

### **1. Build the Docker Image**

```bash
docker build -t myfastapi-app .
```

### **2. Run the Docker Container**

```bash
docker run -d -p 9000:9000 --name myfastapi-container myfastapi-app
```

Access the chatbot at: [http://localhost:9000](http://localhost:9000)

### **3. Stop and Remove the Container**

```bash
docker stop myfastapi-container
docker rm myfastapi-container
```

## **Technologies Used**
- **FastAPI**: Web framework for building APIs.  
- **LangChain**: Framework for building language model applications.  
- **FAISS**: Library for efficient similarity search.  
- **OpenAI GPT-4**: Large language model for generating responses.
