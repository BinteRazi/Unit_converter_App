# Import libraries
import streamlit as st
from pyngrok import ngrok

# Title of the app
st.title("🚀 Unit Converter")
st.write("Convert between various units easily!")

# Sidebar for unit categories
unit_category = st.sidebar.selectbox(
    "Select Unit Category",
    ["Length", "Weight", "Temperature", "Volume"]
)

# Conversion logic based on selected category
if unit_category == "Length":
    st.header("Length Converter")
    length_units = ["Meters", "Kilometers", "Miles", "Feet", "Inches"]
    from_unit = st.selectbox("From", length_units)
    to_unit = st.selectbox("To", length_units)
    value = st.number_input("Enter value", value=1.0)

    # Conversion formulas
    if from_unit == "Meters":
        if to_unit == "Kilometers":
            result = value / 1000
        elif to_unit == "Miles":
            result = value * 0.000621371
        elif to_unit == "Feet":
            result = value * 3.28084
        elif to_unit == "Inches":
            result = value * 39.3701
        else:
            result = value
    elif from_unit == "Kilometers":
        if to_unit == "Meters":
            result = value * 1000
        elif to_unit == "Miles":
            result = value * 0.621371
        elif to_unit == "Feet":
            result = value * 3280.84
        elif to_unit == "Inches":
            result = value * 39370.1
        else:
            result = value
    elif from_unit == "Miles":
        if to_unit == "Meters":
            result = value * 1609.34
        elif to_unit == "Kilometers":
            result = value * 1.60934
        elif to_unit == "Feet":
            result = value * 5280
        elif to_unit == "Inches":
            result = value * 63360
        else:
            result = value
    elif from_unit == "Feet":
        if to_unit == "Meters":
            result = value * 0.3048
        elif to_unit == "Kilometers":
            result = value * 0.0003048
        elif to_unit == "Miles":
            result = value * 0.000189394
        elif to_unit == "Inches":
            result = value * 12
        else:
            result = value
    elif from_unit == "Inches":
        if to_unit == "Meters":
            result = value * 0.0254
        elif to_unit == "Kilometers":
            result = value * 0.0000254
        elif to_unit == "Miles":
            result = value * 0.000015783
        elif to_unit == "Feet":
            result = value * 0.0833333
        else:
            result = value

    st.success(f"Result: {value} {from_unit} = {result:.4f} {to_unit}")

elif unit_category == "Weight":
    st.header("Weight Converter")
    weight_units = ["Kilograms", "Grams", "Pounds", "Ounces"]
    from_unit = st.selectbox("From", weight_units)
    to_unit = st.selectbox("To", weight_units)
    value = st.number_input("Enter value", value=1.0)

    # Conversion formulas
    if from_unit == "Kilograms":
        if to_unit == "Grams":
            result = value * 1000
        elif to_unit == "Pounds":
            result = value * 2.20462
        elif to_unit == "Ounces":
            result = value * 35.274
        else:
            result = value
    elif from_unit == "Grams":
        if to_unit == "Kilograms":
            result = value / 1000
        elif to_unit == "Pounds":
            result = value * 0.00220462
        elif to_unit == "Ounces":
            result = value * 0.035274
        else:
            result = value
    elif from_unit == "Pounds":
        if to_unit == "Kilograms":
            result = value * 0.453592
        elif to_unit == "Grams":
            result = value * 453.592
        elif to_unit == "Ounces":
            result = value * 16
        else:
            result = value
    elif from_unit == "Ounces":
        if to_unit == "Kilograms":
            result = value * 0.0283495
        elif to_unit == "Grams":
            result = value * 28.3495
        elif to_unit == "Pounds":
            result = value * 0.0625
        else:
            result = value

    st.success(f"Result: {value} {from_unit} = {result:.4f} {to_unit}")

elif unit_category == "Temperature":
    st.header("Temperature Converter")
    temp_units = ["Celsius", "Fahrenheit", "Kelvin"]
    from_unit = st.selectbox("From", temp_units)
    to_unit = st.selectbox("To", temp_units)
    value = st.number_input("Enter value", value=0.0)

    # Conversion formulas
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            result = (value * 9/5) + 32
        elif to_unit == "Kelvin":
            result = value + 273.15
        else:
            result = value
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            result = (value - 32) * 5/9
        elif to_unit == "Kelvin":
            result = (value - 32) * 5/9 + 273.15
        else:
            result = value
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            result = value - 273.15
        elif to_unit == "Fahrenheit":
            result = (value - 273.15) * 9/5 + 32
        else:
            result = value

    st.success(f"Result: {value} {from_unit} = {result:.4f} {to_unit}")

elif unit_category == "Volume":
    st.header("Volume Converter")
    volume_units = ["Liters", "Milliliters", "Gallons", "Cubic Meters"]
    from_unit = st.selectbox("From", volume_units)
    to_unit = st.selectbox("To", volume_units)
    value = st.number_input("Enter value", value=1.0)

    # Conversion formulas
    if from_unit == "Liters":
        if to_unit == "Milliliters":
            result = value * 1000
        elif to_unit == "Gallons":
            result = value * 0.264172
        elif to_unit == "Cubic Meters":
            result = value / 1000
        else:
            result = value
    elif from_unit == "Milliliters":
        if to_unit == "Liters":
            result = value / 1000
        elif to_unit == "Gallons":
            result = value * 0.000264172
        elif to_unit == "Cubic Meters":
            result = value / 1e6
        else:
            result = value
    elif from_unit == "Gallons":
        if to_unit == "Liters":
            result = value * 3.78541
        elif to_unit == "Milliliters":
            result = value * 3785.41
        elif to_unit == "Cubic Meters":
            result = value * 0.00378541
        else:
            result = value
    elif from_unit == "Cubic Meters":
        if to_unit == "Liters":
            result = value * 1000
        elif to_unit == "Milliliters":
            result = value * 1e6
        elif to_unit == "Gallons":
            result = value * 264.172
        else:
            result = value

    st.success(f"Result: {value} {from_unit} = {result:.4f} {to_unit}")
