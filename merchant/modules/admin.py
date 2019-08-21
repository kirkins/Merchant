import asyncio
import os
import sys

from pyrogram import Filters

from merchant import BOT, ADMINS


@BOT.on_message(Filters.user(users=ADMINS) & Filters.command('update', '!'))
async def pull_update():
    proc = await asyncio.create_subprocess_shell("git pull")
    await proc.wait()
    os.execl(sys.executable, sys.executable, *sys.argv)


@BOT.on_message(Filters.user(users=ADMINS) & Filters.command('restart', '!'))
async def restart():
    os.execl(sys.executable, sys.executable, *sys.argv)


@BOT.on_message(Filters.user(users=ADMINS) & Filters.command('cleancache', '!'))
async def clean_cache():
    asyncio.create_subprocess_shell("rm -rf cache")
