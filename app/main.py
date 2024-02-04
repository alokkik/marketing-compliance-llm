# from os import environ
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from app.model.fscot import Fscot
# from app.model.rag import Rag
# from llama_index.readers import SimpleWebPageReader
# from app.template.template import *

# app = FastAPI()

# # FSCOT
# fscot = Fscot() # Few Shot Chain of Thought
# class FewShotLLMRequest(BaseModel):
#     url: str

# # RAG 
# rag = Rag()
# class RagLLMRequest(BaseModel):
#     url: str


# @app.post("/fscot")
# async def few_shot_llm(request: FewShotLLMRequest):
#     try:
#         text_to_check_for_compliance = fscot.get_specific_text(request.url)
#         result = fscot.check_for_compliance(text_to_check_for_compliance, fscot_compliance_template)
#         return {"non_complaint_results": result}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# @app.post("/rag")
# async def rag_llm(request: RagLLMRequest):
#     try:
#         documents = SimpleWebPageReader(html_to_text=True).load_data([environ["STRIPE_URL"]])
#         rag.index_documents(documents)
#         text_to_check_for_compliance = rag.get_specific_text(request.url)
#         non_complaint_results = rag.check_for_compliance(text_to_check_for_compliance, rag_non_compliance_template)
#         complaint_suggestions = rag.check_for_compliance(non_complaint_results, rag_suggestion_template)
#         return {"non_complaint_results": non_complaint_results, "suggestions": complaint_suggestions}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

from os import environ
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.model.fscot import Fscot
from app.model.rag import Rag
from llama_index.readers import SimpleWebPageReader
from app.template.template import *
import logging

app = FastAPI()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# FSCOT
fscot = Fscot()  # Few Shot Chain of Thought
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
        logger.info("FSCOT compliance check successful")
        logger.info(f"Non-compliant results: {result}")
        return {"non_complaint_results": result}
    except Exception as e:
        logger.error(f"Error in FSCOT compliance check: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/rag")
async def rag_llm(request: RagLLMRequest):
    try:
        documents = SimpleWebPageReader(html_to_text=True).load_data([environ["STRIPE_URL"]])
        rag.index_documents(documents)
        text_to_check_for_compliance = rag.get_specific_text(request.url)
        non_complaint_results = rag.check_for_compliance(text_to_check_for_compliance, rag_non_compliance_template)
        logger.info(f"Non-compliant results: {non_complaint_results}")
        complaint_suggestions = rag.check_for_compliance(non_complaint_results, rag_suggestion_template)
        logger.info(f"Possible suggestions: {complaint_suggestions}")
        logger.info("RAG non-compliance check successful")
        return {"non_complaint_results": non_complaint_results, "suggestions": complaint_suggestions}
    except Exception as e:
        logger.error(f"Error in RAG compliance check: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
