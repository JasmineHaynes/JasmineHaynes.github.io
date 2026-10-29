import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="People Analytics Lab", page_icon="🧭", layout="wide")
st.title("People Analytics Lab")
st.caption("Interactive portfolio demonstration using synthetic data only.")
st.warning("This is not a trained attrition model and must not be used to make employment decisions.")

st.sidebar.header("Explore hypothetical inputs")
engagement = st.sidebar.slider("Engagement (1–5)", 1.0, 5.0, 3.2, 0.1)
support = st.sidebar.slider("Manager support (1–5)", 1.0, 5.0, 3.4, 0.1)
workload = st.sidebar.slider("Workload (1–5)", 1.0, 5.0, 3.0, 0.1)
tenure = st.sidebar.slider("Tenure (months)", 1, 120, 36)

c1, c2, c3 = st.columns(3)
c1.metric("Engagement input", f"{engagement:.1f}/5")
c2.metric("Manager support input", f"{support:.1f}/5")
c3.metric("Tenure input", f"{tenure} months")

labels = ["Engagement", "Manager support", "Workload", "Tenure"]
values = [engagement / 5 * 100, support / 5 * 100, workload / 5 * 100, tenure / 120 * 100]
fig, ax = plt.subplots()
ax.barh(labels, values)
ax.set_xlim(0, 100)
ax.set_xlabel("Selected input mapped to 0–100 for visualization (not a risk score)")
ax.set_title("Illustrative indicator profile")
st.pyplot(fig)
plt.close(fig)

st.markdown("""
### Interpretation and limitations
- Values are user-selected hypothetical inputs; no real employee data is collected.
- Bars are rescaled inputs, not a prediction, diagnosis, or validated risk score.
- A real project needs documented data provenance, a research question, appropriate evaluation, uncertainty, and privacy/fairness review.
""")
