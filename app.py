import streamlit as st
from sqlalchemy import create_engine
from agent import create_agent
from database import create_database_from_csv
from chart import plot_chart

st.set_page_config(page_title="AI SQL Data Analyst", layout="wide")

st.title("📊 AI SQL Data Analyst Agent")

# Upload CSV
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    st.success("CSV uploaded successfully!")

    # Create SQLite DB from CSV
    engine = create_engine("sqlite:///data.db")
    create_database_from_csv(uploaded_file, engine)

    st.info("Database created from CSV")

    # Create AI Agent
    agent = create_agent(engine)

    # Ask question
    question = st.text_input("Ask a question about your data")

    if st.button("Run Query"):
        if question:
            with st.spinner("Thinking..."):
                result = agent.run(question)

            st.subheader("Answer")
            st.write(result)

            # Optional chart generation
            try:
                plot_chart(question, engine)
            except:
                pass
