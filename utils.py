import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import uuid
from jinja2 import Template
import os
import streamlit as st

def run_detection(df, model):
    df_clean = df.copy()
    df_clean = df_clean.select_dtypes(include=['number']).fillna(0)
    y_pred = model.predict(df_clean)
    df['Prediction'] = y_pred
    return df

def generate_report(df):
    if 'Prediction' not in df.columns:
        return "No prediction data available."

    normal = (df['Prediction'] == 0).sum()
    attacks = (df['Prediction'] == 1).sum()
    template_path = "templates/report_template.html"

    if not os.path.exists(template_path):
        return "Template not found."

    with open(template_path) as file:
        template = Template(file.read())

    html = template.render(
        normal=normal,
        attacks=attacks,
        total=len(df)
    )

    os.makedirs("reports", exist_ok=True)
    output_path = f"reports/report_{uuid.uuid4().hex[:6]}.html"
    with open(output_path, "w") as f:
        f.write(html)

    return output_path

def visualize_data(df):
    if 'Prediction' not in df.columns:
        st.warning("Please run detection first.")
        return

    fig, ax = plt.subplots()
    sns.countplot(data=df, x='Prediction', ax=ax)
    ax.set_xticklabels(['Normal', 'Attack'])
    st.pyplot(fig)
