# Week 6 – Initial Dashboard UI (Streamlit)

## 🎯 Objective

This week, you'll begin building a simple **web-based dashboard** for your data center monitor using **Streamlit**.  
You will read system metrics from `log.csv` and display them in a dashboard format with tables and charts.

---

## 🧠 Reminder: Where does `log.csv` come from?

Your `log.csv` file should already exist from **Week 4 or Week 5**.  
It contains fields like:  
`Timestamp, CPU, Memory, Disk, Ping_Status, Ping_ms`

If you **don’t have one**, you can generate it by re-running your previous logger script (e.g., from Week 5):

``bash
python main.py

This will log 5 entries with system info and create log.csv.

Alternatively, you can use the example below.

⸻

🧪 Sample log.csv (Optional)

If needed, copy the following and save it as log.csv in the same folder:

Timestamp,CPU,Memory,Disk,Ping_Status,Ping_ms

2025-10-01 12:00:00,15.2,40.1,58.9,UP,22.5

2025-10-01 12:00:10,18.3,42.0,59.1,UP,20.8

2025-10-01 12:00:20,19.5,43.2,59.4,UP,19.7

2025-10-01 12:00:30,22.0,44.5,59.6,DOWN,-1

2025-10-01 12:00:40,21.1,44.2,59.3,UP,21.2


⸻

✅ Tasks
	1.	Create a new file app.py using Streamlit.
	2.	Load log.csv and:
	•	Show the latest 5 entries as a table
	•	Plot line charts for CPU, Memory, Disk
	•	Display a warning if file is missing
	3.	Run the dashboard with:

streamlit run app.py

To quickly view the last 5 entries from `log.csv` in your terminal, run:

``bash
python read_log.py
``

This script loads `log.csv` with pandas and prints the latest 5 rows in a table format.


⸻

✅ Submission Checklist
	•	app.py shows table + charts from log.csv
	•	requirements.txt includes streamlit and pandas
	•	Screenshot of your dashboard
	•	All files committed and pushed to GitHub

⸻

💡 Bonus (Optional)
	•	Add sidebar filters or search
	•	Highlight Ping_Status with colors
