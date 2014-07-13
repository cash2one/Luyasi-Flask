# -*- coding: utf-8 -*-
"""
    Framework need widget
    ~~~~~~~~~~~

    Capthcha widget

    :copyright: (c) 2014 by Kinorsi -- <kinorsi@gmail.com>
    :license: BSD, see LICENSE for more details.
"""
from wtforms.widgets import HTMLString, html_params, Input, Select

class CaptchaWidget(object):
    #----------------------------------------------------------------------
    def __call__(self, field, **kwargs):
        html  = "<div class='row'>\
                    <div class='col-md-3'>\
                        <a href='#' class='captcha'></a>\
                    </div>\
                    <div class='col-md-9'>\
                        <input %s/>\
                    </div>\
                </div>"
        kwargs.setdefault('id', field.id)
        kwargs.setdefault('name', field.name)
        attr = html_params(**kwargs)
        html = HTMLString(html % attr)
        return html

class DatetimeWidget(Input):
    """Datetime picker widget. Only add class _datetime in the input tag."""
    #----------------------------------------------------------------------
    def __init__(self):
        """"""
        self.input_type='text'

    #----------------------------------------------------------------------
    def __call__(self, field, **kwargs):
        cls = kwargs.get('class', None)
        if cls is not None:
            cls = cls + ' _datetime'
            kwargs['class'] = cls
        else:
            kwargs.setdefault('class', '_datetime')

        html = super(DatetimeWidget, self).__call__(field, **kwargs)
        return html
    
########################################################################
class Select2Widget(Select):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        
        
    
    