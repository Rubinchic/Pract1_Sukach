import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from assistant import Assistant
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("BOT_TOKEN не знайдено в .env файлі!")

bot = Bot(token=TOKEN)
dp = Dispatcher()
assistant = Assistant()

# FSM States
class AddNoteState(StatesGroup):
    waiting_for_note = State()
    waiting_for_tags = State()

class SearchNoteState(StatesGroup):
    waiting_for_keyword = State()

class TagSearchState(StatesGroup):
    waiting_for_tag = State()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Вітаю! Я асистент-бот.\n"
        "Команди:\n"
        "/add — додати нотатку\n"
        "/list — список нотаток\n"
        "/search — пошук нотаток за словом\n"
        "/tagsearch — пошук нотаток за тегом\n"
        "/help — коротка інструкція"
    )

@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(
        "/add — додати нотатку\n"
        "/list — список нотаток\n"
        "/search — пошук нотаток за словом\n"
        "/tagsearch — пошук нотаток за тегом"
    )

@dp.message(Command("add"))
async def cmd_add(message: types.Message, state: FSMContext):
    await message.answer("Введіть текст нотатки:")
    await state.set_state(AddNoteState.waiting_for_note)

@dp.message(AddNoteState.waiting_for_note)
async def process_note(message: types.Message, state: FSMContext):
    await state.update_data(note=message.text)
    await message.answer(
        "Введіть теги через кому (наприклад: робота, ідеї), або відправте '-' якщо без тегів:"
    )
    await state.set_state(AddNoteState.waiting_for_tags)

@dp.message(AddNoteState.waiting_for_tags)
async def process_tags(message: types.Message, state: FSMContext):
    data = await state.get_data()
    note = data["note"]
    text = message.text.strip()
    if text in ["-", "нема", "none"]:
        tags = []
    else:
        tags = [t.strip() for t in text.split(",") if t.strip()]
    assistant.add_note(note, tags=tags)
    await message.answer("Нотатку додано.")
    await state.clear()

@dp.message(Command("list"))
async def cmd_list(message: types.Message):
    notes = assistant.list_notes()
    if not notes:
        await message.answer("Немає нотаток.")
        return
    text = ""
    for i, n in enumerate(notes, 1):
        tags = f" [Теги: {', '.join(n['tags'])}]" if n['tags'] else ""
        text += f"{i}. {n['note']}{tags}\n"
    await message.answer(text)

@dp.message(Command("search"))
async def cmd_search(message: types.Message, state: FSMContext):
    await message.answer("Введіть ключове слово для пошуку:")
    await state.set_state(SearchNoteState.waiting_for_keyword)

@dp.message(SearchNoteState.waiting_for_keyword)
async def process_search(message: types.Message, state: FSMContext):
    keyword = message.text
    found = assistant.search_notes(keyword)
    if not found:
        await message.answer("Нічого не знайдено.")
    else:
        text = ""
        for n in found:
            tags = f" [Теги: {', '.join(n['tags'])}]" if n['tags'] else ""
            text += f"- {n['note']}{tags}\n"
        await message.answer(text)
    await state.clear()

@dp.message(Command("tagsearch"))
async def cmd_tagsearch(message: types.Message, state: FSMContext):
    await message.answer("Введіть тег для пошуку (наприклад: робота):")
    await state.set_state(TagSearchState.waiting_for_tag)

@dp.message(TagSearchState.waiting_for_tag)
async def process_tagsearch(message: types.Message, state: FSMContext):
    tag = message.text.strip()
    found = assistant.search_by_tag(tag)
    if not found:
        await message.answer("Нічого не знайдено за цим тегом.")
    else:
        text = ""
        for n in found:
            tags = f" [Теги: {', '.join(n['tags'])}]" if n['tags'] else ""
            text += f"- {n['note']}{tags}\n"
        await message.answer(text)
    await state.clear()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
