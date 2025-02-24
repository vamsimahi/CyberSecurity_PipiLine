import streamlit as st
import time
from task_manager import TaskManager
from scope_validator import ScopeValidator

# Initialize Streamlit app
st.set_page_config(page_title="Cybersecurity Scanner", layout="wide")

st.title("🔍 Cybersecurity Agentic Pipeline")
st.sidebar.header("Scan Settings")

# Define allowed scope
ALLOWED_DOMAINS = ["example.com","sample.com"]
ALLOWED_IPS = ["192.168.1."]

# User input for target
target = st.sidebar.text_input("Enter Target (Domain/IP)", "example.com")

if st.sidebar.button("Start Scan"):
    st.sidebar.success(f"Scanning: {target}")

    # Scope Validation
    scope_validator = ScopeValidator(ALLOWED_DOMAINS, ALLOWED_IPS)
    if not scope_validator.is_allowed(target):
        st.error("❌ Target is out of scope! Exiting...")
    else:
        # Initialize Task Manager
        task_manager = TaskManager()

        # Define initial tasks
        task_manager.add_task({"action": "nmap", "target": target})
        task_manager.add_task({"action": "gobuster", "target": f"http://{target}"})

        st.session_state["tasks"] = task_manager.task_queue
        st.session_state["log"] = []

# Display Active Tasks
st.subheader("📌 Task Execution")
if "tasks" in st.session_state:
    for task in st.session_state["tasks"]:
        st.write(f"🛠️ Executing: `{task['action']}` on `{task['target']}`...")

# Start Execution and Stream Logs
if "tasks" in st.session_state and st.sidebar.button("Run Tasks"):
    task_manager = TaskManager()

    log_output = []
    for task in st.session_state["tasks"]:
        with st.spinner(f"Running `{task['action']}` on `{task['target']}`..."):
            if task["action"] == "nmap":
                output = task_manager.nmap_agent.scan(task["target"])
            elif task["action"] == "gobuster":
                output = task_manager.gobuster_agent.scan(task["target"])
            elif task["action"] == "ffuf":
                output = task_manager.ffuf_agent.scan(task["target"])
            else:
                output = "Unknown Task"
            
            log_output.append(f"✅ **{task['action']} Completed** for `{task['target']}`\n```\n{output}\n```")
            time.sleep(2)

    # Store logs
    st.session_state["log"] = log_output

# Show Logs in Real-Time
st.subheader("📜 Scan Logs")
if "log" in st.session_state:
    for log_entry in st.session_state["log"]:
        st.markdown(log_entry)

# Summary Section
st.subheader("📊 Final Report")
if "log" in st.session_state and len(st.session_state["log"]) > 0:
    st.success("✅ Scan Completed. Review logs for details.")
else:
    st.warning("No scans have been executed yet.")
