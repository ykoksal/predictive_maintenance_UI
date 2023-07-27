# Predictive Maintenance Analytics Platform

## Description

This is a web application for analyzing data in a predictive maintenance project. It runs on the Flask framework 
and developed with Python 3.10 using [AdminLTE](https://adminlte.io/) templates. It includes;
- a dashboard for operational time and durations by stop types,
- an interactive dashboard for IoT sensor time series data of production lines,
- an interactive dashboard for machine failure probabilities within a given time.

  Here is a sample deployment I made on heroku, but the language is in Turkish:
  https://kora-demo.herokuapp.com/#

## Requirements

- Python 3.10.x
- Internet connection (some libraries are CDN-hosted)

## Setup

1. Download the project files or clone the repository to your local machine.
2. Open your terminal/command prompt and navigate to the project directory:

```cd path/to/project-directory```

3. (Optional) Set up a virtual environment:

```python -m venv venv```

Activate the virtual environment:

- On Windows:
  ```
  venv\Scripts\activate
  ```

- On macOS/Linux:
  ```
  source venv/bin/activate
  ```
  
4. Install the required libraries:

```pip install -r requirements.txt```

5. Run the Flask application:

```python app.py```

6. Open your web browser and navigate to `http://localhost:5000/` to access the application.


