from django import template

register = template.Library()


@register.filter(name='is_done')
def todos_filter(todos, state=True):
    return [todo for todo in todos if todo.is_done is state]
