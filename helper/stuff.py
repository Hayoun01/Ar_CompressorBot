#    This file is part of the CompressorBot distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
#    License can be found in < https://github.com/1Danish-00/CompressorBot/blob/main/License> .

from .worker import *


async def up(event):
    if not event.is_private:
        return
    stt = dt.now()
    ed = dt.now()
    v = ts(int((ed - uptime).seconds) * 1000)
    ms = (ed - stt).microseconds / 1000
    p = f"🌋Pɪɴɢ = {ms}ms"
    await event.reply(v + "\n" + p)


async def start(event):
    ok = await event.client(GetFullUserRequest(event.sender_id))
    await event.reply(
        f"مرحبا `{ok.user.first_name}`\nهذا هو بوت ضغط الفيديوهات الذي يمكنك من ترميز الفيديوهات.\nتقليل حجم مقاطع الفيديو مع تغيير ضئيل في الجودة\nيمكنك إنشاء عينات/لقطات شاشة أيضًا.",
        buttons=[
            [Button.inline("HELP", data="ihelp")],
            [
                Button.url("قناة البوت", url="t.me/dramakokp"),
                Button.url("المطور", url="t.me/Hayyoun"),
            ],
        ],
    )


async def help(event):
    await event.reply(
        "**🐠 بوت ضغط الفيديوهات عالي الجودة **\n\n+هذا البوت يقوم بضغط مقاطع الفيديو مع تغيير ضئيل في الجودة.\n+إنشاء عينة فيديو مضغوط\n+لقطات الشاشة أيضا\n+سهل الإستخدام\n-نظرًا لإعدادات الجودة ، يستغرق الروبوت وقتًا للضغط.\nلذا تحلى بالصبر ولا نزال أرسل مقاطع الفيديو واحدًا تلو الآخر بعد الإكمال.\nلا ترسل رسائل غير مرغوب فيها.\n\nفقط قم بإعادة توجيه الفيديو للحصول على الخيارات"
    )


async def ihelp(event):
    await event.edit(
        "**🐠 بوت ضغط الفيديوهات عالي الجودة **\n\n+هذا البوت يقوم بضغط مقاطع الفيديو مع تغيير ضئيل في الجودة.\n+إنشاء عينة فيديو مضغوط\n+لقطات الشاشة أيضا\n+سهل الإستخدام\n-نظرًا لإعدادات الجودة ، يستغرق الروبوت وقتًا للضغط.\nلذا تحلى بالصبر ولا نزال أرسل مقاطع الفيديو واحدًا تلو الآخر بعد الإكمال.\nلا ترسل رسائل غير مرغوب فيها.\n\nفقط قم بإعادة توجيه الفيديو للحصول على الخيارات",
        buttons=[Button.inline("العودة", data="beck")],
    )


async def beck(event):
    ok = await event.client(GetFullUserRequest(event.sender_id))
    await event.edit(
        f"مرحبا `{ok.user.first_name}`\nهذا هو بوت ضغط الفيديوهات الذي يمكنك من ترميز الفيديوهات.\nتقليل حجم مقاطع الفيديو مع تغيير ضئيل في الجودة\nيمكنك إنشاء عينات/لقطات شاشة أيضًا.",
        buttons=[
            [Button.inline("مساعدة", data="ihelp")],
            [
                Button.url("قناة البوت", url="t.me/dramakokp"),
                Button.url("المطور", url="t.me/Hayyoun"),
            ],
        ],
    )


async def sencc(e):
    key = e.pattern_match.group(1).decode("UTF-8")
    await e.edit(
        "Choose Mode",
        buttons=[
            [
                Button.inline("الضغط الافتراضي", data=f"encc{key}"),
                Button.inline("ضغط مخصص", data=f"ccom{key}"),
            ],
            [Button.inline("العودة", data=f"back{key}")],
        ],
    )


async def back(e):
    key = e.pattern_match.group(1).decode("UTF-8")
    await e.edit(
        "🐠  **ما يجب القيام به** 🐠",
        buttons=[
            [
                Button.inline("توليد عينة", data=f"gsmpl{key}"),
                Button.inline("لقطات الشاشة", data=f"sshot{key}"),
            ],
            [Button.inline("ضغط", data=f"sencc{key}")],
        ],
    )


async def ccom(e):
    await e.edit("أرسل اسمك المخصص لهذا الملف")
    wah = e.pattern_match.group(1).decode("UTF-8")
    wh = decode(wah)
    out, dl, thum, dtime = wh.split(";")
    chat = e.sender_id
    async with e.client.conversation(chat) as cv:
        reply = cv.wait_event(events.NewMessage(from_users=chat))
        repl = await reply
        if "." in repl.text:
            q = repl.text.split(".")[-1]
            g = repl.text.replace(q, "mkv")
        else:
            g = repl.text + ".mkv"
        outt = f"encode/{chat}/{g}"
        x = await repl.reply(
            f"اسم الملف المخصص : {g}\n\nأرسل صورة مصغرة له."
        )
        replyy = cv.wait_event(events.NewMessage(from_users=chat))
        rep = await replyy
        if rep.media:
            tb = await e.client.download_media(rep.media, f"thumb/{chat}.jpg")
        elif rep.text and not (rep.text).startswith("/"):
            url = rep.text
            os.system(f"wget {url}")
            tb = url.replace("https://telegra.ph/file/", "")
        else:
            tb = thum
        omk = await rep.reply(f"تم تحديد الصورة المصغرة {tb} بنجاح")
        hehe = f"{outt};{dl};{tb};{dtime}"
        key = code(hehe)
        await customenc(omk, key)
