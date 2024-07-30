# Cryptocurrency Payment Gateway using Django
This project implements a Cryptocurrency Payment Gateway using Django. The application's frontend is styled using Bootstrap. Built a payment gateway that enabled merchants to accept cryptocurrency payments. Integrated Web3.py for processing transactions on the Ethereum network. Ensured security and efficiency in transaction handling.

## Installation

To run this project on your local machine, follow the steps below:

### Prerequisites

Ensure you have the following installed on your local machine:

- Python 3.8 or higher
- Web3.py
- Ethereum
- Solidity
- Django
- Redis

### Setup

1. Clone the repository:
    ```
    git clone https://github.com/farrukhrazzaqbutt/Cryptocurrency-Payment-Gateway.git
    ```

### Server

1. Install Django and other dependencies:
    ```
    pip install -r requirements.txt
    ```
2. Run the Migrations:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
3. Run the server:
    ```
    python manage.py runserver
    ```
Now, your application should be running at `localhost:8000`.