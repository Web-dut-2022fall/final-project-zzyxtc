from django import template

register = template.Library()


@register.simple_tag()
def check_collected_book(user, book_object):
    if user.is_anonymous:
        return False

    return True if user.collection.books.filter(id=book_object.id).all() \
        else False


@register.simple_tag()
def check_collected_discussion(user, discussion):
    if user.is_anonymous:
        return False

    return True if user.collection.discussions.filter(id=discussion.id).all() \
        else False


@register.simple_tag
def get_omit_discussions(user, num=5):
    """
    得到指定数量的某一用户的讨论
    """
    return user.discussions.all()[:num]


@register.simple_tag
def get_omit_replys(user, num=5):
    """
    得到指定用户的回复
    """
    return user.replys.all()[:num]


@register.inclusion_tag('tag/show_user_replys.html')
def show_user_replys(replys):
    context = {
        'replys': replys,
    }
    return context


@register.inclusion_tag('tag/common_field.html')
def field(field):
    """
    返回一个常用的渲染表单字段的html代码

    :field: 将要渲染的表单字段对象
    :return: 用在模板里的上下文
    """
    context = {
        'field': field,
    }
    return context
