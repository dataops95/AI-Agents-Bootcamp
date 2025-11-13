import os
from crewai import Crew, Process
from agents import analyzer, resume_builder, cover_letter_writer, reviewer
from tasks import analyze_task, customize_resume_task, write_cover_letter_task, review_task
from utils import read_resume, fetch_job_description

JOB_URL = """https://www.linkedin.com/jobs/view/4332410813/?alternateChannel=search&eBP=CwEAAAGafUi-ibzBAvgd2cdHeAfCZU-JdPFibckbbJrGYXGzNcAW31_-AIBFPLei3G1HEVeeqK7xg8ckGSiOZ_vno_WGAU9GCrHHLPQ7XTw9H-qbJwhnJ3khm9j5Kz0j-kO9X52Y7A9dfLpsFMYWlmmjnY3DjHqiVT4s7MDdPnvwAnsJQSUW1oBtQpZHRAZuEkq_23l5KmFNCJ7Ntb8R-6NgHBlgP1w8WHmahDnZ5GJD0dGDEYwgSn07eHrlQmHMneOfQJzNYcyavDrRz6EJkVrbZczY-ng5e-MoDcTNx_wYBk2KrBlNm02WdwnB0DlfHP0z-gmreu8MSyLjHL_IVEJPE6DjHAF2sOi8Rd8b2s2zKlBTBrinZk1pDKsz4qnRyoSTYTezKiOwJy82PWGvdRhSnAc7w50WGiCnpjvaC7bWM44Pas-AiYi8_Eaoak2I1VyvPAjf6OfRsvxtnA-MP5pVzX55PnzJfo0J6cuWNxBhQrxt6yTQYqXZcuFrmm9MWTML1hTTkk6UzA&refId=VMCageMJRyXqMTlkHqxiFw%3D%3D&trackingId=olJfLn%2Ff7q%2BdHNca0%2B8Log%3D%3D"""

RESUME_PATH = "resume.pdf"

resume_content = read_resume(RESUME_PATH)
job_html = fetch_job_description(JOB_URL)

inputs = {
    "job_url": JOB_URL,
    "resume_content": resume_content[:4000],
    "job_description": job_html
}

crew = Crew(
    agents=[analyzer, resume_builder, cover_letter_writer, reviewer],
    tasks=[analyze_task, customize_resume_task, write_cover_letter_task, review_task],
    process=Process.sequential,
    verbose=True,
    max_iters=3
)

print("""Starting the multi-agent resume tailoring process...""")
results = crew.kickoff(inputs)

outputs_dir = "outputs"
os.makedirs(outputs_dir, exist_ok=True)

final = results.tasks_output[-1].raw

with open(f"{outputs_dir}/TAILORED_RESUME.txt", 'w', encoding='utf-8') as f:
    f.write(final.get("resume", "No resume generated."))

with open(f"{outputs_dir}/COVER_LETTER.txt", 'w', encoding='utf-8') as f:
    f.write(final.get("cover_letter", "No cover letter generated."))

print("\nDone! check outputs folder")