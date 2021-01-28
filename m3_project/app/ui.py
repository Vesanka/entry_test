from objectpack.ui import BaseEditWindow, make_combo_box
from m3_ext.ui import all_components as ext

from django.contrib.auth.models import User
import datetime
import app.actions
import app.controller


class UserAddWindow(BaseEditWindow):

    def _init_components(self):
        """
        Здесь следует инициализировать компоненты окна и складывать их в
        :attr:`self`.
        """
        super(UserAddWindow, self)._init_components()

        self.field__password = ext.ExtStringField(
            label=u'password',
            name='password',
            allow_blank=False,
            anchor='100%'
        )

        self.field__last_login = ext.ExtDateField(
            label=u'last login',
            name='last_login',
            anchor='100%')

        self.field__is_superuser = ext.ExtCheckBox(
            label=u'superuser',
            name='superuser',
            checked=False,
            anchor='100%'
        )

        self.field__username = ext.ExtStringField(
            label=u'username',
            name='username',
            allow_blank=False,
            anchor='100%')

        self.field__first_name = ext.ExtStringField(
            label=u'first name',
            name='first_name',
            anchor='100%')

        self.field__last_name = ext.ExtStringField(
            label=u'last name',
            name='last_name',
            anchor='100%')

        self.field__email = ext.ExtStringField(
            label=u'email address',
            name='email',
            anchor='100%')

        self.field__is_staff = ext.ExtCheckBox(
            label=u'is staff',
            name='is_staff',
            checked=False,
            anchor='100%'
        )

        self.field__is_active = ext.ExtCheckBox(
            label=u'is active',
            name='is_active',
            checked=True,
            anchor='100%'
        )

        self.field__joined = ext.ExtDateField(
            label=u'date joined',
            name='joined',
            value=datetime.date.today,
            anchor='100%')

    def _do_layout(self):
        """
        Здесь размещаем компоненты в окне
        """
        super(UserAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__password,
            self.field__last_login,
            self.field__is_superuser,
            self.field__username,
            self.field__first_name,
            self.field__last_name,
            self.field__email,
            self.field__is_staff,
            self.field__is_active,
            self.field__joined
        ))

    def set_params(self, params):
        """
        Установка параметров окна

        :params: Словарь с параметрами, передается из пака
        """
        super(UserAddWindow, self).set_params(params)
        self.height = 'auto'


class PermissionAddWindow(BaseEditWindow):
    
    def _init_components(self):
        """
        Здесь следует инициализировать компоненты окна и складывать их в
        :attr:`self`.
        """
        super(PermissionAddWindow, self)._init_components()
    
        self.field__name = ext.ExtStringField(
            label=u'name',
            name='name',
            allow_blank=False,
            anchor='100%'
        )

        self.field__content_type = ext.ExtDictSelectField(
            label=u'content type',
            name='content_type',
            pack=app.actions.ContentTypePack
        )

        self.field__codename = ext.ExtStringField(
            label=u'codename',
            name='codename',
            allow_blank=False,
            anchor='100%'
        )
   
    def _do_layout(self):
        """
        Здесь размещаем компоненты в окне
        """
        super(PermissionAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__name,
            self.field__content_type,
            self.field__codename
        ))

    def set_params(self, params):
        """
        Установка параметров окна

        :params: Словарь с параметрами, передается из пака
        """
        super(PermissionAddWindow, self).set_params(params)
        self.height = 'auto'