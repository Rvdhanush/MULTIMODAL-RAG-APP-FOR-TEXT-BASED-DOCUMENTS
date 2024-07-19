from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.schema.messages import HumanMessage, SystemMessage
from langchain.schema.document import Document
from langchain.vectorstores import FAISS
from langchain.retrievers.multi_vector import MultiVectorRetriever
import os
import uuid
import base64
from fastapi import FastAPI, Request, Form, Response, File, UploadFile
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
import json
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)

#openai_api_key = os.getenv("OPENAI_API_KEY")
embeddings = OpenAIEmbeddings(openai_api_key="sk-luminator-support-development-hcW5lLOkU07F2gF7ZO7GT3BlbkFJ0KPqd7AOjM8KgYBrSQ51")

db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

prompt_template = """You are a Schnell bot, analyzing information for maintenance.
Answer the question based only on the following context, which can include text, and tables:
{context}
Question: {question}
Don't answer if you are not sure and decline to answer and say "Sorry, I don't have much information about it."
Return the answer in a list of points format:
Answer:
"""

qa_chain = LLMChain(llm=ChatOpenAI(model="gpt-4", openai_api_key="sk-luminator-support-development-hcW5lLOkU07F2gF7ZO7GT3BlbkFJ0KPqd7AOjM8KgYBrSQ51", max_tokens=1024),
                    prompt=PromptTemplate.from_template(prompt_template))

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/get_answer")
async def get_answer(question: str = Form(...)):
    relevant_docs = db.similarity_search(question)
    context = ""
    for d in relevant_docs:
        if d.metadata['type'] == 'text':
            context += '[text]' + d.metadata['original_content']
        elif d.metadata['type'] == 'table':
            context += '[table]' + d.metadata['original_content']
    result = qa_chain.run({'context': context, 'question': question})

    # Format the result to display as points
    points = result.split('\n')
    formatted_result = "<ul>"
    for point in points:
        formatted_result += f"<li>{point.strip()}</li>"
    formatted_result += "</ul>"
    
    return JSONResponse({"result": formatted_result})
