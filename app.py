import streamlit as st
import google.generativeai as genai
import re

# Set up page configurations
st.set_page_config(page_title="Zoro-Gamma Resume Optimizer", layout="wide")

st.title("Zoro-Gamma Resume Optimizer")

# Sidebar for configuration
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("Gemini API Key", type="password", help="Enter your Gemini API Key. It will be used securely for the session.")
    st.info("The application requires a valid Gemini API Key to function.")

st.write("Optimize your resume against your target Job Description using advanced gap analysis and ATS-friendly 'Luffy-XYZ' rewrites.")

# Layout for Inputs
st.subheader("Input Details")
col1, col2 = st.columns(2)

with col1:
    job_description = st.text_area("Target Job Description", height=350, placeholder="Paste the complete target Job Description here...")

with col2:
    current_resume = st.text_area("Current Resume", height=350, placeholder="Paste your complete current Resume text here...")

# System Instruction specific to prompt requirements
system_instruction = """Role: You are a Principal Resume Architect with 16+ years of experience specializing in the US IT market. Your expertise lies in ATS optimization, gap analysis, and "Human-In-The-Loop" storytelling.

Task: Perform a deep-dive comparison between the provided [Resume] and [Job Description].

Step 1: Silent Gap Analysis
* Identify specific technical skills, tools, or methodologies present in the JD but missing from the resume.
* Explain why these gaps matter for this specific role. 
* CRITICAL: You must wrap this entire analysis section inside <analysis> and </analysis> tags.

Step 2: The "Luffy-XYZ" Rewrite 
For any section requiring tailoring, rewrite the bullet points using the Luffy-XYZ Format:
* X (Action): Use strong, varied verbs.
* Y (Context/Tools): Explicitly name the tech stack, libraries, or frameworks used.
* Z (Outcome): Describe the qualitative impact or the "Human" value added.
Constraint: NO quantification. Do not use percentages or arbitrary numbers. Focus on technical depth and complexity instead.
Tone: Professional but conversational—avoid "corporate-speak" clichés.

Step 3: Gamma Integration Prep
Add the missing tools identified in Step 1 to the current resume by creating 5 to 6 high-impact Luffy-XYZ bullet points. Integrate these naturally across the current 2 projects as well as the professional summary. 

Output Constraint: 
After your <analysis> block, output ONLY the restructured project sections and professional summary formatted in clean Markdown, optimized for direct input into the Gamma editor."""

if st.button("Optimize Resume"):
    if not api_key:
        st.error("Please enter your Gemini API Key in the sidebar.")
    elif not job_description.strip():
        st.error("Please provide the Target Job Description.")
    elif not current_resume.strip():
        st.error("Please provide your Current Resume.")
    else:
        with st.spinner("Analyzing your resume and generating optimized narrative..."):
            try:
                # Initialize Gemini with the API Key
                genai.configure(api_key=api_key)
                
                # Setup model to use the specified system prompt
                model = genai.GenerativeModel(
                    model_name="gemini-2.5-flash",
                    system_instruction=system_instruction
                )
                
                user_prompt = f"Job Description:\n{job_description}\n\nResume:\n{current_resume}"
                
                # Fetch Response
                response = model.generate_content(user_prompt)
                
                st.subheader("Optimization Results")
                
                # Extract text
                response_text = response.text
                
                # Parse output via regex
                analysis_match = re.search(r'<analysis>(.*?)</analysis>', response_text, re.DOTALL | re.IGNORECASE)
                
                if analysis_match:
                    # Output gap analysis
                    analysis_content = analysis_match.group(1).strip()
                    with st.expander("View AI Gap Analysis"):
                        st.markdown(analysis_content)
                    
                    # Remove full tag block
                    clean_resume = re.sub(r'<analysis>.*?</analysis>', '', response_text, flags=re.DOTALL | re.IGNORECASE).strip()
                    
                    # Show optimized resume
                    st.markdown(clean_resume)
                else: # Fallback in case of model error/non-compliance
                    st.warning("The model did not include the <analysis> delimiter correctly. Printing full raw output.")
                    st.markdown(response_text)
                    
            except Exception as e:
                st.error(f"Application encountered an error while communicating with Gemini API: {e}")

