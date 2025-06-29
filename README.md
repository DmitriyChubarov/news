# Задание
### Необходимо создать сервер авторизации и новостей с комментариями и лайками на Django с использованием RestFramework на python 3.
### Модели:
 - Users (имя пользователя, пароль в зашифрованном виде)<img src="https://cdn-icons-png.flaticon.com/512/14090/14090371.png" alt="галочка" width="16" style="vertical-align: middle;">
 - News (дата новости, заголовок новости, текст новости, автор)<img src="https://cdn-icons-png.flaticon.com/512/14090/14090371.png" alt="галочка" width="16" style="vertical-align: middle;">
 - Comments (Дата комментария, текст комментария, автор)<img src="https://cdn-icons-png.flaticon.com/512/14090/14090371.png" alt="галочка" width="16" style="vertical-align: middle;">
 - Опционально: Tokens (при авторизации можно создавать токены и хранить их в базе или использовать JWT токены)<img src="https://cdn-icons-png.flaticon.com/512/14090/14090371.png" alt="галочка" width="16" style="vertical-align: middle;">
   
### Интерфейс:
 - У каждого пользователя может быть две роли – пользователь и админ, админ может зайти в админ-панель, пользователь – нет. <img src="https://cdn-icons-png.flaticon.com/512/14090/14090371.png" alt="галочка" width="16" style="vertical-align: middle;">
 - Каждый пользователь может создать новость. <img src="https://cdn-icons-png.flaticon.com/512/14090/14090371.png" alt="галочка" width="16" style="vertical-align: middle;">
 - Все пользователи могут получать списки всех новостей с пагинацией. <img src="https://cdn-icons-png.flaticon.com/512/14090/14090371.png" alt="галочка" width="16" style="vertical-align: middle;">
 - Пользователи могут удалять и изменять свои новости.<img src="https://cdn-icons-png.flaticon.com/512/14090/14090371.png" alt="галочка" width="16" style="vertical-align: middle;">
 - Админ может удалять и изменять любую новость.<img src="https://cdn-icons-png.flaticon.com/512/14090/14090371.png" alt="галочка" width="16" style="vertical-align: middle;">
 - Также нужно добавить механизм лайков и комментариев новостей – лайкать и комментировать может любой пользователь
 - Автор может удалять комментарии к своим новостям
 - Админ может удалять любые комментарии.
 - При получении списка новостей и одной конкретной новости нужно показать количество лайков и комментариев.
 - Плюсом будет добавление списка последних 10 комментариев при получении списка новостей и одной новости.

### Роуты
 - POST register (передаем имя пользователя и пароль) <img src="https://cdn-icons-png.flaticon.com/512/14090/14090371.png" alt="галочка" width="16" style="vertical-align: middle;">
 - POST auth (передаем имя пользователя и пароль, получаем токен если пользователь с таким паролем есть и ошибку, если такого пользователя нет) <img src="https://cdn-icons-png.flaticon.com/512/14090/14090371.png" alt="галочка" width="16" style="vertical-align: middle;">
 - GET news (получаем список новостей с пагинацией) <img src="https://cdn-icons-png.flaticon.com/512/14090/14090371.png" alt="галочка" width="16" style="vertical-align: middle;">
 - POST news (создаем новость, проверка на авторизацию)<img src="https://cdn-icons-png.flaticon.com/512/14090/14090371.png" alt="галочка" width="16" style="vertical-align: middle;">
 - PATCH news (обновляем новость, проерка на атворизацию, проверка на наличие прав) <img src="https://cdn-icons-png.flaticon.com/512/14090/14090371.png" alt="галочка" width="16" style="vertical-align: middle;">
 - DELETE news (удаляем новость, проверка на авторизацию, проверка на наличие прав) <img src="https://cdn-icons-png.flaticon.com/512/14090/14090371.png" alt="галочка" width="16" style="vertical-align: middle;">
 - GET comments (получение списка комментариев новости с пагинацией)
 - POST comments (создание нового комментария, проверка на авторизацию)<img src="https://cdn-icons-png.flaticon.com/512/14090/14090371.png" alt="галочка" width="16" style="vertical-align: middle;">
 - DELETE comments<img src="https://cdn-icons-png.flaticon.com/512/14090/14090371.png" alt="галочка" width="16" style="vertical-align: middle;">
 - Нужна стандартная админка Django (пользователи админки могут не пересекаться с пользователями в таблице Users)
