# WDF Processor

**Author**: Prasad Aradhye  
**Affiliation**: University of Edinburgh  

## Overview

`wdf_processor` is a Python tool designed for processing and visualizing spectral data from WDF files (e.g., Raman spectra). It provides robust functionality to streamline spectral analysis and visualization, including:

- Loading and processing `.wdf` files.
- Interpolating spectra to a fixed length for consistency.
- Truncating data to specific wavenumber ranges.
- Plotting spectral data and associated white light images with customizable features.

This tool is ideal for researchers and scientists who work with spectral data and need efficient processing pipelines.

---

## Features

- **File Loader**: Easily load `.wdf` files with customizable truncation and interpolation options.
- **Data Visualization**: Built-in integration with `matplotlib` for clear and informative spectral plots.
- **White Light Image Support**: Visualize white light images with scale bars and cropping functionality.
- **Open Source**: Fully extensible and licensed for research and academic use.

---

## Installation

### Dependencies

To use this tool, you need the following Python libraries:

- [numpy](https://pypi.org/project/numpy/)  
- [scipy](https://pypi.org/project/scipy/)  
- [matplotlib](https://pypi.org/project/matplotlib/)  
- [tqdm](https://pypi.org/project/tqdm/)  
- [Pillow](https://pypi.org/project/Pillow/) (PIL fork for image processing)  
- [renishawWiRE](https://pypi.org/project/renishawWiRE/) (MIT License)  

### Installation Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/Aradhye-sys/wdf_processor.git
   ```

2. Navigate to the project directory:
   ```bash
   cd wdf_processor
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage Instructions

1. **Load WDF Files**: Use the tool to select and load multiple `.wdf` files.
2. **Preprocess Spectral Data**:
   - Interpolate spectra to a uniform length.
   - Truncate data to specific wavenumber ranges as needed.
3. **Visualize Data**:
   - Plot spectral maps for exploratory analysis.
   - Display white light images with scale bars for detailed observations.
4. **Export Results**: Save plots and processed data for use in publications or further analysis.

---

## Licensing and Authorship

This tool is licensed under the **MIT License with a Co-Authorship Clause**. See the `LICENSE` file for detailed terms.

### Co-Authorship Policy

If this software contributes significantly to your research or publications, **Prasad Aradhye must be included as a co-author**. For minor usage, please include the following acknowledgment:

> "This work utilized the WDF Processor tool developed by Prasad Aradhye, University of Edinburgh."

---

## Citation

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14470842.svg)](https://doi.org/10.5281/zenodo.14470842)

If you use this tool in your research, please cite it as:

> Prasad Aradhye. "WDF Processor: A Python Tool for Processing and Visualizing WDF Spectral Data." University of Edinburgh, 2024. DOI: [10.5281/zenodo.14470842](https://doi.org/10.5281/zenodo.14470842)

For BibTeX:
```bibtex
@software{aradhye_wdf_processor,
  author = {Prasad Aradhye},
  title = {WDF Processor: A Python Tool for Processing and Visualizing WDF Spectral Data},
  year = {2024},
  institution = {University of Edinburgh},
  doi = {10.5281/zenodo.14470842},
  url = {https://github.com/Aradhye-sys/wdf_processor}
}
```

---

## Acknowledgments

- This project uses the `renishawWiRE` library, licensed under the MIT License.
- Special thanks to the University of Edinburgh for providing support and resources during the development of this tool.

---

## Contact

For inquiries, support, or collaboration, please contact:

**Prasad Aradhye**  
Email: P.Aradhye@sms.ed.ac.uk
University of Edinburgh  
