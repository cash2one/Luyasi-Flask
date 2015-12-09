# -*- coding:utf-8 -*-

# Security 信息翻译用
SECURITY_MSG_UNAUTHORIZED = ((u'抱歉，您没有权限查看。'), 'error')
SECURITY_MSG_CONFIRM_REGISTRATION = ((u'验证链接已经发送到 %(email)s，请到邮箱中验证，谢谢~'), 'success')
SECURITY_MSG_EMAIL_CONFIRMED = ((u'您的邮箱已经验证成功，谢谢。'), 'success')
SECURITY_MSG_ALREADY_CONFIRMED = ((u'您的邮箱已经被验证。'), 'info')
SECURITY_MSG_INVALID_CONFIRMATION_TOKEN = ((u'验证token无效。'), 'error')
SECURITY_MSG_EMAIL_ALREADY_ASSOCIATED = ((u'%(email)s 已经被使用。'), 'error')
SECURITY_MSG_PASSWORD_MISMATCH = ((u'密码不正确'), 'error')
SECURITY_MSG_RETYPE_PASSWORD_MISMATCH = ((u'两次密码不一致'), 'error')
SECURITY_MSG_INVALID_REDIRECT = ((u'禁止向外部域重定向'), 'error')
SECURITY_MSG_PASSWORD_RESET_REQUEST = ((u'重置密码的链接已经发送到 %(email)s '), 'info')
SECURITY_MSG_PASSWORD_RESET_EXPIRED = ((u'您没有在 %(within)s 内重置密码，请重新验证。 新的验证链接已经发送到 %(email)s.'), 'error')
SECURITY_MSG_INVALID_RESET_PASSWORD_TOKEN = ((u'密码token无效。'), 'error')
SECURITY_MSG_CONFIRMATION_REQUIRED = ((u'请到您的邮箱进行验证。'), 'error')
SECURITY_MSG_CONFIRMATION_REQUEST = ((u'验证链接已经发送到 %(email)s.'), 'info')
SECURITY_MSG_CONFIRMATION_EXPIRED = ((u'您没有在 %(within)s 内验证邮箱，请重新验证。 新的验证链接已经发送到 %(email)s。'), 'error')
SECURITY_MSG_LOGIN_EXPIRED = ((u'您没有在 %(within)s 内登录，请重新登录。新的登录链接已经发送到 %(email)s。'), 'error')
SECURITY_MSG_LOGIN_EMAIL_SENT = ((u'登录链接已经发送到 %(email)s。'), 'success')
SECURITY_MSG_INVALID_LOGIN_TOKEN = ((u'登录失效'), 'error')
SECURITY_MSG_DISABLED_ACCOUNT = ((u'用户被禁用了。'), 'error')
SECURITY_MSG_EMAIL_NOT_PROVIDED = ((u'请填写邮箱'), 'error')
SECURITY_MSG_INVALID_EMAIL_ADDRESS = ((u'邮箱地址无效'), 'error')
SECURITY_MSG_PASSWORD_NOT_PROVIDED = ((u'请填写密码'), 'error')
SECURITY_MSG_PASSWORD_NOT_SET = ((u'此用户没有设置密码'), 'error')
SECURITY_MSG_PASSWORD_INVALID_LENGTH = ((u'密码长度不能小于6位'), 'error')
SECURITY_MSG_USER_DOES_NOT_EXIST = ((u'用户不存在或密码不正确'), 'error')
SECURITY_MSG_INVALID_PASSWORD = ((u'无效密码'), 'error')
SECURITY_MSG_PASSWORDLESS_LOGIN_SUCCESSFUL = ((u'您已经登录。'), 'success')
SECURITY_MSG_PASSWORD_RESE = ((u'您已经重置密码并自动登陆。'), 'success')
SECURITY_MSG_PASSWORD_IS_THE_SAME = ((u'新旧密码必须不相同'), 'error')
SECURITY_MSG_PASSWORD_CHANGE = ((u'您的密码更改成功。'), 'success')
SECURITY_MSG_LOGIN = ((u'请先登陆'), 'info')
SECURITY_MSG_REFRESH = ((u'访问这个页面需要重新授权'), 'info')
