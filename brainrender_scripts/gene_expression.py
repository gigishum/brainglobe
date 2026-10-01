from pathlib import Path

from myterial import orange
from rich import print

from brainrender import Scene, settings
from brainrender.actors import Points
from brainrender.atlas_specific import GeneExpressionAPI

settings.SHOW_AXES = False
scene = Scene(inset=False)

settings.SHADER_STYLE = "plastic"


# Path to your brainmapper results
cells_path = '/Users/brainrender/points.npy' 


cells = Points(cells_path, radius=45, colors="palegoldenrod", alpha=0.8)
scene.add(cells)


# Define gene of interest
gene = "Gpr161" 

# Get gene expression data
geapi = GeneExpressionAPI()
expids = geapi.get_gene_experiments(gene)
data = geapi.get_gene_data(gene, expids[1])

gene_actor = geapi.griddata_to_volume(data, min_quantile=99, cmap="inferno")
act = scene.add(gene_actor)


# Define brainn region of interest
mpo = scene.add_brain_region("MPO", alpha=0.2, color="purple")


scene.add_silhouette(act)

scene.render(zoom=1.6)
