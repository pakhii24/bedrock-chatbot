import boto3
import streamlit as st

# AWS Bedrock client
client = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1"
)

MODEL_ID = "us.anthropic.claude-sonnet-4-20250514-v1:0"

# Page config
st.set_page_config(page_title="My AI Chatbot", page_icon="🤖")
st.title("🤖 AI Chatbot")
st.caption("Powered by Amazon Bedrock + Claude")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask me anything..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Build message history for Bedrock
    bedrock_messages = [
        {"role": m["role"], "content": [{"text": m["content"]}]}
        for m in st.session_state.messages
    ]

    # Call Bedrock Converse API
    response = client.converse(
        modelId=MODEL_ID,
        system=[{"text": "You are a helpful AI assistant. Be friendly, clear and concise."}],
        messages=bedrock_messages
    )

    # Get response text
    reply = response["output"]["message"]["content"][0]["text"]

    # Display and save assistant response
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)