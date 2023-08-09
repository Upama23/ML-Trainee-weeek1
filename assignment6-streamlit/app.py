import streamlit as st
import pandas as pd

def app():
    st.sidebar.title("Navigation")
    pages = ["Employee Data Entry", "Department Data Entry", "Visualize Data"]
    choice = st.sidebar.radio("Select Page", pages)

    if "employee_data" not in st.session_state:
        st.session_state.employee_data = pd.DataFrame(columns=['Empno', 'Ename', 'Job', 'Deptno'])
    if "department_data" not in st.session_state:
        st.session_state.department_data = pd.DataFrame(columns=['Deptno', 'Dname', 'Loc'])

    if choice == "Employee Data Entry":
        employee_data_entry()
    elif choice == "Department Data Entry":
        department_data_entry()
    elif choice == "Visualize Data":
        visualize_data()


def employee_data_entry():
    st.title('Employee Data Entry')
    empno = st.text_input('Employee Number (Empno)')
    ename = st.text_input('Employee Name (Ename)')
    job = st.text_input('Job')
    deptno = st.text_input('Department Number (Deptno)')

    if st.button('Add Employee'):
        if empno and ename and job and deptno:
            st.session_state.employee_data.loc[len(st.session_state.employee_data)] = [empno, ename, job, deptno]
            st.success('Employee added successfully!')
        else:
            st.error('All fields are required for employee data entry.')

def department_data_entry():
    st.title('Department Data Entry')
    deptno = st.text_input('Department Number (Deptno)')
    dname = st.text_input('Department Name (Dname)')
    loc = st.text_input('Location (Loc)')

    if st.button('Add Department'):
        if deptno and dname and loc:
            st.session_state.department_data.loc[len(st.session_state.department_data)] = [deptno, dname, loc]
            st.success('Department added successfully!')
        else:
            st.error('All fields are required for department data entry.')

def visualize_data():
    st.title('Visualize Data')
    if not st.session_state.employee_data.empty and not st.session_state.department_data.empty:
        merged_data = pd.merge(st.session_state.employee_data[['Empno', 'Ename', 'Deptno']],
                               st.session_state.department_data[['Deptno', 'Dname']],
                               on='Deptno', how='inner')
        st.dataframe(merged_data)
    else:
        st.warning('No data available to visualize. Please add employee and department data first.')


if __name__ == "__main__":
    app()
