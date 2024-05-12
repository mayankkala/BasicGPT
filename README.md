##BasicGPT
---
## Overview
This project is an AI-powered chatbot that provides weather information based on user queries in English language. It utilizes OpenAI API for natural language processing, Groq API for weather data retrieval, and integrates with ChatGPT for enhanced conversational capabilities.

## Features
- **Natural Language Processing:** Understands English queries for weather information.
- **API Integration:** Utilizes OpenAI API for language processing and Groq API for weather data.
- **ChatGPT Integration:** Enhances conversational experience with ChatGPT's capabilities.
- **Function Calling:** Weather information is retrieved through function calls in AI.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/weather-ai-chatbot.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Obtain API keys:
   - OpenAI API Key: [Get your key here](https://openai.com/)
   - Groq API Key: [Get your key here](https://groq.io/)
   - ChatGPT API Key: [Get your key here](https://chat.openai.com/)
2. Set your API keys:
   - OpenAI API Key:
     ```bash
     export OPENAI_API_KEY="your-openai-api-key"
     ```
   - Groq API Key:
     ```bash
     export GROQ_API_KEY="your-groq-api-key"
     ```
   - ChatGPT API Key:
     ```bash
     export CHATGPT_API_KEY="your-chatgpt-api-key"
     ```
3. Run the application:
   ```bash
   python app.py
   ```
4. Access the chatbot at `http://localhost:5000` in your web browser.

## API References
- [OpenAI API Documentation](https://beta.openai.com/docs/)
- [Groq API Documentation](https://groq.io/docs/)
- [ChatGPT API Documentation](https://beta.openai.com/docs/)

## Contributing
Contributions are welcome! Please follow the [contribution guidelines](CONTRIBUTING.md).

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
