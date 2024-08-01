from urllib import response
import streamlit as st
import requests
import pandas as pd

st.set_page_config(
    page_title="Punch Clock App",
    page_icon=":stopwatch:",
    layout="centered", 
    initial_sidebar_state="auto",
    menu_items={
        "About": "A punch clock webapp that performs CRUD operation in a Postgres database using SQLAlchemy, FastAPI and Pydantic,\
              hosted on Streamlit and containerized in Docker.",
        "Get Help": "https://github.com/RStremel/punch-clock-crud"
    })

# st.image("frontend\logo.png", width=200)

st.title("Punch Clock App :stopwatch:", 
         help="Attention, workers: don't forget to punch in and out of the clock as you begin and \
            end your shifts. We are watching you!")

st.markdown("A punch clock webapp that performs CRUD operation in a Postgres database using \
            SQLAlchemy, FastAPI and Pydantic, hosted on Streamlit and containerized in Docker.")
            
st.markdown("For more information, check out the [GitHub repository](https://github.com/RStremel/punch-clock-crud).")

with st.expander("Add a new check-in and check-out record"):
    with st.form("new_record"):
        employee_name = st.text_input("Employee Name")
        employee_id = st.text_input("Employee ID")
        workplace = st.selectbox(
            "Where did you go to work today?",
            ("Main office", "Coworking space", "Remote"),
            index=None,
            placeholder="Select your workplace..."
        )
        day_worked = st.date_input("Select the day worked")

        submit_button = st.form_submit_button("Add record")

        # if submit_button: #if submit button is clicked
        #     response = requests.post(
        #         "http://backend:8000/records/",
        #         json={
        #             "employee_name": employee_name,
        #             "employee_id": employee_id,
        #             "workplace": workplace,
        #             "day_worked": day_worked
        #         }
        #     )
            # show_response_message(response)

with st.expander("Check records"): #all records and specific record id will be in the same expander
    if st.button("Check all records"):
        st.text("It's gonna show all records DELETE THIS!!!")
        # response = requests.get("http://backend:8000/records/")
        # if response.status == 200:
        #     records = response.json()
        #     df = pd.DataFrame(records)

        #     df = df[[ # is this really necessary?
        #         "id",
        #         "employee_name",
        #         "employee_id",
        #         "workplace",
        #         "day_worked",
        #         "created_at"]]
            
        #     st.write(df.to_html(index=False), unsafe_allow_html=True)
        # else:
        #     show_response_message(response)

    record_id = st.number_input("Select the record ID", min_value=1, placeholder=1, step=1)
    if st.button("Check record ID"):
        st.text(f"It's gonna show the record for id {record_id} DELETE THIS!!!")
        # response = requests.get(f"http://backend:8000/records/{record_id}")
        # if response.status == 200:
        #     records = response.json()
        #     df = pd.DataFrame([records])

        #     df = df[[ # is this really necessary?
        #         "id",
        #         "employee_name",
        #         "employee_id",
        #         "workplace",
        #         "day_worked",
        #         "created_at"]]
            
        #     st.write(df.to_html(index=False), unsafe_allow_html=True)
        # else:
        #     show_response_message(response)

with st.expander("Delete a record"):
    record_id = st.number_input("Select the record ID to be deleted", min_value=1, placeholder=1, step=1)
    if st.button("Delete record ID"):
        st.text(f"It's gonna DELETE this record id {record_id} DELETE THIS!!!")
        # response = requests.delete(f"http://backend:8000/records/{record_id}")
        # show_response_message(response)

with st.expander("Update record"):
    with st.form("update_record"):
        update_id = st.number_input("Select the record ID to be updated", min_value=1, placeholder=1, step=1)
        new_employee_name = st.text_input("New Employee Name")
        new_employee_id = st.text_input("New Employee ID")
        new_workplace = st.selectbox(
            "Where did you go to work today?",
            ("Main office", "Coworking space", "Remote"),
            index=None,
            placeholder="Select your workplace..."
        )
        new_day_worked = st.date_input("Select the day worked")
        
        submit_update_button = st.form_submit_button("Update record")

        # if submit_update_button:
        #     updated_data = {}
        #     if new_employee_name:
        #         updated_data["employee_name"] = new_employee_name
        #     if new_employee_id:
        #         updated_data["employee_id"] = new_employee_id
        #     if new_workplace:
        #         updated_data["workplace"] = new_workplace
        #     if new_day_worked:
        #         updated_data["day_worked"] = new_day_worked

        #     if updated_data:
        #         response = requests.put(f"http://backend:8000/records/{updated_data}", json=updated_data)
        #         show_response_message(response)
        #     else:
        #         st.error("No record data to be updated")
            

