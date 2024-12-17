import plotly.express as px

def plot_battery_impedance(dataframe):
    fig = px.line(
        dataframe, x="Cycle", y="Battery_Impedance", color="Battery_ID",
        title="Battery Impedance vs Aging (Charge/Discharge Cycles)",
        labels={"Cycle": "Cycle Number", "Battery_Impedance": "Battery Impedance (Ohms)"}
    )
    return fig

def plot_re(dataframe):
    fig = px.line(
        dataframe, x="Cycle", y="Re", color="Battery_ID",
        title="Electrolyte Resistance (Re) vs Aging (Charge/Discharge Cycles)",
        labels={"Cycle": "Cycle Number", "Re": "Re (Ohms)"}
    )
    return fig

def plot_rct(dataframe):
    fig = px.line(
        dataframe, x="Cycle", y="Rct", color="Battery_ID",
        title="Charge Transfer Resistance (Rct) vs Aging (Charge/Discharge Cycles)",
        labels={"Cycle": "Cycle Number", "Rct": "Rct (Ohms)"}
    )
    return fig
