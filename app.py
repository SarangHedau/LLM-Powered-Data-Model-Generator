import streamlit as st

from src.llm import generate_data_model
from src.dbt_generator import generate_dbt_models
from src.star_schema import generate_star_schema
from src.render import (
    render_fact_tables,
    render_dimension_tables,
    render_relationships,
)

# ----------------------------------------------------
# Page Configuration
# ----------------------------------------------------
st.set_page_config(
    page_title="LLM Powered Data Model Generator",
    page_icon="🧠",
    layout="wide"
)

# ----------------------------------------------------
# Title
# ----------------------------------------------------
st.title("🧠 LLM Powered Data Model Generator")

st.markdown("""
Generate **Fact Tables**, **Dimension Tables**, **Relationships**, and a **Star Schema**
from any database schema using **Gemini AI**.
""")

# ----------------------------------------------------
# User Input
# ----------------------------------------------------
user_prompt = st.text_area(
    "Enter your Schema + Business Requirement",
    height=350,
    placeholder="""
Example:

Schema:

Customers
---------
CustomerID
CustomerName
City

Orders
------
OrderID
CustomerID
ProductID
Quantity
SalesAmount
OrderDate

Products
--------
ProductID
ProductName
Category

Business Requirement:

Build a Sales Data Warehouse.

KPIs:
- Revenue
- Monthly Sales
- Sales by Category
- Customer Performance

Generate:
1. Fact Tables
2. Dimension Tables
3. Grain
4. Relationships
5. Star Schema
6. dbt Models
"""
)

# ----------------------------------------------------
# Generate Button
# ----------------------------------------------------
if st.button("🚀 Generate Data Model", use_container_width=True):

    if not user_prompt.strip():
        st.warning("Please enter a schema and business requirement.")
        st.stop()

    with st.spinner("🤖 Gemini is analyzing your schema..."):

        try:

            result = generate_data_model(user_prompt)

            st.success("✅ Data Model Generated Successfully!")

            st.divider()

            # ---------------------------------------------
            # Fact Tables
            # ---------------------------------------------
            render_fact_tables(result.fact_tables)

            st.divider()

            # ---------------------------------------------
            # Dimension Tables
            # ---------------------------------------------
            render_dimension_tables(result.dimension_tables)

            st.divider()

            # ---------------------------------------------
            # Relationships
            # ---------------------------------------------
            render_relationships(result.relationships)

            st.divider()

            st.subheader("⭐ Star Schema Diagram")

            graph = generate_star_schema(result)

            st.graphviz_chart(graph.source)

            st.divider()

            st.subheader("🛠 Generating dbt Models...")

            folder = generate_dbt_models(result)

            st.success("dbt Models Generated!")

            st.write(f"Saved to: {folder}")


            # ---------------------------------------------
            # Raw JSON (Optional)
            # ---------------------------------------------
            with st.expander("📄 View Raw JSON"):
                st.json(result.model_dump())

        except Exception as e:

            st.error("❌ Error while generating the data model.")

            st.exception(e)