import os

from pypdf import PdfReader
from prompts import resume_parser_prompt
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from data_model import ResumeDataModel

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

class ResumeParser:
    def __init__(self, resume,model,prompt):
        self.resume = resume
        self.model = model
        self.prompt = prompt
        
        
    def extract_text(self):
        resume_text=""
        reader=PdfReader(self.resume)
        
        num_pages=len(reader.pages)
        
        for page in range(num_pages):
            pages=reader.pages[page]
            resume_text+=pages.extract_text(0)
            
        return resume_text
    
    
    def parse_resume(self,resume_text):
        
        #get the full prompt
        full_prompt=resume_text + "\n\n" + self.prompt
        
        #since we need a structured output
        #we have already defined the pydantic model
        #we will chain it with
        
        resume_structured_data=self.model.with_structured_output(ResumeDataModel)
        resume_data=resume_structured_data.invoke(full_prompt)
        
        return resume_data
    
 
model=GoogleGenerativeAI(model="gemini-2.0-flash",
                         google_api_key=GOOGLE_API_KEY)

resume_pdf=None #for now nonw will take in resume
resume_parser=ResumeParser(resume_pdf,model,resume_parser_prompt)

    

                
