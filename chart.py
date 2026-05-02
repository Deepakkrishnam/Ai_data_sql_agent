import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import text
import streamlit as st

def plot_chart(question, engine):
    try:
        query = "SELECT * FROM data LIMIT 10"
        df = pd.read_sql(text(query), engine)

        if df.shape[1] >= 2:
            st.subheader("Sample Chart")
            plt.figure()
            df.iloc[:, 0].value_counts().plot(kind="bar")
            st.pyplot(plt)
    except Exception as e:
        st.warning("Chart could not be generated")
