import SimpleITK as sitk
import numpy as np
import pyvista as pv

# Read segmentation (robust, slicer-compatible)
img = sitk.ReadImage("output_seg02.nrrd")
seg = sitk.GetArrayFromImage(img).astype(np.uint8)  # (Z, Y, X)

# Get spatial info
spacing = img.GetSpacing()      # (X, Y, Z)
origin = img.GetOrigin()        # (X, Y, Z)

# Convert to PyVista format
grid = pv.ImageData()
grid.dimensions = seg.shape[::-1]  # (X, Y, Z)
grid.spacing = spacing
grid.origin = origin

grid.point_data["seg"] = seg.flatten(order="F")

# Extract surface
surface = grid.contour([0.5])

# Render
plotter = pv.Plotter()
plotter.add_mesh(surface, opacity=1.0)
plotter.show()
