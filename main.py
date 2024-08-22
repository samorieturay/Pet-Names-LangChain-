#Practicing LangChain with ChatGPT.

from langchain.llms import openai #Choosing ChatGPT to be the large language model of our choosing
from dotenv import load_dotenv

load_dotenv()

def generate_pet_name():
    llm = openai(temperature = 0.9) #temperature states how creative/accurate we want our responses to  be. 1 meaning super creative and 0 being as factual as possible

    name = llm("I have a pet cat and I want a cool name for it. Suggest me five cool names for my cat,") #this is my prompt

    return name