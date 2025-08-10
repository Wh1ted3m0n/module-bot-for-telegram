from core import config, bot
import asyncio

def main():
    bot1 = bot.RssBot(config.TOKEN,config.ID_CHANNEL)
    asyncio.run(bot1.run())
if __name__ == "__main__":
    main()
