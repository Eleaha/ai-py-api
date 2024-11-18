from fastapi import HTTPException
from models import generate_letter

def get_letter(to_name, from_name, subject, emotion, location, timescale, when, additional):
    query_values = {
        "to_name": to_name,
        "from_name": from_name, 
        "subject": subject,
        "emotion": emotion,
        "location": location,
        "timescale": timescale,
        "when": when,
        "additional": additional
    }

    if query_values["subject"] == None or query_values["emotion"] == None or query_values["from_name"] == None:
        raise HTTPException(status_code=400, detail="Please provide the mandatory queries for from_name, subject and emotion")

    prompt_variables = {}

    for query in query_values:
        if query_values[query] == None:
            prompt_variables[query] = "n/a"
        else:
            prompt_variables[query] = query_values[query]
            
    return generate_letter([prompt_variables])