# Indoor Plant E-commerce Platform

## Overview
This is a full-featured e-commerce platform for selling indoor plants, developed using Python and the Django framework. The platform offers a seamless shopping experience with secure user authentication, a robust shopping cart system, and integrated payment processing through Razorpay.

## Features
- **Frontend:** Developed using HTML, CSS, Bootstrap, and JavaScript.
- **Backend:** Powered by Django.
- **User Authentication:** Secure OTP (One-Time Password) verification for user signup and login.
- **Shopping Cart:** Add, remove, and manage items with ease.
- **Payment Gateway:** Seamless transactions through Razorpay.

## Installation

### Prerequisites
- Python 3.x
- Django 3.x
- Razorpay API keys

### Steps

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/plant-ecommerce.git
    cd plant-ecommerce
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Configure environment variables:**
    Create a `.env` file in the project root directory and add your Razorpay API keys and other environment variables:
    ```
    RAZORPAY_KEY_ID=your_key_id
    RAZORPAY_KEY_SECRET=your_key_secret
    ```

6. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7. **Access the application:**
    Open your browser and go to `http://127.0.0.1:8000/`

## Usage

### User Authentication
- Users can sign up and log in using OTP verification.
- Secure user data handling.

### Shopping Cart
- Browse and select plants to add to the cart.
- Manage cart items (add/remove).
- Proceed to checkout for payment.

### Payment Processing
- Integration with Razorpay for secure and seamless transactions.
- Users can pay for their orders directly through the platform.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.

## License
This project is licensed under the MIT License.

## Contact
For any inquiries or support, please contact [your email].

---

Developed by [Your Name]
