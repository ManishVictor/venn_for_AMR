import numpy as np
from pycirclize import Circos
from pycirclize.parser import Matrix
import pandas as pd
import matplotlib.pyplot as plt
# Create from-to table dataframe & convert to matrix
# fromto_table_df = pd.DataFrame(
#     [
#      ['class a ', 'Permafrost', 1],
# ['class a ', 'SeaWater', 1],
# ['class a ', 'Sediment', 1],
# ['class a ', 'Proteobacteria', 1],
# ['class a ', 'Unknown', 1],
# ['class a ', 'Gemmatimonadetes', 1],
# ['class b3', 'Sediment', 1],
# ['class b3', 'Proteobacteria', 1],
# ['class b3', 'Permafrost', 1],
# ['class b3', 'SeaWater', 1],
# ['class b3', 'Acidobacteria', 1],
# ['class b3', 'Proteobacteria', 1],
# ['class b1b2', 'Sediment', 1],
# ['class b1b2', 'SeaWater', 1],
# ['class b1b2', 'Proteobacteria', 1],
# ['class b1b2', 'Bacteroidetes', 1],
# ['class d', 'Sediment', 1],
# ['class d', 'SeaWater', 1],
# ['class d', 'Proteobacteria', 1],
# ['class d', 'Bacteroidetes', 1],
# ['class d', 'Permafrost', 1],
# ['class d', 'C.Marinimicrobia', 1],
# ['class d', 'Proteobacteria', 1],
# ['class d', 'Unknown', 1],
# ['class d', 'Planctomycetes', 1],
# ['class d', 'Chloroflexi', 1], 
#     ],
#     columns=["from", "to", "value"],  # Column name is optional
# )
fromto_table_df = pd.DataFrame(
    [
['Proteobacteria','class a ',1],
['Proteobacteria','class b3',1],
['Proteobacteria','class b3',1],
['Proteobacteria','class d',1],
['Proteobacteria','class b1b2',1],
['Permafrost','class a ',1],
['Permafrost','class b3',1],
['Permafrost','class d',1],
['Sediment','class a ',1],
['Sediment','class b3',1],
['Sediment','class b1b2',1],
['Sediment','class d',1],
['SeaWater','class a ',1],
['SeaWater','class d',1],
['SeaWater','class b3',1],
['SeaWater','class b1b2',1],
['Bacteroidetes','class b1b2',1],
['Bacteroidetes','class d',1],
['Candidatus Marinimicrobia','class d',1],
['Proteobacteria','class d',1],
['Planctomycetes','class d',1],
['Chloroflexi','class d',1],
['Gemmatimonadetes','class a ',1],
['Acidobacteria','class b3',1],
['Bacteria[Unknown]','class a ',1],
['Bacteria[Unknown]','class d',1],
['MAG','class b3',1],
['MAG','class a ',1],
['MAG','class b1b2',1],
['MAG','class d',1],
['MAG','Bacteroidetes',1],
['MAG','Gammaproteobacteria',1],
['MAG','Candidatus Marinimicrobia',1],
['MAG','Acidobacteria',1],
['MAG','Bacteria[Unknown]',1],
['MAG','Planctomycetes',1],
['MAG','Nitrosomonadales',1],
['MAG','Flavobacteriaceae',1],
['MAG','Proteobacteria',1],
['MAG','Prolixibacteraceae',1],
['MAG','Chloroflexi',1],
['MAG','Kordiimonadaceae',1],
['MAG','Sphingomonadaceae',1],
['MAG','Kordiimonadaceae',1],
['MAG','Gemmatimonadetes',1]
    ],
    columns=["from", "to", "value"],  # Column name is optional
)
matrix = Matrix.parse_fromto_table((fromto_table_df))

print(matrix)

circos = Circos.initialize_from_matrix(
    matrix,
    start=-265,
    end=95,
    space=0.5,
    cmap="hsv",#"tab10",#"hsv",#Set2 is beautiful
    label_kws=dict(orientation = 'vertical',size=6, r=105, color="black"),
    link_kws=dict(direction = -1, ec="black", lw=0.1),
)
#print(fromto_table_df.to_string(index=False))
#print(np.unique(np.array(fromto_table_df['from'])+np.array(fromto_table_df['to'])))
fig = circos.plotfig()
plt.savefig('Test_Circos.pdf', dpi=1200)
plt.show()
