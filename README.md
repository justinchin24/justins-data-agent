# 🤖 Enterprise Support Data Agent

An AI-powered data extraction pipeline and web interface that transforms unstructured IT support tickets into validated, structured JSON objects using Python, Pydantic, Streamlit, and the Google GenAI SDK.

## 🏗️ Architecture & Tech Stack
- **Backend (`agent.py`):** Utilizes `google-genai` and Pydantic structured outputs to guarantee schema-compliant extraction. Includes robust error handling (`try/except`) and timestamped logging.
- **Frontend (`app.py`):** A clean, interactive Streamlit web dashboard featuring side-by-side metrics, action item checklists, and collapsible raw JSON output viewers.
- **Data Validation (`schemas.py`):** Strictly enforces output schemas for fields like Category, Priority, Summary, and Action Items.

## 🚀 Local Setup & Installation

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/justins-data-agent.git
cd justins-data-agent

2. **Create and activate a virtual environment:**

python -m venv .venv
# On Windows:
.venv\Scripts\activate

3. **Install dependencies:**

pip install google-genai pydantic python-dotenv streamlit

4. **Configure your environment variables:**
Create a `.env` file in the root directory and add your Google Gemini API key:

GEMINI_API_KEY=your_actual_api_key_here

5. **Run the Streamlit Web App:**

streamlit run app.py

