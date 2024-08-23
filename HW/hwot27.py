from jinja2 import Template

spisok = [
    {"href": "index", "zagolov": "Главная"},
    {"href": "news", "zagolov": "Новости"},
    {"href": "about", "zagolov": "О компании"},
    {"href": "shop", "zagolov": "Магазин"},
    {"href": "contacts", "zagolov": "Контакты"}
]

link = """
<ul>
    {% for s in spisok -%}
        {% if s.zagolov == "Главная" %}
            <li><a href="/{{ s.href }}" class="active">{{ s.zagolov }}</a></li>
        {% else %}
            <li><a href="/{{ s.href }}">{{ s.zagolov }}</a></li>
        {% endif -%}
    {% endfor -%}
</ul>
"""

tm = Template(link)
msg = tm.render(spisok=spisok)
print(msg)
