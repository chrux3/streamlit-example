# streamlit_app.py

import streamlit as st
import pandas as pd
from google.oauth2 import service_account
from gsheetsdb import connect

# Create a connection object.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
    ],
)

# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
## @st.cache(ttl=600)
## def run_query(query):
##     rows = conn.execute(query, headers=1)
##     return rows
## 
## sheet_url = st.secrets["private_gsheets_url"]
## rows = run_query(f'SELECT * FROM "{sheet_url}"')
conn = connect(credentials=credentials)

def run_query():
    gsheet_url = st.secrets["private_gsheets_url"]
    rows = conn.execute(f'SELECT * FROM "{gsheet_url}"')
    return rows

st.title("Connect to Google Sheets")

rows = run_query()
df_gsheet = pd.DataFrame(rows)
st.write(df_gsheet)

# Print results.
#for row in rows:
#    st.write(row)
