from agents.research.research_agent import ResearchAgent
from agents.script.script_agent import ScriptAgent


def main():

    research_agent = ResearchAgent()
    script_agent = ScriptAgent()

    topic = input("Enter a topic: ")

    print("\nResearching topic...\n")

    research_result = research_agent.research(topic)

    # Stop if research failed
    if research_result.startswith("Research Agent Error"):
        print(research_result)
        return

    print("Writing script...\n")

    script = script_agent.write_script(research_result)

    # Stop if script generation failed
    if script.startswith("Script Agent Error"):
        print(script)
        return

    print("=" * 60)
    print(script)
    print("=" * 60)


if __name__ == "__main__":
    main()