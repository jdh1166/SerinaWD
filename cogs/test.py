from discord.ext import commands

class ExampleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='hello')
    async def hello(self, ctx):
        await ctx.send("안녕하세요, Cog입니다!")

# Cog 등록
def setup(bot):
    bot.add_cog(ExampleCog(bot))
