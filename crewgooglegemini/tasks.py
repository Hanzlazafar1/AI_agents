from crewai import Task
from agents import researcher,news_writer
from tools import tool


researcher=Task(
    description=(
        "identify the next big trend in {topic}"
        "focus on identifying pros and cons and the overall narrative"
        "your final report should clearly articulate the key points"
        "it marketing opportunities ,and potential risks"
    ),
    expected_output="A comprehensive 3 Paragraphs long report on the latest ai trends",
    tools=[tool],
    agent=researcher,   
)

writer_task=Task(
    description=(
        "Compose an insightful article on {topic}"
        "focus on the latest trends and how it's impacting the industry"
        "this artice should be easy to understand ,engaging and positive."
        "it marketing opportunities ,and potential risks"
    ),
    expected_output=" A 4 Paragraph article on {topic} advancements formatted as markdown.",
    tools=[tool],
    agent=news_writer,   
    output_file="new-blog-post.md"
)