# autoPOTS Demonstration

This is the analysis used in the publication "Fully automated sample processing and analysis workflow for low-input proteome profiling" by Liang et al. with the Kelly lab at Brigham Young University. 

## Publication
Fully Automated Sample Processing and Analysis Workflow for Low-Input Proteome Profiling
Yiran Liang, Hayden Acor, Michaela A. McCown, Andikan J. Nwosu, Hannah Boekweg, Nathaniel B. Axtell, Thy Truong, Yongzheng Cong, Samuel H. Payne, and Ryan T. Kelly
Analytical Chemistry Article ASAP
DOI: 10.1021/acs.analchem.0c04240 

## Repository contents
This repository contains all information, data and code necessary to replicate the analyses in the manuscript. The file names are intentionally self explanatory, but are briefly reviewed below.

* ~/data - a folder that contains data files or url to data files

* Quantitative_QC.ipynb - a jupyter notebook that checks the quality of the lymphocyte data and generates figure 5a
* B_cells_versus_T_cells.ipynb - a jupyter notebook containing code comparing B cells to T cells; generates figure 5b and Suplementary Information on distinguishing proteins.
* GSEA_ALL.ipynb - a jupyter notebook that performs Gene Set Enrichment Analysis on the proteins identified. Used in generating figure 5c.

* Normalization.ipynb - a jupyter notebook demonstrating our normalization method. 
* PCA.ipynb - a jupyter notebook that creates a PCA plot of the lymphocytes by type. This figure demonstrates the grouping by type much like the correlations shown in Quantitative_QC.ipynb and is not used in the publication.

* load_data.py - a python script containing all code required for parsing data files and loading them into data frames.
* data_utils.py - a python script containing functions that are used in several notebooks to manipulate the dataset.
* plot_utils.py - a python script containing graphing functions used in multiple notebooks

* data.md  explains how data files in the repository relate to the supplemental tables from the manuscript
* data_descriptor.ipynb demonstrates how to use the methods in load_data.py, and describes the resulting dataframes.
* LICENSE.md
* README.md 

## Contact
