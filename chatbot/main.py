from microsoftbotframework import MsBot
from chatbot.response import Bot

decider = Bot()
bot = MsBot()
bot.add_process(decider.respond)

if __name__ == '__main__':
    bot.run()