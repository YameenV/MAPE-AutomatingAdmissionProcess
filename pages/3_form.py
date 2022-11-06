import streamlit as st
from helper import defaultConfig
from logging import PlaceHolder
from unicodedata import category
from PIL import Image

defaultConfig()

img = Image.open("./media/UCoE-Web-Logo.png")
st.image(img)
st.title('Form Filling')
# personal
tab1, tab2, tab3, tab4 = st.tabs(["Personal", "Mother", "Father", "Marks"])
with tab1:
    #personal
    name = st.text_input("Name", placeholder="Name")
    col1, col2 = st.columns(2)
    with col1:
        option = st.selectbox(
            'Gender',
            ('Male', 'Female', 'Other'))
    with col2:
        option = st.selectbox(
            'Type of Candidate',
            ("MH", "OHU", "J&K", "AMMI/NONCET", "OTHER")
        )
    capid = st.text_input("Cap ID", placeholder="CAP ID")
    col1, col2, col3 = st.columns(3)
    with col1:
        nationality = st.text_input("Student Nationality", "eg : India")
    with col2:
        Type_of_Disability = st.text_input("Type of Diasbility * If any")
    with col3:
        option = st.selectbox(
            "Only One Child",
            ("Yes", "No")
        )
    col1, col2 = st.columns(2)
    with col1:
        category = st.text_input("Category", placeholder="Category")
        caste = st.text_input("Caste", placeholder="Caste")
    with col2:
        religion = st.text_input("Religion", placeholder="Religion")
        Sub_caste = st.text_input("Sub Caste", placeholder="Sub Caste")
    col1, col2 = st.columns(2)
    with col1:
        date = st.date_input(
            "When's your birthday",)
    with col2:
        date_words = st.text_input("In Words", placeholder="In Words")
    col1, col2, col3 = st.columns(3)
    with col1:
        birth_place = st.text_input("Birth Place ", placeholder="Eg : Mumbai")
    with col2:
        option = st.selectbox(
            "Blood Group",
            ("A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-")
        )
    with col3:
        Domicile = st.text_input("Domicile")
    aadhar_no = st.text_input("Adhar Card Number")
    permanant_add = st.text_input("Permanent Address")
    col1, col2 = st.columns(2)
    with col1:
        mobile = st.text_input("Mobile Number")
    with col2:
        email = st.text_input("Email")
    col1, col2 = st.columns(2)
    with col1:
        name_school = st.text_input("Name of College ")
    with col2:
        extra = st.text_input("Extra Curricular Activities and Acheiment")
with tab2:
    # Mother
    name_mother = st.text_input(
        "Name of Mother/Gaurdian", placeholder="Name of Mother/Gaurdian")
    col1, col2 = st.columns(2)
    with col1:
        Qualification_mother = st.text_input(
            "Qualification", placeholder="Qualification")
    with col2:
        option = st.selectbox(
            "Qualification",
            ("Job", "Business", "Housewife")
        )
    col1, col2, col3 = st.columns(3)
    with col1:
        email_mother = st.text_input("Email", placeholder="Email")
    with col2:
        company_mother = st.text_input("Company", placeholder="Company")
    with col3:
        phone_no_mother = st.text_input(
            "Phone Number", placeholder="Phone Number")
with tab3:
    # Father
    name_father = st.text_input(
        "Name of Father/Gaurdian", placeholder="Name of Father/Gaurdian", key=2)
    col1, col2, col3 = st.columns(3)
    with col1:
        email_father = st.text_input("Email", placeholder="Email", key=1)
    with col2:
        company_father = st.text_input("Company", placeholder="Company", key=3)
    with col3:
        phone_no_father = st.text_input(
            "Phone Number", placeholder="Phone Number", key=4)
    col1, col2 = st.columns(2)
    with col1:
        Qualification_father = st.text_input(
            "Qualification", placeholder="Qualification", key=5)
    with col2:
        option = st.selectbox(
            "Qualification",
            ("Job", "Business")
        )
with tab4:
    #marks
    col1, col2 = st.columns(2)
    with col1:
        st.text("SSC or Equivalent Level*")
        board_ssc = st.text_input("Board", key=6)
        seat_ssc = st.text_input("Seat No", key=7)
        marks_ssc = st.text_input("Marks Obtained", key=8)
        outof_ssc = st.text_input("Out Off", key=9)
        percent_ssc = st.text_input("percentage", key=10)
    with col2:
        st.text("HSC or Equivalent Level*")
        board_hsc = st.text_input("Board")
        seat_hsc = st.text_input("Seat No")
        marks_hsc = st.text_input("Marks Obtained")
        outof_hsc = st.text_input("Out Off")
        percent_hsc = st.text_input("percentage")
        total_pcm = st.text_input("Total Marks in PCM")
    st.subheader('Entrance Exams')
    col1, col2 = st.columns(2)
    with col1:
        st.text("JEE-Mains")
        seat_jee = st.text_input("Seat NO.")
        physics_jee = st.text_input("Physics")
        chemistry_jee = st.text_input("Chemistry")
        maths_jee = st.text_input("Mathematics")
        total_jee = st.text_input("Total PCM")
        year_jee = st.text_input("Exam")
    with col2:
        st.text("MHT-CET")
        seat_cet = st.text_input("Seat NO.", key=12)
        physics_cet = st.text_input("Physics", key=13)
        chemistry_cet = st.text_input("Chemistry", key=14)
        maths_cet = st.text_input("Mathematics", key=15)
        total_cet = st.text_input("Total PCM", key=16)
        year_cet = st.text_input("Exam", key=17)
st.button("Submit")