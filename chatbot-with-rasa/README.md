## Conversational Chatbot with Rasa

#### Description

This project builds a conversational AI agent using the Rasa framework. We build a simple chatbot that handles basic intents (greet, goodbye, ask_weather) and responds appropriately. The chatbot uses Rasa’s natural language understanding (NLU) to detect intents and rule-based dialogue management to generate responses. It starts with a terminal-based chatbot and extends to a web interface using HTML and JavaScript, connected via Rasa’s REST API.

#### Concepts Covered

Conversational AI: Agents that process user inputs and manage dialogue flows.
Rasa Framework: Open-source tool for NLU and dialogue management.
NLU Pipeline: Detects intents and entities from user text.
Dialogue Management: Uses rules or models to select context-aware responses.
Rasa REST API: Enables communication with external clients (e.g., web interfaces).
Web Interface: Uses HTML/CSS for structure/styling and JavaScript for API calls.

#### Files

data/nlu.yml: Defines intents and example utterances.
data/rules.yml: Specifies dialogue rules for responses.
domain.yml: Lists intents, responses, and actions.
endpoints.yml: Configures Rasa’s REST API endpoint.
index.html: Web interface for interacting with the chatbot.
train_and_run.sh: Script to train and run the Rasa server with REST API.

#### Instructions

1. Install dependencies: pip install rasa 
2. Place all files in your_project folder. (replace with name of your folder)
3. Make train_and_run.sh executable: chmod +x train_and_run.sh 
4. Run ./train_and_run.sh to train and start the Rasa server. 
5. Test in terminal: Interact directly after the server starts. 
6. Test in web: Open index.html in a browser (e.g., via python -m http.server and visit http://localhost:8000/your_project/index.html).

#### Example Interactions

Input: “hi” → Response: “Hello! How can I assist you today?”
Input: “what’s the weather like?” → Response: “It’s sunny and warm today! Perfect for a walk.”
Input: “bye” → Response: “Goodbye! Have a great day!”