#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import matplotlib.colors as mcolors
import squarify
import networkx as nx
import plotly.express as px
import numpy as np

df=pd.read_csv(r"C:\Users\gouth\Desktop\Goutham\Stats\DataSet\heart.csv")
df.head()


# In[9]:


#DensityPlot
plt.figure(figsize = (4,3))
sns.kdeplot(
    data = df,
    x = 'age',
    hue = 'sex',
    shade = True,
    palette = 'coolwarm'
)
plt.title('Density plot of Age and Sex')
plt.xlabel('Age')
plt.ylabel('Density')
plt.show()


# In[10]:


#Bullet Graph
target_value = df[df['target'] == 1]['restecg'].mean()
min_value = df['restecg'].min()
max_value = df['restecg'].max()
fig, ax = plt.subplots(figsize=(10, 3))
ax.barh(0, 
        max_value - min_value, 
        left = min_value, 
        height = 0.5, 
        color = 'lightyellow'
       )
actual_value = df[df['target'] == 1]['restecg'].mean()
ax.barh(0, 
        actual_value - min_value, 
        left=min_value, 
        height = 0.5, 
        color = 'lavender'
       )
ax.axvline(x=target_value, 
           color = 'red', 
           linewidth = 2, 
           label = f'Target Age: {target_value:.2f}'
           )
ax.set_xlim([min_value, max_value])
ax.set_title('Bullet Graph: electrical activity of heart while resting vs Target (Heart Disease Patients)',
             fontsize=14)
ax.set_xlabel('restecg', fontsize=12)
ax.set_yticks([])
ax.legend()
plt.tight_layout()
plt.show()


# In[11]:


#Tree Map
tree_data = df.groupby(['age', 'cp']).size().reset_index(name='count')
tree_data['label'] = tree_data.astype(str).agg(' - '.join, 
                                               axis=1)
norm = mcolors.Normalize(vmin=tree_data['count'].min(), 
                         vmax=tree_data['count'].max())
colors = [plt.get_cmap("YlGnBu") (norm(c)) for c in tree_data['count']]
plt.figure (figsize=(12, 8))
squarify.plot(sizes=tree_data['count'], 
              label=tree_data['label'], 
              color=colors, 
              alpha=0.7
             )
plt.title("Tree Map for Heart Disease Dataset (age vs chest pain)")
plt.axis('off')
plt.show()


# In[12]:


#Path Diagram
G = nx.DiGraph()
G.add_node('Age')
G.add_node('Sex')
G.add_node('Cholesterol')
G.add_node('Blood Pressure')
G.add_node ('HeartRate')
G.add_node ('Target')
G.add_edges_from([('Age', 'Target'), 
                    ('Cholesterol', 'Target'), 
                    ('Sex', 'Target'), 
                    ('Blood Pressure', 'Target'), 
                    ('HeartRate', 'Target'), 
                    ('Age', 'Cholesterol'), 
                    ('Cholesterol', 'Blood Pressure'), 
                    ('HeartRate', 'Blood Pressure')]
                )
pos = nx.spring_layout(G)
plt.figure (figsize=(8, 6))
nx.draw(G, 
        pos, 
        with_labels = True, 
        node_size = 3000, 
        node_color = 'orange', 
        font_size = 12, 
        font_weight = 'bold',
        arrowsize = 20
       )
plt.title('Path Diagram for Heart Disease Prediction')
plt.show()


# In[13]:


#Network
nodes = ['Age', 'Sex', 'CP', 'trtbps', 'Chol', 'FBS', 'RestECG', 'Thalachh', 'Exng', 'OldPeak', 'Slp', 'CAA', 'Thall',
'Target']

edges = [('Age', 'trtbps'), ('Age', 'Chol'), ('Age', 'Thalach'), ('Sex', 'trtbps'), ('Sex', 'Chol'), ('Sex', 'Thalach'), ('СР!',
'trtbps'), ('CP', 'Chol'), ('CP', 'Thalach'), ('trtbps', 'Target'), ('Chol', 'Target'), ('Thalach', 'Target'), ('FBS',
'Target'),('Exng', 'Target'), ('OldPeak', 'Target'), ('Slp', 'Target'), ('CAA', 'Target'), ('Thall', 'Target')]

G = nx.DiGraph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)
pos = nx.spring_layout(G, seed=42)
edge_x = []
edge_y = []
for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, yl = pos[edge[1]]
    edge_x.append(x0)
    edge_y.append(y0)
    edge_x.append(x1)

node_x = [pos[node][0] for node in nodes]
node_y = [pos[node][1] for node in nodes]
fig = go.Figure()
fig.add_trace(go.Scatter(x=edge_x, 
                         y=edge_y, 
                         mode='lines', 
                         line=dict(width=1, color='black'), 
                         hoverinfo='none')
             )
fig.add_trace(go.Scatter(x=node_x, 
                         y=node_y, 
                         mode='markers+text', 
                         text=nodes, 
                         textposition='top center',
                         marker=dict(size=20, 
                                     color='skyblue', 
                                     line=dict(width=2, color='black')
                                    ),
                         hoverinfo='text')
             )
fig.update_layout( title="Network Diagramfor Heart Disease Dataset", 
                  showlegend=False, 
                  plot_bgcolor='white',
                  xaxis=dict(showgrid=False, zeroline=False), 
                  yaxis=dict(showgrid=False, zeroline=False), 
                  title_x=0.5, 
                  title_y=0.95
                 )
fig.show()


# In[2]:


correlation_matrix = df.corr()
plt.figure (figsize=(10, 8))
sns.heatmap(correlation_matrix, 
            annot = True, 
            cmap = 'rainbow', 
            fmt = '.2f', 
            linewidths = 0.5)
plt.title('Correlation Matrix for Heart Dataset')
plt.show()


# In[5]:


#Choropleth Map
countries = ["India", "USA", "UK", "Germany", "France"]
df["Country"] = np.random.choice(countries, size=len(df))
country_counts = df.groupby("Country")["target"].mean().reset_index() 
country_counts.columns = ["Country", "Heart_Disease_Rate"]
fig = px.choropleth(country_counts,
                    locations="Country",
                    locationmode="country names",
                    color="Heart_Disease_Rate",
                    color_continuous_scale="Reds",
                    title="Choropleth Map: HeartDisease Rate by Country")
fig.show()

