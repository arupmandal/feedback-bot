# Copyright Â©ï¸ 2022 Sanila Ranatunga. All Rights Reserved
# You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [feedback-bot] (https://github.com/sanila2007/feedback-bot)

# Read GNU General Public License v3.0: https://github.com/sanila2007/feedback-bot/blob/mai/LICENSE
# Don't forget to follow github.com/sanila2007 because I'm doing these things for free and open source
# Star and fork and enjoy!


import pyrogram
from plugins import quotes_text

FEEDBACK_REPLY_TEXT = "First please select a bot!!ð®"

CONTACT_TEXT = "**Contact**\n\nâ You can connect with the admin from here.\n\nâ Type your message here and send.\n\nâ After you finish click <<**Finishð©**>>"

REPLY_MESSAGE = "Click any button from ReplyKeyboard as your choice. Don't send feedbacks directly. Use contact or feedback sections. **WE DO NOT COLLECT DIRECT FEEDBACKS.**\n\nUse `@sanilaassistant_bot` for get the BOT LIST in inline mode."

LEARN_TEXT = "Please select the bot that you want to learn!!ð¨âð«"

START_TEXT_CAPTION_TEXT = "This is a multi functional bot that can give & collect feedbacks from" \
                          " users and broadcast replies to them.\n\n" \
                          "Some of my bots,\n" \
                          "â¬â¬â¬ â <a href=https://t.me/songdownload597_bot>Song Download Bot</a>\n" \
                          "â¬â¬â¬ â <a href=https://t.me/torrentdownloader88_bot>Torrent Download Bot</a>\n" \
                          "â¬â¬â¬ â <a href=https://t.me/youtubevideodownloader45_bot>Youtube Vide Download Bot</a>\n" \
                          "â¬â¬â¬ â <a href=https://t.me/telgeraph200_bot>Telegraph Uploader Bot</a>\n\n" \
                          "<i>*Note:</i> When sending feedbacks through this bot **DO NOT SEND FEEDBACKS DIRECTLY** because those aren't accepted. Therefore please use **FEEDBACK OR CONTACT SECTIONS!!**\n\nUse `@sanilaassistant_bot` for get the BOT LIST in inline mode."

REPORT_BUGS_TEXT = "Please select a bot!!ð®"

CHANGELOG_TEXT = "**Changelog**\n\n" \
                 "ð0.8\n âAdded CAPTCHA /captcha\n âAdded facility to rate bots\n âAdded log channel (admin only)\n âInstant view supports\n âAdded ForceReply\n âFeedback improvements\n âStickers has been restricted\n âMinor bug fixes\n\n  " \
                 "ð0.7\n âNow you can't send feedbacks empty \nâRemoved unnecessary features\n âImproved feedback centre\n âImproved report bugs centre\n âImproved contact section and added features\n âImproved changelog section\n âImprovements in repository\n âMinor bugs fixes\n\n " \
                 "<a href=https://github.com/sanila2007/feedback-bot/blob/mai/release%20notes/release_notes.txt>see more...</a>\n\n" \
                 "*Note: Every version releases aren't available here. Just major updates only. If ou want to get the minor releases too," \
                 "you can check <a href=https://github.com/sanila2007/feedback-bot/releases>Releases</a>"

SANILA_ASSISTANT_TEXT = "Reporting Areaâ¼ï¸\n\nBot = <a href=https://t.me/sanilaassistant_bot> Sanila's Assistant Bot</a>\n\n" \
                        "â Type your report here and send it\n\n" \
                        "â After you finish click <<**Finishð©**>>\n\n" \
                        "â You will get answer for your feedback around <b><b>24hours.</b></b>"

SONG_DOWNLOADER_TEXT = "Reporting Areaâ¼ï¸\n\nBot = <a href=https://t.me/songdownload597_bot> Song Downloader Bot</a>\n\n" \
                       "â Type your report here and send it\n\n" \
                       "â After you finish click <<**Finishð©**>>\n\n" \
                       "â You will get answer for your feedback around <b><b>24hours.</b></b>"

TORRENT_DOWNLOADER_TEXT = "Reporting Areaâ¼ï¸\n\nBot = <a href=https://t.me/torrentdownloader88_bot> Torrent Downloader Bot</a>\n\n" \
                          "â Type your report here and send it\n\n" \
                          "â After you finish click <<**Finishð©**>>\n\n" \
                          "â You will get answer for your feedback around <b><b>24hours.</b></b>"

YOUTUBE_VIDEO_DOWNLOADER_TEXT = "Reporting Areaâ¼ï¸\n\nBot = <a href=https://t.me/youtubevideodownloader45_bot>Youtube Video Downloader Bot</a>\n\n" \
                                "â Type your report here and send it\n\n" \
                                "â After you finish click <<**Finishð©**>>\n\n" \
                                "â You will get answer for your feedback around <b><b>24hours.</b></b>"

TELEGRAPH_UPLOADER_TEXT = "Reporting Areaâ¼ï¸\n\nBot = <a href=https://t.me/telgeraph200_bot>Telegraph Uploader Bot</a>\n\n" \
                                "â Type your report here and send it\n\n" \
                                "â After you finish click <<**Finishð©**>>\n\n" \
                                "â You will get answer for your feedback around <b><b>24hours.</b></b>"

FEEDBACK_FINISH_TEXT = "Thanks for your feedback!\n\nYour valuable feedbacks help us to build our bots much friendly. When you sending your feedback please include a screenshot of it because it helps us to decide what is the error.\n\nIt usually takes about 48 hours to get back to you, please accept our apologies in advance for any reply that exceeds this time frame.\n\nFeedback Centre."

DONT_SEND = "Telegraph Uploader\n\nA telegram bot which can upload media such as images, videos & animations to the telegra.ph"

DONT_SEND2 = "Feedback Bot\n\nMulti functional bot that can give & collect feedbacks from users and broadcast replies to them with cool functions such as rating bots, completing captchas & etc...\n\nDeveloper : <a href=https://github.com/sanila2007>Sanila Ranatunga</a>"

DONT_SEND3 = "Music Download Bot\n\nOne of the most powerful Song download bot found on Telegram...\n\nDeveloper : <a href=https://github.com/sanila2007>Sanila Ranatunga</a>"

DONT_SEND4 = "Text to File Bot\n\nTEXT TO FILE BOT JUST SENT YOUR CODE OR TEXT MESSAGE THEN I WILL CONVERT IT INTO FILE\n\nDEVELOPER : <a href=https://github.com/hbbots>Amal Mohan</a>"

DONT_SEND5 = "QR Code Generator Bot\n\nTelegram Bot that can generate QR codes\n\nDEVELOPER : <a href=https://github.com/hbbots>Amal Mohan</a>"

DONT_SEND6 = "Youtube Video Bot\n\nTelegram bot that can download videos, thumbnail and playlist videos from Youtube VERY QUICKLY.\n\nDEVELOPER : <a href=https://github.com/hbbots>Amal Mohan</a>"

DONT_SEND7 = "Torrent Search Bot\n\nTelegram Bot that can search & download torrents from YTS, Piratebay, Anime, etc...\n\nDEVELOPER : <a href=https://github.com/sanila2007>Sanila Ranatunga</a>"

DONT_SEND8 = "Random Name Generator Bot\n\nTelegram bot that can generate random names for their users.\n\nDEVELOPER : <a href=https://github.com/hbbots>Amal Mohan</a>"

# Copyright Â©ï¸ 2022 Sanila Ranatunga. All Rights Reserved