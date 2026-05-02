from langchain_groq import ChatGroq
from langchain_experimental.sql import SQLDatabaseChain
from langchain_community.utilities import SQLDatabase

def create_agent(engine):
    db = SQLDatabase(engine)

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0,
        max_tokens=1024
    )

    db_chain = SQLDatabaseChain.from_llm(
        llm=llm,
        db=db,
        verbose=True
    )

    return db_chain
