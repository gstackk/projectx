
"""
Natural Language to SQL Engine

Converts business questions
into BigQuery SQL queries.
"""

# -------------------------
# IMPORTS
# -------------------------

from groq import Groq
from google.cloud import bigquery
from dotenv import load_dotenv
import os

# -------------------------
# CONFIGURATION
# -------------------------

load_dotenv()

groq_client = Groq(
    api_key=os.getenv("YOUR_API_KEY")
)

bq_client = bigquery.Client()

# -------------------------
# SCHEMA DEFINITION
# -------------------------

SCHEMA = """
Table:
your_dataset.your_table

Columns:
column_1
column_2
column_3
column_4
"""

# -------------------------
# SYSTEM PROMPT
# -------------------------

SYSTEM_PROMPT = f"""
You are a BigQuery SQL expert.

Return ONLY valid BigQuery SQL.

Rules:
- Return SQL only
- No explanations
- No markdown
- No code fences
- SELECT statements only
- Use only approved tables

Schema:

{SCHEMA}
"""

# -------------------------
# SQL GENERATION
# -------------------------

def generate_sql(question):

    response = groq_client.chat.completions.create(
        model="your_model_name",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    sql = response.choices[0].message.content.strip()

    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")
    sql = sql.strip()

    if "SELECT" in sql.upper():
        sql = sql[sql.upper().find("SELECT"):]

    return sql

# -------------------------
# SQL VALIDATION
# -------------------------

def validate_sql(sql):

    forbidden_keywords = [
        "INSERT",
        "UPDATE",
        "DELETE",
        "DROP",
        "ALTER",
        "CREATE",
        "TRUNCATE",
        "MERGE"
    ]

    sql_upper = sql.upper()

    for keyword in forbidden_keywords:

        if keyword in sql_upper:
            raise ValueError(
                f"Blocked keyword detected: {keyword}"
            )

    if not sql_upper.lstrip().startswith("SELECT"):

        raise ValueError(
            "Only SELECT statements are allowed."
        )

    allowed_tables = [
        "your_dataset.your_table"
    ]

    if not any(
        table.lower() in sql.lower()
        for table in allowed_tables
    ):
        raise ValueError(
            "Query references an unauthorized table."
        )

# -------------------------
# QUERY EXECUTION
# -------------------------

def execute_query(sql):

    query_job = bq_client.query(sql)

    return query_job.to_dataframe()

# -------------------------
# MAIN PROGRAM
# -------------------------

if __name__ == "__main__":

    question = input(
        "Ask a business question: "
    )

    sql = generate_sql(question)

    validate_sql(sql)

    print("\nGenerated SQL:\n")
    print(sql)

    results = execute_query(sql)

    print("\nResults:\n")
    print(results)
``
