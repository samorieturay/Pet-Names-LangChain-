#Practicing LangChain with ChatGPT.

from langchain_community.llms import OpenAI  # Correct import
from dotenv import load_dotenv
import os
load_dotenv()

def generate_pet_name():
    llm = OpenAI(temperature = 0.9) #temperature states how creative/accurate we want our responses to  be. 1 meaning super creative and 0 being as factual as possible

    name = llm("I have a pet cat and I want a cool name for it. Suggest me five cool names for my cat,") #this is my prompt

    return name

if __name__ == "__main__":
    pet_names = generate_pet_name()
    print(pet_names)
