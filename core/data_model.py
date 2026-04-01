
from pydantic import BaseModel,Field,HttpUrl


#class to store education details
class EducationDataModel(BaseModel):
    degree: str
    graduation_year: int
    
# class to store professional experience
class ProfExpDataModel(BaseModel):

    post: str
    years: str
    summary_of_job: str
    
    
# class to store resume details
class ResumeDataModel(BaseModel):
    is_fresher:bool=Field(default=False)
    education: list[EducationDataModel]
    professional_exp: list[ProfExpDataModel] = Field(default=[])
    skills: list[str]
    summary: str | None=None
    


class JobDetailsDataModel(BaseModel):
    company_name: str
    title : str
    location : str
    job_type : str
    description : str
    requirements : list[str]
    salary :str = Field(default="Not available")
    url : HttpUrl
    