from crewai import Task
from tools import yt_tool
from agents import blog_researcher, blog_writer
from dotenv import load_dotenv
import os
api_key = os.getenv("OPENAI_API_KEY")
## Research Task
research_task = Task(
    description=(
        """
            Identify the video {topic}.
            Get detailed information about the video from the channel
        """
    ),
    expected_output='A comprehensive 3 paragraphs long report based on the {topic} of video content.',
    tools=[yt_tool],
    agent=blog_researcher,
)

## Writing Task
write_task = Task(
    description=(
        """
            Get the info from the youtube channel on the topic {topic}.
        """
    ),
    expected_output='Summarize the info from the youtube channel video on the topic {topic}.',
    tools=[yt_tool],
    agent=blog_writer,
    async_execution=False,# If you don't want your agents to work parallely
    output_file='new-blog-post.md' # We can customize our outputs
)
