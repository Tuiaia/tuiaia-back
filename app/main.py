from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from Data.DataStructure import ConjuntoDados

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Notice(BaseModel):
    notice: str


@app.post('/')
async def classify(notice: Notice):
    return notice.notice

@app.get('/newsletter')
async def newsletter():
    dados = ConjuntoDados()
    dados.load_data()
    return dados.transform_json()
    