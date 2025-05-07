import streamlit as st
import geopandas as gpd
import folium
from streamlit_folium import st_folium
import branca.colormap as cm
from shapely.geometry import Point

def map_path() :
    shapefile_path = r"C:\Magang Grapari\Magang\streamlit\data\JemberSHP\ADMINISTRASIDESA_AR_25K.shp"
    return gpd.read_file(shapefile_path)

def kecamatan_list() :
    kecamatan_list = sorted(map_path()['WADMKC'].unique())
    kecamatan_list.append("Semua")
    kecamatan_list.append("Search Kecamatan")
    return kecamatan_list

def map(kecamatan, desa):
    gdf = map_path()
    selected_kecamatan = kecamatan
    selected_desa = desa
    # Identifikasi wilayah yang dipilih
    selected_area = gdf.copy()

    highlight_geom = None  # untuk menyimpan geometri wilayah yang akan di-zoom dan di-highlight

    if selected_kecamatan != "Semua" and selected_desa != "Semua":
        highlight_geom = gdf[(gdf['WADMKC'] == selected_kecamatan) & (gdf['NAMOBJ'] == selected_desa)]
    elif selected_kecamatan != "Semua":
        highlight_geom = gdf[gdf['WADMKC'] == selected_kecamatan]
    elif selected_desa != "Semua":
        highlight_geom = gdf[gdf['NAMOBJ'] == selected_desa]



    #colormap
    colormap = cm.linear.YlOrRd_09.scale(gdf['SHAPE_Area'].min(), gdf['SHAPE_Area'].max())
    colormap.caption = 'Luas Area'

    if highlight_geom is not None and not highlight_geom.empty:
        centroid = highlight_geom.geometry.unary_union.centroid
        m = folium.Map(location=[centroid.y, centroid.x], zoom_start=13)
    else:
        center = gdf.geometry.unary_union.centroid.coords[:][0]
        m = folium.Map(location=[center[1], center[0]], zoom_start=10)

    # Plot semua wilayah
    def style_all(feature):
        return {
            'fillColor': colormap(feature['properties']['SHAPE_Area']),
            'color': 'gray',
            'weight': 1,
            'fillOpacity': 0.9,
        }

    def highlight_style(feature):
        return {
            # 'fillColor': '#ffff00',
            'color': 'red',
            'weight': 3,
            'fillOpacity': 0.9,
        }

    folium.GeoJson(
        gdf,
        name="Batas Wilayah",
        style_function=style_all,
        highlight_function=highlight_style,
        tooltip=folium.GeoJsonTooltip(
            fields=["WADMKC", "NAMOBJ"],
            aliases=["Kecamatan:", "Desa:"],
            sticky=True,
            opacity=0.9,
            direction='auto'
        ),
        popup=folium.GeoJsonPopup(
            fields=["WADMPR", "WADMKK", "WADMKC", "NAMOBJ", "SHAPE_Area"],
            aliases=["Provinsi:", "Kabupaten:", "Kecamatan:", "Desa:", "Luas Area:"],
            labels=True
        ),
        zoom_on_click=True
    ).add_to(m)


    #highlight jika ada wilayah dipilih
    if highlight_geom is not None and not highlight_geom.empty:
        folium.GeoJson(
            highlight_geom,
            name="Wilayah Dipilih",
            style_function=lambda feature: {
                'fillColor': 'none',
                'color': 'red',
                'weight': 4,
                'fillOpacity': 0,
            },
            tooltip=folium.GeoJsonTooltip(
                fields=["WADMPR", "WADMKK", "WADMKC", "NAMOBJ", "SHAPE_Area"],
                aliases=["Provinsi:", "Kabupaten:", "Kecamatan:", "Desa:", "Luas Area:"],
                sticky=False
            )
        ).add_to(m)

    colormap.add_to(m)

    #peta
    st_data = st_folium(m, width=800, height=600)

    clicked_location = st_data.get("last_clicked")
    if clicked_location:
        point = Point(clicked_location["lng"], clicked_location["lat"])
        matched_area = gdf[gdf.geometry.contains(point)]

        if not matched_area.empty:
            filter_result = matched_area
        else:
            filter_result = highlight_geom if highlight_geom is not None and not highlight_geom.empty else gdf
    else:
        filter_result = highlight_geom if highlight_geom is not None and not highlight_geom.empty else gdf

