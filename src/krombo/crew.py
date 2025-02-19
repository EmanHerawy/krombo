from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
# from krombo.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class Krombo():
	"""Krombo crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def security_auditor(self) -> Agent:
		return Agent(
			config=self.agents_config['security_auditor'],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True
		)

	@agent
	def sentiment_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['sentiment_analyst'],
			verbose=True
		)

	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
		)

	@task
	def sentiment_task(self) -> Task:
		return Task(
			config=self.tasks_config['sentiment_task'],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Krombo crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
