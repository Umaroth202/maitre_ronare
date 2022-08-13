import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix = '=', descrition = "Bot Guide du serveur des Girafes Kawaii")

funFact = ["L'eau mouille", 
			"Le feu brule", 
			"Lorsque vous volez, vous ne touchez pas le sol", 
			"Winter is coming", "Mon créateur est Umaroth", 
			"Il n'est pas possible d'aller dans l'espace en restant sur terre", 
			"La terre est ronde",
			"La moitié de 2 est 1",
			"7 est un nombre heureux",
			"Les allemands viennent d'allemagne",
			"Le coronavirus est un virus se répandant en Europe, en avez vous entendu parler ?",
			"J'apparais 2 fois dans l'année, a la fin du matin et au début de la nuit, qui suis-je ?",
			"Le plus grand complot de l'humanité est",
			" je ne sais plus, désolé.",
			"Pourquoi lisez vous ca ?",
			"La Girafe Originelle est la plus belle des girafes.",
			"UmaR est un grand sage et ses décisions sont toujours juste."]

@bot.event
async def on_ready():
	print("Ready !")
	await bot.change_presence(activity=discord.Game(name="=cmd | Guide du serveur des Girafes Kawaii"))
	print("-------------")

@bot.command()
async def minecraft(ctx):
	embed = discord.Embed(title = "**Minecraft**", description = "Si le serveur n'est pas allumé, merci de mentionner <@636884457558900766> ou <@924963714925461514>.", url = "", color=0xfa8072)
	embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url, url = "")
	embed.add_field(name = "IP", value = "Girafe_kawaii.aternos.me", inline = True)
	embed.add_field(name = "Version", value = "Java 1.19", inline = True)
	embed.add_field(name = "Crack", value = "Autorisé", inline = True)
	embed.set_footer(text = random.choice(funFact))

	await ctx.send(embed = embed)

@bot.command()
async def cmd(ctx):
	embed = discord.Embed(title = "**Liste des Commandes**", description = "Liste des commandes de Maître Ronare", url = "", color=0xfa8072)
	embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url, url = "")
	embed.add_field(name = "Utilitaire", value = "**=cmd** : Affiche ce message \n**=ping** : Affiche le ping du bot \n**=minecraft** : Affiche des informations sur le serveur minecraft", inline = True)
	embed.add_field(name = "Fun", value = "**=funfact** : Affiche une funfact aléatoire", inline = True)
	embed.add_field(name = "Admin", value = "**=say** : Ecrit un message avec le bot \n**=statut** : Modifie le statut du bot", inline = True)
	embed.set_footer(text = random.choice(funFact))

	await ctx.send(embed = embed)

@bot.command()
@commands.has_permissions(manage_messages = True)
async def statut(ctx, *, args):
	message = ctx.message
	await message.delete()
	
	await ctx.send(f'Le statut du bot est "{args}".')
	await bot.change_presence(activity=discord.Game(name=args))

@bot.command()
@commands.has_permissions(manage_messages = True)
async def say(ctx, *, args):
    message = ctx.message
    await message.delete()

    await ctx.send(f"{args}")

@bot.command()
async def ping(ctx):
	await ctx.send(f'Mon ping est de {bot.latency * 1000} ms.')

@bot.command()
async def funfact(ctx):
	await ctx.send(random.choice(funFact))

bot.run("MTAwNzk1NTAyMDQzMzU5MjM3MA.GQf3-5.JQDUkDEyPsAhf9-upK1mIZ3G3b_HUsH5ReiwU0")