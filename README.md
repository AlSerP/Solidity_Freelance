## Скачать проект с репозитория

Клонирование репозитоория:

```bash
$ git clone https://github.com/AlSerP/Solidity_Freelance
```

## Работа с *git*

```bash
$ git remote add origin https://github.com/AlSerP/Solidity_Freelance.git
```

Загрузить изменения с репозитория:

```bash
$ git pull
```

Создать новую ветку:

```bash
$ git checkout -b new_branch
```

Переключиться на существующую ветку:

```bash
$ git checkout  old_branch
```

Добавить файлы с изменениями:

```bash
$ git add file1 file2 folder/
```

Сделать коммит:

```bash
$ git commit -m "new commit"
```

Отправить изменения на репозиторий:

```bash
$ git push origin branch
```

## Venv

Создание Venv'а:

```bash
$ python3 -m venv new_venv
```

Если получаем ошибку:
*"The virtual environment was not created successfully because ensurepip is not available... "*

Нужно дополнительно установить:

```bash
sudo apt-get install python3-venv
```

Вход в *venv*:

```bash
$ source new_venv/bin/activate
```

Для выхода из виртуального окружения *venv* наберите:

```bash
deactivate
```

Установка *pygame*:

```bash
(bomberman_venv) ~$ python3 -m pip install --upgrade pip
(bomberman_venv) ~$ pip install pygame
```
