import os


def generate_dbt_models(data_model):

    output_folder = "generated_models"

    os.makedirs(output_folder, exist_ok=True)

    # ----------------------------
    # Generate Fact Models
    # ----------------------------

    for fact in data_model.fact_tables:

        filename = os.path.join(
            output_folder,
            f"{fact.dbt_model}.sql"
        )

        sql = f"""{{{{ config(materialized='table') }}}}

SELECT *

FROM {{{{ source('raw', '{fact.source_table}') }}}}
"""

        with open(filename, "w") as f:
            f.write(sql)

    # ----------------------------
    # Generate Dimension Models
    # ----------------------------

    for dim in data_model.dimension_tables:

        filename = os.path.join(
            output_folder,
            f"{dim.dbt_model}.sql"
        )

        sql = f"""{{{{ config(materialized='table') }}}}

SELECT *

FROM {{{{ source('raw', '{dim.source_table}') }}}}
"""

        with open(filename, "w") as f:
            f.write(sql)

    return output_folder