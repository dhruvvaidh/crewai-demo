from dotenv import load_dotenv
load_dotenv()
from crewai import Crew,Process
from tasks import research_task,write_task
from agents import blog_researcher, blog_writer
import os
api_key = os.getenv("OPENAI_API_KEY")
crew = Crew(
    agents=[blog_researcher,blog_writer],
    tasks=[research_task,write_task],
    process=Process.sequential, # Sequential Task execution is default
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

result = crew.kickoff(inputs={'topic':'AI VS ML vs Data Science'})
print(result)