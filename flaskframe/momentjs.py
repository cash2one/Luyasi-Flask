from jinja2 import Markup

class momentjs(object):

    def __init__(self, timestamp):
        self.timestamp = timestamp

    def format_utc(self, fmt):
        return self.render("format(\"%s\")" % fmt)
    
    def format(self, fmt):
        return self.render("format(\"%s\")" % fmt, utc=False)

    def calendar(self):
        return self.render("calendar()")

    def fromNow(self):
        return self.render("fromNow()")

    def render(self, format, utc=True):
        format_str = "%Y-%m-%d %H:%M:%S Z"
        if not utc:
            format_str = "%Y-%m-%d %H:%M:%S"
        return Markup("<script>\ndocument.write(moment(\"%s\").%s);\n</script>" % (self.timestamp.strftime(format_str), format))

