from crewai import Task
from agents import analyzer, resume_builder, cover_letter_writer, reviewer

analyze_task = Task(
    description="""
    Fetch the job description from {job_url} and extract:
    - required skills
    - years of experience
    - key responsibilities
    - company values(if mentioned)
    Output as bullet points.
""",
    expected_output="structured bullet points of job requirements",
    agent=analyzer
)

customize_resume_task = Task(
    description="""
    using the job analysis and the user's original resume ({resume_content}),
    rewrite the resume to:
    - prioritize relevant skills and experiences
    - use keywords from the job description
    - keep it under 1 page summary
""",
    expected_output="customized resume text",
    agent=resume_builder
)

write_cover_letter_task = Task(
    description="""
    write a 3 paragraph cover letter :
    1. strong opening (why this role/company)
    2. highlight 2-3 matching achievements
    3. call to action
    use first person and sound human.
""",
    expected_output="professional cover letter",
    agent=cover_letter_writer
)

review_task = Task(
    description=""""
    Review the trailored resume and cover letter for:
    - are 80% of the job keywords present?
    - is formatting clean (no tables, no images)
    - grammer and tome check
    if issues found, delegate fixes back to resume builder or cover letter writer.
    """,
    expected_output="final approved resume and cover letter(or revision requests)",
    agent=reviewer
)