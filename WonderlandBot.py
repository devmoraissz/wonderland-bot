from os import name
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

# Carregar as variáveis do arquivo .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot {bot.user} está online com todos os poderes!")

# Criar um canal
@bot.command()
async def criar_canal(ctx, *, nome):
    guild = ctx.guild
    await guild.create_text_channel(nome)
    await ctx.send(f"✅ Canal **{nome}** criado com sucesso!")

# Deletar um canal
@bot.command()
async def deletar_canal(ctx, canal_id: int):
    canal = bot.get_channel(canal_id)
    if canal:
        await canal.delete()
        await ctx.send("❌ Canal deletado!")
    else:
        await ctx.send("Canal não encontrado.")

# Enviar mensagem
@bot.command()
async def enviar(ctx, *, mensagem):
    await ctx.send(mensagem)

# Falar em chat especifico
@bot.command()
async def falar(ctx, canal_id: int, *, mensagem):
    canal = bot.get_channel(canal_id)
    if canal:
        await canal.send(mensagem)
        await ctx.send("✅ Mensagem enviada com sucesso!")
    else:
        await ctx.send("❌ Canal não encontrado.")

# Banir um usuário
@bot.command()
async def banir(ctx, membro: discord.Member, *, motivo=None):
    await membro.ban(reason=motivo)
    await ctx.send(f"🚫 {membro} foi banido. Motivo: {motivo}")
    
#ID DISCORD
@bot.command()
async def termos(ctx):
    canal1 = bot.get_channel(1350242671733641236)  # substitua pelo ID real
    canal2 = bot.get_channel(1350242446851964958)  # substitua pelo ID real

    embed = discord.Embed(
        title=" TERMOS E CONDIÇÕES – WONDERLAND STORE <a:verificado_WS:1408246328722460713>  ",
        description=" Ao realizar um pagamento e compra, você concorda com os seguintes termos e condições. "
                    "O descumprimento de nossos termos pode resultar em perdas de todos os benefícios da Wonderland Store. "
                    "Dependendo do caso, você corre o risco de entrar na nossa BlackList. "
                    "Esteja ciente de todos os termos e condições antes de realizar qualquer pagamento ou compra em nossa loja.",
        color=0xff69b4
    )

    embed.add_field(name="\u200b", value="\u200b", inline=False)

    embed.add_field(
        name=" <:1_WS:1408250408798912594> Reembolso",
        value=" Devido à natureza digital dos nossos produtos, não oferecemos reembolso, ressarcimento, devolução ou estorno após o envio do arquivo.\n\n"
              " O reembolso só pode ser solicitado em casos de erro ou falha em nosso envio.\n\n"
              " É vetado o reembolso da conversão em casos onde o arquivo foi enviado."
             f" Para conhecer nossos produtos antes da compra, acesse os seguintes canais: "
             f"{canal1.mention if canal1 else '#canal1_nao_encontrado'}, "
             f"{canal2.mention if canal2 else '#canal2_nao_encontrado'}.\n"
              " Isso permitirá que você faça uma avaliação adequada do que está adquirindo.",
        inline=False
    )

    embed.add_field(name="\u200b", value="\u200b", inline=False)

    embed.add_field(
        name=" <:2_WS:1408251453788913694> Direitos Autorais e uso",
        value=" De acordo com a Lei de Direitos Autorais (Lei federal nº 9.610/1998), não é permitido revender, compartilhar ou distribuir os produtos da Wonderland Store.\n\n"
              " Não realizamos alterações/modificações em produtos de outras lojas sem a autorização de quem o criou.\n\n"
              " Produtos disponibilizados free ou booster devem ser para uso próprio. Revenda, compartilhamento ou modificações por terceiros são estritamente proibidos.",
        inline=False
    )

    embed.add_field(name="\u200b", value="\u200b", inline=False)

    embed.add_field(
        name=" <:3_WS:1408251491449311364> Pagamentos",
        value=" A produção inicia apenas após pagamento total ou entrada de 50% do valor. O restante é cobrado na entrega.\n\n"
              " O pagamento é realizado através do ticket, com comprovante obrigatório para registro. Pagamentos fora desse meio não serão aceitos.\n\n"
              " Após a confirmação do pagamento final, seu produto será enviado em até 24 horas.",
        inline=False
    )

    embed.add_field(name="\u200b", value="\u200b", inline=False)

    embed.add_field(
        name=" <:4_WS:1408251514824167566> Entregas e Arquivos",
        value=" Caso haja perda de arquivos e solicite reenvio, será cobrado 50% do valor total do produto.\n\n"
              " Tickets ficarão abertos por 72 horas para download e conferência de falhas/erros.\n\n"
              " Prazos de entrega são informados no ticket e somente em dias úteis (finais de semana não inclusos). "
              "Atualizações após a criação, terão prazo estendido e taxa adicional.",
        inline=False
    )

    embed.add_field(name="\u200b", value="\u200b", inline=False)

    embed.add_field(
        name=" <:5_WS:1408251545052643401> Orientações",
        value=" Em caso de RP de gravidez, aconselhamos encomendar o PED antecipadamente, respeitando o prazo de tempo adequado.",
        inline=False
    )

    # Adiciona o rodapé do embed com a mensagem de finalização
    embed.add_field(
    name="\u200b",
    value="Na Wonderland Store, cada criação é feita com amor e cuidado. "
          "Ao valorizar nosso trabalho, você ajuda a manter esse espaço mágico, organizado e especial para todos.",
    inline=False
    )

    # Assinatura final
    embed.add_field(
        name="\u200b",
        value="**Com carinho,**\n**Equipe Wonderland Store ❤️**",
        inline=False
    )

    await ctx.send(embed=embed)


bot.run(TOKEN)

