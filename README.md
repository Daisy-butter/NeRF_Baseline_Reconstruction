<h1 align="center">3D Reconstruction Based on NeRF</h1>

---

This project explores 3D object reconstruction and novel view synthesis based on **Neural Radiance Fields (NeRF)**, a powerful neural rendering technique that has achieved remarkable success in computer vision. By leveraging a neural network to learn a volumetric scene representation, NeRF enables photorealistic novel view generation from a sparse set of input images.  
We build upon the official **[nerf-pytorch](https://github.com/yenchenlin/nerf-pytorch)** implementation and apply it to real-world objects captured via handheld smartphone cameras.

---

## 📁 Project Structure

### 🔧 Core Scripts

- **`run_nerf.py`**  
  The main training and rendering script for the NeRF model. Key functions include:
  - `batchify`: Applies a function to inputs in smaller chunks to reduce memory usage.
  - `run_network`: Prepares inputs and runs the MLP.
  - `batchify_rays`: Batches rays for rendering.
  - `render`, `render_path`: Render rays or camera paths.
  - `create_nerf`: Instantiates the NeRF model.
  - `raw2outputs`: Converts raw model outputs to RGB and depth.
  - `render_rays`: Performs volumetric rendering along rays.

- **`run_nerf_helpers.py`**  
  Contains helper functions and model classes:
  - `img2mse`, `mse2psnr`, `to8b`: Image and metric utilities.
  - `Embedder`, `get_embedder`: Positional encoding.
  - `NeRF`: MLP-based scene representation.
  - `get_rays`, `ndc_rays`: Ray computation utilities.
  - `sample_pdf`: Hierarchical sampling.

- **`load_llff.py` / `load_blender.py` / `load_deepvoxels.py` / `load_LINEMOD.py`**  
  Data loaders for LLFF, Blender, DeepVoxels, and LINEMOD datasets respectively.

---

### 📂 Directory Layout

- **`configs/`**  
  Training configuration files for different scenes and experiments.

- **`data/`**  
  Contains the input image datasets formatted in LLFF style.  
  Datasets are created from real-world objects via COLMAP and converted using LLFF scripts.

- **`logs/`**  
  Training logs, visualizations, and model outputs:
  - `summaries/`: TensorBoard logs.
  - `donggua&hotcrush/`: Training logs and rendered videos for a stationery bag object.
  - `test/`: Comparison experiments (e.g., a soda can object).

- **`LLFF-master/`**  
  Contains scripts for transforming camera pose data into LLFF format.  
  (Imported from [Fyusion/LLFF](https://gitcode.com/Fyusion/LLFF.git))

---

## 🏗️ Training Workflow

### (1) Prepare the Dataset

- Capture multi-view images of an object using a handheld camera.
- Estimate camera poses using **COLMAP**.
- Convert the results to LLFF format using the LLFF pose script.
- Optionally downsample high-resolution images using `data/downsample.py`.

### (2) Start Training

- Create a new config file in the `configs/` folder (e.g., `test.txt`) and point it to your dataset.
- Make sure the data format matches LLFF.
- Start training:

```bash
python run_nerf.py --config configs/test.txt
