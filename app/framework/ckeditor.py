#-*- coding: utf-8 -*-

from flask.ext.wtf import Form
from flask import url_for
from wtforms import TextField, Field
import simplejson as json

########################################################################
class CKEditorWidget(object):
    def __init__(self, import_js=False, ckeditor_config=None):
        self.ckeditor_cfg = ckeditor_config
        self.import_js = import_js
    #----------------------------------------------------------------------
    def __call__(self, field):
        if self.import_js:
            # 如果页面不提供ckeditor.js，则自己取到js
            static_dir = url_for('static', filename='base/3partylib/ckeditor/ckeditor.js')
            html  = '<script src="{}"></script> \
                     <textarea name="{}" id="{}">\
                        {}\
                     </textarea>\
                     <script>\
                        CKEDITOR.replace( "{}", {});\
                     </script>'
            html = str.format(html, static_dir, field.name, field.id, field.data or '', field.id, json.dumps(self.ckeditor_cfg))
        else:
            html  = '<textarea name="{}" id="{}">\
                        {}\
                     </textarea>\
                     <script>\
                        CKEDITOR.replace( "{}", {});\
                     </script>'            
            html = str.format(html, field.name, field.id, field.data or '', field.id, json.dumps(self.ckeditor_cfg))
        
        return html

class CKEditorField(Field):
    def __init__(self, label=None, validators=None, filters=tuple(), 
                description='', id=None, default=None, 
                widget=None, _form=None, _name=None, 
                _prefix='', _translations=None, import_js=False, ckeditor_config={'filebrowserBrowseUrl': '', 'filebrowserUploadUrl': '/a.php'}):
        super(CKEditorField, self).__init__(label=label, validators=validators, filters=filters, 
                description=description, id=id, default=default, 
                widget=widget, _form=_form, _name=_name, 
                _prefix=_prefix, _translations=_translations)
        self.widget = CKEditorWidget(import_js=import_js, ckeditor_config=ckeditor_config)