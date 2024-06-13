# Django Data Analysis Web Application

This is a Django-based web application that allows users to upload CSV files, perform data analysis using pandas and numpy, and display the results and visualizations on the web interface.

## Features

- **File Upload**: Users can upload CSV files through a web form.
- **Data Analysis**: Basic data analysis is performed, including:
  - Displaying the first few rows of the data.
  - Calculating summary statistics (mean, median, standard deviation) for numerical columns.
  - Identifying and handling missing values.
- **Data Visualization**: Generates basic plots such as histograms for numerical columns using matplotlib and seaborn.
- **User Interface**: A simple and user-friendly interface to display data analysis results and visualizations.

## Setup Instructions

### Prerequisites

- Python 3.x
- Django 3.x
- pandas
- numpy
- matplotlib
- seaborn

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-name>
2. Create and activate a virtual environment:
   ```bash 
   python -m venv venv
   source venv/bin/activate
   # On Windows use `venv\Scripts\activate`
4. Install dependencies:
   ```bash
   pip install -r requirements.txt.
6. Apply migrations:
   ```bash
   python manage.py migrate
7. Run the development server:
   ```bash
   python manage.py runserver
   
