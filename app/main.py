from os import environ
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.model.fscot import Fscot
from app.model.rag import Rag
from llama_index.readers import SimpleWebPageReader
from app.template.template import *

app = FastAPI()

# FSCOT
fscot = Fscot() # Few Shot Chain of Thought
class FewShotLLMRequest(BaseModel):
    url: str

# RAG 
rag = Rag()
class RagLLMRequest(BaseModel):
    url: str


@app.post("/fscot")
async def few_shot_llm(request: FewShotLLMRequest):
    try:
        text_to_check_for_compliance = fscot.get_specific_text(request.url)
        result = fscot.check_for_compliance(text_to_check_for_compliance, fscot_compliance_template)
        return {"non_complaint_results": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/rag")
async def rag_llm(request: RagLLMRequest):
    try:
        documents = SimpleWebPageReader(html_to_text=True).load_data([environ["STRIPE_URL"]])
        rag.index_documents(documents)
        text_to_check_for_compliance = rag.get_specific_text(request.url)
        non_complaint_results = rag.check_for_compliance(text_to_check_for_compliance, rag_non_compliance_template)
        complaint_suggestions = rag.check_for_compliance(non_complaint_results, rag_suggestion_template)
        return {"non_complaint_results": non_complaint_results, "suggestions": complaint_suggestions}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
