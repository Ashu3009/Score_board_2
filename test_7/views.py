import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def admin_view(request):
    return render(request, 'test_7/admin.html')

def viewer_view(request):
    return render(request, 'test_7/viewer.html')

def winner_view(request):
    return render(request, 'test_7/winner.html')

def video_view(request):
    return render(request, 'test_7/video.html')

@csrf_exempt
def set_display(request):
    global current_display
    if request.method == 'POST':
        data = json.loads(request.body)
        current_display["mode"] = data.get("mode", "viewer")
        return JsonResponse({"status": "success", "mode": current_display["mode"]})
    return JsonResponse(current_display)

def get_display(request):
    return JsonResponse(current_display)