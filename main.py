import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.markdown("""
    <style>
    /* Main page styles */
    body {
        background-color: #f0f2f6;
        color: #333333;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #2e4053;
        text-align: center;
    }
    /* Sidebar styles */
    .css-1d391kg {
        background-color: #3e606f;
    }
    .css-qrbaxs a {
        color: white;
        font-size: 18px;
        padding: 10px 20px;
    }
    .css-qrbaxs a:hover {
        background-color: #558b6e;
        border-radius: 8px;
        text-decoration: none;
    }
    /* Visualizations' container styles */
    .stPlotlyChart {
        background-color: white;
        border-radius: 8px;
        padding: 20px;
        margin: 20px auto;
    }
    </style>
""", unsafe_allow_html=True)

data = pd.read_csv("employee_data.csv")

st.title("Employee Data Dashboard")

st.sidebar.title("Navigation")
pages = ["Age Distribution", "Gender Distribution", "Job Title Distribution", 
         "Workload Satisfaction", "Weekly Hours Worked", "Stress Levels", 
         "Overall Satisfaction", "Considering Leaving", "Correlation Heatmap",
         "Work-Life Balance", "Remote Work Days", "Promotion Status", "Achieved Goals"]
page_selection = st.sidebar.radio("Select a visualization:", pages)

if page_selection == "Age Distribution":
    st.subheader("Age Distribution of Employees")
    plt.figure(figsize=(10, 6))
    plt.hist(data['Age'], bins=10, color='skyblue', edgecolor='black')
    plt.xlabel('Age')
    plt.ylabel('Number of Employees')
    st.pyplot(plt)

elif page_selection == "Gender Distribution":
    st.subheader("Gender Distribution")
    gender_counts = data['Gender'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig)

elif page_selection == "Job Title Distribution":
    st.subheader("Distribution of Job Titles")
    job_title_counts = data['JobTitle'].value_counts()
    plt.figure(figsize=(10, 6))
    job_title_counts.plot(kind='bar', color='green')
    plt.xlabel('Job Title')
    plt.ylabel('Number of Employees')
    st.pyplot(plt)

elif page_selection == "Workload Satisfaction":
    st.subheader("Average Workload Satisfaction by Department")
    avg_workload_satisfaction = data.groupby('Department')['WorkloadSatisfaction'].mean()
    plt.figure(figsize=(10, 6))
    avg_workload_satisfaction.plot(kind='bar', color='purple')
    plt.xlabel('Department')
    plt.ylabel('Average Workload Satisfaction')
    st.pyplot(plt)

elif page_selection == "Weekly Hours Worked":
    st.subheader("Weekly Hours Worked by Department")
    avg_weekly_hours = data.groupby('Department')['WeeklyHoursWorked'].mean()
    plt.figure(figsize=(10, 6))
    avg_weekly_hours.plot(kind='bar', color='orange')
    plt.xlabel('Department')
    plt.ylabel('Average Weekly Hours Worked')
    st.pyplot(plt)

elif page_selection == "Stress Levels":
    st.subheader("Stress Levels by Department")
    avg_stress_levels = data.groupby('Department')['StressLevel'].mean()
    plt.figure(figsize=(10, 6))
    avg_stress_levels.plot(kind='bar', color='red')
    plt.xlabel('Department')
    plt.ylabel('Average Stress Level')
    st.pyplot(plt)

elif page_selection == "Overall Satisfaction":
    st.subheader("Overall Satisfaction by Promotion Status")
    avg_satisfaction_by_promotion = data.groupby('PromotionLast12Months')['OverallSatisfaction'].mean()
    plt.figure(figsize=(10, 6))
    avg_satisfaction_by_promotion.plot(kind='bar', color='blue')
    plt.xlabel('Promotion Last 12 Months')
    plt.ylabel('Average Overall Satisfaction')
    st.pyplot(plt)

elif page_selection == "Considering Leaving":
    st.subheader("Distribution of Employees Considering Leaving the Company")
    considering_leaving_counts = data['ConsideringLeaving'].value_counts()
    plt.figure(figsize=(10, 6))
    considering_leaving_counts.plot(kind='bar', color='gray')
    plt.xlabel('Considering Leaving')
    plt.ylabel('Number of Employees')
    st.pyplot(plt)

elif page_selection == "Correlation Heatmap":
    st.subheader("Correlation Heatmap")
    numeric_data = data.select_dtypes(include=['float64', 'int64'])
    plt.figure(figsize=(12, 8))
    corr_matrix = numeric_data.corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    st.pyplot(plt)

elif page_selection == "Work-Life Balance":
    st.subheader("Work-Life Balance by Job Title")
    avg_worklife_balance = data.groupby('JobTitle')['WorkLifeBalance'].mean()
    plt.figure(figsize=(10, 6))
    avg_worklife_balance.plot(kind='bar', color='cyan')
    plt.xlabel('Job Title')
    plt.ylabel('Average Work-Life Balance')
    st.pyplot(plt)

elif page_selection == "Remote Work Days":
    st.subheader("Distribution of Remote Work Days")
    plt.figure(figsize=(10, 6))
    remote_work_days = data['RemoteWorkDays'].value_counts()
    remote_work_days.plot(kind='bar', color='pink')
    plt.xlabel('Remote Work Days')
    plt.ylabel('Number of Employees')
    st.pyplot(plt)

elif page_selection == "Promotion Status":
    st.subheader("Promotion Status by Department")
    promotion_by_dept = data.groupby('Department')['PromotionLast12Months'].value_counts(normalize=True).unstack()
    plt.figure(figsize=(10, 6))
    promotion_by_dept.plot(kind='bar', stacked=True)
    plt.xlabel('Department')
    plt.ylabel('Promotion Status Proportion')
    st.pyplot(plt)

elif page_selection == "Achieved Goals":
    st.subheader("Achieved Goals by Department")
    avg_goals_by_department = data.groupby('Department')['AchievedGoals'].mean()
    plt.figure(figsize=(10, 6))
    avg_goals_by_department.plot(kind='bar', color='yellow')
    plt.xlabel('Department')
    plt.ylabel('Average Achieved Goals')
    st.pyplot(plt)
