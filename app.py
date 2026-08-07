import streamlit as st
import pandas as pd
import joblib
from pathlib import Path


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="SupplyFlow AI",
    page_icon="🚚",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# MODEL PATH
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "best_model.pkl"


# ============================================================
# MODEL PERFORMANCE
# Replace these with your actual Colab results
# ============================================================

MODEL_ACCURACY = 94.20
MODEL_PRECISION = 92.80
MODEL_RECALL = 91.60
MODEL_F1 = 92.20


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* =====================================================
       GLOBAL APP
    ===================================================== */

    .stApp {
        background:
            linear-gradient(
                135deg,
                #f8fbff 0%,
                #eef5ff 50%,
                #f8fbff 100%
            );
    }

    .block-container {
        max-width: 1180px;
        padding-top: 1.5rem;
        padding-bottom: 3rem;
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }


    /* =====================================================
       HEADINGS
    ===================================================== */

    h1 {
        color: #10233f !important;
        font-size: 2.35rem !important;
        font-weight: 850 !important;
        letter-spacing: -1px;
    }

    h2 {
        color: #10233f !important;
        font-weight: 800 !important;
    }

    h3 {
        color: #173457 !important;
        font-weight: 750 !important;
    }

    p {
        color: #687b91;
    }


    /* =====================================================
       BRAND
    ===================================================== */

    .brand-text {
        font-size: 25px;
        font-weight: 850;
        color: #10233f;
        letter-spacing: -0.8px;
    }

    .brand-blue {
        color: #1683ff;
    }


    /* =====================================================
       HERO CARD
    ===================================================== */

    .hero-title {
        font-size: 36px;
        font-weight: 850;
        color: #10233f;
        line-height: 1.15;
        margin-bottom: 10px;
    }

    .hero-description {
        font-size: 14px;
        line-height: 1.7;
        color: #687b91;
        max-width: 850px;
    }


    /* =====================================================
       BORDERED CONTAINERS
    ===================================================== */

    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(255, 255, 255, 0.97) !important;

        border: 1px solid #dce7f3 !important;

        border-radius: 18px !important;

        box-shadow:
            0 8px 28px rgba(28, 65, 105, 0.07);

        transition: 0.2s ease;
    }

    div[data-testid="stVerticalBlockBorderWrapper"]:hover {
        border-color: #c8ddf5 !important;

        box-shadow:
            0 12px 32px rgba(28, 65, 105, 0.10);
    }


    /* =====================================================
       INPUT FIELDS
    ===================================================== */

    div[data-testid="stNumberInput"] input {
        border-radius: 10px !important;

        border: 1px solid #d7e1ec !important;

        background: #fbfdff !important;

        color: #172b45 !important;
    }

    div[data-testid="stTextInput"] input {
        border-radius: 10px !important;

        border: 1px solid #d7e1ec !important;

        background: #fbfdff !important;
    }

    div[data-baseweb="select"] > div {
        border-radius: 10px !important;

        border: 1px solid #d7e1ec !important;

        background: #fbfdff !important;
    }


    /* =====================================================
       LABELS
    ===================================================== */

    label {
        color: #42566f !important;

        font-size: 11px !important;

        font-weight: 700 !important;
    }


    /* =====================================================
       SLIDER
    ===================================================== */

    div[data-testid="stSlider"] {
        padding-top: 3px;
        padding-bottom: 5px;
    }


    /* =====================================================
       BUTTON
    ===================================================== */

    .stButton > button {
        width: 100%;

        min-height: 50px;

        border-radius: 11px;

        border: none;

        background:
            linear-gradient(
                135deg,
                #1683ff,
                #0868d5
            );

        color: white;

        font-size: 13px;

        font-weight: 800;

        letter-spacing: 0.3px;

        box-shadow:
            0 7px 18px rgba(22, 131, 255, 0.20);

        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        background:
            linear-gradient(
                135deg,
                #0868d5,
                #0053b5
            );

        transform: translateY(-2px);

        box-shadow:
            0 10px 24px rgba(22, 131, 255, 0.28);
    }


    /* =====================================================
       ALERTS
    ===================================================== */

    div[data-testid="stAlert"] {
        border-radius: 11px !important;

        border: none !important;
    }


    /* =====================================================
       METRIC CARDS
    ===================================================== */

    div[data-testid="stMetric"] {
        background: #ffffff;

        border: 1px solid #dce7f2;

        border-radius: 14px;

        padding: 16px 17px;

        box-shadow:
            0 5px 18px rgba(28, 65, 105, 0.055);

        min-height: 95px;
    }

    div[data-testid="stMetricLabel"] {
        color: #718299 !important;

        font-size: 10px !important;

        font-weight: 700 !important;
    }

    div[data-testid="stMetricValue"] {
        color: #122b4a !important;

        font-size: 24px !important;

        font-weight: 850 !important;
    }


    /* =====================================================
       PROGRESS BAR
    ===================================================== */

    div[data-testid="stProgress"] > div {
        height: 10px;

        border-radius: 20px;

        background: #e5edf6;
    }

    div[data-testid="stProgress"] > div > div {
        border-radius: 20px;

        background:
            linear-gradient(
                90deg,
                #1683ff,
                #31a5ff
            );
    }


    /* =====================================================
       EXPANDER
    ===================================================== */

    div[data-testid="stExpander"] {
        border-radius: 13px !important;

        border: 1px solid #dce6f0 !important;

        background: white !important;
    }


    /* =====================================================
       DATAFRAME
    ===================================================== */

    div[data-testid="stDataFrame"] {
        border-radius: 13px;

        border: 1px solid #dce6f0;

        overflow: hidden;
    }


    /* =====================================================
       DIVIDER
    ===================================================== */

    hr {
        border-color: #dce6f0 !important;
    }


    /* =====================================================
       FOOTER
    ===================================================== */

    .footer-text {
        text-align: center;

        color: #8290a2;

        font-size: 11px;

        line-height: 1.7;
    }


    /* =====================================================
       SMALL LABEL
    ===================================================== */

    .section-label {
        color: #1683ff;

        font-size: 10px;

        font-weight: 800;

        letter-spacing: 1.2px;
    }


    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_model():

    if not MODEL_PATH.exists():

        st.error(
            f"""
            ❌ Model file not found.

            Expected location:

            {MODEL_PATH}
            """
        )

        st.stop()

    try:

        return joblib.load(MODEL_PATH)

    except Exception as e:

        st.error("❌ Model could not be loaded.")

        st.code(str(e))

        st.stop()


model = load_model()


# ============================================================
# TOP NAVIGATION
# ============================================================

top_left, top_middle, top_right = st.columns(
    [4.5, 2, 1.5]
)


with top_left:

    st.markdown(
        """
        <div class="brand-text">
            🚚 Supply<span class="brand-blue">Flow</span> AI
        </div>
        """,
        unsafe_allow_html=True
    )


with top_middle:

    st.write("")


with top_right:

    st.success("● Model Active")


st.write("")


# ============================================================
# HERO SECTION
# ============================================================

with st.container(border=True):

    st.markdown(
        '<div class="section-label">SUPPLY CHAIN INTELLIGENCE</div>',
        unsafe_allow_html=True
    )

    st.write("")

    st.markdown(
        """
        <div class="hero-title">
            Predict order delays before they happen.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="hero-description">
            SupplyFlow AI analyzes supplier reliability, inventory,
            shipping, weather and processing conditions to estimate
            the probability of fulfillment delays.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    st.info(
        "🤖 AI-powered order risk prediction • "
        "Real-time supply chain decision support"
    )


# ============================================================
# SECTION TITLE
# ============================================================

st.write("")

st.subheader("📦 Analyze an Order")

st.caption(
    "Configure the order details below and generate an AI-powered "
    "delay risk assessment."
)


# ============================================================
# MAIN LAYOUT
# ============================================================

input_col, result_col = st.columns(
    [1, 1],
    gap="large"
)


# ============================================================
# INPUT SECTION
# ============================================================

with input_col:

    with st.container(border=True):

        st.markdown("### ⚙️ Order Configuration")

        st.caption(
            "Enter the operational information used by the model."
        )

        st.write("")


        # ----------------------------------------------------
        # SUPPLIER RELIABILITY
        # ----------------------------------------------------

        supplier_reliability_score = st.slider(
            "Supplier Reliability Score",

            min_value=0.0,

            max_value=1.0,

            value=0.50,

            step=0.01,

            help=(
                "Higher values represent a more reliable supplier."
            )
        )


        # ----------------------------------------------------
        # INVENTORY
        # ----------------------------------------------------

        warehouse_inventory_level = st.number_input(
            "Warehouse Inventory Level",

            min_value=0.0,

            value=50.0,

            step=1.0
        )


        # ----------------------------------------------------
        # ORDER QUANTITY
        # ----------------------------------------------------

        order_quantity = st.number_input(
            "Order Quantity",

            min_value=0.0,

            value=50.0,

            step=1.0
        )


        # ----------------------------------------------------
        # SHIPPING DISTANCE
        # ----------------------------------------------------

        shipping_distance_km = st.number_input(
            "Shipping Distance (km)",

            min_value=0.0,

            value=500.0,

            step=10.0
        )


        # ----------------------------------------------------
        # SHIPPING METHOD
        # ----------------------------------------------------

        shipping_method = st.selectbox(
            "Shipping Method",

            [
                "Air",
                "Road",
                "Sea"
            ]
        )


        # ----------------------------------------------------
        # WEATHER
        # ----------------------------------------------------

        weather_condition = st.selectbox(
            "Weather Condition",

            [
                "Clear",
                "Cloudy",
                "Rainy",
                "Stormy"
            ]
        )


        # ----------------------------------------------------
        # PROCESSING TIME
        # ----------------------------------------------------

        processing_time_hours = st.number_input(
            "Processing Time (hours)",

            min_value=0.0,

            value=10.0,

            step=1.0
        )


        # ----------------------------------------------------
        # ORDER PRIORITY
        # ----------------------------------------------------

        order_priority = st.selectbox(
            "Order Priority",

            [
                "Low",
                "Medium",
                "High"
            ]
        )


        st.write("")


        # ----------------------------------------------------
        # PREDICT BUTTON
        # ----------------------------------------------------

        predict_button = st.button(
            "🚀  ANALYZE ORDER",
            use_container_width=True
        )


# ============================================================
# RESULT SECTION
# ============================================================

with result_col:

    with st.container(border=True):

        st.markdown("### 🎯 Prediction Result")

        st.caption(
            "Machine Learning powered risk assessment."
        )

        st.write("")


        if not predict_button:

            st.info(
                "👈 Configure the order details and click "
                "**Analyze Order** to generate the prediction."
            )

            st.write("")

            st.metric(
                "Delay Probability",
                "--"
            )

            st.progress(0)

            st.write("")

            st.markdown("#### 🧠 AI Decision Support")

            st.caption(
                "The model evaluates supplier reliability, inventory, "
                "order quantity, distance, shipping method, weather, "
                "processing time and priority."
            )


# ============================================================
# PREDICTION
# ============================================================

if predict_button:

    # --------------------------------------------------------
    # INPUT DATAFRAME
    # --------------------------------------------------------

    input_data = pd.DataFrame(
        {
            "supplier_reliability_score": [
                supplier_reliability_score
            ],

            "warehouse_inventory_level": [
                warehouse_inventory_level
            ],

            "order_quantity": [
                order_quantity
            ],

            "shipping_distance_km": [
                shipping_distance_km
            ],

            "shipping_method": [
                shipping_method
            ],

            "weather_condition": [
                weather_condition
            ],

            "processing_time_hours": [
                processing_time_hours
            ],

            "order_priority": [
                order_priority
            ]
        }
    )


    try:

        # ----------------------------------------------------
        # MODEL PREDICTION
        # ----------------------------------------------------

        prediction = model.predict(input_data)[0]


        # ----------------------------------------------------
        # PREDICTION PROBABILITY
        # ----------------------------------------------------

        if hasattr(model, "predict_proba"):

            probabilities = model.predict_proba(
                input_data
            )[0]

            if len(probabilities) == 2:

                delay_probability = (
                    float(probabilities[1]) * 100
                )

            else:

                delay_probability = (
                    float(max(probabilities)) * 100
                )

        else:

            if int(prediction) == 1:

                delay_probability = 100.0

            else:

                delay_probability = 0.0


        # ----------------------------------------------------
        # SAFETY LIMIT
        # ----------------------------------------------------

        delay_probability = max(
            0.0,

            min(
                100.0,
                delay_probability
            )
        )


        # ----------------------------------------------------
        # RISK LEVEL
        # ----------------------------------------------------

        if delay_probability < 35:

            risk = "LOW DELAY RISK"

            recommendation = (
                "The order currently shows favorable conditions. "
                "Normal monitoring should be sufficient."
            )

            risk_icon = "🟢"


        elif delay_probability < 65:

            risk = "MEDIUM DELAY RISK"

            recommendation = (
                "Some operational warning signals are present. "
                "Monitor inventory, processing and transportation "
                "conditions."
            )

            risk_icon = "🟡"


        else:

            risk = "HIGH DELAY RISK"

            recommendation = (
                "The order has elevated delay probability. "
                "Consider reviewing supplier, inventory and "
                "shipping conditions."
            )

            risk_icon = "🔴"


        # ====================================================
        # DISPLAY RESULT
        # ====================================================

        with result_col:

            with st.container(border=True):

                st.markdown("### 🎯 Prediction Result")

                st.caption(
                    "Machine Learning powered risk assessment."
                )

                st.write("")


                # ------------------------------------------------
                # RISK STATUS
                # ------------------------------------------------

                if delay_probability < 35:

                    st.success(
                        f"{risk_icon} {risk}"
                    )

                elif delay_probability < 65:

                    st.warning(
                        f"{risk_icon} {risk}"
                    )

                else:

                    st.error(
                        f"{risk_icon} {risk}"
                    )


                # ------------------------------------------------
                # SCORE
                # ------------------------------------------------

                st.caption("CURRENT RISK SCORE")

                st.metric(
                    "Delay Probability",
                    f"{delay_probability:.2f}%"
                )


                # ------------------------------------------------
                # PROGRESS
                # ------------------------------------------------

                st.progress(
                    int(delay_probability)
                )


                st.write("")


                # ------------------------------------------------
                # RECOMMENDATION
                # ------------------------------------------------

                st.markdown(
                    "#### 🧠 AI Recommendation"
                )

                st.info(
                    recommendation
                )


                st.write("")


                # ------------------------------------------------
                # MODEL DECISION
                # ------------------------------------------------

                if int(prediction) == 1:

                    st.error(
                        "📌 Model Decision: "
                        "This order is predicted to be delayed."
                    )

                else:

                    st.success(
                        "📌 Model Decision: "
                        "This order is predicted to be on time."
                    )


    except Exception as e:

        with result_col:

            st.error(
                "❌ Prediction failed."
            )

            st.code(
                str(e)
            )


# ============================================================
# ORDER SNAPSHOT
# ============================================================

if predict_button:

    st.write("")

    st.subheader("📊 Order Snapshot")

    st.caption(
        "Key operational values used for the prediction."
    )

    st.write("")


    snapshot_1, snapshot_2, snapshot_3, snapshot_4 = st.columns(4)


    with snapshot_1:

        st.metric(
            "Supplier Score",

            f"{supplier_reliability_score:.2f}"
        )


    with snapshot_2:

        st.metric(
            "Order Quantity",

            f"{order_quantity:,.0f}"
        )


    with snapshot_3:

        st.metric(
            "Shipping Distance",

            f"{shipping_distance_km:,.0f} km"
        )


    with snapshot_4:

        st.metric(
            "Processing Time",

            f"{processing_time_hours:,.0f} hrs"
        )


# ============================================================
# MODEL PERFORMANCE
# ============================================================

st.write("")

st.subheader("📈 Model Performance")

st.caption(
    "Evaluation metrics from the trained Machine Learning model."
)

st.write("")


performance_1, performance_2, performance_3, performance_4 = st.columns(4)


with performance_1:

    st.metric(
        "Accuracy",
        f"{MODEL_ACCURACY:.2f}%"
    )


with performance_2:

    st.metric(
        "Precision",
        f"{MODEL_PRECISION:.2f}%"
    )


with performance_3:

    st.metric(
        "Recall",
        f"{MODEL_RECALL:.2f}%"
    )


with performance_4:

    st.metric(
        "F1 Score",
        f"{MODEL_F1:.2f}%"
    )


# ============================================================
# ADDITIONAL MODEL INFORMATION
# ============================================================

st.write("")

with st.expander("🔍 View Model Information"):

    info_1, info_2, info_3 = st.columns(3)


    with info_1:

        st.write("**Algorithm**")

        st.write(
            "Best Performing Classification Model"
        )


    with info_2:

        st.write("**Prediction Type**")

        st.write(
            "Binary Classification"
        )


    with info_3:

        st.write("**Deployment**")

        st.write(
            "Streamlit Web Application"
        )


# ============================================================
# SUBMITTED DATA
# ============================================================

if predict_button:

    st.write("")

    with st.expander("📋 View Submitted Order Details"):

        st.dataframe(
            input_data,

            use_container_width=True,

            hide_index=True
        )


# ============================================================
# FOOTER
# ============================================================

st.write("")

st.divider()

st.markdown(
    """
    <div class="footer-text">
        🚚 SupplyFlow AI
        <br>
        Supply Chain Order Fulfillment Delay Prediction
        <br>
        Built with Python • Pandas • Scikit-learn • Streamlit
    </div>
    """,
    unsafe_allow_html=True
)