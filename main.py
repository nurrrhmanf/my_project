import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Load token dari .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Inisialisasi bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents, case_insensitive=True)

@bot.event
async def on_ready():
    print(f"Bot {bot.user.name} sudah online dan siap digunakan!")

# Command untuk informasi perubahan iklim
@bot.command()
async def info(ctx):
    embed = discord.Embed(
        title="Perubahan Iklim",
        description=(
            "**Definisi**\n"
            "Perubahan iklim adalah perubahan besar dalam cuaca yang berlangsung lama, "
            "seperti musim panas yang makin panas atau hujan yang tak menentu.\n\n"
            
            "**Masalah**\n"
            "- Suhu Bumi semakin panas.\n"
            "- Permukaan laut naik, membuat banjir lebih sering terjadi.\n"
            "- Cuaca menjadi ekstrem, seperti badai atau kekeringan.\n\n"
            
            "**Penyebab**\n"
            "- Asap dari pabrik, mobil, dan pembakaran bahan bakar.\n"
            "- Penebangan hutan yang mengurangi jumlah pohon.\n\n"
            
            "**Solusi**\n"
            "- Kurangi polusi dengan menggunakan transportasi umum atau sepeda.\n"
            "- Gunakan energi ramah lingkungan seperti tenaga surya.\n"
            "- Tanam lebih banyak pohon untuk membantu menyerap polusi."
        ),
        color=discord.Color.blue(),
    )
    embed.set_footer(text="Informasi oleh Bot Perubahan Iklim")
    
    # Kirim embed dengan gambar lokal
    with open("images/perubahan-iklim.jpg", "rb") as file:
        picture = discord.File(file, filename="perubahan-iklim.jpg")
        embed.set_image(url="attachment://perubahan-iklim.jpg")
        await ctx.send(file=picture, embed=embed)

@bot.command()
async def tips(ctx):
    embed = discord.Embed(
        title="Tips Mengurangi Jejak Karbon",
        description=(
            "1. Gunakan transportasi umum atau sepeda.\n"
            "2. Kurangi penggunaan plastik sekali pakai.\n"
            "3. Tanam pohon atau tanaman di sekitar rumah.\n"
            "4. Gunakan lampu hemat energi.\n"
            "5. Daur ulang sampah rumah tangga."
        ),
        color=discord.Color.green(),
    )
    embed.set_footer(text="Informasi oleh Bot Perubahan Iklim")
    
    # Kirim embed dengan gambar lokal
    with open("images/penghijauan.jpg", "rb") as file:
        picture = discord.File(file, filename="penghijauan.jpg")
        embed.set_image(url="attachment://penghijauan.jpg")
        await ctx.send(file=picture, embed=embed)

# Menjalankan bot
if TOKEN:
    bot.run(TOKEN)
else:
    print("Error: Token bot tidak ditemukan. Periksa file .env!")
