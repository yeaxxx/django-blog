from django.conf.urls.defaults import patterns

from blog.models import Entry


entry_info_dict = {
    'queryset': Entry.live.all(),
    'date_field': 'pub_date',
}

entry_info_dict_w_month = dict.copy(entry_info_dict)
entry_info_dict_w_month['month_format'] = '%m'

entry_detail_dict = {
    'queryset': Entry.objects.all(),
    'date_field': 'pub_date',
    'month_format': '%m'}

urlpatterns = patterns('django.views.generic.date_based',
    (r'^$',
        'archive_index',
        dict(entry_info_dict, num_latest=15),
        'blog_entry_archive'),
    (r'^(?P<year>\d{4})/$',
        'archive_year',
        dict(entry_info_dict, make_object_list=True),
        'blog_entry_archive_year'),
    (r'^(?P<year>\d{4})/(?P<month>\d{2})/$',
        'archive_month',
        entry_info_dict_w_month,
        'blog_entry_archive_month'),
    (r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$',
        'archive_day',
        entry_info_dict_w_month,
        'blog_entry_archive_day'),
    (r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        'object_detail',
        entry_detail_dict,
        'blog_entry_detail'),)