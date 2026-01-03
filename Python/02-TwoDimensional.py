#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv(r"C:\Users\gouth\Desktop\Goutham\Stats\DataSet\heart.csv")
df.head()


# In[5]:


#Histogram
plt.figure(figsize = (4 ,3))
df['age'].plot(
    kind = 'hist',
    bins = 20,
    color = "purple",
    edgecolor = "yellow"
)
plt.title("Histogram: Age distribution")
plt.xlabel("Age")
plt.ylabel("Frequencey")
plt.show()


# In[6]:


#Line Plot
plt.figure(figsize = (4,3))
df.groupby('age')['chol'].mean().plot(
    kind = 'line',
    color = 'orange',
    marker = 'o'
)
plt.title('Line Plot: Age vs Cholesterol Levels')
plt.xlabel('Age')
plt.ylabel('Average Cholesterol')
plt.grid(True)
plt.show()


# In[7]:


#Frequency Curve
plt.figure (figsize=(4,3))
sns.kdeplot(df['oldpeak'], 
            color='grey', 
            alpha=0.6)
plt.title ('Oldpeak (ST Depression) Distribution (Frequency Curve)')
plt.xlabel('Oldpeak (ST Depression)')
plt.ylabel('Density')
plt.show()


# In[9]:


#Frequencu Polygon
plt.figure (figsize=(8,6))

# //Plot the histogram
sns.histplot(data=df, 
             x='age', 
             hue='fbs', 
             multiple='stack', 
             kde=False, 
             palette="coolwarm", 
             bins=20, stat="density"
            )

# //Overlay the frequency polygon (KDE withfill=False)
sns.kdeplot(data=df, 
            x='age', 
            hue='fbs', 
            common_norm=False, 
            fill=False, 
            linewidth=2
           )

plt.title('Fasting Blood Sugar vs Age (Frequency Polygon)')
plt.xlabel('Age')
plt.ylabel('Density')
plt.show()


# In[10]:


#Ogive Curve
age_data = df['age']
sorted_age = sorted(age_data)
cumulative_freq = [i for i in range(len(sorted_age))]
plt.figure (figsize=(4, 3))
plt.plot(sorted_age, 
         cumulative_freq, 
         marker='o', 
         color='b', 
         linestyle='-', 
         label='Ogive'
        )
plt.title ('Ogive Curve for Age')
plt.xlabel('Age')
plt.ylabel('Cumulative Frequency')
plt.grid(True)
plt.legend()
plt.show()


# In[11]:


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

