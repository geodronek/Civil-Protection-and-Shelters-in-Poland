# "C:/Users/kamil/OneDrive/Desktop/geo_dronek/OC_geodronek/Silesia/wojewodztwa/wojewodztwa.shp"
# "C:/Users/kamil/OneDrive/Desktop/geo_dronek/OC_geodronek/Silesia/all_powiaty_silesia.gpkg"
# "C:/Users/kamil/OneDrive/Desktop/geo_dronek/OC_geodronek/Silesia/all_schrony_silesia.gpkg"

from mpl_toolkits.axes_grid1 import make_axes_locatable
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import geodatasets

path_file = 'C:/Users/kamil/OneDrive/Desktop/geo_dronek/OC_geodronek/Silesia/all_schrony_silesia_new(powiaty).gpkg'
gdf = gpd.read_file(path_file)

# print(gdf.columns)

all_county = gdf['powiat_nowe'].unique()
# posortowana alfabetycznie lista powiatów!
list_county = sorted(all_county, key=str.casefold)

schrony = gdf.loc[(gdf['Rodzaj_obi'] == '[1] - (S) - schron')]
schrony_z = gdf.loc[(gdf['Rodzaj_obi'] == '[1] - (S) - schron')
                    & (gdf['Przeznacze'] == '[2] - Z')]
schrony_m = gdf.loc[(gdf['Rodzaj_obi'] == '[1] - (S) - schron')
                    & (gdf['Przeznacze'] == '[1] - M')]

ukrycia = gdf.loc[(gdf['Rodzaj_obi'] == '[2] - (U) - ukrycie')]
ukrycia_z = gdf.loc[(gdf['Rodzaj_obi'] == '[2] - (U) - ukrycie')
                    & (gdf['Przeznacze'] == '[2] - Z')]
ukrycia_m = gdf.loc[(gdf['Rodzaj_obi'] == '[2] - (U) - ukrycie')
                    & (gdf['Przeznacze'] == '[1] - M')]

mds = gdf.loc[(gdf['Rodzaj_obi'] == '[3] - MDS')]
mds_z = gdf.loc[(gdf['Rodzaj_obi'] == '[3] - MDS')
                & (gdf['Przeznacze'] == '[2] - Z')]
mds_m = gdf.loc[(gdf['Rodzaj_obi'] == '[3] - MDS')
                & (gdf['Przeznacze'] == '[1] - M')]

# The number of shelters in each county
print(f'\nLiczba Schronień w województwie śląskim:\nSchrony|Ukrycia|MDS\n(ogółem/dla mieszkańców/dla załóg zakładów pracy)')
print(f'S: {len(schrony)}/{len(schrony_m)}/{len(schrony_z)}\nU: {len(ukrycia)}/{len(ukrycia_m)}/{len(ukrycia_z)}\nM: {len(mds)}/{len(mds_m)}/{len(mds_z)}')

i = 1
for county_name in list_county:
    schrony_count_o = len(
        gdf[
            (gdf['powiat_nowe'] == county_name) &
            (gdf['Rodzaj_obi'] == '[1] - (S) - schron')
        ]
    )

    schrony_count_m = len(
        gdf[
            (gdf['powiat_nowe'] == county_name) &
            (gdf['Rodzaj_obi'] == '[1] - (S) - schron') &
            (gdf['Przeznacze'] == '[1] - M')
        ]
    )

    schrony_count_z = len(
        gdf[
            (gdf['powiat_nowe'] == county_name) &
            (gdf['Rodzaj_obi'] == '[1] - (S) - schron') &
            (gdf['Przeznacze'] == '[2] - Z')
        ]
    )  # Ukrycia
    ukrycia_count_o = len(
        gdf[
            (gdf['powiat_nowe'] == county_name) &
            (gdf['Rodzaj_obi'] == '[2] - (U) - ukrycie')
        ]
    )

    ukrycia_count_m = len(
        gdf[
            (gdf['powiat_nowe'] == county_name) &
            (gdf['Rodzaj_obi'] == '[2] - (U) - ukrycie') &
            (gdf['Przeznacze'] == '[1] - M')
        ]
    )

    ukrycia_count_z = len(
        gdf[
            (gdf['powiat_nowe'] == county_name) &
            (gdf['Rodzaj_obi'] == '[2] - (U) - ukrycie') &
            (gdf['Przeznacze'] == '[2] - Z')
        ]
    )  # MDS
    mds_count_o = len(
        gdf[
            (gdf['powiat_nowe'] == county_name) &
            (gdf['Rodzaj_obi'] == '[3] - MDS')
        ]
    )

    mds_count_m = len(
        gdf[
            (gdf['powiat_nowe'] == county_name) &
            (gdf['Rodzaj_obi'] == '[3] - MDS') &
            (gdf['Przeznacze'] == '[1] - M')
        ]
    )

    mds_count_z = len(
        gdf[
            (gdf['powiat_nowe'] == county_name) &
            (gdf['Rodzaj_obi'] == '[3] - MDS') &
            (gdf['Przeznacze'] == '[2] - Z')
        ]
    )

    info = f"{i}. {county_name}: {schrony_count_o}/{schrony_count_m}/{schrony_count_z}| {ukrycia_count_o}/{ukrycia_count_m}/{ukrycia_count_z} | {mds_count_o}/{mds_count_m}/{mds_count_z}"
    i += 1
    print(info)

# zapis do pliku:
rows = []                                  # 1) przed pętlą

i = 1
for county_name in list_county:
    schrony_count_o = len(gdf[(gdf['powiat_nowe']==county_name) & (gdf['Rodzaj_obi']=='[1] - (S) - schron')])
    schrony_count_m = len(gdf[(gdf['powiat_nowe']==county_name) & (gdf['Rodzaj_obi']=='[1] - (S) - schron') & (gdf['Przeznacze']=='[1] - M')])
    schrony_count_z = len(gdf[(gdf['powiat_nowe']==county_name) & (gdf['Rodzaj_obi']=='[1] - (S) - schron') & (gdf['Przeznacze']=='[2] - Z')])

    ukrycia_count_o = len(gdf[(gdf['powiat_nowe']==county_name) & (gdf['Rodzaj_obi']=='[2] - (U) - ukrycie')])
    ukrycia_count_m = len(gdf[(gdf['powiat_nowe']==county_name) & (gdf['Rodzaj_obi']=='[2] - (U) - ukrycie') & (gdf['Przeznacze']=='[1] - M')])
    ukrycia_count_z = len(gdf[(gdf['powiat_nowe']==county_name) & (gdf['Rodzaj_obi']=='[2] - (U) - ukrycie') & (gdf['Przeznacze']=='[2] - Z')])

    mds_count_o = len(gdf[(gdf['powiat_nowe']==county_name) & (gdf['Rodzaj_obi']=='[3] - MDS')])
    mds_count_m = len(gdf[(gdf['powiat_nowe']==county_name) & (gdf['Rodzaj_obi']=='[3] - MDS') & (gdf['Przeznacze']=='[1] - M')])
    mds_count_z = len(gdf[(gdf['powiat_nowe']==county_name) & (gdf['Rodzaj_obi']=='[3] - MDS') & (gdf['Przeznacze']=='[2] - Z')])

    rows.append({
        "Lp": i,
        "Powiat": county_name,
        "Schrony_ogółem": schrony_count_o,
        "Schrony_mieszkańcy": schrony_count_m,
        "Schrony_zakłady": schrony_count_z,
        "Ukrycia_ogółem": ukrycia_count_o,
        "Ukrycia_mieszkańcy": ukrycia_count_m,
        "Ukrycia_zakłady": ukrycia_count_z,
        "MDS_ogółem": mds_count_o,
        "MDS_mieszkańcy": mds_count_m,
        "MDS_zakłady": mds_count_z
    })
    i += 1

df_out = pd.DataFrame(rows)                # 2) po pętli
df_out.to_csv(
    r"C:\Users\kamil\OneDrive\Desktop\geo_dronek\OC_geodronek\Silesia\wyniki_schrony_powiaty_silesia.csv",
    index=False, encoding="utf-8-sig"
)


# gdf.plot()
# plt.show()



path_file2 = 'C:/Users/kamil/OneDrive/Desktop/geo_dronek/OC_geodronek/Silesia/powiaty_silesia.gpkg'
gdf2 = gpd.read_file(path_file2)

# MAPA
fig, ax = plt.subplots(1, 1)
divider = make_axes_locatable(ax)
cax = divider.append_axes('bottom', size='5%', pad=0.1)
gdf2.plot(
    column='ludnosc_ogolem',
    ax=ax,
    legend=True,
    cax=cax,
    #cmap='RdBu_r',
    legend_kwds={
        "label": "Populacja woj. śląskiego\n [stan na XII 2024]", "orientation": "horizontal"}
)

plt.show()

'''
print('\n---POWIATY: LUDNOŚĆ---')
#print(gdf2['nazwa_powiat'])
#print(gdf2['ludnosc_ogolem'])

powiaty_a = gdf2['nazwa_powiat']
#print(powiaty_a)
#powiaty = sorted(powiaty_a, key=str.casefold)

ludnosc_a = gdf2['ludnosc_ogolem']
#print(ludnosc_a)

def populacja():
    i=1
    j=0
    for powiat in powiaty_a:
        print(f'{i}.{powiat}; {ludnosc_a[j]}')
        i+=1
        j+=1

populacja()   

print(f'\n---schrony / 1000 mieszkańcow---')
print(f'Liczba schronów dla ludności w województwie śląskim: {len(schrony_m)}')
print(f'Populacja {powiaty_a[4]}: {ludnosc_a[4]}')
print(f'Liczba schronów dla mieszkańców w {powiaty_a[4]}:')
print(type(schrony_count_m))
'''

path_file3 = 'C:/Users/kamil/OneDrive/Desktop/geo_dronek/OC_geodronek/Silesia/a_warstwy_geopandas/wyniki_schrony_powiaty_silesia.csv'
pd = pd.read_file(path_file3)



