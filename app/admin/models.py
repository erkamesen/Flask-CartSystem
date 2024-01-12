from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from wtforms import validators
from flask import redirect, url_for, request


class MyModelView(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated and getattr(current_user, 'is_admin', False)

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('_user.login', next=request.url))


class CourseModelView(MyModelView):
    column_list = ('name', 'price', 'category')
    form_columns = ('name', 'description', 'price', 'category',
                    'image', 'total_hours', 'is_active')
    column_searchable_list = ('name',)
    column_filters = ('category.name', )
    form_args = {
        'name': {
            'validators': [validators.DataRequired()]
        },
        'price': {
            'validators': [validators.NumberRange(min=0)]
        },
        'stock': {
            'validators': [validators.NumberRange(min=0)]
        }
    }


class CategoryModelView(MyModelView):
    column_list = ('name',)
    form_columns = ('name',)
    form_args = {
        'name': {
            'validators': [validators.DataRequired()]
        }
    }


class UserModelView(MyModelView):
    column_exclude_list = ["password"]
    form_excluded_columns = ["password"]
    column_searchable_list = ["username", "email"]
