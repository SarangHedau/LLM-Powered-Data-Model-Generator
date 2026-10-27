from typing import List, Optional

from pydantic import BaseModel, Field


# -------------------------
# Fact Table
# -------------------------
class FactTable(BaseModel):
    name: str
    source_table: Optional[str] = None
    grain: Optional[str] = None

    measures: List[str] = Field(default_factory=list)
    foreign_keys: List[str] = Field(default_factory=list)

    dbt_model: Optional[str] = None


# -------------------------
# Dimension Table
# -------------------------
class DimensionTable(BaseModel):
    name: str
    source_table: Optional[str] = None

    attributes: List[str] = Field(default_factory=list)

    primary_key: Optional[str] = None
    surrogate_key: Optional[str] = None

    scd_type: Optional[str] = None

    dbt_model: Optional[str] = None


# -------------------------
# Relationship
# -------------------------
class Relationship(BaseModel):
    fact_table: str
    dimension_table: str

    join_key: Optional[str] = None


# -------------------------
# Star Schema
# -------------------------
class StarSchema(BaseModel):
    fact_table: Optional[str] = None
    dimensions: List[str] = Field(default_factory=list)


# -------------------------
# Final Response
# -------------------------
class DataModelResponse(BaseModel):
    fact_tables: List[FactTable] = Field(default_factory=list)

    dimension_tables: List[DimensionTable] = Field(default_factory=list)

    relationships: List[Relationship] = Field(default_factory=list)

    star_schema: Optional[StarSchema] = None