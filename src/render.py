import streamlit as st


def render_fact_tables(facts):
    st.subheader("📊 Fact Tables")

    for fact in facts:
        with st.expander(f"📦 {fact.name}", expanded=True):

            st.write(f"**Source Table:** {fact.source_table}")
            st.write(f"**Grain:** {fact.grain}")
            st.write(f"**dbt Model:** {fact.dbt_model}")

            st.write("### Measures")
            st.write(fact.measures)

            st.write("### Foreign Keys")
            st.write(fact.foreign_keys)


def render_dimension_tables(dimensions):
    st.subheader("📋 Dimension Tables")

    for dim in dimensions:
        with st.expander(f"📁 {dim.name}"):

            st.write(f"**Source Table:** {dim.source_table}")

            st.write(f"**Primary Key:** {dim.primary_key}")

            st.write(f"**Surrogate Key:** {dim.surrogate_key}")

            st.write(f"**SCD Type:** {dim.scd_type}")

            st.write(f"**dbt Model:** {dim.dbt_model}")

            st.write("### Attributes")

            st.write(dim.attributes)


def render_relationships(relationships):

    st.subheader("🔗 Relationships")

    for relation in relationships:

        st.write(
            f"{relation.fact_table}  →  {relation.dimension_table} ({relation.join_key})"
        )