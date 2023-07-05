from sys import argv
from time import sleep

from origamibot import OrigamiBot as Bot
from origamibot.listener import Listener

import giphy


class BotsCommands:
    def __init__(self, bot: Bot):
        self.bot = bot

    def start(self, message):
        self.bot.send_message(
            message.chat.id,
            'Hello user!\nSend your search request in form \n/gif <search request>"\nand I\'ll send you a gif')

    def gif(self, message, search_request: str):
        self.bot.send_message(
            message.chat.id,
            giphy.get_image_url(search_request)
            )

    def _not_a_command(self):
        print('I am not a command')


class MessageListener(Listener):
    def __init__(self, bot):
        self.bot = bot
        self.m_count = 0

    def on_command_failure(self, message, err=None):
        if err is None:
            self.bot.send_message(message.chat.id,
                                  'Add your search request')
        else:
            self.bot.send_message(message.chat.id,
                                  f'Error in search:\n{err}')


if __name__ == '__main__':
    token = (argv[1] if len(argv) > 1 else input('Enter bot token: '))
    bot = Bot(token)

    bot.add_listener(MessageListener(bot))

    bot.add_commands(BotsCommands(bot))

    bot.start()
    while True:
        sleep(1)
