# Polling Application

## Overview
This project is a web-based polling application that allows users to create polls, vote, and view real-time results. It's designed for ease of use and provides a secure platform for gathering opinions or feedback on any topic.

## Features
- **Poll Creation:** Users can create polls with custom questions and up to four options.
- **Voting System:** Participants can vote on polls, with mechanisms in place to ensure each user votes only once per poll.
- **Real-Time Results:** Instant feedback with visual charts displaying the poll outcomes.
- **Poll Management:** Administrators can manage, update, or delete polls.
- **Responsive Design:** Accessible on all devices, including desktops, tablets, and smartphones.

## Technology Stack
- **Frontend:** HTML5, CSS3, JavaScript
- **Backend:** Flask (Python), Jinja2
- **Database:** MongoDB
- **Libraries:** PyMongo, Flask-PyMongo, WTForms

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/polling-app.git
   ```
2. Navigate to the project directory:
   ```bash
   cd polling-app
   ```
3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Set up MongoDB:
   - Ensure MongoDB is installed and running on your machine.
   - Configure your MongoDB URI in the project settings.

6. Run the application:
   ```bash
   flask run
   ```
7. Access the application at `http://127.0.0.1:5000/`.

## Usage
- **Create Poll:** Go to the "Create Poll" page, enter your question and options, and submit.
- **Vote:** Select a poll, choose your option, and vote.
- **View Results:** Results are displayed immediately after voting.
- **Admin Management:** Admins can access poll management features.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any features or improvements.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.