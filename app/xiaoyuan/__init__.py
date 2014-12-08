#-*- coding:utf-8 -*-
from ..core import Service, db
from .models import Academy, Class, Message, MessageUserAssociation, ClassApply, MemberInfo

class AcademyService(Service):
    __model__ = Academy


class ClassService(Service):
    __model__ = Class

class MessageService(Service):
    __model__ = Message

    def get_my_msgs(self, user_id):
        query = self.__model__.query.join(self.__model__.user_assocs).filter(
            MessageUserAssociation.user_id == user_id,
            self.__model__.reply_message_id == None
        ).order_by(self.__model__.update_at.desc(), self.__model__.create_at.desc())

        return query

    def create(self, content=None, sender=None, reply_msg=None):
        """Override the ~method:Service.create~, cause the message need assosication."""
        msg = self.new(content=content, sender=sender, reply_message_id=reply_msg.id)
        association = MessageUserAssociation()
        association.user = reply_msg.sender
        association.message = msg
        reply_msg.sender.message_assocs.append(association)
        db.session.commit()
        return msg

class ClassApplyService(Service):
    __model__ = ClassApply
    
    #----------------------------------------------------------------------
    def get_applies(self, class_ids, page=1, per_page=20, error_out=True):
        """取自己班的的加入申请"""
        if len(class_ids)==0:
            return None

        query = self.__model__.query\
                        .filter(Class.id.in_(class_ids))\
                        .paginate(page, per_page, error_out)
        return query        
        
class MemberInfoService(Service):
    __model__ = MemberInfo