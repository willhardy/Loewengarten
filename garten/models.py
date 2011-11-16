from django.db import models
from django.utils.translation import ugettext_lazy as _

class Member(models.Model):
    user = models.ForeignKey('auth.User', verbose_name=_("user"))
    telephone = models.CharField(_("telephone"), max_length=16, default="", blank=True)
    delivery_group = models.ForeignKey('DeliveryGroup', verbose_name=_("delivery group"))
    date_joined = models.DateField(_("date joined"), null=True, blank=True)

    def __unicode__(self):
        return unicode(self.user)
    
    class Meta:
        verbose_name = _("member")
        verbose_name_plural = _("members")


class DeliveryGroup(models.Model):
    name = models.CharField(_("name"), max_length=32)
    address = models.TextField(_("address"), default="", blank=True)
    location = models.CharField(_("location"), max_length=64, default="", blank=True)

    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = _("delivery group")
        verbose_name_plural = _("delivery groups")


class Vegetable(models.Model):
    name    = models.CharField(_("name"), max_length=32)
    harvest = models.CharField(_("harvest"), max_length=32)
    storage = models.BooleanField(_("storage"), default=False)

    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = _("vegetable")
        verbose_name_plural = _("vegetable")


class Delivery(models.Model):
    date       = models.DateField(_("date"))
    vegetables = models.ManyToManyField(Vegetable, verbose_name=_("vegetables"), blank=True)
    letter     = models.TextField(_("letter"), default="", blank=True)

    def __unicode__(self):
        return unicode(self.date)
    
    class Meta:
        verbose_name = _("delivery")
        verbose_name_plural = _("deliveries")


class Task(models.Model):
    name    = models.CharField(_("name"), max_length=32)
    date    = models.DateField(_("date"))
    people_required = models.PositiveSmallIntegerField(_("number of people required"), default=1)
    members = models.ManyToManyField(Member, verbose_name=_("members"))
    delivery_group = models.ForeignKey(DeliveryGroup, null=True, blank=True, verbose_name=_("delivery group"))

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _("task")
        verbose_name_plural = _("tasks")

class GardenVisit(models.Model):
    member        = models.ForeignKey(Member, verbose_name=_("member"))
    start_date    = models.DateField(_("from"))
    end_date      = models.DateField(_("to"))
    number_people = models.PositiveSmallIntegerField(_("number of people"), default=1)
    confirmed     = models.BooleanField(_("confirmed"), default=False)
    title         = models.CharField(_("title"), max_length=255, default="", blank=True)
    comments      = models.TextField(_("comments"), default="", blank=True)

    def __unicode__(self):
        return self.title or '{0}, {1}'.format(self.member, self.start_date)
    
    class Meta:
        verbose_name = _("garden visit")
        verbose_name_plural = _("garden visits")

