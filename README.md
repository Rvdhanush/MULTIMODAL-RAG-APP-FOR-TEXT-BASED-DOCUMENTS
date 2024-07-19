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

1. **Create a virtual environment and activate it**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. **Install the required Python packages**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Create a .env file in the root directory and add your OpenAI API key**:
    ```sh
    OPENAI_API_KEY=your_openai_api_key
    ```

4. **Run the FastAPI server**:
    ```sh
    uvicorn main:app --reload
    ```

    ![image](https://github.com/user-attachments/assets/721c68fa-b943-4844-b274-b914c159214d)


