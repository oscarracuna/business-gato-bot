import os
import random
import asyncio
import praw
import discord
from dotenv import load_dotenv, dotenv_values
from discord import app_commands
from discord.ext import commands


load_dotenv()
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)

reddit = praw.Reddit(
    client_id=os.getenv("PRAW_CLIENT_ID"),
    client_secret=os.getenv("PRAW_SECRET"),
    user_agent="u/Rhaenesis"
)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    print(f'ID: {bot.user.id}')
    print('===========================')


@bot.command()
async def hi(ctx):
    await ctx.send('hewwo uwu')

@bot.command()
async def joined(ctx, member: discord.Member):
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def meme(ctx):
    subreddits = ["memes", "dankmemes", "shitposting", "itmemes", "it_memes"]
    randosub = random.choice(subreddits)
    memes_submissions = reddit.subreddit(randosub).top(time_filter='month', limit=100)
    memes_list = [submission for submission in memes_submissions if not submission.stickied]

    if memes_list:
        submission = random.choice(memes_list)
        await ctx.send(submission.url)
    else:
        await ctx.send("No more memes for you.")

@bot.command()
async def decider(ctx):
    possibilities = [
        "yes",
        "no",
        "maybe",
        "fo sho",
        "nah",
        "Outlook not too good",
        "Outlook OK",
        "Ask again",
        "Cannot tell"
    ]
    answer = random.choice(possibilities)
    await ctx.send(answer)







bot.run(os.getenv("BOT_TOKEN"))
