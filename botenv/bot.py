import discord
from discord.ext import commands
from passwords import token_name
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

# A dictionary to store user contexts
user_contexts = {}

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command(name='multistep', description='Command with multiple steps')
async def multistep(ctx):
    user_id = ctx.author.id

    # Check if the user is already in a multi-step process
    if user_id in user_contexts:
        await ctx.send("You are already in a multi-step process.")
        return

    # Step 1
    await ctx.send("Step 1: Please enter something.")
    response1 = await bot.wait_for('message', check=lambda m: m.author == ctx.author, timeout=60)

    # Step 2
    await ctx.send(f"Step 2: You entered: {response1.content}. Now, please enter something else.")
    response2 = await bot.wait_for('message', check=lambda m: m.author == ctx.author, timeout=60)

    # Process the information
    result = f"You entered: {response1.content} and {response2.content}"

    # Do something with the result (e.g., send it back to the user)
    await ctx.send(result)

    # Cleanup: Remove user context
    del user_contexts[user_id]

# Replace 'your_token_here'

bot.run(token_name)