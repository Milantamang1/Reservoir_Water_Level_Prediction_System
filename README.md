
# Reservoir Water Level Prediction

This project implements a **Reservoir Water Level Prediction System** using machine learning algorithms like LSTM (Long Short-Term Memory) and BiLSTM (Bidirectional LSTM). It is designed to help optimize hydroelectric power generation by forecasting reservoir water levels using historical and environmental data.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [System Workflow](#system-workflow)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The system predicts reservoir water levels by analyzing historical datasets, including rainfall, temperature, and past water levels. This aids in better planning and management of hydroelectric power generation.

## Features

- User-friendly interface built using Django framework.
- Input support in multiple formats: URL, Text, and PDF.
- Predictive model using advanced LSTM and BiLSTM networks.
- Admin functionality to summarize and rank prediction results.

## System Workflow

1. **Input**: User uploads data in one of the supported formats (URL, Text, or PDF).
2. **Processing**: The system preprocesses the data and applies the LSTM/BiLSTM models to make predictions.
3. **Output**: A summarized slide or report is generated showcasing the predictions.
4. **Admin Features**: Admins can execute additional pipelines to rank and compare predictions.

## Technologies Used

- **Backend**: Python, Django
- **Frontend**: HTML, CSS, JavaScript
- **Machine Learning Models**: LSTM, BiLSTM (implemented in TensorFlow/PyTorch)
- **Database**: SQLite/PostgreSQL

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd hydropower_3
   ```

2. Set up a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations to set up the database:

   ```bash
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

6. Open your browser and navigate to `http://127.0.0.1:8000/`.

## Usage

1. Upload data through the user interface.
2. View the predicted reservoir water levels in a graphical or tabular format.
3. Admins can log in to access advanced features for data ranking and summarization.

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature/bugfix: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m "Description of feature"`.
4. Push to the branch: `git push origin feature-name`.
5. Create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
