#-*- coding:utf-8 -*-
from flask import current_app, request, Blueprint, url_for, send_from_directory, redirect
from werkzeug.utils import secure_filename
from . import route

import os
import datetime

import oss
from oss.oss_api import *
oss=OssAPI('oss.aliyuncs.com','LOM0bPzhMCZyWzEk','1Zsgbt6uH85oIJbKIpD2xT2AKVBLBm')

bp = Blueprint('upload-frontend', __name__, template_folder='templates', static_folder='static', url_prefix='/uploader')

#----------------------------------------------------------------------
def allowed_files(filename):
    """Allowed file type.
    :param filename: file name.
    """
    return '.' in filename and filename.rsplit('.', 1)[1] in current_app.config['ALLOWED_EXTENSIONS']

@route(bp, '/upload', methods=['GET', 'POST'])
def upload_file():
<<<<<<< HEAD
    if request.method == 'POST':
        upload_file = request.files['upload']
        if upload_file and allowed_files(upload_file.filename):
            filename = secure_filename(upload_file.filename)
            filenames = os.path.splitext(filename)
            filename = filenames[0] + '_' + str(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S_%f')) + filenames[1]
            upload_file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            res = oss.put_object_from_fp('hz-kinorsi-bucket', filename, upload_file)
            #file_url = url_for('.uploaded_file', filename=filename)
            file_url = 'http://hz-kinorsi-bucket.oss-cn-hangzhou.aliyuncs.com/' + filename
            return str.format("<script type='text/javascript'>window.parent.CKEDITOR.tools.callFunction({}, '{}');</script>",
                              request.args['CKEditorFuncNum'], file_url)

    return ''
=======
	if request.method == 'POST':
		upload_file = request.files['upload']
		if upload_file and allowed_files(upload_file.filename):
			filename = secure_filename(upload_file.filename)
			filenames = os.path.splitext(filename)
			filename = filenames[0] + '_' + str(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S_%f')) + filenames[1]
			upload_file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
			res = oss.put_object_from_fp('img-kinorsi', filename, upload_file)
			#file_url = url_for('.uploaded_file', filename=filename)
			file_url = 'http://img-kinorsi.oss-cn-hangzhou.aliyuncs.com/' + filename
			return str.format("<script type='text/javascript'>window.parent.CKEDITOR.tools.callFunction({}, '{}');</script>",
			                  request.args['CKEditorFuncNum'], file_url)

	return ''
>>>>>>> origin/master


@route(bp, '/uploads/<filename>', methods=['GET', 'POST'])
def uploaded_file(filename):
    """Return file in uploader
    :param filename: file name.
    """
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename)
