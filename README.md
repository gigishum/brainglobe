# Overview
<img width="636" height="583" alt="BrainGlobe workflow" src="https://github.com/user-attachments/assets/bcf2b9d5-b0e8-4b15-a362-b0e4d8202e54" />

# Workflow
Before BrainGlobe: Obtain high-resolution, volumetric data (e.g., BrainSaw, serial 2P, whole-brain light sheet, etc)
1. **`Brainreg`**: _Atlas registration._ Select an appropriate atlas, at an appropriate age, at an appropriate resolution (e.g., Allen Adult Mouse Brain Atlas 25µm) for automatic transformation. Main output are deformation matrices which instruct how the template brain and sample brain spaces should transform to match each other. Optimize by changing parameters and re-running. 
2. **`Cellfinder`**: _Cell detection._ Load both raw 3D volumes of the signal and background channels for automatic cell detection. Main output are 3D coordinates of detected and rejected cells. Optimize by manual labelling cells, re-training the cell detection classifier, and re-running. 
3. Combination of the two with **`brainmapper`**: These two output (transformation and cell coordinates) are combined together, so cell coordinates will also be transformed to the sample brain space. Main output is an .npy file. 
4. **`Brainrender`**: _Visualizations._ Using custom or sample scripts, generate visualizations (e.g., detected cells in 3D atlas space, implant locations, heatmap gene expression levels, etc).
5. **Custom scripts**: This is entirely up to how the individual. Some sample scripts are included in this repo.
* Workflow: <br/>
  * `brainreg` → `cellfinder` → `brainmapper` (widget) → `brainrender` → custom scripts <br/>
* Alternatively, if you want to batch process multiple brains with the same parameters and leave it running, you can run: <br/>
  * `brainmapper` (one-line command line tool) → `brainrender`

# Installation
`conda create -c conda-forge --name brainglobe python=3.12` <br/>
`conda activate brainglobe` <br/>
`conda install -c conda-forge niftyreg` #mac users <br/>
`pip install brainglobe "napari[pyqt6]"` <br/>

`pip install imageio-ffmpeg` # optional <br/>
`pip install brainglobe --upgrade` # when time comes <br/>

# Open BrainGlobe
`conda activate brainglobe` <br/>
`napari` <br/>

# Official documentation
**BrainGlobe** [Documentation](https://brainglobe.info/index.html) <br/>

**`brainreg`** [Documentation](https://brainglobe.info/documentation/brainreg/index.html) <br/>
**`cellfinder`** [Documentation](https://brainglobe.info/documentation/cellfinder/index.html) <br/>
**`brainrender`** [Documentation](https://brainglobe.info/documentation/brainrender/index.html) <br/>
**`brainrender`** [Sample scripts (GitHub)](https://github.com/brainglobe/brainrender/tree/main/examples) <br/>

**`brainmapper` (widget)** [Documentation](https://brainglobe.info/documentation/brainglobe-utils/transform-widget.html) <br/>
**`brainmapper` (command line tool)** [Documentation](https://brainglobe.info/documentation/brainglobe-workflows/brainmapper/index.html)

# Jupyter Lab (Optional) 
`conda activate brainglobe` <br/>
`pip install jupyterlab ipykernel` <br/>
`python -m ipykernel install --user --name=brainglobe `<br/>

