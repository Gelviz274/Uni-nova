from django.contrib import admin
from .models import UserProfile, Carrera, Universidad, Semestre

class CarreraInline(admin.TabularInline):
    model = Carrera
    extra = 1

class UniversidadAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    inlines = [CarreraInline]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['carrera'].queryset = Carrera.objects.none()
        return form

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "carrera":
            kwargs["queryset"] = Carrera.objects.filter(universidad=request.resolver_match.kwargs['object_id'])
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Universidad, UniversidadAdmin)
admin.site.register(Semestre)
admin.site.register(UserProfile)
