from crewai import Crew 
from crewai import Process
from tasks  import writer_task,researcher
from agents import researcher,news_writer

crew=Crew(
    agents=[researcher,news_writer],
    tasks=[writer_task,researcher],
    process=Process.sequential,

)

result=crew.kickoff(inputs={'topic':'AI in healthcare'})
print(result)