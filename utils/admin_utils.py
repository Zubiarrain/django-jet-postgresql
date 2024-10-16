from django.contrib import admin
from django.db.models.functions import ExtractYear

# -----------------  FUNCIONES PARA CREACION DE CLASES --------------


def crear_inline(nombre_clase, model, model_admin, formset=None, readonly_fields=None):
    """
    Funcion para crear Inlines de manera simple
    """

    # Utiliza type() para crear una nueva clase con el nombre y la clase base proporcionados
    nueva_clase = type(nombre_clase, (admin.StackedInline,), {})
    nueva_clase.model = model
    nueva_clase.fields = model_admin.fields
    nueva_clase.extra = 0
    nueva_clase.raw_id_fields = model_admin.raw_id_fields
    if formset:
        nueva_clase.formset = formset
    if readonly_fields:
        nueva_clase.readonly_fields = readonly_fields
    else:
        nueva_clase.readonly_fields = model_admin.readonly_fields

    # Devuelve la nueva clase
    return nueva_clase


def crear_custom_filter_heredero(
    nombre_clase, clase_base, title, parameter_name, nombre_campos_filter
):
    """
    Funcion para crear Filtros de manera simple
    El nombre de la clase se compone del nombre de la clase en la que se crea el filtro, el nombre del filtro y la palbra Filter.

    Por ejemplo, si en la clase "Colada" se crea un filtro llamado "Estructura" el nombre será ColadaEstructuraFilter
    """

    # Utiliza type() para crear una nueva clase con el nombre y la clase base proporcionados

    nueva_clase = type(nombre_clase, (clase_base,), {})
    nueva_clase.title = title
    nueva_clase.parameter_name = parameter_name
    nueva_clase.nombre_campos_filter = nombre_campos_filter

    # Devuelve la nueva clase
    return nueva_clase


# ----------------- FILTERS --------------


class CustomFilter(admin.SimpleListFilter):
    """
    Filtro que permite limitar las opciones de los filtros a las contempladas dentro de las opciones ya filtradas por filtros anteriores
    """

    parameter_name = ""
    nombre_campos_filter = []

    def lookups(self, request, model_admin):

        queryset = model_admin.get_queryset(request)
        filtros_previos = request.GET.dict()

        # Aplico todos los filtros ya aplicados
        for campo, filtro in filtros_previos.items():

            if campo != self.parameter_name and campo in self.nombre_campos_filter:
                if filtro != "Desconocido":
                    if "fecha" in campo and filtro:
                        queryset = queryset.filter(
                            **{
                                f"{campo}__range": (
                                    f"{filtro}-01-01",
                                    f"{filtro}-12-31",
                                )
                            }
                        )
                    else:
                        queryset = queryset.filter(**{campo: filtro})
                else:
                    queryset = queryset.filter(**{f"{campo}__isnull": True})

        # Obtén los valores únicos para 'mi_campo' después del filtro anterior
        values = (
            queryset.distinct()
            .order_by(self.parameter_name)
            .values_list(self.parameter_name, flat=True)
        )
        # Genera las opciones del filtro 'mi_campo' basadas en los valores relevantes

        lookups = [
            (value, str(value)) if value is not None else ("Desconocido", "Desconocido")
            for value in values
        ]

        # lookups = [(value, str(value)) for value in values]
        return lookups

    def queryset(self, request, queryset):
        value = self.value()
        if value:
            if value == "Desconocido":
                queryset = queryset.filter(**{f"{self.parameter_name}__isnull": True})
            else:
                queryset = queryset.filter(**{self.parameter_name: value})
        return queryset


class AñoFilter(CustomFilter):
    """
    Filtro por año aplicando filtros ya aplicados
    """

    title = "Año"
    parameter_name = ""
    nombre_campos_filter = []

    def lookups(self, request, model_admin):
        # nombres_de_campos = [campo.name for campo in model_admin.model._meta.get_fields()]

        queryset = model_admin.get_queryset(request)
        filtros_previos = request.GET.dict()
        for campo, filtro in filtros_previos.items():
            if campo != self.parameter_name and campo in self.nombre_campos_filter:
                if filtro != "Desconocido":
                    queryset = queryset.filter(**{campo: filtro})
                else:
                    queryset = queryset.filter(
                        **{f"{self.parameter_name}__isnull": True}
                    )
        queryset = queryset.annotate(año=ExtractYear(self.parameter_name))
        values = queryset.distinct().order_by("año").values_list("año", flat=True)

        lookups = [
            (value, str(value)) if value is not None else ("Desconocido", "Desconocido")
            for value in values
        ]
        return lookups

    def queryset(self, request, queryset):

        value = self.value()

        if value:
            if value == "Desconocido":
                queryset = queryset.filter(**{f"{self.parameter_name}__isnull": True})
            else:
                queryset = queryset.filter(
                    **{
                        f"{self.parameter_name}__range": (
                            f"{self.value()}-01-01",
                            f"{self.value()}-12-31",
                        )
                    }
                )
        return queryset
