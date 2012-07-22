from django.db import connection
from django.conf import settings
from django.template import Template, Context

class SQLLogMiddleware(object):
    def process_request(self, request):
        if not settings.DEBUG:
            return None

        #db.reset_queries()
        return None


    def process_response ( self, request, response ):
        if not settings.DEBUG:
            return response

        time = 0.0
        for q in connection.queries:
            time += float(q['time'])

        t = Template("<p><em>Total query count:</em> {{ count }}<br/><em>Total execution time:</em> {{ time }}</p>")

        content = response.content.decode('utf-8')
        content += t.render(Context({'count':len(connection.queries),'time':time}))
        response.content = content.encode('utf-8')
        return response