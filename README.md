# Загрузка в Telegram фотографий космоса

Программа позволяет автоматически выкладывать фотографии в Telegram-канал через бота с указанной задержкой между постами, а также скачивать фотографии космоса от NASA и SpaceX. Программа создаёт три папки: `NASA_APOD`, `NASA_EPIC` и `SpaceX`, и сохраняет фотографии в соответствующие директории. Бот берет фотографии именно из этих папок.

## Установка

1. **Настройка окружения:**
   - В корневой директории проекта создайте файл `.env` и добавьте в него следующие строки:
     ```
     NASA_API=
     TG_BOT_API=
     TG_CHANNEL_ID=
     DELAY_HOURS=
     ```
   - Заполните значения после знака `=`:
     - `NASA_API` — ваш API-ключ NASA. Получить его можно на [официальном сайте NASA](https://api.nasa.gov/).
     - `TG_BOT_API` — токен вашего Telegram-бота. Для его получения создайте бота через [BotFather](https://core.telegram.org/bots#botfather) в Telegram.
     - `TG_CHANNEL_ID` — ссылка на ваш канал в формате `@Channel`.
     - `DELAY_HOURS` — задержка между постами в часах. Если не указана, по умолчанию 4 часа.

2. **Установка зависимостей:**
   - Убедитесь, что у вас установлен Python 3.
   - Откройте командную строку и перейдите в папку с проектом:
     ```
     cd путь/к/папке/с/проектом
     ```
   - Обновите `pip` и установите зависимости:
     ```
     pip install --upgrade pip
     pip install -r requirements.txt
     ```

## Использование

1. **Скачивание фотографий NASA APOD (Astronomy Picture of the Day):**
```
python download_nasa_apod_images.py
```
Программа скачает 100 случайных фотографий дня.

2. **Скачивание фотографий NASA EPIC (Earth Polychromatic Imaging Camera):**
```
python download_nasa_epic_images.py
```
Программа скачает доступные снимки Земли из NASA EPIC.

3. **Скачивание фотографий определённого запуска SpaceX:**
```
python download_spacex_launch_images.py --id <ID_запуска>
```
Замените `<ID_запуска>` на ID интересующего вас запуска.

4. **Скачивание фотографий последнего запуска SpaceX:**
```
python download_spacex_launch_images.py
```
Программа скачает фотографии последнего доступного запуска SpaceX.

5. **Запуск бота с указанием времени задержки между постами:**
```
python launch_telegram_bot.py --hours <количество_часов>
```
Замените `<количество_часов>` на желаемое значение задержки между постами в часах.

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).