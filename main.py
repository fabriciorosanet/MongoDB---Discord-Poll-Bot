import discord
from discord.ext import commands
from pytz import timezone
from datetime import datetime
import asyncio
import os
from dotenv import load_dotenv
from pymongo import MongoClient
import logging

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
MONGO_URI = os.getenv('MONGO_URI')
MONGO_DB = os.getenv('MONGO_DB')
MONGO_COLLECTION = os.getenv('MONGO_COLLECTION')

logging.basicConfig(level=logging.DEBUG)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)  
    db = client[MONGO_DB]
    collection = db[MONGO_COLLECTION]
    client.admin.command('ping')
    print("Conectado ao MongoDB Atlas com sucesso!")
except Exception as e:
    print(f"Erro ao conectar com o MongoDB Atlas: {e}")

responses_data = []
saopaulo_tz = timezone('America/Sao_Paulo')

class PollButton(discord.ui.Button):
    def __init__(self, label, custom_id):
        super().__init__(label=label, style=discord.ButtonStyle.primary, custom_id=custom_id)

    async def callback(self, interaction: discord.Interaction):
        response_data = {
            "User": interaction.user.name,
            "Response": self.label,
            "Poll Datetime": datetime.now().astimezone(saopaulo_tz).isoformat()
        }
        responses_data.append(response_data)

        print(f'Usuário: {response_data["User"]} votou: {response_data["Response"]} em {response_data["Poll Datetime"]}')
        await interaction.response.send_message(f'Você votou: {self.label}', ephemeral=True)

class PollView(discord.ui.View):
    def __init__(self, options, timeout=None):
        super().__init__(timeout=timeout)
        for i, option in enumerate(options):
            self.add_item(PollButton(label=option, custom_id=f"poll_option_{i+1}"))

    async def on_timeout(self):
        for child in self.children:
            child.disabled = True
        await self.message.edit(view=self)
        print("Enquete encerrada.")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print("Bot pronto para enviar enquetes!")

    channel_ids = []

    question = "Quem aqui tem interesse em Oportunidades Internacionais?"
    options = [
        "Tenho muito interesse!",
        "Tenho interesse, mas preciso me planejar melhor.",
        "Ainda não pensei nisso, mas pode ser uma opção.",
        "Prefiro atuar no mercado nacional."
    ]
    
    poll_duration = 604800  # Duração da enquete em segundos (7 dias)
    view = PollView(options, timeout=poll_duration)

    for channel_id in channel_ids:
        channel = bot.get_channel(channel_id)
        if channel:
            try:
                view.message = await channel.send(f"**{question}**", view=view)
            except Exception as e:
                print(f"Falha ao enviar enquete para o canal {channel_id}: {e}")

    await asyncio.sleep(poll_duration)
    print(f"Enquete de {poll_duration} segundos encerrada.")

@bot.command(name="salvar_respostas")
async def save_responses(ctx):
    if responses_data:
        try:
            collection.insert_many(responses_data)
            responses_data.clear()  
            await ctx.send("Respostas salvas no banco de dados MongoDB.")
        except Exception as e:
            await ctx.send(f"Erro ao salvar no MongoDB: {e}")
            print(f"Erro ao salvar no MongoDB: {e}")
    else:
        await ctx.send("Nenhuma resposta registrada ainda.")

bot.run(DISCORD_TOKEN)
