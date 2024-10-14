# Square Calculator

This is a simple Python application that calculates the square of a given number and prints it. The project also includes a test suite using `pytest` to ensure the functionality of the application.

## Table of Contents

- [Project Structure](#project-structure)
- [Setup](#setup)
- [Running the Application](#running-the-application)
- [Running the Tests](#running-the-tests)
- [GitHub Actions Workflow](#github-actions-workflow)

## Project Structure

```
your-repo/
├── .github/
│   └── workflows/
│       └── python-app.yml
├── square_calculator.py
└── test_square_calculator.py
```

- **square_calculator.py**: Contains the main application logic.
- **test_square_calculator.py**: Contains the test suite for the application.
- **.github/workflows/python-app.yml**: Contains the GitHub Actions workflow.

## Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
    ```

2. **Set up a virtual environment (optional but recommended)**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install --upgrade pip
    pip install pytest
    ```

## Running the Application

To run the application, execute the `square_calculator.py` script:

```bash
python square_calculator.py
```

You will be prompted to enter a number, and the application will print the square of the entered number.

## Running the Tests

To run the tests using `pytest`, execute the following command:

```bash
pytest test_square_calculator.py
```

This will run the test suite and provide a report of the test results.

## GitHub Actions Workflow

The project includes a GitHub Actions workflow (`.github/workflows/square_calculator.yml`) that automates the process of building, testing, and generating artifact attestations.


### Triggering the Workflow

The workflow is triggered on `workflow_dispatch` for demo purposes. 
