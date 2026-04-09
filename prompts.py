from langchain_core.prompts import PromptTemplate

Song_picker_template = """You need to analyse the user's mood based on the given sentence "{sentence}". Only reply with one word that is the mood, nothing else."""
song_picker = PromptTemplate.from_template(template = Song_picker_template)

Genre_decide_template = """You need to find the genre for a song for the given mood "{mood}" The original user statement was this {sentence}, from which the mood is deduced. Reply with only 1 word which is the genre and nothing else."""
genre_decide = PromptTemplate.from_template(template = Genre_decide_template)

Song_recommend_temp = """You need to recommend the best song based on the genre which is{genre}. The user whom you are recommending this to has the mood {mood}. Just the name of the song, with the name of the artist. Nothing else."""
song_recommend = PromptTemplate.from_template(template = Song_recommend_temp)