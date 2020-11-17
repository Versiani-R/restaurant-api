from django.contrib import admin

from api.models import Restaurant, Dishes


"""
Although the user admin should be able to controll the dishes and restaurants,
The only way of the user to controll ( add, remove, update ) dishes is through proper
api calling.
"""

class DishesInline(admin.StackedInline):
    model = Dishes
    extra = 1


class RestaurantAdmin(admin.ModelAdmin):
    fields = ['email', 'password', 'restaurant_name', 'owner_name', 'address', 'phone_number', 'token_id']
    inlines = [DishesInline]


admin.site.register(Restaurant, RestaurantAdmin)
