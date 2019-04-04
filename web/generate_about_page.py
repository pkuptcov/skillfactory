# coding: utf-8
from web import horoscope


def generate_page(head, body):
    page = f"<html>{head}{body}</html>"
    return page


def generate_head(title):
    head = f"""<head>
    <meta charset='utf-8'>
    <title>{title}</title>
    </head>
    """
    return head


def generate_body(header):
    body = f"<h1>{header}</h1>"
    time_list = ""
    for time in horoscope.times:
        time_list += f"<li>{time.capitalize()};</li>"
    times = f"<b>Времена дня:</b><ul>{time_list}</ul>"

    advice_list = ""
    for advice in horoscope.advices:
        advice_list += f"<li>{advice};</li>"
    advices = f"<b>Глаголы:</b><ul>{advice_list}</ul>"

    promise_list = ""
    for promise in horoscope.promises:
        promise_list += f"<li>{promise};</li>"
    promises = f"<b>Ожидания:</b><ul>{promise_list}</ul>"

    image = "<img src='crayfish.gif' height=100px width=100px />"
    link = "<hr><a href='index.html'>Главная</a>"
    body += f"{image}<ol><li>{times}</li><li>{advices}</li><li>{promises}</li></ol>{link}"
    return f"<body>{body}</body>"


def save_page(title, header, output="about.html"):
    fp = open(output, "w", encoding='utf-8')
    page = generate_page(
        head=generate_head(title),
        body=generate_body(header=header)
    )
    print(page, file=fp)
    fp.close()


save_page(
    title="Гороскоп на сегодня",
    header="О чем все это"
)

