import streamlit as st
from PIL import Image
img = Image.open("UCoE-Web-Logo.png")
st.image(img)
st.title('Admission process')
tab1, tab2, tab3 = st.tabs(["Personal", "Marks", "Admission"])
with tab1:
    # -Aadhar
    # -leaving
    # -photo of student
    # -Student domicile certificate
    # - Student Medical certificate
    # -if defence certificate
    # -Gap certificate
    col1, col2 = st.columns(2)
    with col1:
        upload_photo = st.file_uploader("Photo of Student")
        upload_adhaar = st.file_uploader("Adhaar card")
        upload_lc = st.file_uploader("Leaving Certificate")
        migrant = st.checkbox("Click If you are Migrant Student")
        if migrant:
            upload_migrant = st.file_uploader("Migrant Certificate")
        gap = st.checkbox("Click if you have Gap Certificate")
        if gap:
            upload_gap = st.file_uploader("Gap certificate")
        defence = st.checkbox("click if you have Defence Certificate")
        if defence:
            upload_defence = st.file_uploader(" Defence Certificate")
    with col2:
        upload_domicile = st.file_uploader("Student domicile certificate")
        upload_medical = st.file_uploader("Student Medical certificate")
        upload_income = st.file_uploader("Income Certificate")
        upload_caste = st.file_uploader("Caste Certificate")
with tab2:
    # 10/12/cet/jee
    upload_ten = st.file_uploader("10th Marksheet")
    upload_twelve = st.file_uploader("12th Marksheet")
    cet = st.checkbox("Click to take Addmission with CET")
    jee = st.checkbox("Click to take Addmission with JEE")
    if cet:
        upload_cet = st.file_uploader("CET Marksheet")
    if jee:
        upload_jee = st.file_uploader("JEE Marksheet")
with tab3:
    # -Cap receipt( cum Acknowledgement letter)
    # -Addmission reporting/
    # seat acceptance letter
    upload_cap_recipt = st.file_uploader(
        "Cap receipt( cum Acknowledgement letter)")
    upload_report_letter = st.file_uploader(
        "Admission reporting/seat acceptance letter")
col1, col2 = st.columns(2)
with col1:
    st.button('Reset')
with col2:
    st.button("Submit")
def form():
    st.markdown("")
page_names_to_funcs = {
    "Page 2": form,
}