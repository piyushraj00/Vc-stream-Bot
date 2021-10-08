from config import Config
from helpers.logger import LOGGER
from pyrogram import Client, errors
from youtubesearchpython import VideosSearch
from pyrogram.handlers import InlineQueryHandler
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardButton, InlineKeyboardMarkup

buttons = [
            [
                InlineKeyboardButton("📌 Updates Channel", url="https://t.me/YoutubeVideoDownloaderService"),
            
            
                InlineKeyboardButton("👥 Support Group", url="https://t.me/VCMusicGroup")],
                [InlineKeyboardButton("♻️ Other Bots", url="https://t.me/DeCodeSupport"),
            ],
            [
                InlineKeyboardButton("🔺 Creator", url="t.me/TronManTRONIC"),
            ]
         ]

def get_cmd(dur):
    if dur:
        return "/stream"
    else:
        return "/live"

@Client.on_inline_query()
async def search(client, query):
    answers = []
    if query.query == "ABOUT":
        answers.append(
            InlineQueryResultArticle(
                title="About This Bot 🌀",
                input_message_content=InputTextMessageContent(f"**🤖 Name : VC Streamer Bot\n\n👨‍💻 Developer : [ᴘɪʏᴜꜱʜ ʀᴀᴊ 🇮🇳](t.me/TronManTRONIC)\n\n📢 Channel : [ᴘɪʏᴜꜱʜ ᴘʀᴏᴊᴇᴄᴛꜱ™](telegram.dog/YoutubeVideoDownloaderService)\n\n👥 Group : [ᴘʀ ᴘʀᴏᴊᴇᴄᴛ ꜱᴜᴘᴘᴏʀᴛ™](telegram.dog/VCMusicGroup)\n\n📝 Language : [Python3](python.org)\n\n📚 Library : [Pyrogram](pyrogram.org)\n\n📡 Server : [Heroku](heroku.com]**", disable_web_page_preview=True),
                reply_markup=InlineKeyboardMarkup(buttons)
                )
            )
        await query.answer(results=answers, cache_time=0)
        return
    string = query.query.lower().strip().rstrip()
    if string == "":
        await client.answer_inline_query(
            query.id,
            results=answers,
            switch_pm_text=("✍️ Type An Video Name To Search !"),
            switch_pm_parameter="help",
            cache_time=0
        )
    else:
        videosSearch = VideosSearch(string.lower(), limit=50)
        for v in videosSearch.result()["result"]:
            answers.append(
                InlineQueryResultArticle(
                    title=v["title"],
                    description=("Duration: {} Views: {}").format(
                        v["duration"],
                        v["viewCount"]["short"]
                    ),
                    input_message_content=InputTextMessageContent(
                        "{} https://www.youtube.com/watch?v={}".format(get_cmd(v["duration"]), v["id"])
                    ),
                    thumb_url=v["thumbnails"][0]["url"]
                )
            )
        try:
            await query.answer(
                results=answers,
                cache_time=0
            )
        except errors.QueryIdInvalid:
            await query.answer(
                results=answers,
                cache_time=0,
                switch_pm_text=("❌ No Results Found !"),
                switch_pm_parameter="",
            )


__handlers__ = [
    [
        InlineQueryHandler(
            search
        )
    ]
]
