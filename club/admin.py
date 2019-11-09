from django.contrib import admin

from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# from .models import Data1
from .models import Club
from .models import Role
from .models import ClubDate
from .models import ClubMember
from .models import Attd
from .models import AttdRole



from .models import Data2
from .models import Best



# class Data1Resource(resources.ModelResource):
#     class Meta:
#         model = Data1

# class Data1Admin(ImportExportModelAdmin):
#     resource_class = Data1Resource
#     list_display = ('date1','place', 'worker','thing')
#     list_filter = ['place','worker']
#     search_fields = ['date1','thing']
   
# admin.site.register(Data1, Data1Admin)
class ClubResource(resources.ModelResource):
    class Meta:
        model = Club

class ClubAdmin(ImportExportModelAdmin):
    resource_class = ClubResource
    list_display = ('name',)
    # fields = ('date1','name', 'member','role')
    # list_filter = ['name','role','member']
    # search_fields = ['date1']
   
admin.site.register(Club, ClubAdmin)

class RoleResource(resources.ModelResource):
    class Meta:
        model = Role

class RoleAdmin(ImportExportModelAdmin):
    resource_class = RoleResource
    list_display = ('name',)
    # fields = ('date1','name', 'member','role')
    # list_filter = ['name','role','member']
    # search_fields = ['date1']
   
admin.site.register(Role, RoleAdmin)

class ClubDateResource(resources.ModelResource):
    class Meta:
        model = ClubDate

class ClubDateAdmin(ImportExportModelAdmin):
    resource_class = ClubDateResource
    list_display = ('club','date1')
    # fields = ('date1','name', 'member','role')
    list_filter = ['club',]
    search_fields = ['date1']
   
admin.site.register(ClubDate, ClubDateAdmin)

class ClubMemberResource(resources.ModelResource):
    class Meta:
        model = ClubMember

class ClubMemberAdmin(ImportExportModelAdmin):
    resource_class = ClubMemberResource
    list_display = ('club','member','is_member')
    # fields = ('date1','name', 'member','role')
    list_filter = ['club','is_member']
    search_fields = ['member']
   
admin.site.register(ClubMember, ClubMemberAdmin)

class AttdResource(resources.ModelResource):
    class Meta:
        model = Attd

class AttdAdmin(ImportExportModelAdmin):
    resource_class = AttdResource
    list_display = ('clubdate','clubmember')
    # fields = ('date1','name', 'member','role')
    list_filter = ['clubmember',]
    search_fields = ['clubdate',]
   
admin.site.register(Attd, AttdAdmin)


class AttdRoleResource(resources.ModelResource):
    class Meta:
        model = AttdRole

class AttdRoleAdmin(ImportExportModelAdmin):
    resource_class = AttdRoleResource
    list_display = ('attd','role')
    # fields = ('date1','name', 'member','role')
    list_filter = ['role',]
    # search_fields = ['attd__name',]
   
admin.site.register(AttdRole, AttdRoleAdmin)



# class Data2Resource(resources.ModelResource):
#     class Meta:
#         model = Data2

# class Data2Admin(ImportExportModelAdmin):
#     resource_class = Data2Resource
#     list_display = ('date1','name', 'member','role')
#     fields = ('date1','name', 'member','role')
#     list_filter = ['name','role','member']
#     search_fields = ['date1']
   
# admin.site.register(Data2, Data2Admin)

# class BestResource(resources.ModelResource):
#     class Meta:
#         model = Best

# class BestAdmin(ImportExportModelAdmin):
#     resource_class = BestResource
#     list_display = ('date1','title','name')
#     list_filter = ['title','name',]
#     search_fields = ['date1']
   
# admin.site.register(Best, BestAdmin)