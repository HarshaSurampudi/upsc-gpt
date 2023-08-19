import streamlit as st
import pandas as pd
import numpy as np
from agent import evaluate_answer

st.title('UPSC Answer evaluator')

st.write("This app evaluates your answers for UPSC exam. Please enter the question and your answer in the text boxes below and click on the submit button to evaluate your answer.")

question = st.text_area("Question")
answer = st.text_area("Answer")

def evaluate_ans(question, answer):
    return evaluate_answer(question, answer)

if st.button("Submit"):
    st.write("Evaluating your answer...")   
    result = evaluate_ans(question, answer)
    st.write(result)
    