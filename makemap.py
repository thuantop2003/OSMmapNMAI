import folium

# Tọa độ của vùng cần khoanh
north, south, east, west = 21.02743, 21.02221, 105.83977, 105.82522

# Tính toán tọa độ trung bình để căn giữa bản đồ
center_lat = (north + south) / 2
center_lon = (east + west) / 2

# Tạo bản đồ với tọa độ trung bình làm trung tâm
map_osm = folium.Map(location=[center_lat, center_lon], zoom_start=17)

# Tạo hình chữ nhật để khoanh vùng
folium.Rectangle(bounds=[(south, west), (north, east)], color='red', fill=True, fill_color='red', fill_opacity=0.2).add_to(map_osm)

# Hiển thị bản đồ
map_osm.save('map_with_rectangle.html')
