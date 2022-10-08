# Проект парсинга pep
### Режимы работы
Запуск парсера информации из статей о нововведениях в Python
```
python main.py whats-new
```
Запуск парсера статусов версий Python
```
python main.py latest-versions
```
Запуск парсера, который скачивает архив документации Python
```
python main.py download
```
Запуск парсинга документов PEP
```
python main.py pep
```

### Аргументы командной строки

```
positional arguments:
  {whats-new,latest-versions,download,pep}      Режимы работы парсера

optional arguments:
  -h, --help                                    show this help message and exit
  -c, --clear-cache                             Очистка кеша
  -o {pretty,file}, --output {pretty,file}      Дополнительные способы вывода данных
```