
from src.models import User


@admin.register(User)
class BookAdmin(admin.ModelAdmin):
    pass
