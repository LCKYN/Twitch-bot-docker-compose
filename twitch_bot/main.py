import os
from collections import Counter

from dotenv import load_dotenv
from src.file_management import read_file
from twitchio.ext import commands

load_dotenv()

TWITCH_TOKEN = os.getenv("TWITCH_TOKEN")
TWITCH_CHANNEL = os.getenv("TWITCH_CHANNEL")


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            token=TWITCH_TOKEN,
            prefix="!",
            initial_channels=[TWITCH_CHANNEL],
        )

    async def event_ready(self):
        print(f"Logged in as | {self.nick}")
        print(f"User id is | {self.user_id}")

    async def event_message(self, message):
        # Ignore messages from self.
        if message.echo:
            return

        # Ignore messages that don't start with "!".
        if not message.content.startswith("!"):
            return

        print("test")
        print(message.content)

        # Remove the "!" from the message.
        input_string = message.content[1:]

        # Get the dialog message.
        dialog = await read_file("./commands/dialog_command.csv")

        if input_string in dialog:
            await message.channel.send(dialog[input_string])

        # await self.handle_commands(message)


if __name__ == "__main__":
    print("Starting bot...")
    bot = Bot()
    bot.run()
