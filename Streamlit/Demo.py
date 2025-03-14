import streamlit as st  


# Set Page Configuration
st.set_page_config(page_title="Styled Streamlit App", layout="wide")

# Set the Title 
st.title('WEB PAGE DESIGN USING STREAMLIT')
st.markdown('---')
# Set the Header
st.header('1: This is Header for My Web Page')
st.markdown('---')
# Set the Sub Header
st.subheader('1.1: This is Sub Header for My Web Page')
st.markdown('---')

# Adding a paragraph
st.text('This is a simple text paragraph added to the Streamlit app.')

st.markdown('---')
# Adding a code block
st.code("print('Hello, Streamlit!')", language="python")
st.markdown('---')
# Adding a SQL Code Block
sql_code = """
SELECT customer_id, customer_name, total_amount
FROM orders
WHERE order_date >= '2024-01-01'
ORDER BY total_amount DESC;
"""

st.code(sql_code, language="sql")
st.markdown('---')

# Write the code block using write function : formulas written using latex syntax
st.write("Here is the quadratic formula:")  
st.write(r"$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$")  

# Create and Display DataFrame 
import pandas as pd

# Title
st.title("New DataFrame Example in Streamlit")

# Creating a new DataFrame
new_data = {
    "Employee ID": [101, 102, 103, 104, 105],
    "Name": ["John", "Emma", "Liam", "Olivia", "Sophia"],
    "Department": ["HR", "Finance", "IT", "Marketing", "Sales"],
    "Salary": [50000, 60000, 75000, 55000, 65000]
}

new_df = pd.DataFrame(new_data)

# Displaying the DataFrame
st.write("### Employee DataBase")
st.dataframe(new_df)  