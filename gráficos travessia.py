import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.interpolate import make_interp_spline
import numpy as np

planilha = r'C:\Users\moesios\Desktop\CONTORNO\C11.xlsx'
df_graf = pd.read_excel(planilha, sheet_name='Planilha2')

df_long = pd.melt(df_graf, id_vars=['HORA'], value_vars=['Passeio', 'Ônibus', 'Cargas', 'Motocicleta'],
                  var_name='Tipo de Veículo', value_name='Fluxo de Veículos')
df_long['Fluxo de Veículos'] = df_long['Fluxo de Veículos'].fillna(0).astype(int)

plt.figure(figsize=(14, 8))
sns.set(style="whitegrid")
palette = sns.color_palette("hls", len(df_long['Tipo de Veículo'].unique()))

for i, vehicle_type in enumerate(df_long['Tipo de Veículo'].unique()):
    df_subset = df_long[df_long['Tipo de Veículo'] == vehicle_type]
    x = np.arange(len(df_subset['HORA']))
    y = df_subset['Fluxo de Veículos']
    
    x_smooth = np.linspace(x.min(), x.max(), 300)
    spl = make_interp_spline(x, y, k=3)
    y_smooth = spl(x_smooth)
    
    plt.plot(x_smooth, y_smooth, label=vehicle_type, linewidth=2.5, color=palette[i])
    plt.scatter(x, y, color=palette[i], edgecolor='black', s=50)

plt.title('Fluxo Médio de Veículos Diário por Hora - Est. Berico José Bernardes, próximo à Est. João de Oliveira Remião', fontsize=20, family='Arial', color='black')
plt.xlabel('Hora', fontsize=16, family='Arial', color='black')
plt.ylabel('Fluxo de Veículos', fontsize=16, family='Arial', color='black')

plt.xticks(ticks=np.arange(len(df_subset['HORA'])), labels=df_subset['HORA'], rotation=-45, fontsize=12, family='Arial', color='black')
plt.yticks(fontsize=12, family='Arial', color='black')

plt.legend(title='Tipo de Veículo', title_fontsize='13', fontsize='11', loc='upper right', frameon=True)

plt.grid(True, which='both', linestyle='--', linewidth=0.5, color='grey')

plt.tight_layout()

plt.show()