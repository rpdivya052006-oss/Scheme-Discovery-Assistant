import streamlit as st
from streamlit_mic_recorder import speech_to_text

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Scheme Discovery Assistant",
    page_icon="🇮🇳",
    layout="centered"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------
st.markdown("""
<style>
    .stApp {
        background-color: #F8F7F2;
    }

    .main-title {
        font-size: 36px;
        font-weight: 800;
        color: #166534;
        margin-bottom: 8px;
    }

    .subtitle {
        font-size: 18px;
        color: #555555;
        margin-bottom: 25px;
    }

    .section-title {
        font-size: 25px;
        font-weight: 700;
        color: #166534;
        margin-top: 15px;
    }

    .scheme-card {
        background: white;
        padding: 22px;
        border-radius: 18px;
        margin: 15px 0;
        border: 1px solid #E5E5E5;
        box-shadow: 0 3px 12px rgba(0,0,0,0.06);
    }

    .scheme-title {
        font-size: 22px;
        font-weight: 700;
        color: #166534;
    }

    .benefit {
        font-size: 16px;
        color: #333333;
        margin: 8px 0;
    }

    .match {
        font-size: 18px;
        font-weight: 700;
        color: #E67E22;
    }

    .voice-box {
        background: #FFF7ED;
        border: 1px solid #FDBA74;
        border-radius: 14px;
        padding: 14px;
        margin: 15px 0;
    }

    .voice-title {
        font-size: 17px;
        font-weight: 700;
        color: #C2410C;
    }

    div.stButton > button {
        width: 100%;
        border-radius: 12px;
        min-height: 48px;
        font-size: 16px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# LANGUAGE
# --------------------------------------------------
if "language" not in st.session_state:
    st.session_state.language = "English"

language = st.radio(
    "Language / மொழி",
    ["English", "Tamil"],
    horizontal=True
)

st.session_state.language = language


# --------------------------------------------------
# TRANSLATIONS
# --------------------------------------------------
if language == "Tamil":

    texts = {
        "title": "Scheme Discovery Assistant",
        "subtitle": "உங்களுக்கு தகுதியான அரசு திட்டங்களை எளிதாக கண்டறியுங்கள்.",
        "find": "எனக்கான திட்டங்களை கண்டுபிடி",
        "back": "← பின்செல்",
        "next": "அடுத்து →",
        "submit": "திட்டங்களை காண்பி",
        "results": "உங்களுக்கான திட்டங்கள்",
        "details": "திட்ட விவரங்கள்",
        "benefit": "நன்மை",
        "why": "ஏன் இது உங்களுக்கு பொருந்துகிறது?",
        "eligibility": "தகுதி",
        "documents": "தேவையான ஆவணங்கள்",
        "download": "Checklist பதிவிறக்கம்",
        "apply": "விண்ணப்பிக்க",
        "voice": "🎙️ உங்கள் பதிலை பேசுங்கள்",
        "voice_hint": "Type செய்ய முடியாதவர்கள் microphone button-ஐ அழுத்தி பதிலை சொல்லலாம்.",
        "voice_processing": "Voice answer பெறப்படுகிறது...",
        "voice_error": "Voice answer புரியவில்லை. மீண்டும் முயற்சிக்கவும்.",
        "your_answer": "உங்கள் பதில்",
    }

else:

    texts = {
        "title": "Scheme Discovery Assistant",
        "subtitle": "Find government schemes that you may be eligible for.",
        "find": "Find my schemes",
        "back": "← Back",
        "next": "Next →",
        "submit": "Show my schemes",
        "results": "Schemes for You",
        "details": "Scheme Details",
        "benefit": "Benefit",
        "why": "Why this matched you",
        "eligibility": "Eligibility",
        "documents": "Required Documents",
        "download": "Download Checklist",
        "apply": "Apply",
        "voice": "🎙️ Speak your answer",
        "voice_hint": "Users who cannot type can press the microphone button and speak their answer.",
        "voice_processing": "Processing voice answer...",
        "voice_error": "Could not understand the voice answer. Please try again.",
        "your_answer": "Your answer",
    }


# --------------------------------------------------
# SCHEME DATA
# --------------------------------------------------
schemes = [
    {
        "name": "PM-KISAN",
        "benefit": "Financial support for eligible farmer families.",
        "category": "Farmers",
        "occupation": "Farmer",
        "income": 300000,
        "need": "Agriculture",
        "documents": [
            "Aadhaar Card",
            "Bank Account Details",
            "Land Records"
        ],
        "eligibility": [
            "Applicant should be an eligible farmer",
            "Valid Aadhaar should be available",
            "Eligible agricultural land ownership"
        ]
    },
    {
        "name": "Pradhan Mantri Ujjwala Yojana",
        "benefit": "LPG connection support for eligible households.",
        "category": "Women",
        "occupation": "Any",
        "income": 300000,
        "need": "Cooking Gas",
        "documents": [
            "Aadhaar Card",
            "Address Proof",
            "Bank Account Details"
        ],
        "eligibility": [
            "Eligible household",
            "Applicant must satisfy scheme conditions",
            "Valid identity and address proof"
        ]
    },
    {
        "name": "Post Matric Scholarship",
        "benefit": "Financial assistance for eligible students.",
        "category": "SC/ST/OBC",
        "occupation": "Student",
        "income": 250000,
        "need": "Education",
        "documents": [
            "Aadhaar Card",
            "Income Certificate",
            "Community Certificate",
            "College ID"
        ],
        "eligibility": [
            "Student studying in an eligible institution",
            "Income should satisfy applicable limits",
            "Valid community certificate where applicable"
        ]
    },
    {
        "name": "Ayushman Bharat PM-JAY",
        "benefit": "Health coverage for eligible families.",
        "category": "General",
        "occupation": "Any",
        "income": 500000,
        "need": "Healthcare",
        "documents": [
            "Aadhaar Card",
            "Identity Proof",
            "Family Details"
        ],
        "eligibility": [
            "Family must fall under applicable eligibility criteria",
            "Valid identity information",
            "Scheme availability in the relevant area"
        ]
    }
]


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

if "step" not in st.session_state:
    st.session_state.step = 0

if "answers" not in st.session_state:
    st.session_state.answers = {}

if "selected_scheme" not in st.session_state:
    st.session_state.selected_scheme = None


# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------
def home_page():

    st.markdown(
        f'<div class="main-title">🇮🇳 {texts["title"]}</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="subtitle">{texts["subtitle"]}</div>',
        unsafe_allow_html=True
    )

    st.info(
        "This assistant provides an initial scheme-matching guide. "
        "Always verify the latest eligibility and application details "
        "on official government portals."
    )

    if st.button(texts["find"], type="primary"):
        st.session_state.page = "form"
        st.session_state.step = 0
        st.session_state.answers = {}
        st.rerun()


# --------------------------------------------------
# QUESTIONS
# --------------------------------------------------
questions = [

    {
        "key": "age",
        "title": "What is your age?",
        "tamil": "உங்கள் வயது என்ன?",
        "type": "number"
    },

    {
        "key": "gender",
        "title": "What is your gender?",
        "tamil": "உங்கள் பாலினம்?",
        "type": "select",
        "options": ["Male", "Female", "Other"]
    },

    {
        "key": "occupation",
        "title": "What is your occupation?",
        "tamil": "உங்கள் தொழில் என்ன?",
        "type": "select",
        "options": [
            "Student",
            "Farmer",
            "Employee",
            "Self-employed",
            "Unemployed",
            "Other"
        ]
    },

    {
        "key": "income",
        "title": "What is your annual family income?",
        "tamil": "உங்கள் குடும்பத்தின் ஆண்டு வருமானம் என்ன?",
        "type": "number"
    },

    {
        "key": "state",
        "title": "Which state do you live in?",
        "tamil": "நீங்கள் எந்த மாநிலத்தில் வசிக்கிறீர்கள்?",
        "type": "select",
        "options": [
            "Tamil Nadu",
            "Kerala",
            "Karnataka",
            "Andhra Pradesh",
            "Telangana",
            "Maharashtra",
            "Other"
        ]
    },

    {
        "key": "category",
        "title": "What is your category?",
        "tamil": "உங்கள் சமூகப் பிரிவு என்ன?",
        "type": "select",
        "options": [
            "General",
            "SC",
            "ST",
            "OBC",
            "Other"
        ]
    },

    {
        "key": "need",
        "title": "What support do you need?",
        "tamil": "உங்களுக்கு எந்த உதவி தேவை?",
        "type": "select",
        "options": [
            "Education",
            "Agriculture",
            "Healthcare",
            "Cooking Gas",
            "Employment",
            "Housing",
            "Financial Support"
        ]
    }
]


# --------------------------------------------------
# VOICE VALUE CONVERTER
# --------------------------------------------------
def clean_number(text):

    if not text:
        return None

    text = text.lower().strip()

    replacements = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "ten": "10",
        "twenty": "20",
        "thirty": "30",
        "forty": "40",
        "fifty": "50",
        "sixty": "60",
        "seventy": "70",
        "eighty": "80",
        "ninety": "90"
    }

    for word, number in replacements.items():
        if word in text:
            text = text.replace(word, number)

    digits = "".join(
        character for character in text
        if character.isdigit()
    )

    if digits:
        return int(digits)

    return None


# --------------------------------------------------
# VOICE MATCHING
# --------------------------------------------------
def match_voice_to_option(text, options):

    if not text:
        return None

    text = text.lower().strip()

    # Exact / partial matching
    for option in options:

        if option.lower() in text:
            return option

    # Common Tamil/English voice words
    mappings = {
        "student": ["student", "students", "மாணவர்", "மாணவி"],
        "farmer": ["farmer", "farm", "விவசாயி"],
        "employee": ["employee", "job", "வேலை"],
        "self-employed": ["self employed", "business", "தொழில்"],
        "unemployed": ["unemployed", "jobless", "வேலை இல்லை"],

        "male": ["male", "man", "ஆண்"],
        "female": ["female", "woman", "பெண்"],

        "education": ["education", "study", "school", "college", "கல்வி"],
        "agriculture": ["agriculture", "farmer", "விவசாயம்"],
        "healthcare": ["health", "hospital", "medical", "மருத்துவம்"],
        "cooking gas": ["gas", "lpg", "cooking", "சமையல் எரிவாயு"],
        "employment": ["employment", "job", "வேலை"],
        "housing": ["house", "housing", "home", "வீடு"],
        "financial support": ["money", "financial", "finance", "பணம்"],

        "general": ["general"],
        "sc": ["sc"],
        "st": ["st"],
        "obc": ["obc"]
    }

    for option in options:

        key = option.lower()

        if key in mappings:

            for word in mappings[key]:

                if word.lower() in text:
                    return option

    return None


# --------------------------------------------------
# FORM PAGE
# --------------------------------------------------
def form_page():

    total = len(questions)
    step = st.session_state.step
    question = questions[step]

    progress = (step + 1) / total

    st.progress(progress)

    st.caption(f"Step {step + 1} of {total}")

    title = (
        question["tamil"]
        if language == "Tamil"
        else question["title"]
    )

    st.markdown(
        f'<div class="section-title">{title}</div>',
        unsafe_allow_html=True
    )

    key = question["key"]

    # ----------------------------------------------
    # NUMBER QUESTIONS
    # ----------------------------------------------
    if question["type"] == "number":

        current_value = st.session_state.answers.get(key, 0)

        value = st.number_input(
            texts["your_answer"],
            min_value=0,
            max_value=120 if key == "age" else 10000000,
            value=current_value,
            key=f"number_{key}"
        )

        st.markdown(
            f"""
            <div class="voice-box">
                <div class="voice-title">{texts["voice"]}</div>
                <div>{texts["voice_hint"]}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        voice_language = "ta-IN" if language == "Tamil" else "en-IN"

        voice_text = speech_to_text(
            language=voice_language,
            start_prompt="🎙️ Start speaking",
            stop_prompt="⏹️ Stop",
            just_once=True,
            key=f"voice_{key}"
        )

        if voice_text:

            converted = clean_number(voice_text)

            if converted is not None:

                st.session_state.answers[key] = converted

                st.success(
                    f"Voice answer: {converted}"
                )

                st.rerun()

            else:

                st.warning(texts["voice_error"])


    # ----------------------------------------------
    # SELECT QUESTIONS
    # ----------------------------------------------
    else:

        options = question["options"]

        default_index = 0

        if key in st.session_state.answers:

            try:
                default_index = options.index(
                    st.session_state.answers[key]
                )

            except ValueError:
                default_index = 0

        value = st.selectbox(
            texts["your_answer"],
            options,
            index=default_index,
            key=f"select_{key}"
        )

        # Voice option
        st.markdown(
            f"""
            <div class="voice-box">
                <div class="voice-title">{texts["voice"]}</div>
                <div>{texts["voice_hint"]}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        voice_language = "ta-IN" if language == "Tamil" else "en-IN"

        voice_text = speech_to_text(
            language=voice_language,
            start_prompt="🎙️ Start speaking",
            stop_prompt="⏹️ Stop",
            just_once=True,
            key=f"voice_{key}"
        )

        if voice_text:

            matched_option = match_voice_to_option(
                voice_text,
                options
            )

            if matched_option:

                st.session_state.answers[key] = matched_option

                st.success(
                    f"Voice answer: {matched_option}"
                )

                st.rerun()

            else:

                st.warning(
                    f'Heard: "{voice_text}" — '
                    f"{texts['voice_error']}"
                )

    st.write("")

    # ----------------------------------------------
    # NAVIGATION
    # ----------------------------------------------
    col1, col2 = st.columns(2)

    with col1:

        if step > 0:

            if st.button(texts["back"]):

                st.session_state.step -= 1
                st.rerun()

    with col2:

        button_text = (
            texts["submit"]
            if step == total - 1
            else texts["next"]
        )

        if st.button(button_text, type="primary"):

            # Save current select/number answer
            if question["type"] == "number":

                st.session_state.answers[key] = value

            else:

                st.session_state.answers[key] = value

            if step == total - 1:

                st.session_state.page = "results"
                st.rerun()

            else:

                st.session_state.step += 1
                st.rerun()


# --------------------------------------------------
# MATCHING LOGIC
# --------------------------------------------------
def calculate_match(scheme):

    answers = st.session_state.answers

    score = 0
    total = 5

    # Occupation
    if scheme["occupation"] == "Any":
        score += 1

    elif answers.get("occupation") == scheme["occupation"]:
        score += 1

    # Income
    if answers.get("income", 0) <= scheme["income"]:
        score += 1

    # Category
    category = answers.get("category")

    if scheme["category"] == "General":
        score += 1

    elif category in ["SC", "ST", "OBC"]:
        score += 1

    # Need
    if answers.get("need") == scheme["need"]:
        score += 1

    # State
    score += 1

    return int((score / total) * 100)


# --------------------------------------------------
# RESULTS PAGE
# --------------------------------------------------
def results_page():

    st.markdown(
        f'<div class="section-title">🎯 {texts["results"]}</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Based on the information you provided:"
    )

    filter_option = st.selectbox(
        "Filter by category",
        [
            "All",
            "Education",
            "Agriculture",
            "Healthcare",
            "Cooking Gas"
        ]
    )

    matched_schemes = []

    for scheme in schemes:

        percentage = calculate_match(scheme)

        if filter_option != "All":

            if scheme["need"] != filter_option:
                continue

        matched_schemes.append(
            (scheme, percentage)
        )

    matched_schemes.sort(
        key=lambda x: x[1],
        reverse=True
    )

    for scheme, percentage in matched_schemes:

        st.markdown(
            f"""
            <div class="scheme-card">

                <div class="scheme-title">
                    {scheme["name"]}
                </div>

                <div class="match">
                    {percentage}% Match
                </div>

                <div class="benefit">
                    <b>{texts["benefit"]}:</b>
                    {scheme["benefit"]}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.progress(percentage / 100)

        with st.expander(
            f"✓ {texts['why']}"
        ):

            st.write(
                f"✓ Occupation: "
                f"{st.session_state.answers.get('occupation', 'Not provided')}"
            )

            st.write(
                f"✓ Income: ₹"
                f"{st.session_state.answers.get('income', 0):,}"
            )

            st.write(
                f"✓ Need: "
                f"{st.session_state.answers.get('need', 'Not provided')}"
            )

        if st.button(
            f"{texts['details']} →",
            key="details_" + scheme["name"]
        ):

            st.session_state.selected_scheme = scheme
            st.session_state.page = "details"
            st.rerun()

        st.markdown("---")


# --------------------------------------------------
# DETAILS PAGE
# --------------------------------------------------
def details_page():

    scheme = st.session_state.selected_scheme

    if scheme is None:

        st.session_state.page = "results"
        st.rerun()

    if st.button(texts["back"]):

        st.session_state.page = "results"
        st.rerun()

    st.markdown(
        f'<div class="section-title">{scheme["name"]}</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"### 💰 {texts['benefit']}"
    )

    st.write(scheme["benefit"])

    st.markdown(
        f"### ✅ {texts['eligibility']}"
    )

    for item in scheme["eligibility"]:
        st.write(f"☑️ {item}")

    st.markdown(
        f"### 📄 {texts['documents']}"
    )

    for item in scheme["documents"]:
        st.write(f"☐ {item}")

    checklist = f"""
{scheme["name"]} - Document Checklist

Required Documents:
"""

    for document in scheme["documents"]:
        checklist += f"\n☐ {document}"

    st.download_button(
        label=f"📥 {texts['download']}",
        data=checklist,
        file_name=f"{scheme['name']}_checklist.txt",
        mime="text/plain"
    )

    st.write("")

    st.link_button(
        f"🌐 {texts['apply']}",
        "https://www.india.gov.in/"
    )

    st.warning(
        "Please verify the latest eligibility and application "
        "information on official government websites."
    )


# --------------------------------------------------
# PAGE ROUTING
# --------------------------------------------------
if st.session_state.page == "home":

    home_page()

elif st.session_state.page == "form":

    form_page()

elif st.session_state.page == "results":

    results_page()

elif st.session_state.page == "details":

    details_page()
