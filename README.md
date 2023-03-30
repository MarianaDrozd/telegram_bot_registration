# telegram_bot_registration
A simple telegram bot for registration on website.
For running locally:
- clone the repo;
- create virtual environment;
- rename .env.example to .env;
- run `pip install -r requirements.txt`;
- run migrations: `python manage.py migrate`;
- run server `python manage.py runserver`;
- open another terminal tab and run `python telegram_registration/bot.py` for running Telegram bot.
This code was deployed to pythonanywhere: http://tgbotdjango.pythonanywhere.com/
