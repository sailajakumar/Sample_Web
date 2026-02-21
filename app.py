#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import dash
from dash import dcc, html, Input, Output
import pandas as pd
import os

# Sample dataset
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [100, 150, 200, 180, 220],
    "Profit": [20, 40, 60, 50, 70]
}

df = pd.DataFrame(data)

app = dash.Dash(__name__)
server=app.server

app.layout = html.Div([
    html.H2("Online Sales & Profit App"),

    html.Label("Select Month"),
    dcc.Dropdown(
        id="month_dropdown",
        options=[{"label": m, "value": m} for m in df["Month"]],
        value="Jan",
        clearable=False
    ),

    html.Label("Select Data Type"),
    dcc.Dropdown(
        id="type_dropdown",
        options=[
            {"label": "Sales", "value": "Sales"},
            {"label": "Profit", "value": "Profit"}
        ],
        value="Sales",
        clearable=False
    ),

    html.H3(id="output_text")
])

@app.callback(
    Output("output_text", "children"),
    Input("month_dropdown", "value"),
    Input("type_dropdown", "value")
)
def fetch_value(selected_month, selected_type):
    value = df[df["Month"] == selected_month][selected_type].values[0]
    return f"{selected_type} for {selected_month} is: {value}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)


# In[ ]:




