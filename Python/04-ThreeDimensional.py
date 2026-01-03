#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import numpy as np
import plotly.express as px

df=pd.read_csv(r"C:\Users\gouth\Desktop\Goutham\Stats\DataSet\heart.csv")
df.head()


# In[4]:


#Box-WiskerPlot
plt.figure(figsize = (4,3))
sns.boxplot(x='target', 
            y='chol',
            hue='target',
            data = df, 
            palette = 'Set2'
           )
plt.title("Box-WiskerPlot: Cholesterol vs Heart Disease")
plt.xlabel("Heart Disease Output (0 = No, 1 = Yes)")
plt.ylabel("Cholesterol level")
plt.show()


# In[5]:


#Waterfall Chart
feature_contributions = df.drop(columns = 'target').mean()
initial_value = df['target'].mean()
contributions = feature_contributions - initial_value
fig = go.Figure(go.Waterfall(
    x = contributions.index,
    y = contributions.values,
    measure = ["relative"]*len(contributions),
    text = contributions.values,
    textposition = "outside"
))
fig.add_trace(go.Waterfall(
    x = ["Final Target"],
    y = [df['target'].mean() - initial_value],
    measure = ["total"],
    text = [f"Final Target: {df['target'].mean()}"],
    textposition="outside"
))
fig.update_layout(
    title = "Waterfall Chart of Feature Contributions to Heart Disease Output",
    xaxis_title = "Features",
    yaxis_title = "Contribution",
    showlegend = False
)
fig.show()


# In[6]:


#Area Chart
df[['chol', 'thalach']].cumsum().plot.area(alpha=0.5, 
                                           figsize=(10, 6)
                                          )
plt.title('Cumulative Area Chart of Cholesterol and Maximum heart rate')
plt.xlabel('Index')
plt.ylabel('Cumulative Sum')
plt.legend(["Cholesterol", "Maximum Heart Rate"])
plt.show()


# In[7]:


#Scatter Plot
plt.figure(figsize = (6,5))
sns.scatterplot(x = 'age',
                y = 'thalach',
                hue = 'target',
                data = df,
                style = 'target',
                palette = 'cool'
               )
plt.title('Scatter Plot: Age vs Maximum Heart Rate')
plt.xlabel('Age')
plt.ylabel('Maximum Heart Rate')
plt.show()


# In[7]:


#Gantt Chart
df_gantt = df.copy()
df_gantt["Patient_ID"] = df_gantt.index.astype(str)
df_gantt["Start_Day"] = pd.to_datetime("2025-01-01") + pd.to_timedelta(df_gantt.index, unit="D")
df_gantt["End_Day"] = df_gantt["Start_Day"] + pd.to_timedelta(np.random.randint(2, 7, size=len(df)), unit="D")
df_gantt["target_label"] = df_gantt["target"].map({0: "No Heart Disease", 1: "Heart Disease"})
fig = px.timeline(
    df_gantt.head(30),
    x_start="Start_Day",
    x_end="End_Day",
    y="Patient_ID",
    color="target_label",
    title="Gantt Chart: Patient Observation Period",
    labels={"target_label": "Condition"}
)
fig.update_yaxes(autorange="reversed")
fig.update_layout(xaxis_title="Observation Period", yaxis_title="Patient ID")
fig.show()


# In[8]:


#Heat map
plt.figure(figsize=(12,8))
corr = df.corr()
sns.heatmap(corr,
            annot=True,
            cmap="coolwarm",
            fmt=".2f")
plt.title("Heat Map of Heart Dataset (Correlation)")
plt.show()

