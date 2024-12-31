# software-development-project
Sprint 4 - Software Development Tools: Project

# Software Development Project

# Vehicle Data Explorer

This project is a Streamlit web app designed to explore and analyze vehicle data interactively. It provides tools for visualizing the dataset with histograms and scatter plots, as well as toggling visualizations based on user inputs.

## Features
- Interactive Histogram: Explore price distribution across different parameters.
- Scatter Plot: Visualize the relationship between vehicle mileage (odometer) and price.
- Dynamic Checkboxes: Toggle visualizations on and off to customize your exploration.
- Web Deployment: Hosted on Render for easy access.

## Technologies and Libraries Used
- **Python**: Core programming language.
- **Pandas**: For data manipulation and analysis.
- **Plotly Express**: For creating interactive visualizations.
- **Streamlit**: To build the interactive web app.

## Project Demo
- Access the live web app here: https://software-development-project-514o.onrender.com


## Setting Up the Environment

To replicate the environment used for this project and run locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/Ajlaaa12/software-development-project.git
   cd software-development-project
2. Create the Conda environment:
   Install Conda if you don't already have it
   conda env create -f environment.yml
3. Activate the environment:
   conda activate myenv
4. Run the application or scripts as needed
   streamlit run app.py
   Add and commit the changes:
   ```bash
   git add README.md
   git commit -m "Update README with environment setup instructions"
   git push origin main

## File Structure
- app.py: The main Python script for the Streamlit application.
- vehicles_us.csv: The dataset used for analysis and visualization.
- .streamlit/config.toml: Configuration file for Streamlit deployment.
- environment.yml: Environment configuration for Conda.
- requirements.txt: List of Python dependencies for the app.
- notebooks/: Jupyter notebooks for exploratory data analysis (EDA).

## Deployment on Render
- This project has been deployed on Render
- To replicate the deployment
   - Add the following files to the project root:
      - requirements.txt: Include all the required Python libraries
      - .streamlit/config.toml: Add the configuration below:
         - [server]
           headless = true
           port = 10000

           [browser]
           serverAddress = "0.0.0.0"
           serverPort = 10000
   - Push the changes to the repository
   - Link the repository to Render and configure it to use streamlit run app.py as the start command

# Contributions are welcome! Follow these steps:
- Fork the repository
- Create a feature branch:
   - git checkout -b feature-name
- Commit your changes:
   - git commit -m "Add feature description"
- Push to your forked repository and create a pull request