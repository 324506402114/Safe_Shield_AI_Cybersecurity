"""
SafeShield AI
AI-Powered Digital Safety & Phishing Risk Analyzer

HackNowa Global Hackathon 2026
Problem Statement: Digital Safety & Cybersecurity

SafeShield AI analyzes suspicious messages and URLs using:
    - NLP-based text classification
    - URL lexical analysis
    - Cybersecurity heuristics
    - Explainable risk scoring

IMPORTANT:
SafeShield AI does not open or interact with submitted URLs.
It analyzes URL strings only.
"""

import sys
from pathlib import Path

import streamlit as st


# ============================================================
# Project Path Configuration
# ============================================================

ROOT_DIR = Path(__file__).resolve().parent

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))


# ============================================================
# SafeShield Imports
# ============================================================

from src.risk_engine import RiskEngine


# ============================================================
# Page Configuration
# ============================================================

st.set_page_config(
    page_title="SafeShield AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# Custom CSS
# ============================================================

st.markdown(
    """
    <style>

    /* Main application */

    .main {
        padding-top: 1rem;
    }


    /* Header */

    .safeshield-header {
        padding: 1.5rem;
        border-radius: 15px;
        border: 1px solid rgba(128, 128, 128, 0.25);
        margin-bottom: 1.5rem;
    }


    .safeshield-title {
        font-size: 2.7rem;
        font-weight: 800;
        margin-bottom: 0.3rem;
    }


    .safeshield-subtitle {
        font-size: 1.05rem;
        opacity: 0.8;
    }


    /* Risk cards */

    .risk-card {
        padding: 1.5rem;
        border-radius: 15px;
        border: 1px solid rgba(128, 128, 128, 0.25);
        text-align: center;
        margin-bottom: 1rem;
    }


    .risk-score {
        font-size: 3rem;
        font-weight: 800;
    }


    .risk-label {
        font-size: 1.2rem;
        font-weight: 700;
    }


    /* Explanation boxes */

    .explanation-box {
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid;
        margin-bottom: 0.7rem;
        background-color: rgba(128, 128, 128, 0.08);
    }


    /* Footer */

    .footer {
        text-align: center;
        opacity: 0.65;
        padding: 2rem 0 1rem 0;
        font-size: 0.9rem;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# Session State
# ============================================================

if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = None


if "last_message" not in st.session_state:
    st.session_state.last_message = ""


# ============================================================
# Load Risk Engine
# ============================================================

@st.cache_resource
def load_risk_engine():
    """
    Load the SafeShield risk engine once per Streamlit session.
    """

    return RiskEngine()


engine = load_risk_engine()


# ============================================================
# Helper Functions
# ============================================================

def get_risk_color(risk_level: str) -> str:
    """
    Return display color based on risk level.
    """

    if risk_level == "LOW RISK":
        return "#16a34a"

    if risk_level == "SUSPICIOUS":
        return "#f59e0b"

    if risk_level == "HIGH RISK":
        return "#dc2626"

    return "#6b7280"


def get_risk_icon(risk_level: str) -> str:
    """
    Return icon based on risk level.
    """

    if risk_level == "LOW RISK":
        return "🟢"

    if risk_level == "SUSPICIOUS":
        return "🟠"

    if risk_level == "HIGH RISK":
        return "🔴"

    return "⚪"


def analyze_message(message: str):
    """
    Run SafeShield analysis safely.
    """

    try:

        return engine.analyze(
            message=message,
            model_path="models/text_detector.joblib",
        )

    except Exception as error:

        st.error(
            f"Analysis failed: {error}"
        )

        return None


# ============================================================
# Header
# ============================================================

st.markdown(
    """
    <div class="safeshield-header">

        <div class="safeshield-title">
            🛡️ SafeShield AI
        </div>

        <div class="safeshield-subtitle">
            AI-Powered Digital Safety & Phishing Risk Analyzer
        </div>

        <br>

        <div>
            Analyze suspicious messages and URLs using
            machine learning, cybersecurity heuristics,
            and explainable risk scoring.
        </div>

    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# Sidebar
# ============================================================

with st.sidebar:

    st.header("🛡️ SafeShield AI")

    st.markdown(
        """
        ### How it works

        **1. Message Analysis**

        NLP analyzes suspicious language patterns.

        **2. URL Analysis**

        URLs are inspected using lexical and structural
        security indicators.

        **3. Risk Engine**

        Multiple signals are combined into a 0–100 score.

        **4. Explanation**

        SafeShield explains the indicators contributing
        to the result.
        """
    )

    st.divider()

    st.subheader("🔒 Privacy & Safety")

    st.info(
        """
        SafeShield does not open submitted URLs.

        It analyzes URL strings locally and does not
        require visiting suspicious websites.

        Never enter real passwords, OTPs, banking
        credentials, API keys, or other sensitive data.
        """
    )

    st.divider()

    st.subheader("📊 Risk Levels")

    st.markdown(
        """
        🟢 **0–29 — LOW RISK**

        🟠 **30–59 — SUSPICIOUS**

        🔴 **60–100 — HIGH RISK**
        """
    )

    st.divider()

    st.caption(
        "HackNowa Global Hackathon 2026"
    )

    st.caption(
        "Problem: Digital Safety & Cybersecurity"
    )


# ============================================================
# Main Input Area
# ============================================================

st.subheader("🔍 Analyze a Message")

st.write(
    "Paste a suspicious message below. "
    "SafeShield AI will analyze the message and any URLs "
    "contained within it."
)


example_message = (
    "URGENT! Your account will be blocked today. "
    "Verify your password and OTP immediately at "
    "http://192.168.1.50/login"
)


message = st.text_area(
    "Message to analyze",
    height=180,
    placeholder=(
        "Example: "
        "Your account requires verification..."
    ),
)


# ============================================================
# Example Button
# ============================================================

if st.button(
    "🧪 Load Demo Example",
    use_container_width=True,
):

    st.session_state.last_message = (
        example_message
    )

    st.rerun()


# Use saved demo message when available
if (
    not message.strip()
    and st.session_state.last_message
):

    message = st.session_state.last_message


# ============================================================
# Analyze Button
# ============================================================

analyze_button = st.button(
    "🔎 Analyze for Cybersecurity Risk",
    type="primary",
    use_container_width=True,
)


if analyze_button:

    if not message.strip():

        st.warning(
            "Please enter a message before starting the analysis."
        )

    else:

        with st.spinner(
            "Analyzing message and URL indicators..."
        ):

            result = analyze_message(
                message
            )

        if result is not None:

            st.session_state.analysis_result = (
                result
            )

            st.session_state.last_message = (
                message
            )


# ============================================================
# Display Results
# ============================================================

result = st.session_state.analysis_result


if result is not None:

    st.divider()

    st.subheader(
        "🛡️ SafeShield Analysis Result"
    )

    risk_score = result[
        "risk_score"
    ]

    risk_level = result[
        "risk_level"
    ]

    risk_color = get_risk_color(
        risk_level
    )

    risk_icon = get_risk_icon(
        risk_level
    )


    # --------------------------------------------------------
    # Main Risk Result
    # --------------------------------------------------------

    st.markdown(
        f"""
        <div class="risk-card">

            <div class="risk-score"
                 style="color: {risk_color};">

                {risk_score}/100

            </div>

            <div class="risk-label">

                {risk_icon}
                {risk_level}

            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


    # --------------------------------------------------------
    # Metrics
    # --------------------------------------------------------

    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.metric(
            "Risk Score",
            f"{risk_score}/100",
        )


    with col2:

        st.metric(
            "Text Prediction",
            result[
                "text_analysis"
            ]["prediction"],
        )


    with col3:

        st.metric(
            "URLs Detected",
            result[
                "url_analysis"
            ]["url_count"],
        )


    with col4:

        st.metric(
            "URL Risk",
            f"{result['url_analysis']['highest_url_score']}/100",
        )


    # --------------------------------------------------------
    # Risk Progress
    # --------------------------------------------------------

    st.subheader(
        "📈 Risk Score"
    )

    st.progress(
        int(risk_score)
    )


    # --------------------------------------------------------
    # Explanation
    # --------------------------------------------------------

    st.subheader(
        "🧠 Why did SafeShield assign this score?"
    )

    for explanation in result[
        "explanations"
    ]:

        st.markdown(
            f"""
            <div class="explanation-box">
                🔎 {explanation}
            </div>
            """,
            unsafe_allow_html=True,
        )


    # --------------------------------------------------------
    # Analysis Columns
    # --------------------------------------------------------

    left_col, right_col = st.columns(2)


    # ========================================================
    # Text Analysis
    # ========================================================

    with left_col:

        st.subheader(
            "💬 Message Analysis"
        )

        text_analysis = result[
            "text_analysis"
        ]

        st.write(
            f"**Prediction:** "
            f"{text_analysis['prediction']}"
        )

        st.write(
            f"**Suspicious probability:** "
            f"{text_analysis['suspicious_probability']:.2%}"
        )

        st.write(
            f"**Legitimate probability:** "
            f"{text_analysis['legitimate_probability']:.2%}"
        )

        st.progress(
            int(
                text_analysis[
                    "suspicious_probability"
                ]
                * 100
            )
        )


    # ========================================================
    # URL Analysis
    # ========================================================

    with right_col:

        st.subheader(
            "🔗 URL Analysis"
        )

        url_analysis = result[
            "url_analysis"
        ]

        if url_analysis[
            "url_count"
        ] == 0:

            st.success(
                "No URLs detected."
            )

        else:

            for index, url_result in enumerate(
                url_analysis["urls"],
                start=1,
            ):

                st.write(
                    f"**URL {index}:**"
                )

                st.code(
                    url_result["url"],
                    language=None,
                )

                url_score = url_result[
                    "risk_score"
                ]

                url_level = url_result[
                    "risk_level"
                ]

                st.write(
                    f"Risk: **{url_score}/100 — "
                    f"{url_level}**"
                )

                for indicator in url_result[
                    "indicators"
                ]:

                    st.write(
                        f"• {indicator}"
                    )


    # --------------------------------------------------------
    # Security Signals
    # --------------------------------------------------------

    st.subheader(
        "🚨 Security Signals"
    )

    heuristic_col1, heuristic_col2, heuristic_col3 = (
        st.columns(3)
    )

    heuristics = result[
        "heuristics"
    ]


    with heuristic_col1:

        if heuristics[
            "urgency_detected"
        ]:

            st.error(
                "⚠️ Urgency language detected"
            )

        else:

            st.success(
                "No strong urgency signal"
            )


    with heuristic_col2:

        if heuristics[
            "sensitive_request_detected"
        ]:

            st.error(
                "🔐 Sensitive-information request detected"
            )

        else:

            st.success(
                "No sensitive-information request detected"
            )


    with heuristic_col3:

        if heuristics[
            "multiple_urls"
        ]:

            st.warning(
                "🔗 Multiple URLs detected"
            )

        else:

            st.success(
                "No multiple-URL signal"
            )


    # --------------------------------------------------------
    # Recommendations
    # --------------------------------------------------------

    st.subheader(
        "🛡️ Recommended Safety Actions"
    )

    for recommendation in result[
        "recommendations"
    ]:

        st.info(
            f"✓ {recommendation}"
        )


    # --------------------------------------------------------
    # Raw Result
    # --------------------------------------------------------

    with st.expander(
        "🔧 View Technical Analysis"
    ):

        st.json(
            result
        )


# ============================================================
# Demo Examples
# ============================================================

st.divider()

st.subheader(
    "🧪 Try These Demo Scenarios"
)

demo_col1, demo_col2, demo_col3 = st.columns(
    3
)


with demo_col1:

    st.markdown(
        """
        **🟢 Normal Message**

        > Your package has been delivered
        > successfully. Thank you for shopping
        > with us.
        """
    )


with demo_col2:

    st.markdown(
        """
        **🟠 Suspicious Message**

        > Congratulations! You won a reward.
        > Claim your prize immediately.
        """
    )


with demo_col3:

    st.markdown(
        """
        **🔴 High-Risk Example**

        > Your account will be blocked.
        > Verify your OTP and password immediately
        > at a suspicious URL.
        """
    )


# ============================================================
# Project Information
# ============================================================

st.divider()

st.subheader(
    "ℹ️ About SafeShield AI"
)

about_col1, about_col2 = st.columns(2)


with about_col1:

    st.markdown(
        """
        **Technology Stack**

        - Python
        - Streamlit
        - Scikit-learn
        - TF-IDF
        - Logistic Regression
        - URL lexical analysis
        - Explainable risk scoring
        """
    )


with about_col2:

    st.markdown(
        """
        **Security Philosophy**

        SafeShield AI is designed as a defensive
        decision-support tool.

        It does not claim that a message is definitely
        malicious. Instead, it identifies risk indicators
        and provides actionable safety recommendations.

        Always verify suspicious communications through
        trusted official channels.
        """
    )


# ============================================================
# Footer
# ============================================================

st.markdown(
    """
    <div class="footer">

        🛡️ SafeShield AI —
        Digital Safety & Cybersecurity

        <br>

        Built for HackNowa Global Hackathon 2026

        <br>

        Defensive analysis only •
        URLs are analyzed without being opened

    </div>
    """,
    unsafe_allow_html=True,
)