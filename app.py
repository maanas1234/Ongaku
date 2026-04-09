from langgraph.graph import StateGraph, END
from typing import TypedDict
from LLM import get_llm
from prompts import song_picker,genre_decide,song_recommend


llm = get_llm()

class Mystate(TypedDict):
    sentence : str
    mood : str
    genre: str
    song : str

def node_1(state:Mystate) -> dict:
    song_picker_temp= song_picker.format(sentence = state['sentence'])
    response = llm.invoke(song_picker_temp)
    #state['mood']=response
    return {"mood":response.content}

def node_2(state:Mystate) -> dict:
    genre_decide_temp= genre_decide.format(mood=state['mood'],sentence=state['sentence'])
    response = llm.invoke(genre_decide_temp)
    #state['genre'] = response.content
    return {"genre":response.content}

def node_3(state:Mystate) -> dict:
    song_recommend_t = song_recommend.format(genre = state['genre'],mood = state['mood'])
    final_out = llm.invoke(song_recommend_t)
    #state['song']= final_out.content
    return {"song":final_out.content}



graph = StateGraph(Mystate)

graph.add_node("node_one", node_1)
graph.add_node("node_two", node_2)
graph.add_node("node_three",node_3)

graph.add_edge("node_one", "node_two")
graph.add_edge("node_two", "node_three")
graph.add_edge("node_three",END)

graph.set_entry_point("node_one")

app=graph.compile()
result = app.invoke({"sentence":"My girlfriend and I talked on VC for 1hr last night. It was fun.","mood":"","genre":"","song":""})

print(f"final: {result}")


