from langchain_core.prompts import PromptTemplate

Song_picker_template = """You need to analyse the user's mood based on the given sentence "{mood}", and suggest the user some songs to listen to uplift that mood."""
song_picker = PromptTemplate.from_template(template = Song_picker_template)