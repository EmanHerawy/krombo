from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
# from krombo.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
# from langchain_community.utilities import ArxivAPIWrapper

# Initialize tools
search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()
# research_tool = ArxivAPIWrapper()

@CrewBase
class Krombo():
	"""Krombo crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def wallet_blacklist_checker(self) -> Agent:
		return Agent(
			config=self.agents_config['wallet_blacklist_checker'],
			tools=[search_tool, scrape_tool],
			memory=True,
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True
		)

	@agent
	def transaction_behavior_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['transaction_behavior_analyst'],
			allow_delegation=True,
			memory=True,
			tools=[search_tool],
			verbose=True
		)
	@agent
	def sentiment_reputation_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['sentiment_reputation_analyst'],
			allow_delegation=True,
			memory=True,
			tools=[search_tool],
			verbose=True
		)
	@agent
	def risk_assessment_expert(self) -> Agent:
		return Agent(
			config=self.agents_config['risk_assessment_expert'],
			allow_delegation=True,
			memory=True,
			tools=[search_tool],
			verbose=True
		)



	@task
	def blacklist_check(self) -> Task:
		return Task(
			config=self.tasks_config['blacklist_check'],
		)

	@task
	def transaction_behavior_analysis(self) -> Task:
		return Task(
			config=self.tasks_config['transaction_behavior_analysis'],
		)

	@task
	def sentiment_check(self) -> Task:
		return Task(
			config=self.tasks_config['sentiment_check'],
		)

	@task
	def scam_likelihood_report(self) -> Task:
		return Task(
			config=self.tasks_config['scam_likelihood_report'],
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
