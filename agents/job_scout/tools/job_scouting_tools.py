from langchain.tools import tool
from jobspy import scrape_jobs
from core.data_model import JobDetailsDataModel



SITE_NAMES=["indeed", "linkedin", "zip_recruiter", "google" , "glassdoor", "bayt", "naukri", "bdjobs"]

@tool
def find_jobs(keywords: list,locations:list):
    """
    Based on the keywords and location
    Find jobs at these location in the fields specified in keywords
    :param keywords:
    :param location:
    :return: json
    """
    location=",".join(locations)
    search_term = ",".join(keywords)
    
    
    jobs=scrape_jobs(site_name=SITE_NAMES,
                           search_term=search_term,
                           location=location,
                           results_wanted=25)
    
    
    #manually converting each row of data frame to pydantic object
    found_jobs=[]
    for _,row in jobs.iterrows():
        job = JobDetailsDataModel(
            company_name=row['COMPANY'],
            title=row['TITLE'],
            location=row['CITY'],
            job_type=row['JOB_TYPE'],
            url=row['JOB_URL'],
            description=row['DESCRIPTION'],
            salary=str(row['MIN_AMOUNT']) if row['MIN_AMOUNT'] else "Not available"
        )
        
        found_jobs.append(job)
    
    
    
    return found_jobs


