from crewai import Agent
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Make sure you have your key set
if not os.getenv("GOOGLE_API_KEY"):
    raise ValueError("GOOGLE_API_KEY not found in .env file")

# Pick the Gemini model you want
MODEL_NAME = "gemini-1.5-flash"


analyzer = Agent(
    role="Job Description Analyzer",
    goal="Extract skills, responsibilities, and keywords from job posting.",
    backstory="You are an HR expert who breaks down job ads into structured requirements.",
    llm=MODEL_NAME,
    verbose=True,
    allow_delegation=False
)

resume_builder = Agent(
    role="Resume Customizer",
    goal="Rewrite the user's resume to highlight matching skills and experience.",
    backstory="You are a professional resume writer skilled at tailoring resumes for specific job applications.",
    llm=MODEL_NAME,
    verbose=True,
    allow_delegation=False
)

cover_letter_writer = Agent(
    role="Cover Letter Writer",
    goal="Create a compelling cover letter that aligns the user's experience with the job requirements.",
    backstory="You are an expert cover letter writer who knows how to connect a candidate's background to a job posting.",
    llm=MODEL_NAME,
    verbose=True,
    allow_delegation=False
)

reviewer = Agent(
    role="ATS & Quality Reviewer",
    goal="Review the customized resume and cover letter for ATS compatibility and overall quality.",
    backstory="You are an expert in applicant tracking systems and resume quality assurance.",
    llm=MODEL_NAME,
    verbose=True,
    allow_delegation=False
)
