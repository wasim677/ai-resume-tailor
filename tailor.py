import os
import sys
from google import genai

# Initializes the Gemini client using the GEMINI_API_KEY environment variable
client = genai.Client()

def read_file(filepath):
    if not os.path.exists(filepath):
        print(f"Error: The file '{filepath}' was not found.")
        sys.exit(1)
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def tailor_application(resume_text, job_desc_text):
    prompt = f"""
You are an expert career consultant and hiring specialist.

Target Job Description:
\"\"\"
{job_desc_text}
\"\"\"

Current Resume:
\"\"\"
{resume_text}
\"\"\"

Perform the following tasks:
1. MATCH ANALYSIS: List the top 3 overlapping strengths and top 2 key missing skill gaps.
2. TAILORED SUMMARY: Write a concise 3-sentence professional summary directly aligning the candidate's existing experience to the target role.
3. CUSTOM COVER LETTER: Write a professional, concise 3-paragraph cover letter highlighting relevant achievements without inventing false experience.

Format the response clearly using clean Markdown sections.
"""
    print("Analyzing and tailoring with Gemini...")
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt,
    )
    return response.text

def main():
    resume_path = "resume.txt"
    job_path = "job_description.txt"
    output_path = "tailored_output.md"

    print(f"Reading files: {resume_path} and {job_path}...")
    resume_text = read_file(resume_path)
    job_desc_text = read_file(job_path)

    result = tailor_application(resume_text, job_desc_text)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result)

    print(f"\nDone! Results saved to: {output_path}")

if __name__ == "__main__":
    main()