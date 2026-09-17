import streamlit as st

st.set_page_config(
    page_title="TOHO Report", page_icon="📋", layout="centered"
)

st.title("📋 TOHO Report")
st.write("Fill out the details below please.")

# Form inputs
with st.form("job_report_form"):
  address = st.text_input("Job Address / Location")

  job_types = st.multiselect(
      "Type of Job (Select all that apply)",
      [
          "Flagging",
          "Lane Closure",
          "Road closure",
          "One way two way closure",
          "Need arrow board",
      ],
  )

  crew_desc = st.text_area(
      "Crew Description",
      placeholder="e.g. 1 crew 3 ppl",
  )

  supervisor = st.selectbox(
      "Choose supervisor for the location",
      [
                "Tyler Wilson",
                "Scott Hummer",
                "Robert Melendez",
                "Francisco Ortega",
                "Fernando Fontanez",
                "Chase Lanier",
                "James Hummer"
            ],
  )

  equipment = st.text_area(
      "Additional Equipment Used",
      placeholder="e.g., Arrow Board, Cones...",
  )

  submitted = st.form_submit_button("Submit Report")

  if submitted:
    if address and crew_desc and supervisor and job_types and equipment:
      st.success("Report submitted successfully!")

      # Format the final output to copy or send
      report_summary = f"""
*TOHO REPORT*
*Address:* {address}
*Supervisor:* {supervisor}   
*Job Type:* {job_types}
*Crew:* {crew_desc}
*Equipment:* {equipment}
            """
      st.markdown("### Copy Your Report:")
      st.code(report_summary, language="markdown")
    else:
      st.error("Please fill in all fields.")