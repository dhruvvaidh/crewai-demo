from crewai import Agent
from tools import yt_tool
from dotenv import load_dotenv
import os
api_key = os.getenv("OPENAI_API_KEY")

## Create a senior blog content researcher
blog_researcher = Agent(
    role='Blog researcher from youtube videos',
    goal='Get the relevant video content for the topic{topic} form Yt channel',
    verbose=True,
    backstory=(
        "Expert in understanding videos in AI, Data Science, Machine Learning and Generative AI and providing suggestions"
    ),
    tools = [yt_tool],
    allow_delegation=True #Basically allows some other agent to do the given task
)

## creating a senior blog writer agent with YT tool
blog_writer = Agent(
    role='Blog Writer',
    goal='Narrate compelling tech stories about the video {topic} from YT Channel',
    verbose=True,
    backstory=(
        """
            With a flair for simplifying complex topics you craft engaging
            narratives that captivate and educate, bringing new discoveries
            to light in an accessible manner
        """
    ),
    tools = [yt_tool],
    allow_delegation=True #Basically allows some other agent to do the given task
)

