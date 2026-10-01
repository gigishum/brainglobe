from brainrender.scene import Scene
from brainrender.actors import Points
from brainrender import settings

settings.SHADER_STYLE = "plastic"
cells_path = '/Users/brainrender/points.npy' # path to your brainmapper results

# Initialise brainrender scene
scene = Scene()

# Create points actor
cells = Points(cells_path, radius=45, colors="palegoldenrod", alpha=0.8)

# Visualise injection site (retrosplenial cortex)
scene.add_brain_region("MPO", color="purple", alpha=0.6) # add medial preoptic area

# Add cells
scene.add(cells)

scene.render()
