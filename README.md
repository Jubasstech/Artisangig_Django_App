# Artisangig_Django_App

# Artisangig Web App

The Artisangig Web App is a platform that connects customers with artisans, allowing customers to browse artisans' portfolios and communicate with them to place orders. The app facilitates the process of hiring artisans and provides a seamless experience for both customers and artisans.

## Features

- Customer Registration: Customers can register an account by providing their name, phone number, and address. A profile picture upload is mandatory for customers.

- Artisan Registration: Artisans can sign up by providing their personal details, such as name, phone number, address, and uploading a scanned copy of their NIM or Driver's License. They can also add their bank account number with BVN for payment disbursement purposes.

- Portfolio Upload: Artisans can upload their works, categorizing them based on different categories. They have the freedom to upload as many works as they desire.

- Order Placement: Customers can browse artisans' portfolios, select a desired work, and initiate a chat with the artisan via WhatsApp to place an order.

- Payment Integration: The app integrates with Paystack for secure and convenient payment processing. Customers can make payments to the app owner when placing orders, and payments are disbursed to the artisans upon completion of the gig.

## Technologies Used

- Django: Python web framework used for backend development.
- HTML/CSS: Frontend development for the web app.
- JavaScript: Used for dynamic frontend interactions.
- Paystack API: Integration for payment processing.
- PostgreSQL: Database management system for storing app data.

## Installation and Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/Artisangig.git

Navigate to the project directory:
cd Artisangig

Set up a virtual environment (optional but recommended):

python -m venv env
source env/bin/activate


Install the required dependencies:

pip install -r requirements.txt

Set up the database:
bash
Copy code
python manage.py migrate
Start the development server:
bash
Copy code
python manage.py runserver
Access the web app locally at http://localhost:8000.
Contributing
We welcome contributions to enhance the Artisangig Web App. To contribute, please follow these steps:
Fork the repository.
Create a new branch
git checkout -b feature/your-feature-name
Make your modifications and commit your changes
git commit -m "Add your commit message"
Push the changes to your forked repositoryas
git push origin feature/your-feature-name
Open a pull request, describing the changes you made.
Please ensure that your contributions adhere to the coding conventions and best practices followed in the project.
License
This project is licensed under the MIT License. See the LICENSE file for more details.
Author
Jerome Udoh

Contact
For any inquiries or support, please contact the project team at admin@jubass.com.ng
