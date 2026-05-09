AI SQL Analyst Agent 🤖📊
The AI SQL Analyst Agent is an intelligent interface that allows users to interact with SQL databases using natural language. By leveraging Large Language Models (LLMs), it translates plain English questions into executable SQL queries, fetches the results, and provides data insights.  

🚀 Live Demo
Access the interactive agent here:


AI SQL Analyst Agent App   

🛠️ Tech Stack
Frontend: Streamlit

AI Framework: LangChain

LLM Integration: Google Generative AI (Gemini)

Database: SQLAlchemy (supports SQLite, MySQL, PostgreSQL, etc.)

Language: Python

📋 Features
Natural Language to SQL: Ask questions like "Who are the top 5 customers by revenue?" and get immediate answers.

Schema Awareness: The agent automatically understands your database schema to write accurate queries.

Error Correction: Built-in logic to handle and fix SQL syntax errors dynamically.

Secure Connection: Connects to your database using standard SQLAlchemy connection strings.

📁 Project Structure
app.py: The main application file containing the Streamlit UI and LangChain agent logic.

requirements.txt: List of dependencies including langchain, google-generativeai, and streamlit.


Ai_sql_analyst_agent.txt: Project metadata and deployment links.  

⚙️ Installation & Local Setup
Clone the repository:

Bash
git clone https://github.com/your-username/ai-sql-analyst.git
cd ai-sql-analyst
Install dependencies:

Bash
pip install -r requirements.txt
Set up Environment Variables:
Create a .env file or export your API key:

Bash
GOOGLE_API_KEY=your_gemini_api_key_here
Run the application:

Bash
streamlit run app.py
📖 How It Works
Connect: Provide your database credentials or a local database file.

Query: Type your question in the chat interface.

Analyze: The agent generates SQL, executes it, and presents the final answer in easy-to-read text.
