import streamlit as st
from crewai import Crew, Process
from tasks import research_prospect_task, personalize_content_task, write_email_task
from agents import prospect_researcher, content_personalizer, email_copywriter

# Define the Crew
crew = Crew(
    agents=[prospect_researcher, content_personalizer, email_copywriter],
    tasks=[research_prospect_task, personalize_content_task, write_email_task],
    process=Process.sequential
)

# Streamlit App
st.set_page_config(page_title="Personalized Email Automation", layout="centered")
st.title("🎯 Personalized Email Automation")
st.subheader("Effortlessly generate personalized, engaging emails tailored to your prospects.")

# User Inputs
st.sidebar.header("Prospect Details")
name = st.sidebar.text_input("Prospect Name", placeholder="e.g., John Doe")
title = st.sidebar.text_input("Prospect Title", placeholder="e.g., Head of Marketing")
company = st.sidebar.text_input("Company Name", placeholder="e.g., TechCorp")
industry = st.sidebar.text_input("Industry", placeholder="e.g., Technology")
linkedin_url = st.sidebar.text_input("LinkedIn Profile URL", placeholder="e.g., https://linkedin.com/in/johndoe")
our_product = st.sidebar.text_input("Our Product", placeholder="e.g., Innovative CRM Solution")

if st.sidebar.button("Generate Email"):
    if not all([name, title, company, industry, linkedin_url, our_product]):
        st.error("Please fill in all the fields to proceed.")
    else:
        # Prepare input data
        inputs = {
            "name": name,
            "title": title,
            "company": company,
            "industry": industry,
            "linkedin_url": linkedin_url,
            "our_product": our_product,
        }

        # Kickoff the CrewAI process
        with st.spinner("🔍 Processing... This might take a few moments."):
            result = crew.kickoff(inputs=inputs)

        st.success("✅ Process completed successfully!")
        st.subheader("Crew Execution Result")

        st.markdown(result)
else:
    st.info("Fill in the details in the sidebar and click 'Generate Email' to start.")

# Footer
st.markdown("---")
st.markdown(
    "Developed by [Yazan Risheh](https://www.linkedin.com/in/yazan-risheh-8b87211a1/)"
    "\n"
    "Enhance your sales communications effortlessly!"
)
