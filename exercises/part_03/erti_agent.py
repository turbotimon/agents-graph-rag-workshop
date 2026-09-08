"""Small example: a plain Pydantic AI agent with system instructions."""

from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider

MODEL_NAME = "qwen3.8:27b"
BASE_URL = "https://litellm.kube-ext.isc.heia-fr.ch/v1"
API_KEY = "sk-3QNnuNj3BB-m6F5ERA_w1g"

model = OpenAIChatModel(
    model_name=MODEL_NAME,
    provider=OpenAIProvider(
        base_url=BASE_URL,
        api_key=API_KEY,
    ),
)

agent = Agent(
    model=model,
    instructions="You are Erty, a friendly workshop assistant.",
)

def simple_agent(agent, question: str = "Hello, introduce yourself in one sentence."):
    answer = agent.run_sync(question)
    print(answer.output)

if __name__ == "__main__":
    simple_agent(agent)

