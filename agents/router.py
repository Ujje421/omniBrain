from agents.research_agent import research
from agents.code_agent import generate_code
from agents.file_agent import create_file

def route_task(query):
    if "code" in query:
        return generate_code(query)
    elif "file" in query:
        return create_file(query)
    else:
        return research(query)
