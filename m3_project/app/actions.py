from functools import partial
 
from m3 import actions as m3_actions
 
import objectpack
from objectpack import tree_object_pack
from objectpack.filters import FilterByField, ColumnFilterEngine
from .controller import observer
from objectpack.actions import ObjectPack
from objectpack.slave_object_pack import SlavePack
 
from .models import *
from .ui import *
from django.contrib.auth import models

class ContentTypePack(ObjectPack):

    model = models.ContentType

    add_window = edit_window = objectpack.ui.ModelEditWindow.fabricate(model)

    add_to_menu = True
    add_to_desktop = True

class UserPack(ObjectPack):

    model = models.User

    add_window = edit_window = UserAddWindow

    add_to_menu = True
    add_to_desktop = True


class GroupPack(ObjectPack):

    model = models.Group

    add_window = edit_window = objectpack.ui.ModelEditWindow.fabricate(model)

    add_to_menu = True
    add_to_desktop = True

class PermissionPack(ObjectPack):

    model = models.Permission
    
#    add_window = edit_window = PermissionAddWindow
    add_window = edit_window = objectpack.ui.ModelEditWindow.fabricate(model)

    add_to_menu = True
    add_to_desktop = True
