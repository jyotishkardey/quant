#pip install import-ipynb
import import_ipynb
import shutil
import os

## LIbraries
from phi.agent import Agent
from phi.model.google import Gemini

#Our Modules
from ai_stocks_fundamental_recommendations_analyzer import finance_team
from ai_swot_analyzer import swot_team
from ai_sentiment_analyzer import sentiment_team
from ai_settings import *


def delete_old_memory():
    # Path to the directory you want to delete
    folder_path = 'tmp'

    # Check if the folder exists
    if os.path.exists(folder_path):
        # Delete the folder and its contents
        shutil.rmtree(folder_path)
        print(f"Folder '{folder_path}' has been deleted.")
    else:
        print(f"Folder '{folder_path}' does not exist.")


#Delet old memory before training. So that it works on fresh data
delete_old_memory()

#pip install sqlalchemy
from phi.storage.agent.sqlite import SqlAgentStorage

# Create a storage backend using the Sqlite database
ram = SqlAgentStorage(
    # store sessions in the ai.sessions table
    table_name="agent_sessions",
    # db_file: Sqlite database file
    db_file="/tmp/stocks.db",
)

# Team of Agents
bot_agent = Agent(
    model=Gemini(id="gemini-2.0-flash-exp"),
    team=[sentiment_team, swot_team, finance_team],
    storage=ram,
    instructions=[
        "Combine the expertise of all agents to provide a cohesive, well-supported response."
    ],
    show_tool_calls=True,
    markdown=True,
)

print("Give Yahoo finance ticker names")
bot_agent.cli_app()
