from crewai import Task
from agents import prospect_researcher, content_personalizer, email_copywriter
from tools import search_tool

# Define Tasks
research_prospect_task = Task(
    description=(
        "Conduct thorough research on {name}, their role as {title} at {company}, and the company itself. "
        "Look for recent news, achievements, challenges, or interests related to {name} or their company."
    ),
    expected_output="A detailed dossier on {name} and {company}.",
    tools=[search_tool],
    agent=prospect_researcher
)

personalize_content_task = Task(
    description=(
        "Using the research on {name} and {company}, identify specific ways that {our_product} can address "
        "their potential needs or align with their professional interests."
    ),
    expected_output="A list of personalized talking points and angles to use in the email.",
    agent=content_personalizer
)

write_email_task = Task(
    description=(
        "Craft a highly personalized email to {name} about {our_product}. Use the research and personalized "
        "content to create an email that feels individual, relevant, and engaging."
    ),
    expected_output=(
        "A PersonalizedEmail object containing:\n"
        "1. A compelling, personalized subject line\n"
        "2. The body of the email\n"
        "3. Follow-up notes for the salesperson."
    ),
    agent=email_copywriter
)
