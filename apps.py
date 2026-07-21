# SMART CALCULATOR

import streamlit as st
import pandas as pd
import math

from operations import (
    calculator,
    power,
    square_root,
    percentage,
    percentage_of,
    percentage_change,
    average,
    sine,
    cosine,
    tangent,
    logarithm,
    natural_log,
    factorial,
)

from converter import (
    convert_length,
    convert_weight,
    convert_temperature,
)

from constant import (
    APP_NAME,
    VERSION,
    OPERATORS,
    LENGTH_UNITS,
    WEIGHT_UNITS,
    TEMPERATURE_UNITS,
)

# PAGE CONFIG

st.set_page_config(
    page_title=APP_NAME,
    page_icon="🧮",
    layout="centered",
)

# SESSION STATE

if "history" not in st.session_state:
    st.session_state.history = []


def add_to_history(expression, result):
    st.session_state.history.append(
        {
            "expression": expression,
            "result": result,
        }
    )

st.title("🧮 SMART CALCULATOR")
st.caption("A Python Powered Calculator built using Streamlit")
st.success(
    "👋 Welcome! Select a calculator mode from the sidebar."
)

#SIDEBAR

st.sidebar.title("🧮 SMART CALCULATOR")

st.sidebar.info(
    """
👋 **Welcome!**

Choose a calculator mode from below.
"""
)

mode = st.sidebar.radio(
    "Choose Mode",
    [
        "Basic Math",
        "Power & Root",
        "Scientific Calculator",
        "Percentage",
        "Average",
        "Unit Converter",
        "History",
    ],
)

st.sidebar.markdown("---")
st.sidebar.subheader("✨ Features")

st.sidebar.success("✔ Basic Math")
st.sidebar.success("✔ Scientific Calculator")
st.sidebar.success("✔ Unit Converter")
st.sidebar.success("✔ Percentage Calculator")
st.sidebar.success("✔ Average Calculator")
st.sidebar.success("✔ History")
st.sidebar.success("✔ CSV Download")

st.sidebar.markdown("---")

st.sidebar.caption(f"Version {VERSION}")
st.sidebar.caption("Made with ❤️ by Amisha Goyal")


#BASIC MATHS

if mode == "Basic Math":

    st.header("➕ Basic Calculator")

    col1, col2, col3 = st.columns([2, 1, 2])

    with col1:
        num1 = st.number_input(
            "First Number",
            value=0.0,
            key="num1", 
            help="Enter the first number for calculation.",
)         

    with col2:
        operator = st.selectbox(
            "Operator",
            list(OPERATORS.keys()),
        )

    with col3:
        num2 = st.number_input(
            "Second Number",
            value=0.0,
            key="num2",
            help="Enter the second number for calculation.",
        )

    if st.button("Calculate"):

        symbol = OPERATORS[operator]

        result = calculator(
            num1,
            num2,
            symbol,
        )

        if isinstance(result, str):
            st.error(result)

        else:
            expression = f"{num1} {symbol} {num2}"

            st.success(
                f"{expression} = **{result}**"
            )

            add_to_history(
                expression,
                result,
            )

            st.divider()



# ==========================
# POWER & ROOT
# ==========================

elif mode == "Power & Root":

    st.header("⚡ Power & Root")

    tab1, tab2 = st.tabs(
        ["Power (xⁿ)", "Square Root"]
    )

    # ---------------------
    # Power
    # ---------------------

    with tab1:

        base = st.number_input(
            "Base",
            value=2.0,
            help="Enter the base value.",
        )

        exponent = st.number_input(
            "Exponent",
            value=3.0,
            help="Enter the exponent (power).",
        )

        if st.button("Calculate Power"):

            result = power(
                base,
                exponent,
            )

            expression = f"{base}^{exponent}"

            st.success(
                f"{expression} = **{result}**"
            )

            add_to_history(
                expression,
                result,
            )

    # ---------------------
    # Square Root
    # ---------------------

    with tab2:

        number = st.number_input(
            "Number",
            value=16.0,
            help="Enter a non-negative number.",
        )

        if st.button("Find Square Root"):

            result = square_root(number)

            if isinstance(result, str):
                st.error(result)

            else:

                expression = f"√{number}"

                st.success(
                    f"{expression} = **{result}**"
                )

                add_to_history(
                    expression,
                    result,
                )
                st.divider()

# ==========================
# PERCENTAGE
# ==========================

elif mode == "Percentage":

    st.header("📊 Percentage Calculator")

    tab1, tab2, tab3 = st.tabs(
        [
            "What % is X of Y?",
            "X% of Y",
            "% Change",
        ]
    )

    # -----------------

    with tab1:

        value = st.number_input(
            "Value",
            value=25.0,
        )

        total = st.number_input(
            "Total",
            value=100.0,
        )

        if st.button("Find Percentage"):

            result = percentage(
                value,
                total,
            )

            if isinstance(result, str):
                st.error(result)

            else:

                st.success(
                    f"{value} is **{round(result,2)}%** of {total}"
                )

                add_to_history(
                    f"{value} of {total}",
                    f"{round(result,2)}%",
                )

    # -----------------

    with tab2:

        percent = st.number_input(
            "Percentage",
            value=20.0,
        )

        number = st.number_input(
            "Number",
            value=500.0,
        )

        if st.button("Find Value"):

            result = percentage_of(
                percent,
                number,
            )

            st.success(
                f"{percent}% of {number} = **{result}**"
            )

            add_to_history(
                f"{percent}% of {number}",
                result,
            )

    # -----------------

    with tab3:

        old = st.number_input(
            "Old Value",
            value=100.0,
        )

        new = st.number_input(
            "New Value",
            value=120.0,
        )

        if st.button("Find Change"):

            result = percentage_change(
                old,
                new,
            )

            if isinstance(result, str):
                st.error(result)

            else:

                if result >= 0:
                    status = "Increase 📈"
                else:
                    status = "Decrease 📉"

                st.success(
                    f"{status} : **{abs(result):.2f}%**"
                )

                add_to_history(
                    "Percentage Change",
                    f"{result:.2f}%",
                )
                st.divider()

# ==========================
# AVERAGE
# ==========================


elif mode == "Average":

    st.header("📈 Average Calculator")

    numbers = st.text_input(
        "Enter numbers separated by commas",
        "10,20,30,40",
        help="Example: 10, 20, 30, 40",
    )

    if st.button("Calculate Average"):

        try:

            values = [
                float(i.strip())
                for i in numbers.split(",")
            ]

            result = average(values)

            if isinstance(result, str):
                st.error(result)

            else:

                st.success(
                    f"Average = **{round(result, 2)}**"
                )

                st.info(
                    f"Count = {len(values)} | Sum = {sum(values)}"
                )

                add_to_history(
                    "Average",
                    result,
                )

        except ValueError:

            st.error(
                "Please enter valid numbers."
            )

# ==========================
# SCIENTIFIC CALCULATOR
# ==========================

elif mode == "Scientific Calculator":

    st.header("🧮 Scientific Calculator")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("π (Pi)", round(math.pi, 6))

    with col2:
        st.metric("e", round(math.e, 6))

    tab1, tab2, tab3 = st.tabs(
        [
            "Trigonometry",
            "Logarithm",
            "Factorial",
        ]
    )

    # -------------------------
    # TRIGONOMETRY
    # -------------------------

    with tab1:

        angle = st.number_input(
            "Angle (Degrees)",
            min_value=0,
            max_value=360,
            value=30,
            step=1,
            help="Enter an angle between 0° and 360°.",
        )

        function = st.selectbox(
            "Function",
            [
                "sin",
                "cos",
                "tan",
            ],
        )

        if st.button("Calculate", key="trig"):

            if function == "sin":
                result = sine(angle)

            elif function == "cos":
                result = cosine(angle)

            else:
                result = tangent(angle)

            if isinstance(result, str):
                st.error(result)

            else:
                st.success(
                    f"{function}({angle}) = **{result}**"
                )

                add_to_history(
                    f"{function}({angle})",
                    result,
                )

    # -------------------------
    # LOGARITHM
    # -------------------------

    with tab2:

        number = st.number_input(
            "Number",
            value=10.0,
        )

        log_type = st.selectbox(
            "Log Function",
            [
                "log10",
                "ln",
            ],
        )

        if st.button("Calculate", key="log"):

            if log_type == "log10":
                result = logarithm(number)

            else:
                result = natural_log(number)

            if isinstance(result, str):
                st.error(result)

            else:
                st.success(
                    f"{log_type}({number}) = **{result}**"
                )

                add_to_history(
                    f"{log_type}({number})",
                    result,
                )

    # -------------------------
    # FACTORIAL
    # -------------------------

    with tab3:

        number = st.number_input(
            "Whole Number",
            value=5.0,
        )

        if st.button(
            "Find Factorial",
            key="factorial",
        ):

            result = factorial(number)

            if isinstance(result, str):
                st.error(result)

            else:
                st.success(
                    f"{int(number)}! = **{result}**"
                )

                add_to_history(
                    f"{int(number)}!",
                    result,
                )
                st.divider()
# ==========================
# UNIT CONVERTER
# ==========================

elif mode == "Unit Converter":

    st.header("📏 Unit Converter")

    category = st.selectbox(
        "Category",
        [
            "Length",
            "Weight",
            "Temperature",
        ],
    )

    col1, col2 = st.columns(2)

    # -------------------------
    # LENGTH
    # -------------------------

    if category == "Length":

        with col1:
            from_unit = st.selectbox(
                "From",
                list(LENGTH_UNITS.keys()),
                key="len_from",
            )

        with col2:
            to_unit = st.selectbox(
                "To",
                list(LENGTH_UNITS.keys()),
                key="len_to",
            )

        

    # -------------------------
    # WEIGHT
    # -------------------------

    elif category == "Weight":

        with col1:
            from_unit = st.selectbox(
                "From",
                list(WEIGHT_UNITS.keys()),
                key="wt_from",
            )

        with col2:
            to_unit = st.selectbox(
                "To",
                list(WEIGHT_UNITS.keys()),
                key="wt_to",
            )

        

    # -------------------------
    # TEMPERATURE
    # -------------------------

    else:

        with col1:
            from_unit = st.selectbox(
                "From",
                TEMPERATURE_UNITS,
                key="temp_from",
            )

        with col2:
            to_unit = st.selectbox(
                "To",
                TEMPERATURE_UNITS,
                key="temp_to",
            )

        

    # -------------------------
    # VALUE
    # -------------------------

    value = st.number_input(
        "Value",
        value=1.0,
        help="Enter the value you want to convert.",
    )

    if st.button("Convert"):

        if category == "Length":

            result = convert_length(
                value,
                from_unit,
                to_unit,
            )

        elif category == "Weight":

            result = convert_weight(
                value,
                from_unit,
                to_unit,
            )

        else:

            result = convert_temperature(
                value,
                from_unit,
                to_unit,
            )

        st.success(
            f"{value} {from_unit} = **{result} {to_unit}**"
        )

        add_to_history(
            f"{value} {from_unit} → {to_unit}",
            f"{result} {to_unit}",
        )
        st.divider()

# ==========================
# HISTORY
# ==========================

elif mode == "History":

    st.header("🕒 Calculation History")

    if len(st.session_state.history) == 0:

        st.info("No calculations yet.")

    else:

        for i, item in enumerate(
            reversed(st.session_state.history),
            start=1,
        ):

           st.info(
               f"**{i}.** {item['expression']} = {item['result']}"
           )
        # Download CSV
        df = pd.DataFrame(st.session_state.history)

        csv = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="📥 Download History as CSV",
            data=csv,
            file_name="calculator_history.csv",
            mime="text/csv",
        )

        st.divider()
        
        st.caption(
            "© 2026 Smart Calculator | Made using Python & Streamlit"
        )

