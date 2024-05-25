#from langchain_groq import ChatGroq
from langchain_community.llms import Bedrock
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable import Runnable
from langchain.schema.runnable.config import RunnableConfig

import chainlit as cl


@cl.on_chat_start
async def on_chat_start():
    
    await cl.Message(content="Hello there, I am Titan LLM from AWS Bedrock. How can I help you ?").send()

    #model = ChatGroq(temperature=0,model_name="llama3-70b-8192")
    
    model = Bedrock(
    credentials_profile_name="youtube", model_id="amazon.titan-text-express-v1"
)
    
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You're a very knowledgeable assistant. Please provide answer responsibly.",
            ),
            ("human", "{question}"),
        ]
    )
    runnable = prompt | model | StrOutputParser()
    cl.user_session.set("runnable", runnable)


@cl.on_message
async def on_message(message: cl.Message):
    runnable = cl.user_session.get("runnable")  # type: Runnable

    msg = cl.Message(content="")

    async for chunk in runnable.astream(
        {"question": message.content},
        config=RunnableConfig(callbacks=[cl.LangchainCallbackHandler()]),
    ):
        await msg.stream_token(chunk)

    await msg.send()
