import os
from crewai_tools import SerperDevTool

# Correct way to set the API key
api_key = "ad649cab7769944c7ce63ca3c48e3cfd1fb97a64"  # Put your actual API key here

if api_key:  # Check if API key exists
    os.environ['SERPER_API_KEY'] = api_key
else:
    raise ValueError("SERPER_API_KEY is missing! Please set it correctly.")

# Initialize the tool
tool = SerperDevTool()
