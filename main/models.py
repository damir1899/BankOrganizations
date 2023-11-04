from django.db import models
from autoslug import AutoSlugField
from django.utils.text import slugify


def slugify_function(content):
    return slugify(content)


class FinancialOrganization(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    logo = models.FileField(upload_to='logo/', verbose_name='Логотип', null=True, blank=True)
    bin = models.CharField(max_length=12, verbose_name='БИН')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    fax = models.CharField(max_length=20, verbose_name='Факс')
    email = models.EmailField(max_length=100, verbose_name='E-mail')
    website = models.URLField(max_length=100, verbose_name='Web-сайт')
    second_level_bank = models.CharField(max_length=255, verbose_name='Банк второго уровня')
    insurance_holdings = models.CharField(max_length=255, verbose_name='Страховые холдинги', blank=True, null=True)
    custodian = models.CharField(max_length=255, verbose_name='Кастодиан')
    brokers_dealers = models.CharField(max_length=255, verbose_name='Брокеры-дилеры', blank=True, null=True)
    conglomerates = models.CharField(max_length=255, verbose_name='Банковские конгломераты', blank=True, null=True)
    bank_holdings = models.ManyToManyField('self', blank=True, null=True, verbose_name='Связанные компаний')
    participants = models.ManyToManyField('Executive', blank=True, null=True, related_name='major_participants')
    slug = AutoSlugField(populate_from=slugify_function, unique=True, editable=False)
    
    
    executives = models.ManyToManyField('Executive', through='ExecutiveOnOrganization', 
                                        related_name='organizations', verbose_name='Руководящие лица')
    
    class Meta:
        verbose_name = 'Финансовая Организация'
        verbose_name_plural = 'Финансовые Организации'

    def __str__(self) -> str:
        return f'{self.name}'
    
class Position(models.Model):
    job_title = models.CharField(max_length=255, verbose_name='Название должности')
    
    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
        
    def __str__(self) -> str:
        return self.job_title
    
    
class Executive(models.Model):
    full_name = models.CharField(max_length=200, verbose_name='ФИО')
    image = models.FileField(upload_to='executive_image/', verbose_name='Изображение', blank=True, null=True)
    IIN = models.PositiveBigIntegerField(unique=True)
    position = models.ManyToManyField(Position, verbose_name='Должность')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона', unique=True)
    email = models.EmailField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from=slugify_function, unique=True, editable=False)
    
    class Meta:
        verbose_name = 'Руководящее Лицо'
        verbose_name_plural = 'Руководящие Лица'

    def __str__(self) -> str:
        return f'{self.full_name}'
    

class ExecutiveOnOrganization(models.Model):
    executive = models.ForeignKey(Executive, on_delete=models.PROTECT, verbose_name='Руководящее лицо')
    organization = models.ForeignKey(FinancialOrganization, on_delete=models.PROTECT, verbose_name='Финансовая организация')
    start_date = models.DateField(verbose_name='Дата начала работы')
    end_date = models.DateField(verbose_name='Дата окончания работы', null=True, blank=True,)

    class Meta:
        verbose_name = 'Руководящее лицо в организаций'
        verbose_name_plural = 'Руковдящие лица в организацияз'
        
    def __str__(self) -> str:
        return f'{self.executive} {self.organization} {self.start_date} {self.end_date}'
        
    
    


    
