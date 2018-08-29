# Github Trends

Скрипт выводит список созданных за последнюю неделю **Github**-репозиториев с данными о количестве **"звезд"** и открытых **issues** для них.

# Предварительные настройки

- Установить и запустить [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) для Python
- Установить дополнительные пакеты:
```
pip install -r requirements.txt
```

# Как запустить

Скрипт требует для своей работы установленного интерпретатора **Python** версии **3.5**.

**Запуск на Linux**

```bash
$ python github_trending.py # или python3, в зависимости от настроек системы

# результат выполнения скрипта
https://github.com/felixrieseberg/windows95
Stars: 9928
Open Issues: 49

https://github.com/GoogleChromeLabs/size-plugin
Stars: 861
Open Issues: 8

https://github.com/iReaderAndroid/X2C
Stars: 804
Open Issues: 7

# в случае ошибки запроса данных
Failed to connect to Github

# в случае ошибки загрузки данных запроса
Failed to load repositories data (incorrect format)

```

Запуск на **Windows** происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
