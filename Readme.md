# Krushak AI

**Krushak AI** is a smart chatbot designed to help farmers by answering agriculture-related questions. It brings all the important information farmers need into one place, making it easy to access and understand.

## Overview

Farmers often struggle to find the information they need because it is scattered across many websites and platforms. Many farmers are not even aware of government portals where they can get details about subsidies, loans, or farming equipment. Even when they know about these portals, the information is not well-organized in one place.

**Krushak AI** solves this problem by acting as a one-stop solution for all agriculture-related queries. It provides all the information farmers need and allows them to find answers quickly. To make things even easier, Krushak AI is deployed on WhatsApp, a platform many farmers are familiar with. This eliminates the need for browsing the internet, making data more accessible to those who prefer WhatsApp.

## Features

- **WhatsApp and Website Integration**  
  Krushak AI is available as a chatbot on WhatsApp and a website, ensuring easy access for farmers. The WhatsApp bot is particularly beneficial as many farmers are more comfortable using WhatsApp than browsers.

- **Weather Updates**  
  Provides real-time weather information to help farmers plan their agricultural activities effectively.

- **Region-Based Schemes and Subsidies**  
  By simply providing the name of their region, farmers can access a table with all relevant schemes, subsidies, and loan details. This feature uses pre-prompted sections to deliver organized and accurate data.

- **Crop Information by Name**  
  Farmers can get detailed information about any vegetable just by providing its name. The bot provides essential details such as the best season for cultivation, duration, and the type of soil required.

- **Voice Input on WhatsApp**  
  Utilizing WhatsApp's built-in voice-to-text feature, farmers can speak their queries, making it even easier for those unfamiliar with typing to interact with the bot.

- **Web Scraping for Comprehensive Data**  
  Krushak AI scrapes and consolidates information from across the internet, ensuring farmers receive all the relevant data in one place.

- **AI Capabilities**  
  The chatbot leverages Bard, Google's previous model of Gemini (now discontinued), to provide intelligent and contextually accurate responses to user queries.

## Installation

Follow these steps to set up and run the Krushak AI project locally:

### Prerequisites

1. Ensure you have Python installed (version 3.10 or later).
2. Install Django by running:
   ```bash
   pip install django
   ```

### Steps

1. **Clone the Repository**  
   Clone the Git repository to your local system:

   ```bash
   git clone https://github.com/Lava-Kumar-PL/krushak
   ```

2. **Create and Activate a Virtual Environment**

Create a virtual environment:

```bash
python -m venv env
```

Activate the environment:

- On Windows:
  ```bash
  env\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source env/bin/activate
  ```

3. Install Dependencies
   Use the requirements.txt file to install all required dependencies:

```bash
pip install -r requirements.txt
```

4.Set Up the Environment File

- Create an .env file in the project directory.
- Obtain the session ID for Bard (Google’s previous model of Gemini) by following the guide at [dsdanielpark/Bard-API](https://github.com/dsdanielpark/Bard-API).

- Add the session ID to the .env file as follows:

```makefile
SESSION_ID=<your_session_id>
```

5. Run the Server
   Change to the project directory and start the Django development server:

```bash
cd krushak
```

```bash
python manage.py runserver
```

6. Access the Application
   Open a browser and go to:

```
http://127.0.0.1:8000/
```

## Usage

1. Home Page

After starting the server, you’ll land on the home page. This page introduces you to Krushak AI and its features.

2. Navigation
   Use the navigation bar to switch between different pages, such as:

- **Chatbot**: Access the AI chatbot for agriculture-related queries.
- **Weather**: Check real-time weather updates.
- **Schemes**: View region-based schemes and subsidies.
- **Crop Info**: Get detailed information about vegetables by name.

## Results
  <img src="https://github.com/Lava-Kumar-PL/krushak/blob/main/result/krushak%20.gif" width="550" /> 
  
  <img src="https://github.com/Lava-Kumar-PL/krushak/blob/main/result/chat.png" width="400" />  
     
  <img src="https://github.com/Lava-Kumar-PL/krushak/blob/main/result/gov1.png" width="400" />  <img src="https://github.com/Lava-Kumar-PL/krushak/blob/main/result/gov2.png" width="400" /> !
