# langchain-bedrock-chainlit
Simple Chat UI using Large Language Model via AWS Bedrock, LangChain and Chainlit

### Tech stack being used
- LLMs from [Bedrock](https://aws.amazon.com/bedrock/) website.
- [LangChain](https://www.langchain.com/) as a Framework for LLM
- [LangSmith](https://smith.langchain.com/) for developing, collaborating, testing, deploying, and monitoring LLM applications.
- [Chainlit](https://docs.chainlit.io/langchain) for deploying.

## System Requirements

You must have Python 3.10 or later installed. Earlier versions of python may not compile.

## Steps to Replicate 

1. Fork this repository (optional) and clone it locally.
   ```
   git clone https://github.com/sudarshan-koirala/langchain-bedrock-chainlit.git
   cd langchain-bedrock-chainlit
   ```

2. Create a virtualenv and activate it.
   ```
   python3 -m venv .venv && source .venv/bin/activate
   ```

3. OPTIONAL - Rename example.env to .env with `cp example.env .env`and input the environment variables from [LangSmith](https://smith.langchain.com/). You need to create an account in LangSmith website if you haven't already. Also, you need to set your aws profile, you can follow this [link](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html). First, you need to install the aws cli and configure aws profile.
   ``` 
   LANGCHAIN_TRACING_V2=true
   LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
   LANGCHAIN_API_KEY="your-api-key"
   LANGCHAIN_PROJECT="your-project"
   ```

4. Run the following command in the terminal to install necessary python packages:
   ```
   pip install -r requirements.txt
   ```

5. Run the following command in your terminal to start the chat UI:
   ```
   chainlit run langchain_bedrock_chainlit.py
   ```

## Disclaimer
This is test project and is presented in my youtube video to learn new stuffs. It is not meant to be used in production as it's not production ready. You can modify the code and use for your usecases ✌️
