def send_email(message, recipient, c = None):
    sender = "university.help@gmail.com"
    recipient = "the.elizzaveta@gmail.com"
    c = "@" ".com" ".net" ".ru"
    if c is None:
        print("Enter your email")



send_email('Это сообщение для проверки связи', "the.elizzaveta@gmail.com")
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender  ='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
