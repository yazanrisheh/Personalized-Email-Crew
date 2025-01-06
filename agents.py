from crewai import Agent
from tools import search_tool

# Define Agents
prospect_researcher = Agent(
    role="Prospect Research Specialist",
    goal="Gather detailed, relevant information about the prospect and their company",
    backstory=(
        "You are an expert at researching individuals and companies, with a focus on "
        "finding information that can be used to personalize sales communications."
    ),
    tools=[search_tool],
    verbose=True
)

content_personalizer = Agent(
    role="Content Personalization Expert",
    goal="Identify key points of connection between the prospect's background and our product",
    backstory=(
        "You have a talent for finding meaningful connections between people's backgrounds, interests, "
        "and needs, and how products or services can benefit them."
    ),
    tools=[],
    verbose=True
)

email_copywriter = Agent(
    role="Personalized Email Copywriter",
    goal="Craft a compelling, highly personalized email that resonates with the prospect",
    backstory=(
        "You are a skilled copywriter with a knack for creating emails that feel personal, relevant, "
        "and engaging."
    ),
    tools=[],
    verbose=True
)
