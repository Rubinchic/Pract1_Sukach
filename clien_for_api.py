import requests
import json

API_URL = "https://rubinchic.site/api/movies"

def fetch_movies():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json().get("data", [])
    else:
        print("❌ Не вдалося отримати дані з API.")
        return []

def show_movies(movies):
    print("\n🎬 Усі фільми:")
    for idx, movie in enumerate(movies, 1):
        print(f"{idx}. {movie['title']} ({movie['year']}) — {movie['genre']}, рейтинг: {movie['rating']}")

def select_movies(movies):
    selected = []
    print("\nВведіть номери фільмів через кому, які хочете зберегти (наприклад: 1,3,5):")
    choices = input(">>> ")
    try:
        indices = [int(i.strip()) - 1 for i in choices.split(",")]
        selected = [movies[i] for i in indices if 0 <= i < len(movies)]
    except ValueError:
        print("❌ Некоректне введення. Будь ласка, введіть лише номери.")
    return selected

def save_to_file(movies, filename="selected_movies.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(movies, f, ensure_ascii=False, indent=2)
    print(f"✅ Збережено {len(movies)} фільм(ів) у файл: {filename}")

def main():
    movies = fetch_movies()
    if not movies:
        return

    show_movies(movies)
    selected = select_movies(movies)

    if selected:
        save_to_file(selected)
    else:
        print("ℹ️ Жодного фільму не обрано — файл не створено.")

if __name__ == "__main__":
    main()
