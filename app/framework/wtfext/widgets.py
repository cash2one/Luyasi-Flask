# -*- coding: utf-8 -*-
"""
    Framework need widget
    ~~~~~~~~~~~

    Capthcha widget

    :copyright: (c) 2014 by Kinorsi -- <kinorsi@gmail.com>
    :license: BSD, see LICENSE for more details.
"""
from wtforms.widgets import HTMLString, html_params

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