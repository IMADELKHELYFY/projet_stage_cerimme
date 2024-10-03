import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Charger le fichier CSV
data = pd.read_csv('employee_data.csv')

# Afficher les noms de colonnes pour le diagnostic
st.write("Available columns:", data.columns)

# Configurer le style des graphiques
sns.set(style='whitegrid')

# Titre de l'application
st.title('Employee Performance and Satisfaction Dashboard')

# Afficher les données
if st.checkbox('Show raw data'):
    st.subheader('Raw Data')
    st.write(data)

# Histogramme de la Satisfaction au Travail
if 'WorkloadSatisfaction' in data.columns:
    st.subheader('Distribution of Workload Satisfaction')
    plt.figure(figsize=(10, 5))
    plt.hist(data['WorkloadSatisfaction'], bins=5, alpha=0.7, color='blue')
    plt.title('Distribution of Workload Satisfaction')
    plt.xlabel('Satisfaction Level')
    plt.ylabel('Frequency')
    st.pyplot(plt)
else:
    st.warning("Column 'WorkloadSatisfaction' not found in the data.")

# Graphique à Barres du Niveau de Stress
if 'StressLevel' in data.columns:
    st.subheader('Stress Level Distribution')
    stress_counts = data['StressLevel'].value_counts()
    st.bar_chart(stress_counts)
else:
    st.warning("Column 'StressLevel' not found in the data.")

# Graphique à Barres de la Répartition des Titres de Poste
if 'JobTitle' in data.columns:
    st.subheader('Job Title Distribution')
    job_counts = data['JobTitle'].value_counts()
    st.bar_chart(job_counts)
else:
    st.warning("Column 'JobTitle' not found in the data.")

# Autres visualisations peuvent être ajoutées ici en fonction des autres colonnes...
if 'OverallSatisfaction' in data.columns:
    st.subheader('Overall Satisfaction')
    plt.figure(figsize=(10, 5))
    plt.hist(data['OverallSatisfaction'], bins=5, alpha=0.7, color='green')
    plt.title('Overall Satisfaction Distribution')
    plt.xlabel('Satisfaction Level')
    plt.ylabel('Frequency')
    st.pyplot(plt)
else:
    st.warning("Column 'OverallSatisfaction' not found in the data.")
