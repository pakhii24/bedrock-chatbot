# AI Chatbot using Amazon Bedrock

A conversational AI chatbot built using Amazon Bedrock and Claude Sonnet 4, with a Streamlit web interface.

## Architecture
User → Streamlit UI → Python (boto3) → Amazon Bedrock → Claude Sonnet 4

## Services Used
- Amazon Bedrock (Converse API)
- Anthropic Claude Sonnet 4
- Python 3.11
- Streamlit

## How to Run
1. Install dependencies: pip install boto3 streamlit
2. Configure AWS: aws configure
3. Run the app: python -m streamlit run chatbot.py

## Features
- Multi-turn conversation with memory
- Powered by Claude Sonnet 4 via Amazon Bedrock
- Clean chat UI built with Streamlit
- Maintains full conversation history

## AWS Region
us-east-1 (N. Virginia)

## Author
Pakhi Singh