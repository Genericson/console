import os
import urllib

import jinja2
import os
import cgi
import webapp2
from google.appengine.api import channel
from google.appengine.api import users


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainPage(webapp2.RequestHandler):
  """This page shows the chat UI, it can also create new chats
  or add the current user to a chat"""

  def get(self):
    channel_key = 'thekey'
    token = channel.create_channel(channel_key)
    # Send html with javascript template with the token embedded
    template_values = {'token': token}
    template = JINJA_ENVIRONMENT.get_template('index.html')
    self.response.out.write(template.render(template_values))
  def post(self):
    message = ''
    response = ''
    self.response.write('<html><body>You wrote:<pre>')
    message = cgi.escape(self.request.get('message'))
    self.response.write(message)
    self.response.write('</pre></body></html>')

application = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)
