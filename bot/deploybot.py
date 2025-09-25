#!/usr/bin/python

import asyncio
import os

import dotenv
import telebot.async_telebot

dotenv.load_dotenv()

API_TOKEN = os.getenv("BOT_TOKEN")

ADMIN_IDS = os.getenv("ADMIN_IDS", "909313568").split(",")

dbot = telebot.async_telebot.AsyncTeleBot(API_TOKEN, "Markdown")


@dbot.message_handler(commands=["deploy"])
async def handle_deploy(message: telebot.types.Message):
    user_id = f"{message.from_user.id}"

    if user_id in ADMIN_IDS:
        try:
            command = "echo /root/docker_restart.sh > docker_executor_host"
            os.system(command)
            response_text = "✅ *Успех*"
        except Exception:
            response_text = "❌ *Ошибка при выполнении команды*"

    else:
        response_text = "❌ *Ошибка доступа*"

    # Отправка ответа
    await dbot.send_message(message.chat.id, response_text)


asyncio.run(dbot.polling())
