from assistant import Assistant

def main():
    assistant = Assistant()
    print("Консольний асистент запущено. Команди: /add, /list, /search, /tagsearch, /exit")
    while True:
        cmd = input("> ").strip()
        if cmd == "/add":
            note = input("Введіть нотатку: ")
            tags = input("Теги (через кому, опціонально): ").strip()
            tags_list = [t.strip() for t in tags.split(",")] if tags else []
            assistant.add_note(note, tags=tags_list)
            print("Нотатку додано.")
        elif cmd == "/list":
            notes = assistant.list_notes()
            if not notes:
                print("Немає нотаток.")
            for i, n in enumerate(notes, 1):
                tags = f" [Теги: {', '.join(n['tags'])}]" if n['tags'] else ""
                print(f"{i}. {n['note']}{tags}")
        elif cmd == "/search":
            keyword = input("Введіть ключове слово: ")
            found = assistant.search_notes(keyword)
            if not found:
                print("Нічого не знайдено.")
            for n in found:
                tags = f" [Теги: {', '.join(n['tags'])}]" if n['tags'] else ""
                print(f"- {n['note']}{tags}")
        elif cmd == "/tagsearch":
            tag = input("Введіть тег для пошуку: ").strip()
            found = assistant.search_by_tag(tag)
            if not found:
                print("Нічого не знайдено за цим тегом.")
            for n in found:
                tags = f" [Теги: {', '.join(n['tags'])}]" if n['tags'] else ""
                print(f"- {n['note']}{tags}")
        elif cmd == "/exit":
            print("Бб")
            break
        else:
            print("Невідома команда.")


if __name__ == "__main__":
    main()
