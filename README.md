# Sensor Fault Detection

This project is a **Sensor Fault Detection System** that predicts whether a wafer is **good** or **bad** based on wafer and sensor data. The application runs **locally** and provides routes for training a machine learning model and making predictions.

## Features

- **Home Route (`/`)**: Displays a welcome message: `"Welcome to my application"`.
- **Train Route (`/train`)**: Trains the machine learning model using wafer and sensor data.
- **Predict Route (`/predict`)**: Accepts a test file, processes the data, and returns a prediction file indicating whether each wafer is good or bad.

## Installation

1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd sensor-fault-detection
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

### Running the Application
Start the application locally:
```sh
python app.py
```
By default, it runs on `http://127.0.0.1:5000/`.

### API Endpoints

#### 1. Home Route (`/`)
- **Method**: `GET`
- **Response**: `"Welcome to my application"`

#### 2. Train Route (`/train`)
- **Method**: `GET`
- **Response**: `"Model training completed successfully!"` (or an error message)

#### 3. Predict Route (`/predict`)
- **Method**: `POST`
- **Input**: A CSV file containing test wafer data.
- **Response**: A downloadable prediction file (`predictions.csv`) with wafer classification as **good** or **bad**.
