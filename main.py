import discord
from discord.ext import commands
import os
from keep_alive import keep_alive

# インテントの設定
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'ログイン完了: {bot.user}')

# 「!募集」と打つと反応するコマンド
@bot.command()
async def 募集(ctx):
    embed = discord.Embed(
        title="🌟 スタッフ大募集 🌟", 
        description="当サーバーを一緒に盛り上げてくれるメンバーを募集しています！\n興味のある方はぜひご応募ください。", 
        color=0x00ff00
    )
    
    embed.add_field(
        name="👑 管理者 (Admin)", 
        value="・サーバーのルール整備\n・荒らし対策やトラブル対応\n・運営チームの統括", 
        inline=False
    )
    embed.add_field(
        name="💻 デベロッパー (Developer)", 
        value="・オリジナルBOTの開発・保守\n・サーバーのシステム構築（自動化など）", 
        inline=False
    )
    embed.add_field(
        name="🛠️ 運営 (Moderator/Staff)", 
        value="・イベントの企画・進行\n・ユーザーからの質問対応\n・チャットの盛り上げ", 
        inline=False
    )
    
    embed.set_footer(text="応募をご希望の方は、サーバー管理者へDMまたはチケットを作成してください！")
    
    await ctx.send(embed=embed)

# Webサーバーを起動してRenderのエラーを防ぐ
keep_alive()

# 環境変数からトークンを読み込んでBOTを起動
TOKEN = os.environ.get("DISCORD_TOKEN")
bot.run(TOKEN)
