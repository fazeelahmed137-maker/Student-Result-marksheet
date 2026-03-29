from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Student‑facing
    path('', views.student_login, name='login'),
    path('marksheet/<int:student_id>/', views.marksheet, name='marksheet'),
    path('pdf/<int:student_id>/', views.download_pdf, name='download_pdf'),

    # Admin
    path('admin-panel/login/', views.admin_login, name='admin_login'),
    path('admin-panel/dashboard/', views.admin_dashboard, name='admin_dashboard'),

    # Manual add – students (Handsontable sheet)
    path('select-students/', views.select_students, name='select_students'),
    path('add-students-sheet/<int:department_id>/<int:year_id>/<int:semester_id>/',
         views.add_students_sheet, name='add_students_sheet'),
    path('save-students-api/', views.save_students_api, name='save_students_api'),
    path('delete-student/<int:student_id>/', views.delete_student, name='delete_student'),
    path('api/semesters-for-year/<int:year_id>/', views.get_semesters_for_year, name='semesters_for_year'),

    # Manual add – marks (Handsontable sheet)
    path('select-marks/', views.select_marks, name='select_marks'),
    path('add-marks-sheet/<int:department_id>/<int:year_id>/<int:semester_id>/',
         views.add_marks_sheet, name='add_marks_sheet'),
    path('save-marks-api/', views.save_marks_api, name='save_marks_api'),

    # Excel import – students
    path('import-students/', views.import_students_page, name='import_students_page'),
    path('import-students/upload/', views.import_students_excel, name='import_students_excel'),
    path('import-students/sample/', views.download_student_sample_excel, name='student_sample_excel'),

    # Excel import – marks
    path('import-marks/', views.import_marks_page, name='import_marks_page'),
    path('import-marks/upload/', views.import_marks_excel, name='import_marks_excel'),
    path('import-marks/sample/', views.download_marks_sample_excel, name='marks_sample_excel'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)