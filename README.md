# Airport Management System

Welcome to the Airport Management System, a comprehensive flight booking platform built using Python and MySQL. This system allows users to book, check, and cancel flight tickets with ease.

## Table of Contents


## Project Overview

The Airport Management System is designed to facilitate flight booking operations for users. The system includes functionalities for booking tickets, checking ticket details, and cancelling tickets. It also integrates a user-friendly graphical interface built using Tkinter.

## Features

- **User-friendly Interface:** Intuitive GUI for easy interaction.
- **Flight Booking:** Allows users to book tickets by selecting source, destination, and other details.
- **Ticket Checking:** Enables users to check ticket details using Ticket Number or Passport Number.
- **Ticket Cancellation:** Allows users to cancel booked tickets.
- **Database Integration:** Utilizes MySQL for storing and managing data.

## Installation

### Prerequisites

- Python 3.x
- MySQL
- Required Python packages (listed in `requirements.txt`)

### Steps

1. **Clone the Repository:**
    ```sh
    git clone https://tachyonGUY//airport-management-system.git
    cd airport-management-system
    ```

2. **Install Dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Set Up the Database:**
    - Create a MySQL database named `airline`.
    - Execute the SQL scripts provided in the `database` directory to set up the necessary tables and data.

4. **Run the Application:**
    ```sh
    python main.py
    ```

## Usage

1. **Home Page:**
   - Start the application to see the welcome screen.

2. **User Page:**
   - Navigate to the user page for booking, checking, and cancelling tickets.

3. **Book Ticket:**
   - Select source, destination, travel date, and class to book a ticket.
   - Enter passenger details to complete the booking.

4. **Check Ticket:**
   - Enter Ticket Number or Passport Number to retrieve and display ticket details.

5. **Cancel Ticket:**
   - Enter Ticket Number or Passport Number to view and cancel the ticket.

## Technologies Used

- **Python 3.x:** Main programming language.
- **Tkinter:** GUI library for creating the user interface.
- **MySQL:** Database for storing flight and user information.
- **Pillow:** For image processing and handling.
- **tkcalendar:** For date selection in the booking form.

## Contributing

We welcome contributions from the community! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

Please ensure your code follows the project's coding standards and is well-documented.

## Contact

For any questions or feedback, please contact:

- **Name:** Adarsh Singh
- **Email:** techsingh100@gmail.com
- **GitHub:** [tachyonGUY](https://github.com/tachyonGUY)

Thank you for using the Airport Management System!
