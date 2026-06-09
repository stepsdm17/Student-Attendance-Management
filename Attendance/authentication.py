import jwt
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.urls import resolve

class JWTMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Skip JWT check for login, logout, and static files
        if resolve(request.path_info).url_name in ['login', 'logout'] or request.path.startswith('/static/'):
            return self.get_response(request)
        
        token = request.session.get('jwt_token')
        if token:
            try:
                payload = jwt.decode(token, settings.JWT_SETTINGS['SECRET_KEY'], algorithms=['HS256'])
                request.user = User.objects.get(id=payload['user_id'])
            except (jwt.ExpiredSignatureError, jwt.InvalidTokenError, User.DoesNotExist):
                request.session.flush()
                return JsonResponse({'error': 'Token expired or invalid'}, status=401)
        
        response = self.get_response(request)
        return response