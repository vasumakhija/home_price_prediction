# Home Price Prediction



This project is a web-based application that predicts house prices based on user inputs such as location, square footage, number of bedrooms (BHK), and bathrooms. The application uses a machine learning model to estimate prices based on historical housing data.

---

## Table of Contents

- Features
- [Technologies Used](#technologies-used)
- [File Structure](#file-structure)
- [Setup and Installation](#setup-and-installation)
- [How to Use](#how-to-use)

---

## Features

- Predicts home prices based on location, size, and features.
- User-friendly interface to input house details.
- Real-time prediction using a pre-trained model.
- Location dropdown dynamically populated from the dataset.

---

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask
- **Machine Learning**: Python, scikit-learn, pickle
- **Data Handling**: NumPy, JSON
- **Deployment**: Nginx, REST API

---

## File Structure

1. **`app.js`**:

   - Contains the JavaScript logic for the user interface.
   - Handles events like button clicks and page load.
   - Sends user inputs to the backend API and displays predictions.

2. **`server.py`**:

   - Flask server hosting the API endpoints.
   - Endpoints:
     - `/get_location_names`: Returns available locations.
     - `/predict_home_price`: Predicts the price based on user inputs.

3. **`util.py`**:

   - Core utility functions:
     - Loads saved model and column artifacts.
     - Provides location names.
     - Predicts house prices based on input features.

4. **Machine Learning Artifacts**:

   - `columns.json`: Contains metadata about model input features.
   - `bangalore_home_price_model.pickle`: Trained ML model.

5. **Frontend Files**:

   - HTML and CSS files for the user interface.

---

## Setup and Installation

### Prerequisites

- Python 3.7 or later
- Flask
- npm (for serving static files if needed)

### Steps

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd home-price-prediction
   ```

2. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Start the Flask server:

   ```bash
   python server.py
   ```

4. If using Nginx for deployment, start the Nginx server. Refer to your Nginx configuration for details.

5. Access the web application at `http://127.0.0.1:5000`.

6. Ensure the model artifacts (`columns.json` and `bangalore_home_price_model.pickle`) are in the `aartifacts` directory.

---

## How to Use

1. Open the application in your web browser.
2. Enter the details of the house:
   - **Location**: Select from the dropdown.
   - **Total Area (sq. ft)**: Enter the size of the house.
   - **BHK**: Select the number of bedrooms.
   - **Bathrooms**: Select the number of bathrooms.
3. Click the **Estimate Price** button.
4. View the estimated price displayed in the interface.

