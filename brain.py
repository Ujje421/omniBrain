from agents.router import route_task
from memory.vector_store import store_memory

def run_agent(query):
    result = route_task(query)
    store_memory(query, result)
    return result
