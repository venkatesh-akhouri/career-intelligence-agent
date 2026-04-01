resume_parser_prompt=""" Consider yourself as a HR and a recruiter, you have been given a resume of a candidate,
your task is to extract the relevant details that is helpful for finding a job based on the resume of the candidate according to below
and save it in a strctured format as provided

1) Education of the candidate
2) Professional experience of the candidate
3) whether the candidate is fresher or not
4) If professional experience of the candidate is empty, categorize the candidate as a fresher
5) Skills of the candidate
6) professional summary if available
6) if any field is not found, use default value for that field
"""