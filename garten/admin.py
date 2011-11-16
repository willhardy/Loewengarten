#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from django.contrib import admin
from garten import models

class MemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'delivery_group', 'date_joined')
    list_filter = ('delivery_group',)

class DeliveryGroupAdmin(admin.ModelAdmin):
    pass

class VegetableAdmin(admin.ModelAdmin):
    list_display = ('name', 'harvest', 'storage')

class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('date', 'vegetable_list', )
    list_filter = ('vegetables',)

    def vegetable_list(self, instance):
        return u','.join(v.name for v in instance.vegetables.all())

class TaskAdmin(admin.ModelAdmin):
    list_display = ("name", "date", "people_required", "people_assigned", "delivery_group")

    def people_assigned(self, instance):
        return instance.members.all().count()

class GardenVisitAdmin(admin.ModelAdmin):
    list_display = ("member", "start_date", "end_date", "number_people", "confirmed", "title")
    list_filter = ("confirmed", "start_date")

admin.site.register(models.Member, MemberAdmin)
admin.site.register(models.DeliveryGroup, DeliveryGroupAdmin)
admin.site.register(models.Vegetable, VegetableAdmin)
admin.site.register(models.Delivery, DeliveryAdmin)
admin.site.register(models.Task, TaskAdmin)
admin.site.register(models.GardenVisit, GardenVisitAdmin)

