#!/usr/bin/env python
from random import randint

from pydantic import BaseModel

from crewai.flow import Flow, listen, start

# from crews.content_crew.content_crew import ContentCreationCrew
from .crews.content_crew.content_crew import ContentCreationCrew

class ContentCreationState(BaseModel):
    user_persona: str = "organizer" # This could also be a persona - Organizer or the customer
    social_media_platform: str = "linkedin" # This could be any platform like twitter, facebook, instagram, etc.
    transcript: str = ""
    highlighted_points: list[str] = []
    user_opinion: str = ""
    event_name: str = ""

class ContentCreationFlow(Flow[ContentCreationState]):

    @start()
    def generate_content(self):
        print("Generating content for", self.state.social_media_platform)
        result = (
            ContentCreationCrew()
            .crew()
            .kickoff(inputs={
                "user_persona": self.state.user_persona,
                "social_media_platform": self.state.social_media_platform,
                "transcript": self.state.transcript,
                "highlighted_points": self.state.highlighted_points,
                "user_opinion": self.state.user_opinion,
                "event_name": self.state.event_name
            })
        )

        print("Content generated successfully")
        generated_content = result.raw
        print("--------------------------------")
        print(generated_content)
        # self.state.generated_content = result.raw
        return generated_content

    # I dont think we want to save the content here
    # @listen(generate_content)
    # def save_content(self):
    #     print("Saving content")
    #     with open(f"{self.state.social_media_platform}_post.txt", "w") as f:
    #         f.write(self.state.generated_content)

def get_dummy_transcript():
    data = """
    Welcome Remarks & Hackathon Overview
    "Welcome everyone to the AI Tinkerers Seattle Virtual Practical Agents Hackathon! We're thrilled to have so many innovative minds joining us today from across the globe. This hackathon is designed to push the boundaries of what's possible with AI agents in practical applications.

    Our goal today is to foster collaboration and create functional AI agent systems that can solve real-world problems. We've structured the event to provide you with expert insights, practical tools, and ample time for building. Remember that the emphasis is on creating practical solutions that demonstrate the power of multi-agent systems working together.

    CrewAI Presentation – João Moura
    "Thank you for the introduction. I'm excited to share CrewAI with you all today. We built CrewAI to address a critical need in the AI agent ecosystem - how to efficiently orchestrate multiple specialized agents working together toward a common goal.

    CrewAI is designed with four core principles: modularity, allowing agents to be easily composed; robustness, ensuring reliability even when individual components fail; explainability, making it clear why agents make certain decisions; and interoperability, enabling agents to work with various tools and APIs.

    Let me demonstrate how you can use CrewAI to build a content research and creation system with just a few lines of code..."

    OpenPipe Talk – Kyle Corbitt
    "Great to be here today. At OpenPipe, we're focused on making reinforcement learning practical for everyday developers building AI agents. One of our most interesting recent projects was building an email sorting agent that learns from user behaviors.

    The key insight we discovered is that creating effective training loops is essential. Rather than trying to perfect your model in one shot, it's much more effective to create rapid feedback cycles where your agent learns incrementally from real interactions..."

    Quick-Start Demo: CopilotKit Integration
    "For our final presentation before you all start building, we wanted to show something that might help you get up and running quickly. We've been working on integrating CrewAI with CopilotKit to provide a seamless development experience.

    As you can see in this demo, with just a few configuration steps, you can have a fully functional AI assistant that leverages CrewAI's orchestration capabilities while using CopilotKit's interface components..."
    """
    return data

def kickoff():
    transcript = get_dummy_transcript()
    event_name = "AI Tinkerers Seattle Virtual Practical Agents Hackathon"
    social_media_platform = "twitter"
    user_persona = "organizer"
    opinion = "Love being a part at this hackathon!"
    highlighted_points = ["foster collaboration and create functional AI agent systems that can solve real-world problems. We've structured the event to provide you with expert insights, practical tools, and ample time for building. Remember that the emphasis is on creating practical solutions that demonstrate the power of multi-agent systems working together"]
    content_creation_flow = ContentCreationFlow()
    content_creation_flow.kickoff(inputs={
        "transcript": transcript,
        "social_media_platform": social_media_platform,
        "user_persona": user_persona,
        "user_opinion": opinion,
        "event_name": event_name,
        "highlighted_points": highlighted_points
    })


def plot():
    content_creation_flow = ContentCreationFlow()
    content_creation_flow.plot()


if __name__ == "__main__":
    kickoff()
