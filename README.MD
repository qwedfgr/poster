# Публикуем записи сразу в ВК, FB и telegram

Проект служит для автоматического публикации постов в группах ВКонтакте, Facebook и канале телеграм.

### Как установить
Для использования скрипта необходимо зарегистрировать приложение для ВКонтакте и получить персональный ключ доступа.
Также узнать id сообщества, в котором будет совершаться публикация. 
Для телеграма необходимо зарегистрировать бота и получить его токен. Бота следует добавить в канал в качестве администратора.
Для Facebook следует зарегистрировать приложение и получить токен доступа. Выдать приложению разрешение `publish_to_groups`.
Все параметры необходимо присвоить переменным в файле `.env`.
Пример можно посмотреть в файле `env_exmple`

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
### Как запустить
Для запуска выполните
```bash
python main.py
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).