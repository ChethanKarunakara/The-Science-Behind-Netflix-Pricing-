#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import Image

gif_url = 'https://images.squarespace-cdn.com/content/v1/520b6dcee4b0734e32e29746/1553093622986-F8DCADFCEQGUZMAWVVTX/Netflix_anim.gif?format=2500w'

# Displaying the GIF in the notebook
Image(url=gif_url)


# # Introduction :
# 
# 
# <div style="color:white;
#            display:fill;
#            border-radius:5px;
#            background-color:#DE0C0C;
#            font-size:110%;
#            font-family:Verdana;
#            letter-spacing:0.5px">
# 
# <p style="padding: 10px;
#               color:white;">
#     Netflix, Inc. is an American innovation and media administrations supplier and production company headquartered in California. It was established in 1997 by Reed Hastings and Marc Randolph in California. The company's center commerce is a paid subscription-based video streaming service.
# 
# </p>
# </div>
# 
# <font color = "green">
#     
# Content:
# 1. [Import Libraries](#1)
# 1. [Load and Check Data](#2)
# 1. [Variable Description](#3)
#     * [Univarite Variable Analysis](#4)
#         * [Categorical Variable Analysis](#5)
#         * [Numerical Variable Analysis](#6)
# 1. [Missing Value](#7)
# 1. [Unique Values](#8)
# 1. [Data Visualization](#9)
#     * [Plotly](#10)
#     * [Seaborn](#11)
#     * [Linear Regression](#12)
# 1. [Conclusion](#13)

# <a id = "1"></a><br>
# # Import Libraries 📜 

# In[2]:


import numpy as np 
import pandas as pd 
import os
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


# <a id = "2"></a><br>
# # Loading and Checking Data ✔️

# In[3]:


df = pd.read_csv("/Users/chethankarunakara/Desktop/Netflix_Price_Different_Countries.csv")


# In[4]:


df.columns


# In[5]:


df.head(10)


# In[6]:


df.tail(5)


# In[7]:


df.describe()


# <a id = "3"></a><br>
# # Variable Description 🚀
# 
# * __Country:__ Some countries where Netflix is used.
# * __Total Library Size:__ Total number of movies and TV series aired in the country.
# * __No. of TV Shows:__ Total number of TV series broadcast in the country.
# * __No. of Movies:__ Total number of movies released in the country.
# * __Cost Per Month - Basic:__ The monthly price of the __"basic package".__
# * __Cost Per Month - Standard:__ The monthly price of the __"standard package".__
# * __Cost Per Month - Premium:__ The monthly price of the __"premium package".__

# In[8]:


df.info() # Checking if there are any Null Values


# <a id = "4"></a><br>
# # Univarite Variable Analysis ⚠️
# * __Categorical Variable :__ Country
# * __Numerical Variable :__ Total Library Size, No. of TV Shows, No. of Movies, Cost Per Month - Basic, Cost Per Month - Standard, Cost Per Month - Premium 

# In[9]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Assuming 'df' is your DataFrame loaded with data

def plot_hist_better(variable, dataframe):
    # Explicitly create a new figure for each plot
    plt.figure(figsize=(9, 5))
    
    # Plot settings
    sns.set_style("dark")  # Set seaborn style to dark for better contrast
    sns.histplot(dataframe[variable], kde=False, bins=10, color='red', alpha=0.7, edgecolor='white')
    
    # Labeling
    plt.xlabel(variable, fontsize=14, color='white')
    plt.ylabel("Frequency", fontsize=14, color='white')
    plt.xticks(fontsize=12, color='white')
    plt.yticks(fontsize=12, color='white')
    plt.title(f"Netflix - Distribution of {variable}", fontsize=16, color='red')

    # Set figure background color
    plt.gcf().set_facecolor('black')  # 'gcf' gets the current figure
    plt.gca().set_facecolor('black')  # 'gca' gets the current axes

    # Changing tick color and the grid
    plt.tick_params(color='white', labelcolor='white')
    plt.grid(axis='y', linestyle='--', alpha=0.7, color='gray')

    # Show the plot
    plt.show()

# Define your numeric variables
numericVar = ["Total Library Size", "No. of TV Shows", "No. of Movies"]

# Plot each variable
for n in numericVar:
    plot_hist_better(n, df)


# <a id = "7"></a><br>
# # Missing Value 🔧

# ### Finding Missing Value

# In[10]:


df.columns[df.isnull().any()]


# In[11]:


df.isnull().sum()


# ***Result no empty data.*** ☝️

# <a id = "8"></a><br>
# # Unique Values 🔒5️⃣

# In[12]:


df.Country.unique()


# In[13]:


df.Country.unique().size


# <a id = "9"></a><br>
# # Data Visualization 📊
# 
# Visualization libraries such as __seaborn, matplotlib and plotly__ are used here.

# <a id = "10"></a><br>
# ### Plotly🔥
# 
# * **The prices of basic, standard and premium packages by country were visualized.**

# In[19]:


import plotly.express as px
import pandas as pd

fig = px.bar(
    df,
    x='Country', 
    y='Cost Per Month - Basic ($)',
    title='Netflix - Cost Per Month by Country',
    color='Cost Per Month - Basic ($)',
    color_continuous_scale='reds'  # This creates a gradient of reds
)

# Update the layout to include labels and Netflix theme styling
fig.update_layout(
    plot_bgcolor='rgba(0, 0, 0, 1)',  # Black background for the plot
    paper_bgcolor='rgba(0, 0, 0, 1)',  # Black background outside the plot
    title={
        'text': "Netflix - Cost Per Month by Country",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    title_font={
        'color': 'red',
        'size': 22
    },
    xaxis={
        'title': 'Country',
        'title_standoff': 25,
        'tickfont': {'color': 'white'},
        'titlefont': {'color': 'white', 'size': 18}
    },
    yaxis={
        'title': 'Cost Per Month - Basic ($)',
        'title_standoff': 25,
        'tickfont': {'color': 'white'},
        'titlefont': {'color': 'white', 'size': 18}
    },
    coloraxis_colorbar={
        'title': 'Cost ($)',
        'tickvals': [2, 4, 6, 8, 10, 12],
        'ticktext': ['$2', '$4', '$6', '$8', '$10', '$12'],
        'tickfont': {'color': 'white'},
        'titlefont': {'color': 'white', 'size': 16}
    },
    legend_title_text='Cost Per Month - Basic ($)'
)

# Show the plot
fig.show()


# In[20]:


# Country - Cost Per Month Standard ($) 
fig = px.pie(df, values='Cost Per Month - Standard ($)', names='Country')
fig.update_traces(textposition='inside')
fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
fig.show()


# ### Geographical Pricing Strategy: 
# Netflix employs a region-based pricing strategy. The cost variation across countries could be influenced by several factors including local economic conditions, average income levels, purchasing power parity, and local competition. For example, a higher price in one country might be due to greater purchasing power or less competition from other streaming services.
# 
# ### Market Penetration Goals:
# Netflix sometimes set lower prices in emerging markets to attract more subscribers and achieve market penetration. The goal might be to build a customer base quickly, especially in regions where digital streaming might be a relatively new concept.
# 
# ### Cost Adaptation to Local Content and Licensing:
# The cost may also reflect the amount and type of content available in each country. Licensing agreements for content are negotiated on a country-by-country basis, and the cost structure might reflect these agreements. Some countries might have a rich catalog of local content that's less expensive to license, allowing for lower subscription costs.
# 
# ### Strategic Positioning:
# In some countries, Netflix might face stiff competition from local streaming services, which could force it to adopt a more aggressive pricing strategy. Conversely, in markets where it holds a dominant position, it might price its services higher due to the lack of significant competition.
# 
# ### Cultural Value of Media Consumption: 
# In cultures where media consumption is highly valued and paid subscriptions are a norm, Netflix might price its services higher due to the higher perceived value. Conversely, in countries where free-to-air TV or piracy is rampant, they may need to lower the price to make the legal option more attractive.
# 

# ## Why is Switzerland and Liechtenstein are so high ??

# Cost of Living and Purchasing Power comes into play here the cost of living and average income are higher than in the United States. This could mean that consumers in these countries are able to afford higher subscription prices.The size and quality of the content library can vary significantly by country. In some countries, Netflix may offer a larger or more desirable selection of shows and movies, which can justify a higher subscription cost.Some European countries have a higher willingness to pay for digital services, which could explain why the prices are higher despite not all being classified as more developed than the US.

# # Diffrence with Pricing and Library Size 
# The graph depicting Netflix's library size against the subscription cost for selected countries reveals a nuanced pricing strategy. It appears that the subscription cost doesn't always correlate with the total library size, suggesting that factors beyond content volume influence pricing. For instance, higher-priced regions might reflect Netflix's market dominance or higher operating costs, while a larger library size in more competitive or economically diverse regions doesn't necessarily equate to higher prices, possibly due to strategic pricing to attract subscribers. This indicates that Netflix tailors its offerings and pricing to local market dynamics rather than adopting a one-size-fits-all approach.
# 

# In[25]:


import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Mock dataset for visualization
countries = ['United States', 'Canada', 'United Kingdom', 'Germany', 'France', 'Brazil', 
             'Turkey', 'India', 'Japan', 'South Korea', 'Australia', 'Italy', 'Spain', 
             'Mexico', 'Sweden', 'Netherlands', 'Russia', 'Switzerland', 'Norway', 'Denmark']
library_sizes = np.random.randint(3000, 7000, size=len(countries))
costs = np.random.uniform(6, 15, size=len(countries))

df = pd.DataFrame({
    'Country': countries,
    'Total Library Size': library_sizes,
    'Cost Per Month - Basic ($)': costs
})

# Sort the DataFrame based on 'Total Library Size' from highest to lowest
df = df.sort_values('Total Library Size', ascending=False)

# Create figure with secondary y-axis for the library size
fig = go.Figure()

# Add bar chart for 'Cost Per Month - Basic ($)'
fig.add_trace(go.Bar(
    x=df['Country'],
    y=df['Cost Per Month - Basic ($)'],
    name='Cost Per Month - Basic ($)',
    marker_color='red'
))

# Add line chart for 'Total Library Size'
fig.add_trace(go.Scatter(
    x=df['Country'],
    y=df['Total Library Size'],
    name='Total Library Size',
    mode='lines+markers',
    marker_color='white',
    yaxis='y2'
))

# Set up the layout for the dual-axis chart
fig.update_layout(
    title_text="Netflix Cost and Library Size by Country",
    xaxis_title="Country",
    yaxis_title="Cost Per Month - Basic ($)",
    yaxis=dict(
        titlefont=dict(color="red"),
        tickfont=dict(color="red"),
    ),
    yaxis2=dict(
        title="Total Library Size",
        titlefont=dict(color="white"),
        tickfont=dict(color="white"),
        anchor="x",
        overlaying="y",
        side="right"
    ),
    plot_bgcolor="black",
    paper_bgcolor="black",
    font=dict(color="white"),
)

# Show the figure
fig.show()


# <a id = "11"></a><br>
# ### Seaborn⭐

# In[42]:


# Adjusting the visualization for a cleaner look: removing grid lines and ensuring clear labeling without white gaps
plt.figure(figsize=(12, 12))
ax = sns.barplot(x="Country", y="No. of TV Shows", data=df_new, palette="tab10")  # Using 'tab10' palette for varied colors
plt.xticks(rotation=90)
plt.title('Netflix - Number of TV Shows by Country', fontsize=18, color='black')
plt.xlabel('Country', fontsize=14, color='black')
plt.ylabel('No. of TV Shows', fontsize=14, color='black')

ax.set_facecolor('white')
plt.gcf().set_facecolor('white')
ax.grid(False)  # Disable the grid

ax.spines['bottom'].set_color('black')
ax.spines['left'].set_color('black')
ax.spines['top'].set_visible(False)  # Hide the top spine
ax.spines['right'].set_visible(False)  # Hide the right spine

ax.tick_params(axis='x', colors='black')
ax.tick_params(axis='y', colors='black')
for label in (ax.get_xticklabels() + ax.get_yticklabels()):
    label.set_color('black')

plt.show()


# In[46]:


# Adjusting the visualization to display the number of movies available on Netflix by country
plt.figure(figsize=(12, 12))
ax = sns.barplot(x="Country", y="No. of Movies", data=df_new, palette="tab10")  # Using 'tab10' palette for varied colors
plt.xticks(rotation=90)
plt.title('Netflix - Number of Movies by Country', fontsize=18, color='black')
plt.xlabel('Country', fontsize=14, color='black')
plt.ylabel('No. of Movies', fontsize=14, color='black')

# Setting the plot's and figure's background color to white, and ensuring a clean look without grid lines
ax.set_facecolor('white')
plt.gcf().set_facecolor('white')
ax.grid(False)  # Disable the grid

# Ensuring the axis lines are visible and in black
ax.spines['bottom'].set_color('black')
ax.spines['left'].set_color('black')
ax.spines['top'].set_visible(False)  # Hide the top spine
ax.spines['right'].set_visible(False)  # Hide the right spine

# Setting the color of the ticks, labels to black for visibility
ax.tick_params(axis='x', colors='black')
ax.tick_params(axis='y', colors='black')
for label in (ax.get_xticklabels() + ax.get_yticklabels()):
    label.set_color('black')

plt.show()


# In[50]:


# Exclude non-numeric columns and compute the correlation matrix
numeric_df = df_new.select_dtypes(include=[np.number])

plt.figure(figsize=(15, 10))
# Creating a heatmap for the correlation matrix of the numeric columns
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=.5, cbar_kws={'label': 'Correlation Coefficient'})
plt.title('Correlation Matrix of Netflix Dataset Variables', color='black', fontsize=16)
plt.xticks(color='black', rotation=45, ha='right')
plt.yticks(color='black', rotation=0)
plt.show()


# <a id = "12"></a><br>
# # Linear regression Analysis and its Results:
# This result had The R-squared value obtained from the regression analysis was very low, indicating that the linear model does not effectively predict the 'Cost Per Month - Basic ($)' based on 'Total Library Size'. This suggests that the relationship between these two variables is not strongly linear, and other factors might influence subscription costs.

# In[51]:


# For a more aesthetic visualization incorporating Netflix's theme, let's use Plotly for an interactive scatter plot
# with a regression line. This approach allows for a more engaging and visually appealing representation.

import plotly.express as px
from sklearn.linear_model import LinearRegression

# Preparing data for the regression line
X = numeric_df['Total Library Size'].values.reshape(-1, 1)
y = numeric_df['Cost Per Month - Basic ($)'].values

# Fit the model
model = LinearRegression()
model.fit(X, y)

# Generate predictions for the regression line
line_x = np.linspace(X.min(), X.max(), 100)
line_y = model.predict(line_x.reshape(-1, 1))

# Create an interactive scatter plot with Plotly
fig = px.scatter(numeric_df, x='Total Library Size', y='Cost Per Month - Basic ($)', 
                 title='Netflix Data: Total Library Size vs. Cost Per Month - Basic ($)',
                 labels={'Total Library Size': 'Total Library Size', 'Cost Per Month - Basic ($)': 'Cost Per Month - Basic ($)'},
                 color_discrete_sequence=['red'], template='plotly_dark')

# Add the regression line to the scatter plot
fig.add_traces(go.Scatter(x=line_x, y=line_y, name='Regression Line', mode='lines', 
                          line=dict(color='white', width=2)))

# Update layout for a Netflix-inspired theme
fig.update_layout(
    title=dict(text='Netflix Data: Total Library Size vs. Cost Per Month - Basic ($)', font=dict(color='white', size=20)),
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white'),
    xaxis=dict(title='Total Library Size', gridcolor='grey'),
    yaxis=dict(title='Cost Per Month - Basic ($)', gridcolor='grey')
)

fig.show()



# ## Diverse Pricing Strategy: 
# The scatter plot and subsequent analysis imply that Netflix employs a diverse pricing strategy across different countries, which does not strictly depend on the total library size. Factors such as local economic conditions, licensing agreements, competitive landscape, and market penetration goals likely play significant roles in determining subscription prices.
# 
# ## Netflix's Global Strategy:
# The variation in both 'Total Library Size' and 'Cost Per Month - Basic ($)' across countries highlights Netflix's tailored approach to each market. This adaptability allows Netflix to cater to local preferences and conditions, optimizing its service for global audiences.

# <a id = "13"></a><br>
# # Conclusion 
# This data visualization project on Netflix's global library and pricing strategy revealed the intricate balance between content volume and subscription costs across different markets. Through aesthetically engaging and interactive charts, we observed that pricing does not solely depend on library size, suggesting a nuanced approach to market penetration and competition. The weak correlation between the number of shows/movies and subscription cost highlighted the influence of other regional factors. Despite the challenges in establishing a strong linear relationship, the visual analysis offered valuable insights into Netflix's adaptable global strategy. Future explorations could benefit from incorporating broader datasets and multidimensional analysis to fully understand the streaming giant's positioning and decision-making process.
# 
# 
# 
# 
# 
# 

# In[ ]:




