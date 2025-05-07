import streamlit as st
import pandas as pd
import os as os
import numpy as np
from matplotlib import pyplot as plt
from prettytable import PrettyTable as pt
st.markdown('<h1>Data Visualization</h1>', unsafe_allow_html=True)

st.markdown('---')
files_name = list()
files = st.file_uploader(
    label='Upload Data Anda',
    type=['pdf','xlsx','csv'],
    help='Apabila Anda mendaftar organisasi maka perlu mengupload Data',
    accept_multiple_files=True,
    key='uploadedFile'
)

def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def dateConverter(date_col):
    result = list()
    values = date_col.values
    for value in values :
        result.append(str(value).split('T')[0])
    return result

st.button(
    label='Hapus Terminal',
    key='clearTerminal',
    help='Hapus Terminal',
    on_click=clearTerminal,
    use_container_width=True,
    type='primary'
)

if files :
    figure = plt.figure()
    for file in files :
        files_name.append(file.name)
    selected_files = st.multiselect(label='Select Files', options=files_name)
    if selected_files :
        option = st.radio(label='Select Entity Againts Date', options=['NONE','DATE','BARANG','JUMLAH','KATEGORI'])
        if option != 'NONE':
           for file in files :
               if file.name in selected_files :
                   data = pd.read_excel(file, index_col=0)
                   st.write(data)

                   item = list(data[option])
                   tanggalrapi = dateConverter(data['DATE'])
                   tanggalmess = data['DATE'].values 
                   index = np.arange(len(tanggalrapi))
                   
                   plt.xticks(index, tanggalrapi)
                   plt.gcf().autofmt_xdate()
                   plt.plot(index, item, marker="o", linestyle="--", label=option)
                   plt.xlabel("Tanggal Pembelian", loc='center', labelpad=15.0)
                   plt.ylabel(f'Jumlah {option} Terjual', loc='center', labelpad=15.0)
                   plt.title(label=f'{option} Chart')
                   plt.grid(visible=True)
                   plt.legend(title="Legend")

                   table = pt(["Tanggal (Rapi)", "Tanggal Ngga Rapi", option])
                   for x, y, z in zip(tanggalrapi, tanggalmess, list(item)):
                        table.add_row([x, y, z])

                   clearTerminal() 
                   print("\n===== Data yang diambil =====")
                   print(table)
                #    st.write(data[option])
                #    print(f'Ini adalah Data yang di ambil :\n\n{list(data[option])}\n\nDan ini adalah tanggalnya :\n{data['DATE'].values}')
           st.write(figure)