import streamlit as st
import numpy as np
import pandas as pd
from streamlit_option_menu import option_menu

# Set page config
st.set_page_config(page_title="Statistics Math Hub", layout="wide")

# Custom CSS for LaTeX rendering and styling
st.markdown("""
<style>
    .big-font { font-size: 24px !important; font-weight: bold; }
    .formula { font-size: 22px; text-align: center; padding: 20px; background: #f0f2f6; border-radius: 10px; }
    .eq { font-size: 20px; color: #1f77b4; }
</style>
""", unsafe_allow_html=True)

# Sidebar menu using streamlit-option-menu
with st.sidebar:
    selected = option_menu(
        "Statistics Math Hub",
        ["Statistical Formulas", "Core Equations", "Math & Calculations"],
        icons=['calculator', 'gear', 'function'],
        menu_icon="book",
        default_index=0,
        styles={
            "container": {"padding": "5!important", "background-color": "#fafafa"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px"},
            "nav-link-selected": {"background-color": "#1f77b4"},
        }
    )

# Sample data for calculations
@st.cache_data
def generate_sample_data():
    np.random.seed(42)
    return np.random.normal(50, 10, 30).round(2)

data = generate_sample_data()

# Helper function to apply BODMAS
def calculate_bodmas(expression):
    try:
        # Safely evaluate using BODMAS via Python's order of operations
        return eval(expression, {"__builtins__": {}}, {})
    except:
        return "Invalid expression"

# Page 1: Statistical Formulas
if selected == "Statistical Formulas":
    st.markdown("<h1 class='big-font'>📊 Statistical Formulas</h1>", unsafe_allow_html=True)
    st.markdown("### Key Formulas in Descriptive & Inferential Statistics")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### Measures of Central Tendency")
        st.markdown("<div class='formula'>Mean: $\\bar{x} = \\frac{\\sum x_i}{n}$</div>", unsafe_allow_html=True)
        st.markdown("<div class='formula'>Median: Middle value (sorted)</div>", unsafe_allow_html=True)
        st.markdown("<div class='formula'>Mode: Most frequent value</div>", unsafe_allow_html=True)

        st.markdown("#### Measures of Dispersion")
        st.markdown("<div class='formula'>Variance: $\\sigma^2 = \\frac{\\sum (x_i - \\bar{x})^2}{n}$</div>", unsafe_allow_html=True)
        st.markdown("<div class='formula'>Std Dev: $\\sigma = \\sqrt{\\sigma^2}$</div>", unsafe_allow_html=True)
        st.markdown("<div class='formula'>Range: $max - min$</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("#### Probability & Inference")
        st.markdown("<div class='formula'>Z-Score: $z = \\frac{x - \\mu}{\\sigma}$</div>", unsafe_allow_html=True)
        st.markdown("<div class='formula'>Confidence Interval: $\\bar{x} \\pm z \\cdot \\frac{s}{\\sqrt{n}}$</div>", unsafe_allow_html=True)
        st.markdown("<div class='formula'>Correlation: $r = \\frac{\\sum (x_i - \\bar{x})(y_i - \\bar{y})}{\\sqrt{\\sum (x_i - \\bar{x})^2 \\sum (y_i - \\bar{y})^2}}$</div>", unsafe_allow_html=True)

    st.info("All formulas follow **BODMAS** order in computation.")

# Page 2: Core Equations
elif selected == "Core Equations":
    st.markdown("<h1 class='big-font'>⚙️ Core Statistical Equations</h1>", unsafe_allow_html=True)
    st.markdown("### Breakdown of Equations Behind the Formulas")

    st.markdown("#### 1. Population Mean")
    st.latex(r"\mu = \frac{\sum_{i=1}^{N} x_i}{N}")

    st.markdown("#### 2. Sample Variance (BODMAS Step-by-Step)")
    st.markdown("<p class='eq'>Step 1: $(x_i - \\bar{x})$ → Subtraction</p>", unsafe_allow_html=True)
    st.markdown("<p class='eq'>Step 2: $(x_i - \\bar{x})^2$ → Brackets & Power</p>", unsafe_allow_html=True)
    st.markdown("<p class='eq'>Step 3: $\\sum (x_i - \\bar{x})^2$ → Sum</p>", unsafe_allow_html=True)
    st.markdown("<p class='eq'>Step 4: $\\frac{\\sum (x_i - \\bar{x})^2}{n-1}$ → Division</p>", unsafe_allow_html=True)

    st.latex(r"s^2 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n-1}")

    st.markdown("#### 3. Standard Error")
    st.latex(r"SE = \frac{s}{\sqrt{n}}")

    st.markdown("#### 4. T-Statistic")
    st.latex(r"t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}}")

    st.success("All equations respect **BODMAS**: Brackets → Orders → Division/Multiplication → Addition/Subtraction")

# Page 3: Math & Calculations
elif selected == "Math & Calculations":
    st.markdown("<h1 class='big-font'>🧮 Interactive Math Calculator</h1>", unsafe_allow_html=True)
    st.markdown("### Compute Using BODMAS & Statistics")

    tab1, tab2, tab3 = st.tabs(["Live Data Stats", "BODMAS Calculator", "Z-Score & CI"])

    with tab1:
        st.markdown("#### Sample Dataset (n=30)")
        df = pd.DataFrame(data, columns=["Values"])
        st.dataframe(df.T, use_container_width=True)

        mean = np.mean(data)
        std = np.std(data, ddof=1)
        var = np.var(data, ddof=1)

        col1, col2, col3 = st.columns(3)
        col1.metric("Mean", f"{mean:.2f}")
        col2.metric("Std Dev", f"{std:.2f}")
        col3.metric("Variance", f"{var:.2f}")

    with tab2:
        st.markdown("#### BODMAS Expression Evaluator")
        expr = st.text_input("Enter math expression (e.g., (5+3)*2**3 / 4)", "(15 + 5) * 2 ** 2")
        if st.button("Calculate"):
            result = calculate_bodmas(expr)
            st.markdown(f"**Input:** `{expr}`")
            st.markdown(f"**Result:** `{result}`")
            st.info("Python follows BODMAS automatically!")

    with tab3:
        st.markdown("#### Z-Score & 95% Confidence Interval")
        x = st.number_input("Observed Value (x)", value=55.0)
        mu = st.number_input("Population Mean (μ)", value=50.0)
        sigma = st.number_input("Population Std Dev (σ)", value=10.0)
        n = st.slider("Sample Size (n)", 10, 100, 30)

        z = (x - mu) / (sigma / np.sqrt(n))
        ci = 1.96 * (sigma / np.sqrt(n))
        lower = x - ci
        upper = x + ci

        st.metric("Z-Score", f"{z:.3f}")
        st.write(f"**95% CI:** [{lower:.2f}, {upper:.2f}]")

        st.latex(f"z = \\frac{{{x} - {mu}}}{{{sigma} / \\sqrt{{{n}}}}} = {z:.3f}")

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: grey;'>"
    "Built with ❤️ using Streamlit | BODMAS-Powered Statistics"
    "</p>",
    unsafe_allow_html=True
)
