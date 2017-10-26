# flask-babel-example

### 설치하기 
```
pip install flask-babel 
```

### .pot 파일 만들기 

```shell
$ pybabel extract -F babel.cfg -o messages.pot ./
extracting messages from app.py
extracting messages from config.py
extracting messages from templates/index.html (extensions="jinja2.ext.autoescape,jinja2.ext.with_")
writing PO template file to messages.pot

$ cat messages.pot  
msgid ""
msgstr "" 
```

### 언어별 디렉토리 생성 
```
$ pybabel init -i messages.pot -d ./translations -l en
creating catalog ./translations/en/LC_MESSAGES/messages.po based on messages.pot
$ pybabel init -i messages.pot -d ./translations -l ja
creating catalog ./translations/ja/LC_MESSAGES/messages.po based on messages.pot
$  pybabel init -i messages.pot -d ./translations -l zh
creating catalog ./translations/zh/LC_MESSAGES/messages.po based on messages.pot

$ translations  ls -al 
합계 20
drwxrwxr-x 5 ash84 ash84 4096 2017-10-26 13:13 .
drwxrwxr-x 6 ash84 ash84 4096 2017-10-26 13:13 ..
drwxrwxr-x 3 ash84 ash84 4096 2017-10-26 13:13 en
drwxrwxr-x 3 ash84 ash84 4096 2017-10-26 13:13 ja
drwxrwxr-x 3 ash84 ash84 4096 2017-10-26 13:13 zh
```

### .po 파일에 번역본 넣기 

```
# ko 
msgid "user_name_label"
msgstr "사용자 이름 : "
```


```
# zh 
msgid "user_name_label"
msgstr "用户名 : "
```

### 컴파일 하기 

```
$ pybabel compile -f -d ./translations
compiling catalog ./translations/zh/LC_MESSAGES/messages.po to ./translations/zh/LC_MESSAGES/messages.mo
compiling catalog ./translations/en/LC_MESSAGES/messages.po to ./translations/en/LC_MESSAGES/messages.mo
compiling catalog ./translations/ko/LC_MESSAGES/messages.po to ./translations/ko/LC_MESSAGES/messages.mo
compiling catalog ./translations/ja/LC_MESSAGES/messages.po to ./translations/ja/LC_MESSAGES/messages.mo
```

### 사용하기 

```python
@babel.localeselector
def get_locale():
    return str(request.accept_languages)
```

```html
<body>
<H1>HELLO</H1>
{{ _('user_name_label') }} {{user_name}}
</body>
```

