from browser_use.agent.service import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr
import os
import asyncio


async def siteValidation():
    os.environ["GEMINI_API_KEY"] = "AIzaSyD3HZJpM9X4ayKEwqmdXPKJL0wxe9nHa-0"
    os.environ["ANONYMIZED_TELEMETRY"] = "false"
    task = (
        'Important: I am UI Automation tester validating the tasks'
        'Open Website http://rahulshettyacademy.com/seleniumPractise/'
        'Select first two product and add them to cart'
        'Then print the total value of the cart'
    )

    api_key = os.environ.get("GEMINI_API_KEY")

    llm = ChatGoogleGenerativeAI(model="gemini-2.0-pro-exp-02-05", api_key= SecretStr(api_key))
    agent = Agent(task, llm, use_vision=True)
    history = await agent.run()
    test_result = history.final_result()
    print(test_result)


if __name__ == "__main__":
    asyncio.run(siteValidation())