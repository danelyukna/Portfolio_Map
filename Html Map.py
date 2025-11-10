import folium
import json

# Создаем карту
m = folium.Map(location=[55.76, 37.64], zoom_start=5, tiles="CartoDB dark_matter")
with open('Russia.geojson') as f:
    geojson_data = json.load(f)

# Данные проектов
projects = [
    {
        "city": "Москва",
        "coords": [55.7558, 37.6176],
        "slides": ["moscow1.jpg", "moscow2.jpg"],
        "description": "Проект реновации исторического центра"
    }
]

# Добавляем маркеры
for project in projects:
    html = f"""
    <h3>{project['city']}</h3>
    <p>{project['description']}</p>
    <img src="{project['slides'][0]}" width="250px"><br>
    <button onclick="nextSlide()">›</button>
    """

    iframe = folium.IFrame(html, width=300, height=200)
    folium.Marker(
        location=project["coords"],
        popup=folium.Popup(iframe),
        icon=folium.Icon(color="red")
    ).add_to(m)

folium.GeoJson(
    geojson_data,
    style_function=lambda x: {
        'fillColor': 'yellow',
        'color': 'red',
        'weight': 2,
        'fillOpacity': 0.2
    },
    tooltip=folium.GeoJsonTooltip(fields=['SOVEREIGNT', 'ECONOMY'])
).add_to(m)

# Сохраняем в HTML
m.save("projects_map.html")