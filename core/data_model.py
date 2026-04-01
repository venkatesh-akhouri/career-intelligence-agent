from pydantic import BaseModel


#class to store education details
class EducationDataModel(BaseModel):
    degree: str
    graduation_year: int
    
# class to store professional experience
class ProfExpDataModel(BaseModel):
    post: str
    years: int
    summary_of_job: str
    
    
# class to store resume details
class ResumeDataModel(BaseModel):
    education: list[EducationDataModel]
    professional_exp: list[ProfExpDataModel] | None=None
    skills: list[str]
    summary: str | None=None
    
    
    
    

