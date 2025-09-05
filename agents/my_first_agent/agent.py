import datetime

import random
from google.adk.agents import Agent
from google.adk.tools import google_search, AgentTool


def get_weather(city: str) -> dict:
    """Retrieves the current weather report for a specified city.

    Args:
        city (str): The name of the city for which to retrieve the weather report.

    Returns:
        dict: status and result or error msg.
    """
    conditions = ["sunny", "cloudy", "rainy", "snowy", "windy"]
    condition = random.choice(conditions)
    temp_celsius = random.randint(-10, 35)
    temp_fahrenheit = int(temp_celsius * 9 / 5 + 32)
    report = (
        f"The weather in {city.title()} is {condition} with a temperature of"
        f" {temp_celsius} degrees Celsius ({temp_fahrenheit} degrees Fahrenheit)."
    )
    return {"status": "success", "report": report}


def get_current_time() -> dict:
    """Returns the current server time and timezone.

    Returns:
        dict: status and result or error msg.
    """
    now = datetime.datetime.now().astimezone()
    report = f'The current server time is {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}'
    return {"status": "success", "report": report}


def get_stock_price(symbol: str) -> float:
    """Retrieves the current stock price for a given symbol.

    Args:
        symbol (str): The stock symbol (e.g., "GOOG").

    Returns:
        float: A random stock price.
    """
    return random.uniform(100.00, 400.00)


search_agent = Agent(
    name="search_agent",
    include_contents="none",
    model="gemini-2.5-flash",
    description="Professional search assistant with Google Search capabilities",
    instruction="Answer questions using Google Search when needed. Always cite sources.",
    tools=[google_search],
)

weather_time_stock_agent = Agent(
    name="weather_time_stock_agent",
    model="gemini-2.5-flash",
    description=(
        "Agent to answer questions about the current time, the weather in a city, and the latest stock price of a company."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about the time and weather in a city, and stock prices. If the user requests something you're not capable of supporting, transfer back to main_agent for dispatching to a more appropriate agent."
    ),
    tools=[get_weather, get_current_time, get_stock_price],
)

root_agent = Agent(
    name="root_agent",
    model="gemini-2.5-flash",
    description=("Agent that routes requests to the sub-agent best-suited to a task."),
    instruction=(
        "Use the tools at your disposal or any sub-agents to respond to the user's request."
    ),
    sub_agents=[weather_time_stock_agent],
    tools=[AgentTool(search_agent)],
)

# root_agent = search_agent
