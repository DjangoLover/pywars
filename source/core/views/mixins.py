import json
from django.http import HttpResponse


class PlayerMixin(object):
    """
    Provides utils for working with player object inside views
    """
    def get_player_id(self):
        return self.request.session.session_key


class JSONResponseMixin(object):
    """
    A mixin that can be used to render a JSON response.
    """
    def render_to_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        return HttpResponse(
            self.convert_context_to_json(context),
            content_type='application/json',
            **response_kwargs
        )

    def convert_context_to_json(self, context):
        return json.dumps(context)