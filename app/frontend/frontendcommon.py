#-*- coding:utf-8 -*-
from flask import current_app, request, Blueprint, url_for, send_from_directory, redirect
from werkzeug.utils import secure_filename
from . import route

import os
import datetime

bp = Blueprint('upload-frontend', __name__, template_folder='templates', static_folder='static', url_prefix='/uploader')

#----------------------------------------------------------------------
def allowed_files(filename):
	"""Allowed file type.
	:param filename: file name.
	"""
	return '.' in filename and filename.rsplit('.', 1)[1] in current_app.config['ALLOWED_EXTENSIONS']

@route(bp, '/upload', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		file = request.files['upload']
		if file and allowed_files(file.filename):
			filename = secure_filename(file.filename)
			filenames = os.path.splitext(filename)
			filename = filenames[0] + '_' + str(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S_%f')) + filenames[1]
			file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
			file_url = url_for('.uploaded_file', filename=filename)
			#return "<script type='text/javascript'>window.parent.CKEDITOR.tools.callFunction(" + "CKEditorFuncNum, '$url', '$message');</script>"
			#return redirect(file_url)
			return str.format("<script type='text/javascript'>window.parent.CKEDITOR.tools.callFunction({}, '{}');</script>",
			                  request.args['CKEditorFuncNum'], file_url)

	return ''


@route(bp, '/uploads/<filename>', methods=['GET', 'POST'])
def uploaded_file(filename):
	"""Return file in uploader
	:param filename: file name.
	"""
	return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename)