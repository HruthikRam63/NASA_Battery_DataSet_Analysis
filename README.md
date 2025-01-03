
* * *

NASA Battery Analysis
=====================

This project focuses on analyzing battery aging trends using a large dataset of battery test data. The analysis includes exploring key parameters such as **Battery Impedance**, **Electrolyte Resistance (Re)**, and **Charge Transfer Resistance (Rct)** across cycles of charge and discharge. The project leverages Python libraries for data manipulation, visualization, and trend analysis.

* * *

Project Directory Structure
---------------------------

bash

Copy code

```
NASA-Battery-Analysis/
├── cleaned_dataset/                 # Folder containing cleaned dataset and metadata
│   ├── data/                        # Folder containing all 7565 CSV files
│   └── metadata.csv                 # Metadata CSV file with battery attributes
├── notebooks/                       # Jupyter Notebooks for exploratory analysis
│   └── exploratory_analysis.ipynb   # Jupyter Notebook for data exploration
├── output/                          # Folder to store generated outputs
│   └── figures/                     # Generated plot figures saved as HTML files
├── src/                             # Source code for the analysis
│   ├── __init__.py                  # Package initialization (optional)
│   ├── data_loader.py               # Functions to load and preprocess data
│   ├── plot_generator.py            # Functions to create visualizations
│   └── main.py                      # Main script to run the analysis
├── requirements.txt                 # Python dependencies for the project
└── README.md                        # Documentation for the project
```
* * *
## Installation and Setup

### Prerequisites

* Python 3.10 or higher
* Ensure `pip` is installed and updated

### Installation Steps

1. **Clone this repository:**
    ```bash
    git clone <repository_url>
    cd NASA-Battery-Analysis
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the main analysis script:**
    ```bash
    python src/main.py
    ```

4. **Open the exploratory notebook:**
    ```bash
    jupyter notebook notebooks/exploratory_analysis.ipynb
    ```

* * *

Features and Workflow
---------------------

### 1\. **Data Loading and Preprocessing**

*   The `data_loader.py` script loads the metadata (`metadata.csv`) and processes 7565 individual CSV files.
*   Handles missing values by replacing them with column means.
*   Merges relevant parameters (`Re`, `Rct`, `Battery Impedance`) into a consolidated DataFrame.

### 2\. **Exploratory Data Analysis**

*   **Notebook**: `notebooks/exploratory_analysis.ipynb`
*   Key visualizations:
    *   Ambient Temperature Distribution
    *   Battery Capacity Trends
    *   Correlation Heatmaps
    *   Voltage and Resistance Trends

### 3\. **Visualization of Trends**

*   **Main Script**: `src/main.py`
*   Plots generated:
    *   **Battery Impedance vs Cycles**
    *   **Electrolyte Resistance (Re) vs Cycles**
    *   **Charge Transfer Resistance (Rct) vs Cycles**
*   Interactive plots are saved in the `output/figures/` directory as HTML files.

* * *

Outputs
-------

*   HTML files for visualizations:
    *   `Battery_Impedance.html`
    *   `Re.html`
    *   `Rct.html`
*   Explore trends across battery aging cycles with interactive visualizations.

* * *

Known Issues
------------

*   Empty plots in `notebooks/exploratory_analysis.ipynb` or `output/figures/` may occur due to missing or improperly handled data. Ensure the `metadata.csv` and corresponding files are consistent and complete.
*   Verify file paths if running on different environments.

* * *

Dependencies
------------

All dependencies are listed in `requirements.txt`. Install them using:
```bash
pip install -r requirements.txt
```
* * *

Contributions
-------------

This project is structured for academic and research purposes. Feel free to contribute by submitting pull requests or reporting issues.

* * *
