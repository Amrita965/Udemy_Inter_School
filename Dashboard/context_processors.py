def dashboard_links(request):

    sidebar_links = [
        {'title': 'Dashboard', 'icon': 'fa-tachometer-alt', 'url': '/dashboard/'},
        {'title': 'Students', 'icon': 'fa-user-graduate', 'url': '/dashboard/students/'},
        {'title': 'Teachers', 'icon': 'fa-chalkboard-teacher', 'url': '/dashboard/teachers/'},
        {'title': 'Courses', 'icon': 'fa-book', 'url': '/dashboard/courses/'},
        {'title': 'Attendance', 'icon': 'fa-calendar-days', 'url': '/dashboard/attendance/'},
        {'title': 'Grades', 'icon': 'fa-graduation-cap', 'url': '/grades/'},
        {'title': 'Reports', 'icon': 'fa-chart-bar', 'url': '/reports/'},
    ]

    return {
        'sidebar_links': sidebar_links 
    }