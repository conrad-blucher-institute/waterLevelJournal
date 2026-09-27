# Exploring Deep Learning Methods for Short-Term Tide Gauge Water Level Predictions

This repository contains the dataset and code associated with the paper:

**Vicens-Miquel, M., Tissot, P. E., & Medrano, F. A. (2024).  
"Exploring Deep Learning Methods for Short-Term Tide Gauge Water Level Predictions."  
*Water*, 16(20), 2886.**  
https://doi.org/10.3390/w16202886

## Overview

This study investigates deep learning methods for short-term water level
prediction at tide gauge stations along the Texas coast. The study evaluates
multiple deep learning architectures for operational coastal water level
forecasting across locations with different coastal and metocean conditions.

This repository provides the processed dataset used in the study. The dataset
combines 6-minute water-level and meteorological observations from NOAA Tides
and Currents and the Texas Coastal Ocean Observation Network (TCOON).

## Study Locations

The dataset includes four tide gauge stations along the Texas Gulf Coast:

| Station | Years | Location Type |
|---|---|---|
| Bob Hall Pier | 2008–2012 | Gulf of Mexico / open coast |
| Port Isabel | 2007, 2009–2012 | Inland / ship channel |
| Rockport | 2009–2013 | Bay |
| North Jetty | 2012–2014, 2016, 2018 | Gulf of Mexico / jetty |

The stations represent different coastal environments and water-level
variability along the Texas coast.

## Dataset

The dataset combines observations from:

- **NOAA Tides and Currents**
- **Texas Coastal Ocean Observation Network (TCOON)**

The original observations have a temporal resolution of **6 minutes**.

The dataset includes:

- Water level
- Harmonic tidal prediction
- Surge
- Wind speed
- Wind direction
- Alongshore wind component
- Across-shore wind component

Surge is defined as:

> **Surge = Observed Water Level − Harmonic Prediction**

The study uses surge as the prediction target. The harmonic tidal component is
removed before model training and added back to the predicted surge to
reconstruct total water level.

## Data Preprocessing

The dataset was quality controlled and gap-filled prior to its use for machine
learning.

Years were selected such that fewer than 2% of the 6-minute observations were
missing across the variables considered in the study.

Short gaps were defined as:

- Up to **3 hours** for surge
- Up to **1 hour** for wind

Short gaps were filled using linear interpolation based on averages of the five
6-minute observations immediately before and after each gap.

Longer gaps in the TCOON wind records were filled using corresponding NOAA wind
observations when available, with a correction applied to account for
differences between the two datasets.

For complete details on data selection, quality control, gap filling, and
validation, please refer to the associated publication.

## Citation

If you use this dataset or code, please cite:

```bibtex
@article{vicensmiquel2024waterlevel,
  title={Exploring Deep Learning Methods for Short-Term Tide Gauge Water Level Predictions},
  author={Vicens-Miquel, Marina and Tissot, Philippe E. and Medrano, F. Antonio},
  journal={Water},
  volume={16},
  number={20},
  pages={2886},
  year={2024},
  doi={10.3390/w16202886}
}
