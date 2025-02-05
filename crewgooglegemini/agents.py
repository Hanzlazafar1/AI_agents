
from langchain_google_genai import ChatGoogleGenerativeAI
from crewai import Agent
from tools import tool

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro",
                             verbose=True,
                             temperature=0.5,
                             goole_api_key="AIzaSyBTE8ia5AldxGUiLh-cs3_DoIDWNhDys8A")

# creating a senior researcher agent
researcher=Agent(
    role=" Senior Researcher",
    goal="Undercover ground breaking technologies in {topic}",
    verbose=True,
    memory=True,
    backstory=("Driven by curosity, you are at the forfront of"
               "innovation, eager to explore and shre abckend knowledgethat could change"
               "the world"
               ),


    tools=[tool],
    llm=llm,
    allow_delegation=True
)

## creating another agent with custom tools which is responsible in writing news blog
news_writer=Agent(
    role="Writer",
    goal="Narrate compelling tech stories about {topic}",
    verbose=True,
    memory=True,
    backstory=("with the flair for simplifying complex topics , you craft "
               "engagging narratives that captivate and educate ,bringing new "
               "dicoveries to light in an accessible manner"
               ),


    tools=[tool],
    llm=llm,
    allow_delegation=False
)