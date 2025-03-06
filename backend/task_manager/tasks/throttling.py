from rest_framework.throttling import SimpleRateThrottle

class CreateTaskLimiting(SimpleRateThrottle):
    scope = 'create_task'  # Usa la tasa definida en settings.py

    def get_cache_key(self, request, view):
        if request.user.is_authenticated:
            ident = request.user.pk
        else:
            ident = self.get_ident(request)
        return self.cache_format % {
            'scope': self.scope,
            'ident': ident
        }

class DetailTaskLLimiting(SimpleRateThrottle):
    scope = 'detail_task'  # Usa la tasa definida en settings.py

    def get_cache_key(self, request, view):
        if request.user.is_authenticated:
            ident = request.user.pk
        else:
            ident = self.get_ident(request)
        return self.cache_format % {
            'scope': self.scope,
            'ident': ident
        }

class ViewTasksLimiting(SimpleRateThrottle):
    scope = 'view_tasks'  # Usa la tasa definida en settings.py

    def get_cache_key(self, request, view):
        if request.user.is_authenticated:
            ident = request.user.pk
        else:
            ident = self.get_ident(request)
        return self.cache_format % {
            'scope': self.scope,
            'ident': ident
        }

class UpdateTaskLLimiting(SimpleRateThrottle):
    scope = 'update_task'  # Usa la tasa definida en settings.py

    def get_cache_key(self, request, view):
        if request.user.is_authenticated:
            ident = request.user.pk
        else:
            ident = self.get_ident(request)
        return self.cache_format % {
            'scope': self.scope,
            'ident': ident
        }

# Comments Limiters
class CreateCommentLimiting(SimpleRateThrottle):
    scope = 'add_comment'  # Usa la tasa definida en settings.py

    def get_cache_key(self, request, view):
        if request.user.is_authenticated:
            ident = request.user.pk
        else:
            ident = self.get_ident(request)
        return self.cache_format % {
            'scope': self.scope,
            'ident': ident
        }

class ViewCommentsLimiting(SimpleRateThrottle):
    scope = 'view_comments'  # Usa la tasa definida en settings.py

    def get_cache_key(self, request, view):
        if request.user.is_authenticated:
            ident = request.user.pk
        else:
            ident = self.get_ident(request)
        return self.cache_format % {
            'scope': self.scope,
            'ident': ident
        }

class UpdateCommentLimiting(SimpleRateThrottle):
    scope = 'update_comment'  # Usa la tasa definida en settings.py

    def get_cache_key(self, request, view):
        if request.user.is_authenticated:
            ident = request.user.pk
        else:
            ident = self.get_ident(request)
        return self.cache_format % {
            'scope': self.scope,
            'ident': ident
        }