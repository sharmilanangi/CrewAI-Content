from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai import LLM
import os

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators


@CrewBase
class ContentCreationCrew:
    """Content Creation Crew"""

    agents: List[BaseAgent]
    tasks: List[Task]
    
    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    def __init__(self):
        # Initialize the LLM here
        print(os.getenv("GROQ_API_KEY"))
        print("--------------------------------")
        self.llm = LLM(model="groq/llama-3.3-70b-versatile")

    # If you would lik to add tools to your crew, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def content_analyzer(self) -> Agent:
        return Agent(
            config=self.agents_config["content_analyzer"],  # type: ignore[index]
            llm=self.llm
        )

    @agent
    def content_creator(self) -> Agent:
        return Agent(
            config=self.agents_config["content_creator"],  # type: ignore[index]
            llm=self.llm
        )
    
     # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def analyze_content_task(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_content"],
        )
    
    @task
    def create_content_task(self) -> Task:
        return Task(
            config=self.tasks_config["create_content"], 
            context=[self.analyze_content_task()]
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the Research Crew"""
        
        # Create and return the crew
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
