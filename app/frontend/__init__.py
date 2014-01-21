#-*- coding:utf-8 -*-

from functools import wraps

from flask.ext.security import login_required
from flask.ext.admin.contrib.sqla import ModelView

from .. import appfactory
from ..core import admin, db

from ..security.models import User, Role
from ..qingbank.models import Contact, Department

def create_app(settings_override=None):
    app = appfactory.create_app(__name__, __path__, settings_override)

    # Init assets
    # assets.init_app(app)

    # init Flask-Admin views
    admin.add_view(ModelView(User, db.session, name="Users", endpoint="users", category='User Manage'))
    admin.add_view(ModelView(Role, db.session, name="Roles", endpoint="roles", category='User Manage'))
    admin.add_view(ModelView(Contact,db.session, name='Contacts', endpoint='contacts', category='Qingbank'))
    admin.add_view(ModelView(Department,db.session, name='Departments', endpoint='departments', category='Qingbank'))

    admin.init_app(app)

    # Register custom error handlers
    if not app.debug:
        for e in [500, 404]:
            app.errorhandler(e)(handle_error)

    return app

def handle_error(e):
    return render_template('%s.html' % e.code), e.code    

#用于frotend的route
def route(bp, *args, **kwargs):
    def decorator(f):
        @bp.route(*args, **kwargs)
        @login_required
        @wraps(f)
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)
        return f

    return decorator
