# LLM-Powered Data Model Generator

An AI-powered data modeling assistant that transforms database schemas and business requirements into structured dimensional data models. Built with Python, Streamlit, and Google's Gemini API, the application helps analytics engineers design data warehouse models and visualize star schemas.

## Overview

Designing a data warehouse requires identifying fact tables, dimension tables, table grain, keys, and relationships from raw source schemas and business requirements.

The LLM-Powered Data Model Generator simplifies this process by using a Large Language Model (LLM) to propose dimensional models and present the results through an interactive web application.

The project is designed to support analytics engineering workflows by bridging the gap between business requirements and data warehouse design.

## Features

- **AI-Powered Data Modeling:** Analyze user-provided database schemas and business requirements using the Gemini API.
- **Fact Table Identification:** Propose fact tables, their grain, measures, and foreign keys.
- **Dimension Table Design:** Identify descriptive attributes, primary keys, surrogate keys, and potential Slowly Changing Dimension (SCD) strategies.
- **Relationship Mapping:** Display proposed relationships between fact and dimension tables.
- **Star Schema Visualization:** Generate a graphical representation of the proposed dimensional model using Graphviz.
- **dbt SQL Generation:** Generate and preview SQL models for fact and dimension tables.
- **Structured Output Validation:** Use Pydantic to validate AI-generated responses against defined data models.
- **Interactive Interface:** Explore model details through a Streamlit application.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application logic and backend processing |
| Streamlit | Interactive web interface |
| Google Gemini API | AI-powered data model generation |
| Pydantic | Structured response validation |
| Graphviz | Star schema visualization |
| SQL | Data warehouse model definitions |
| dbt | Analytics engineering model generation workflow |
| python-dotenv | Environment variable management |

## Architecture

```text
User Input
   |
   v
Database Schema + Business Requirements
   |
   v
Streamlit Application
   |
   v
Google Gemini API
   |
   v
Structured AI Response
   |
   v
Pydantic Validation
   |
   +----------------------+
   |          |           |
   v          v           v
Fact &     Dimension   Relationships
Measures   Tables      & Grain
   |          |           |
   +----------+-----------+
              |
              v
      Star Schema Diagram
          (Graphviz)
              |
              v
       dbt SQL Generation
              |
              v
       Model Preview in UI
```

## Project Structure

```text
LLM Data Model/
├── app.py
├── config.py
├── requirements.txt
├── .env                  # Local API key; not committed
├── .gitignore
└── src/
    ├── __init__.py
    ├── llm.py
    ├── prompts.py
    ├── models.py
    ├── render.py
    ├── star_schema.py
    └── dbt_generator.py
```

## Getting Started

### Prerequisites

- Python installed on your system
- Git
- A Google Gemini API key
- Visual Studio Code or another Python editor

### 1. Clone the repository

Replace the placeholder with your GitHub repository URL.

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

### 2. Create a virtual environment

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks environment activation, you can run the virtual environment's Python directly or use Command Prompt activation instead.

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure your Gemini API key

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

Replace the placeholder with your own API key. Never upload this file or expose your API key in screenshots, logs, or public repositories.

### 5. Run the application

```bash
streamlit run app.py
```

Open the local URL shown in the terminal, typically:

```text
http://localhost:8501
```

## Example Use Case

### Input schema

A retail business provides the following source tables:

- `customers`: customer information and segmentation
- `products`: product names, categories, brands, and prices
- `stores`: store locations and regions
- `orders`: order dates, customers, stores, and payment details
- `order_items`: products sold, quantities, discounts, sales, and costs

### Business requirement

Build a sales data warehouse that supports:

- Total revenue and profit analysis
- Monthly sales trends
- Sales by product category and store
- Top customers by revenue
- Average order value
- Quantity sold and discount analysis

### Expected output

The application can propose a dimensional model such as:

| Model | Purpose |
|---|---|
| `fct_sales` | Sales measures, quantities, discounts, and costs |
| `dim_customer` | Customer attributes and segmentation |
| `dim_product` | Product, category, and brand details |
| `dim_store` | Store location and regional attributes |
| `dim_date` | Calendar-based reporting attributes |

The suggested fact table grain is one row per order item. Actual output depends on the supplied schema, business requirements, and AI response.

## Design Considerations

- **Grain:** Define what one row in each fact table represents before selecting measures.
- **Keys:** Validate primary keys, surrogate keys, and foreign key relationships against the source data.
- **Measures:** Confirm the definitions of revenue, cost, profit, and discounts with business stakeholders.
- **AI validation:** Treat generated designs and SQL as proposals that require review.
- **dbt readiness:** Review generated SQL, source references, data types, and model dependencies before executing it in a dbt project.
