from django.shortcuts import render



def admin_view(request):
    return render(request, 'test_7/admin.html')

def viewer_view(request):
    return render(request, 'test_7/viewer.html')

def video_page(request):
    return render(request, "test_7/video.html")



