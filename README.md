
# CO2 Emissions Dashboard

## Overview

This project is an interactive dashboard for **comparing CO2 emissions across countries and sectors** using historical data. Built with **Dash** and **Plotly**, it provides dynamic visualizations to analyze trends and insights effectively.

## Features

- **Bar Chart**: CO2 emissions by country and sector for the latest year.
- **Line Chart**: CO2 emissions trends over time for different countries.
- **Dropdown Filter**: Select countries to filter data dynamically.

## Dataset

The dashboard uses a dataset named `historical_emissions.csv`, which includes:
- **Country**: Name of the country.
- **Sector**: Emission sectors (e.g., Energy, Agriculture).
- **Gas**: Type of gas (e.g., CO2, CH4).
- **Yearly Data (1990–2018)**: CO2 emissions per year.

## Installation

### Prerequisites
Install Python and the required libraries:
```bash
pip install dash pandas plotly
```

### File Setup
1. Place the dataset in the project directory as `historical_emissions.csv`.
2. Save the project script as `app.py`.

## Usage

1. Run the application:
   ```bash
   python app.py
   ```
2. Open the app in your browser at `http://127.0.0.1:8050/`.

## Visualizations

### 1. Bar Chart
Displays CO2 emissions by country and sector for the most recent year.

### 2. Line Chart
Shows CO2 emissions trends over time for different countries.

## Project Structure

```
.
├── app.py                
├── historical_emissions.csv  
└── README.md             
```

## Future Enhancements

- Add sector and gas filters.
- Implement additional chart types like stacked bar charts or heatmaps.
- Optimize performance for large datasets.

