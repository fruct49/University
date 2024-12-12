import random
from utils import load_words, get_record, save_record


def display_word(word, guessed_letters):
    return ''.join([char if char in guessed_letters else '■' for char in word])


def play_game():
    try:
        words = load_words()
    except Exception as e:
        print(f"Ошибка загрузки слов: {e}")
        return

    record = get_record()
    print(f"Ваш текущий рекорд: {record}")

    guessed_words_count = 0
    while True:
        word = random.choice(words).lower()
        guessed_letters = set()
        lives = select_difficulty()
        print("\nНачинаем игру!")

        while lives > 0:
            print(f"\nСлово: {display_word(word, guessed_letters)}")
            print(f"Количество жизней: {'♥' * lives}")

            guess = input("Назовите букву или слово целиком: ").lower().strip()

            # Проверка, является ли введённое значение цифрой
            if guess.isdigit():
                print("Ошибка: Вы ввели цифру. Пожалуйста, вводите только буквы.")
                continue  # Пропускаем этот ход, не уменьшаем количество жизней

            if len(guess) == 1:
                if guess in guessed_letters:
                    print("Вы уже называли эту букву.")
                elif guess in word:
                    print("Правильно!")
                    guessed_letters.add(guess)
                else:
                    print("Неправильно! Вы теряете жизнь.")
                    lives -= 1
            elif len(guess) == len(word):
                if guess == word:
                    print(f"Поздравляем! Вы угадали слово: {word}")
                    guessed_words_count += 1
                    break
                else:
                    print("Неправильно! Вы теряете жизнь.")
                    lives -= 1
            else:
                print("Некорректный ввод. Попробуйте ещё раз.")

            if all(char in guessed_letters for char in word):
                print(f"Поздравляем! Вы угадали слово: {word}")
                guessed_words_count += 1
                break

        if lives == 0:
            print(f"Вы проиграли. Слово было: {word}")

        if input("Хотите сыграть ещё раз? (да/нет): ").lower() != "да":
            break

    print(f"Вы угадали {guessed_words_count} слов.")
    if guessed_words_count > record:
        print("Поздравляем! Вы установили новый рекорд!")
        save_record(guessed_words_count)
    else:
        print(f"Ваш рекорд: {record}. До новых встреч!")


def select_difficulty():
    while True:
        print("\nВыберите уровень сложности:")
        print("1. Лёгкий (7 жизней)")
        print("2. Средний (5 жизней)")
        print("3. Сложный (3 жизни)")
        choice = input("Введите номер уровня: ").strip()
        if choice == "1":
            return 7
        elif choice == "2":
            return 5
        elif choice == "3":
            return 3
        else:
            print("Некорректный выбор. Попробуйте снова.")


if __name__ == "__main__":
    play_game()
