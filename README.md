# Overview
<img width="636" height="583" alt="BrainGlobe workflow" src="https://github.com/user-attachments/assets/bcf2b9d5-b0e8-4b15-a362-b0e4d8202e54" />

# Workflow in a nutshell
1. Obtain high-resolution, volumetric data (e.g., BrainSaw, serial 2P, whole-brain light sheet, etc)
2. **Atlas registration with `brainreg`**: Select an appropriate atlas, at an appropriate age, at an appropriate resolution (e.g., Allen Adult Mouse Brain Atlas 25µm) for automatic transformation. Main output are deformation matrices which instruct how the template brain and sample brain spaces should transform to match each other. Optimize by changing parameters and re-running. 
3. **Cell detection with `cellfinder`**: Load both raw 3D volumes of the signal and background channels for automatic cell detection. Main output are 3D coordinates of detected and rejected cells. Optimize by manual labelling cells, re-training the cell detection classifier, and re-running. 
4. Combination of the two with **`brainmapper`**: These two output (transformation and cell coordinates) are combined together, so cell coordinates will also be transformed to the sample brain space. Main output is an .npy file. 
5. **Visualization with `brainrender`**: Using custom or sample scripts, generate visualizations (e.g., detected cells in 3D atlas space, implant locations, heatmap gene expression levels, etc).
6. **Custom scripts**: This is entirely up to how the individual. Some sample scripts are included in this repo.
* Workflow: <br/>
  * `brainreg` → `cellfinder` → `brainmapper` (widget) → `brainrender` → custom scripts <br/>
* Alternatively, if you want to batch process multiple brains with the same parameters and leave it running, you can run: <br/>
  * `brainmapper` (one-line command line tool) → `brainrender`

# Official documentation
**BrainGlobe** [Documentation](https://brainglobe.info/index.html) <br/>

**`brainreg`** [Documentation](https://brainglobe.info/documentation/brainreg/index.html) <br/>
**`cellfinder`** [Documentation](https://brainglobe.info/documentation/cellfinder/index.html) <br/>
**`brainrender`** [Documentation](https://brainglobe.info/documentation/brainrender/index.html) <br/>
**`brainrender`** [Sample scripts (GitHub)](https://github.com/brainglobe/brainrender/tree/main/examples) <br/>

**`brainmapper` (widget)** [Documentation](https://brainglobe.info/documentation/brainglobe-utils/transform-widget.html) <br/>
**`brainmapper` (command line tool)** [Documentation](https://brainglobe.info/documentation/brainglobe-workflows/brainmapper/index.html)

# Installation
### Create virtual environment called brainglobe <br/>
`conda create -c conda-forge --name brainglobe python=3.12` <br/>
`conda activate brainglobe` <br/>

### Install napari <br/>
Note: Install with PyQt6 backend using conda: <br/>
`conda install -c conda-forge napari pyqt6`<br/>

### Install BrainGlobe core packages <br/>
`pip install brainglobe` <br/>
`pip install imageio-ffmpeg` <br/>

### Install brainreg <br/>
`pip install 'brainreg[napari]'` <br/>
`conda install -c conda-forge niftyreg` (MacOS only) <br/>

### Install cellfinder <br/>
`pip install cellfinder[napari]`<br/>

### Install brainrender <br/>
`conda install -c conda-forge ffmpeg` <br/>
`conda install -c conda-forge hdf5` (MacOS only) <br/>
`pip install brainrender`<br/>

# Install kernel in brainglobe environment
`conda activate brainglobe`<br/>
`pip install ipykernel`<br/>
`python -m ipykernel install --user --name=brainglobe`<br/>
`pip install jupyterlab` (Optional, for if you want to use Jupyter Lab. If you use VS Code or PyCharm, it will automatically be there) <br/>

