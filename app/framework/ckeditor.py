#-*- coding: utf-8 -*-

import re

from wtforms import ValidationError
from wtforms import TextField, Field
from wtforms.widgets import HTMLString
from flask_wtf import Form
from flask import url_for
from flask_babel import gettext
import simplejson as json


########################################################################
class CKEditorWidget(object):
    def __init__(self, import_js=False, ckeditor_config_file_path=None, ckeditor_config=None):
        self.ckeditor_config_file_path = ckeditor_config_file_path
        self.ckeditor_cfg = ckeditor_config
        self.import_js = import_js
    #----------------------------------------------------------------------
    def __call__(self, field, **kwargs):
        import time
        current_milli_time = lambda: int(round(time.time() * 1000))
        html_no_script = '\
                <textarea name="{}" id="{}">\n\
                   {}\n\
                </textarea>\n\
                <script>\n\
                   var ck_{} = CKEDITOR.replace("{}", {});\n\
                   function {}_ckeditor_ready(evt){{\n\
                       var __captcha = $("#{}").parents("form").find(".captcha");\n\
                       if(__captcha.length != 0){{\n\
                           var __anytime = new Date().getTime();\n\
                           __captcha.prepend(\'<img src="/common/captcha/?nothing=' + str(current_milli_time()) + '">\');\n\
                           __captcha.click(function(){{\n\
                                var __anything = new Date().getTime();\n\
                                __captcha.find("img").attr("src", "/common/captcha/?nothing="' + '+__anything);\n\
                           }});\n\
                       }}\n\
                   }}\n\
                   ck_{}.on("instanceReady", {}_ckeditor_ready);\n\
                   \n\
                </script>\n'

        if self.ckeditor_config_file_path:
            self.ckeditor_cfg['customConfig'] = url_for('static', filename=self.ckeditor_config_file_path)

        config_str = json.dumps(self.ckeditor_cfg)
        if self.import_js:
            # 如果页面不提供ckeditor.js，则自己取到js
            static_dir = url_for('static', filename='base/3partylib/ckeditor/ckeditor.js')
            html  = '<script src="{}"></script>\n' + html_no_script

            html = str.format(html, static_dir, field.name, field.id, field.data or '', field.id, field.id, config_str,
                              field.id, field.id, field.id, field.id)
        else:
            html = str.format(html_no_script, field.name, field.id, field.data or '', field.id, field.id, config_str,
                              field.id, field.id, field.id, field.id)

        return HTMLString(html)

class CKEditorRequired(object):
    """Validate the empty content fo the ckeditor"""
    def __init__(self, message=None):
        if not message:
            message = gettext(u"Content can't be empty")
        self.message = message

    def __call__(self, form, field):
        content = re.sub('<p>\s*</p>\n*', '', field.data)
        field.data = content
        if len(content) == 0:
            raise ValidationError(self.message)


class CKEditorField(Field):
    def __init__(self, label=None, validators=None, filters=tuple(),
                description='', id=None, default=None,
                widget=None, _form=None, _name=None,
                _prefix='', _translations=None, import_js=False,
                ckeditor_config_file_path=None,
                ckeditor_config={'filebrowserUploadUrl': '/uploader/upload', 'filebrowserBrowseUrl': ''}):
        super(CKEditorField, self).__init__(label=label, validators=validators, filters=filters,
                description=description, id=id, default=default,
                widget=widget, _form=_form, _name=_name,
                _prefix=_prefix, _translations=_translations)
        self.widget = CKEditorWidget(import_js=import_js, ckeditor_config_file_path=ckeditor_config_file_path, ckeditor_config=ckeditor_config)
