from django.contrib import admin
from www.models import *


#beshoy mainPage
admin.site.register(main_page)
admin.site.register(main_page_moviestrip)


admin.site.register(Album)
admin.site.register(Pictures)
admin.site.register(AblumCover)
admin.site.register(AboutUs)

admin.site.register(video)
admin.site.register(contact)
admin.site.register(radio_ad)
admin.site.register(sorl_test)
