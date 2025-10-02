import time
import os
import asyncio


from livekit.agents import Agent, AgentSession, JobContext, WorkerOptions
from livekit.plugins import openai, silero, cartesia
from pathlib import Path


# IMPORTANT: Replace this with your actual Cartesia API key
CARTESIA_API_KEY = "Your - API Key"
CEREBRAS_API_KEY = "Your - API key"

# Set the API key in environment variables (
os.environ["CARTESIA_API_KEY"] = CARTESIA_API_KEY
os.environ["CEREBRAS_API_KEY"] = CEREBRAS_API_KEY

print("✅ Libraries imported and API keys configured")

# Load the Context from the files to the Agent
def load_context(agent_type=""):
    """Load files from context directory, optionally filtered by agent type"""
    context_dir = Path("context")
    context_dir.mkdir(exist_ok=True)

    all_content = ""
    for file_path in context_dir.glob("*"):
        if file_path.is_file() and (not agent_type or agent_type in file_path.name.lower()):
            try:
                content = file_path.read_text(encoding="utf-8")
                all_content += f"\n=== {file_path.name} ===\n{content}\n"
            except:
                pass

    return all_content.strip() or "No files found"


print(load_context())
print("✅ Context loading function ready")

# Agent Class and their functionalities
class SalesAgent(Agent):
    def __init__(self):
        # Load context once at startup
        context = load_context()
        print(f"📄 Loaded context: {len(context)} characters")

        llm = openai.LLM.with_cerebras(model="llama-3.3-70b")
        stt = cartesia.STT()
        tts = cartesia.TTS()
        vad = silero.VAD.load()

        # Put ALL context in system instructions
        instructions = f"""
        You are a sales agent communicating by voice. All text that you return
        will be spoken aloud, so don't use things like bullets, slashes, or any
        other non-pronouncable punctuation.

        You have access to the following company information:

        {context}

        CRITICAL RULES:
        - ONLY use information from the context above
        - If asked about something not in the context, say "I don't have that information"
        - DO NOT make up prices, features, or any other details
        - Quote directly from the context when possible
        - Be a sales agent but only use the provided information
        """

        super().__init__(
            instructions=instructions,
            stt=stt, llm=llm, tts=tts, vad=vad
        )

    # This tells the Agent to greet the user as soon as they join, with some context about the greeting.
    async def on_enter(self):
        self.session.generate_reply(user_input="Give a short, 1 sentence greeting. Offer to answer any questions.")

    async def on_message(self, message: str):
        print(f"🗣 User said: {message}")

        if any(word in message.lower() for word in ["bye", "goodbye", "exit", "quit"]):
            await self.session.say("Goodbye, have a great day!")
            await self.session.close()
            return

        await self.session.generate_reply(user_input=message)

    async def on_error(self, error: Exception):
        print(f"⚠️ Error: {error}")
        if "Cartesia STT connection closed" in str(error):
            print("🔌 STT closed due to silence/timeout, ending session gracefully.")
            await self.session.close()

    async def _watch_inactivity(self):
        """Auto-close session after 30s of silence."""
        while True:
            await asyncio.sleep(5)  # check every 5s
            if time.time() - self.last_activity > 30:  # 30s silence
                print("⏱️ No user activity for 30s. Closing session.")
                await self.session.say("It seems quiet, I’ll end our chat now. Goodbye!")
                await self.session.close()
                break

print("✅ Sales Agent class ready")


async def safe_stt_start(stt, session):
    while True:
        try:
            await session.add_stt(stt)
            break
        except Exception as e:
            print("⚠️ STT crashed, retrying:", e)
            await asyncio.sleep(2)


from livekit.agents import WorkerOptions, cli

async def entrypoint(ctx: JobContext):
    await ctx.connect()
    agent = SalesAgent()
    session = AgentSession()
    await session.start(room=ctx.room, agent=agent)

if __name__ == "__main__":
    cli.run_app(
        WorkerOptions(entrypoint_fnc=entrypoint)
    )
