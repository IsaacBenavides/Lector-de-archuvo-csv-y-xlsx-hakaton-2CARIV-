from django.urls import path
from reader import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("upload_file/", views.upload_files, name="upload_file"),
    path("read_file/<int:id>", views.read_file, name="read_file"),
    path("save_csv/<int:id>", views.save_csv, name="save_csv"),
    path("save_excel/<int:id>", views.save_excel, name="save_excel"),
    path("list_data/<int:id>", views.list_data, name="list_data"),
    path("list_csv/<int:id>", views.list_csv, name="list_csv"),
    path("list_excel/<int:id>", views.list_excel, name="list_excel"),
    path("statistics/", views.statistic, name="statistics"),
    path("statistics/excel/<int:id>",
         views.statistic_excel, name="statistics_excel"),
    path("statistics/csv/<int:id>",
         views.statistic_csv, name="statistics_csv"),

]
