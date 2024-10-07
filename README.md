# Ragas Critic Model Serverless Setup

## Overview
This project sets up a serverless Flask application using the Ragas Critic Model instead of GPT-4. The application generates text based on input prompts and uses the Hugging Face API for model inference.

## Requirements
- Docker
- Vessl Account

## Setup Instructions

1. **Clone the repository** or download the files.
2. **Set Environment Variables**:
   - Set the Hugging Face token:
     ```bash
     export HUGGINGFACE_HUB_TOKEN="your_huggingface_api_token"
     ```
   - Set the model ID:
     ```bash
     export MODEL_ID="explodinggradients/Ragas-critic-llm-Qwen1.5-GPTQ"
     ```

3. **Build the Docker image**:
   ```bash
   docker build -t ragas-critic-model .
