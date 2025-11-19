import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="System Monitor Dashboard", layout="wide")

st.title("🖥️ System Monitoring Dashboard")
st.markdown("This dashboard reads `log.csv` and displays system metrics.")

CSV_PATH = "log.csv"

if not os.path.exists(CSV_PATH):
    st.warning("`log.csv` not found in the app directory.")
    st.markdown("You can re-run `main.py` from Week 5 to generate log entries, or create a small sample file below.")
    if st.button("Create sample `log.csv`"):
        sample = (
            "Timestamp,CPU,Memory,Disk,Ping_Status,Ping_ms\n"
            "2025-10-01 12:00:00,15.2,40.1,58.9,UP,22.5\n"
            "2025-10-01 12:05:00,20.1,42.3,60.2,UP,25.1\n"
            "2025-10-01 12:10:00,18.9,41.0,59.8,UP,23.0\n"
            "2025-10-01 12:15:00,22.4,43.5,61.0,UP,26.7\n"
            "2025-10-01 12:20:00,19.7,40.8,60.5,UP,24.3\n"
        )
        with open(CSV_PATH, "w", encoding="utf-8") as f:
            f.write(sample)
        st.success("Sample `log.csv` created.")
        st.experimental_rerun()
else:
    try:
        df = pd.read_csv(CSV_PATH, parse_dates=["Timestamp"]) if os.path.getsize(CSV_PATH) > 0 else pd.DataFrame()

        if df.empty:
            st.warning("`log.csv` is empty.")
        else:
            # Ensure numeric types for plotting
            for col in ["CPU", "Memory", "Disk"]:
                if col in df.columns:
                    df[col] = pd.to_numeric(df[col], errors="coerce")

            st.subheader("📊 Latest Records")
            st.dataframe(df.tail(5), use_container_width=True)

            st.subheader("📈 CPU / Memory / Disk Usage Over Time")
            if "Timestamp" in df.columns and any(c in df.columns for c in ["CPU", "Memory", "Disk"]):
                chart_df = df.set_index("Timestamp")[ [c for c in ["CPU","Memory","Disk"] if c in df.columns] ].dropna()
                if chart_df.empty:
                    st.warning("No numeric CPU/Memory/Disk data available to plot.")
                else:
                    st.line_chart(chart_df)
            else:
                st.warning("Required columns missing: ensure `Timestamp`, `CPU`, `Memory`, and `Disk` exist in `log.csv`.")
    except Exception as e:
        st.error(f"Failed to read `log.csv`: {e}")
