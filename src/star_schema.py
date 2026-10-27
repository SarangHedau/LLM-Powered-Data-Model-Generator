from graphviz import Digraph


def generate_star_schema(data_model):
    """
    Creates a Graphviz star schema diagram from the validated data model.
    """

    dot = Digraph("StarSchema")

    dot.attr(rankdir="LR")
    dot.attr("node", fontname="Arial")

    # -------------------------
    # Get Fact Table
    # -------------------------
    if not data_model.fact_tables:
        return dot

    fact = data_model.fact_tables[0]

    dot.node(
        fact.name,
        shape="box",
        style="filled",
        fillcolor="gold"
    )

    # -------------------------
    # Add Dimension Tables
    # -------------------------
    for dim in data_model.dimension_tables:

        dot.node(
            dim.name,
            shape="ellipse",
            style="filled",
            fillcolor="lightblue"
        )

        dot.edge(dim.name, fact.name)

    return dot