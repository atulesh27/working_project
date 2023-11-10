import folium
import plotly.express as px
import pandas as pd

# Create a sample dataset for the chart
data = {
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago', 'Boston'],
    'Latitude': [40.7128, 37.7749, 34.0522, 41.8781, 42.3601],
    'Longitude': [-74.0060, -122.4194, -118.2437, -87.6298, -71.0589],
    'Population': [8175133, 884363, 3971883, 2716000, 694583],
}

df = pd.DataFrame(data)

# Create a bar chart using Plotly
fig = px.bar(df, x='City', y='Population', title='Population of Cities')

# Save the chart as an HTML file
fig.write_html('bar_chart.html')

# Create a folium map
map_center = [37.7749, -122.4194]  # San Francisco's coordinates

mymap = folium.Map(location=map_center, zoom_start=4)

# Add a marker for each city on the map
for index, row in df.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=f"<strong>{row['City']}</strong><br>Population: {row['Population']}",
    ).add_to(mymap)

# Save the map as an HTML file
mymap.save('map.html')



"""" 
# code for dynamic data coming from mongodb server 
import folium
import plotly.express as px
import pandas as pd
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://your_username:your_password@your_host:your_port/your_database')
db = client.your_database
collection = db.cities

# Fetch data from MongoDB and create a DataFrame
cursor = collection.find()
data = []
for document in cursor:
    data.append({
        'City': document['name'],
        'Latitude': document['latitude'],
        'Longitude': document['longitude'],
        'Population': document['population'],
    })

df = pd.DataFrame(data)

# Create a bar chart using Plotly
fig = px.bar(df, x='City', y='Population', title='Population of Cities')

# Save the chart as an HTML file
fig.write_html('bar_chart.html')

# Create a folium map
map_center = [df['Latitude'].mean(), df['Longitude'].mean()]  # Center map on the average coordinates

mymap = folium.Map(location=map_center, zoom_start=4)

# Add a marker for each city on the map
for index, row in df.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=f"<strong>{row['City']}</strong><br>Population: {row['Population']}",
    ).add_to(mymap)

# Save the map as an HTML file
mymap.save('map.html')

# Close the MongoDB connection
client.close()
"""
