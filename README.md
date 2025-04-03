

### Асинхронный парсер PEP

[](https://github.com/IvalexAnna/scrapy_parser_pep/blob/main/README.md#%D0%B0%D1%81%D0%B8%D0%BD%D1%85%D1%80%D0%BE%D0%BD%D0%BD%D1%8B%D0%B9-%D0%BF%D0%B0%D1%80%D1%81%D0%B5%D1%80-pep)

Парсер документов PEP на базе фреймворка Scrapy.

## Описание

[](https://github.com/IvalexAnna/scrapy_parser_pep/blob/main/README.md#%D0%BE%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5)

- Собирает номер, название и статус всех PEP.
- Подсчитывает общее количество каждого статуса, а также общую сумму всех статусов.

Парсер собирает данные с сайта `https://www.python.org/`

Вся собранная информация сохраняется в файлах `csv` в папке `results/...`

## Как запустить проект

[](https://github.com/IvalexAnna/scrapy_parser_pep/blob/main/README.md#%D0%BA%D0%B0%D0%BA-%D0%B7%D0%B0%D0%BF%D1%83%D1%81%D1%82%D0%B8%D1%82%D1%8C-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82)

1. Клонировать репозиторий:

```python
git clone https://github.com/IvalexAnna/scrapy_parser_pep.git
```

2. Создать виртуальное окружение:

```python
python -m venv venv
```

3. Активировать виртуальное окружение, обновить версию `pip` и установить зависимости из `requirements.txt`:

```python
source venv/bin/activate
```

```python
python -m pip install -–upgrade pip.
```

```python
pip install -r requirements.txt
```

4. Запустить в консоле:

```python
scrapy crawl pep
```

[Ivanova Anna](https://github.com/IvalexAnna)