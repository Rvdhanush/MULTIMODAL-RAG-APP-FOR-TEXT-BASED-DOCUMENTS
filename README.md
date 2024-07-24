# MULTIMODAL-RAG-APP-FOR-TEXT-BASED-DOCUMENTS
SchnellGPT for Luminator is an AI-powered web application designed to assist in the installation and maintenance of lamps used in various applications. This app leverages advanced natural language processing and multimodal retrieval to provide detailed, context-specific answers to user queries.

## Features

- **Interactive Web Interface**: Users can ask questions related to lamp installation and maintenance.
- **Contextual Answers**: The app provides detailed, context-specific responses.
- **Multimodal Retrieval**: Utilizes both text and tables to retrieve relevant information.
- **Easy Setup**: Simple to set up and deploy.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: COLAB, Python, FastAPI, LangChain, FAISS, OpenAI
- **Environment Management**: dotenv

## Setup and Installation

### Prerequisites

- Python 3.7 or higher
- Node.js and npm (for frontend dependencies)

### Backend Setup

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Rvdhanush/MULTIMODAL-RAG-APP-FOR-TEXT-BASED-DOCUMENTS.git
    cd MULTIMODAL-RAG-APP-FOR-TEXT-BASED-DOCUMENTS
    ```

2. **Create a virtual environment and activate it**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required Python packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Create a .env file in the root directory and add your OpenAI API key**:
    ```bash
    OPENAI_API_KEY=your_openai_api_key
    ```

5. **Run the FastAPI server**:
    ```bash
    uvicorn main:app --reload
    ```

### Frontend Setup

1. **Navigate to the templates directory** and ensure `index.html` is present.
2. **Ensure the JavaScript code is present in `static/js/script.js`**.

### Running the Application

The application will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Screenshots


https://github.com/Rvdhanush/MULTIMODAL-RAG-APP-FOR-TEXT-BASED-DOCUMENTS/blob/main/Screenshot%202024-07-18%20131323.png

