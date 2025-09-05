## Conversational Chatbot with Rasa

#### Description

This project introduces conversational AI agents using the Rasa framework. We build a simple chatbot that handles basic intents (greet, goodbye, ask_weather) and responds appropriately. The chatbot uses Rasa’s natural language understanding (NLU) to detect intents and rule-based dialogue management to generate responses.

#### Concepts Covered

Conversational AI: Agents that process user inputs and manage dialogue flows.
Rasa Framework: Open-source tool for NLU and dialogue management.
NLU Pipeline: Detects intents and entities from user text.
Dialogue Management: Uses rules or models to select context-aware responses.

#### Files

data/nlu.yml: Defines intents and example utterances.
data/rules.yml: Specifies dialogue rules for responses.
domain.yml: Lists intents, responses, and actions.
train_and_run.sh: Script to train and run the Rasa chatbot.

#### Instructions

Install Rasa: pip install rasa
Create a Rasa project: rasa init --no-prompt
Replace data/nlu.yml, data/rules.yml, and domain.yml with the provided files.
Run train_and_run.sh to train and test the chatbot interactively.
