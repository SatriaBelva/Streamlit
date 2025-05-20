import streamlit as st
import geopandas as gpd
import folium
import pandas as pd
from streamlit_folium import st_folium
import branca.colormap as cm
from shapely.geometry import Point
from folium import Element
from controller import *
from model import *

def load_kabupaten_shp2():
    shapefile_path = r"data/dataSHPTapalKuda/kabupaten_terpilih_jatim.shp"
    return gpd.read_file(shapefile_path)

def table2():
    data = pd.DataFrame(
        {   
            'Kabupaten'         : get_Kabupaten_data(),
            'FB Share REG'      : get_FacebookShare_data(),
            'Status REG'        : get_StatugReg_data(),
            'Close COMP REG'    : get_CloseCompetitionReg_data(),
        }
    )
    return data

def map_REG_status():
    gdf = load_kabupaten_shp2()
    data = table2()

    # Normalisasi nama kabupaten agar cocok
    gdf['Kabupaten'] = gdf['Kabupaten'].str.upper().str.strip()
    data['Kabupaten'] = data['Kabupaten'].str.upper().str.strip()

    # Merge shapefile dengan data REG
    gdf = gdf.merge(data, how='left', on='Kabupaten')

    # Fungsi warna berdasar aturan
    def get_color(status_REG, close_comp_REG):
        if status_REG == "WIN":
            return 'red'
        elif status_REG == "LOSE" and close_comp_REG == "IOH":
            return 'yellow'
        elif status_REG == "LOSE" and close_comp_REG == "XL+":
            return 'blue'
        else:
            return 'lightgray'

    # Style function
    def style_function(feature):
        status_REG = feature['properties'].get('Status REG', '')
        close_comp_REG = feature['properties'].get('Close COMP REG', '')
        color = get_color(status_REG, close_comp_REG)
        return {
            'fillColor': color,
            'color': 'black',
            'weight': 1,
            'fillOpacity': 0.7
        }

    # Pusat peta (tengah semua geometri)
    center = gdf.geometry.unary_union.centroid
    m = folium.Map(location=[center.y, center.x], zoom_start=9)

    for col in gdf.columns:
        if pd.api.types.is_datetime64_any_dtype(gdf[col]):
            gdf[col] = gdf[col].astype(str)

    # Tambah GeoJson ke peta
    folium.GeoJson(
        gdf,
        name="REG Status Map",
        style_function=style_function,
        tooltip=folium.GeoJsonTooltip(
            fields=['Kabupaten', 'Status REG', 'Close COMP REG'],
            aliases=['Kabupaten:', 'Status REG:', 'Close COMP REG:'],
            sticky=True
        )
    ).add_to(m)
    # Tambahkan legend manual
    legend_html = """
    <div style="
        position: fixed;
        top: 10px;
        right: 10px;
        z-index: 9999;
        padding: 10px 14px;
        font-size: 14px;
        font-weight: bold;
        font-family: Arial, sans-serif;
        display: flex;
        flex-direction: row;
        gap: 14px;
        border: 1px solid #ccc;
        border-radius: 8px;
        box-shadow: 2px 2px 6px rgba(0,0,0,0.3);
        background: white;
    ">

            <div style="display: flex; align-items: center;">
            <span style="height: 12px; width: 12px; background-color: red; border-radius: 50%; display: inline-block; margin-right: 8px;"></span>
            Telkomsel
        </div>
        <div style="display: flex; align-items: center;">
            <span style="height: 12px; width: 12px; background-color: yellow; border-radius: 50%; display: inline-block; margin-right: 8px;"></span>
            Indosat
        </div>
        <div style="display: flex; align-items: center;">
            <span style="height: 12px; width: 12px; background-color: blue; border-radius: 50%; display: inline-block; margin-right: 8px;"></span>
            XL
        </div>
    </div>
    """
    m.get_root().html.add_child(Element(legend_html))

    # Tampilkan di Streamlit
    st_data = st_folium(m, width=1540, height=600)