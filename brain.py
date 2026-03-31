from agents.research_agent import research
from agents.code_agent import generate_code
from memory.store import save_memory

def process_query(query):
    if "code" in query:
        result = generate_code(query)
    else:
        result = research(query)

    save_memory(query, result)
    return result
