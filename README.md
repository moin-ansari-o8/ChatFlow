# ChatFlow
A Chatbot
<br>Author - Moin Ansari

## Overview

ChatBot is an interactive chatbot application built in Python that can handle various user intents such as greetings, time, date, and weather updates. This chatbot uses Natural Language Processing (NLP) to match user input with predefined patterns and provide appropriate responses. 

## Features

- **Conversational Chatbot**: Engage in interactive conversations with the chatbot. It is capable of understanding and responding to various user inputs.
- **Time Information**: Provides the current time upon request.
- **Date Information**: Gives today's date when asked.
- **Weather Information**: Retrieves and displays weather conditions for a specified location using web scraping.

## Installation

### Prerequisites

- Python 3.x
- Required Python libraries: `requests`, `beautifulsoup4`

### Steps

1. **Clone the repository:**

    ```bash
    git clone https://github.com/moin-ansari-o8/ChatFlow.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd ChatFlow
    ```

3. **Install required Python libraries:**

    ```bash
    pip install -r requirements.txt
    ```

   Ensure you have a `requirements.txt` file with the necessary libraries. If not, you can create it using:

    ```bash
    pip freeze > requirements.txt
    ```
4. **Run the application:**

    ```bash
    python chatMain.py
    ```
    
## Usage

To interact with the chatbot, run the program and type your messages. The chatbot will respond based on the intents and patterns defined in the `referenceConvo.json` file.

Example input and response:

- **Input**: `hi`
- **Response**: `Hello sir!`

## Contributing

We welcome contributions to improve the chatbot. If you'd like to contribute, please follow these steps:

1. **Fork the repository.**
2. **Create a new branch:**

    ```bash
    git checkout -b feature/your-feature
    ```

3. **Make your changes and commit:**

    ```bash
    git add .
    git commit -m "Add a feature"
    ```

4. **Push to the branch:**

    ```bash
    git push origin feature/your-feature
    ```

5. **Open a Pull Request** to the `main` branch of the original repository.

## Contact

For any questions or feedback, please contact:

- **Email**: your.email@example.com
- **GitHub**: [moin-ansari-o8](https://github.com/moin-ansari-o8)
## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.

