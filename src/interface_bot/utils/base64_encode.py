import base64

from aiogram import Bot

async def get_base64_encoded_image(bot: Bot, photo) -> str:

    file = await bot.get_file(photo.file_id)

    image_stream  = await bot.download_file(file.file_path)
    image_bytes = image_stream.getvalue()
    # image_data = await image_bytes.read()

    base64_string = base64.b64encode(image_bytes).decode('utf-8')

    return base64_string
