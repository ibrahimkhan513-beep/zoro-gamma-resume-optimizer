# ⚔️ Zoro-Gamma Resume Optimizer

An AI-powered Streamlit web application designed to dynamically tailor resumes to USA IT job requirements. This tool performs a deep-dive gap analysis and rewrites resume bullet points using advanced LLM prompt engineering techniques.

## 🚀 Overview

The Zoro-Gamma Resume Optimizer leverages the Google Gemini API to act as a Principal Resume Architect. Instead of simply rewriting text, the application uses **"Chain of Thought" reasoning** (performing a hidden gap analysis before generating output) to ensure high-quality, ATS-optimized results tailored specifically for the US IT market.

### Key Features
* **Silent Gap Analysis:** The AI privately identifies missing tools, skills, and methodologies between the current resume and the target Job Description before making edits.
* **The "Luffy-XYZ" Framework:** Automatically rewrites and injects 5-6 highly targeted bullet points across the Professional Summary and recent projects using a strict formatting rule:
  * **[X] Action:** Strong, varied verbs.
  * **[Y] Context/Tools:** Explicitly names the tech stack.
  * **[Z] Outcome:** Describes the qualitative impact.
* **Zero Quantification Rule:** Forces the AI to focus on technical depth and complexity rather than arbitrary percentages or financial metrics.
* **Secure API Key Handling:** Users input their Gemini API key directly into the Streamlit sidebar, ensuring private keys are never hardcoded into the backend.

## 🛠️ Tech Stack

* **Frontend:** [Streamlit](https://streamlit.io/) (Python)
* **LLM Engine:** [Google Gemini API](https://ai.google.dev/) (`gemini-2.5-flash`)
* **Core Language:** Python 3.x

## 💻 How to Run Locally

If you want to run this application on your own machine:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/zoro-gamma-resume-optimizer.git](https://github.com/your-username/zoro-gamma-resume-optimizer.git)
   cd zoro-gamma-resume-optimizer
