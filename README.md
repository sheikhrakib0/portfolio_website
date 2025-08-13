
# Welcome To My Personal Portfolio

This is a personal portfolio website. This website is made with HTML, CSS, and JS. 
This is a personal portfolio website that also includes a machine learning model.


**Live Frontend:** [https://sheikhrakib.netlify.app/](https://sheikhrakib.netlify.app/)

## Project Architecture

This project has a decoupled architecture:

*   **Frontend:** A static website built with HTML, CSS, and vanilla JavaScript. It is hosted on Netlify. The `stroke.html` page contains a form that sends a request to the machine learning backend.
*   **Backend:** A Python web server built with Flask. It exposes a `/predict` API endpoint that uses a pre-trained `scikit-learn` model to make predictions based on the data submitted from the frontend.

---

## Backend Setup & Dependencies

The backend is powered by Python and several data science libraries.

### Dependencies

The project's Python dependencies are listed in `requirements.txt`:

*   flask
*   joblib
*   pandas
*   numpy
*   scikit-learn
*   gunicorn
*   flask_cors

### Installation

To install the necessary dependencies, navigate to the project directory in your terminal and run:

```bash
pip install -r requirements.txt
```

---

## Running the Backend Locally

To run the Flask server on your local machine, use the following command:

```bash
flask run
```

The server will start, and you can now use the form on the `stroke.html` page (if opened as a local file) to send requests to your local backend, provided you have also updated the `fetch` URL to be a relative path.