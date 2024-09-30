from accounts.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username already exists.'})
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        return JsonResponse({'success': 'User created successfully.'})
    return JsonResponse({'error': 'Invalid request.'})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'success': 'User logged in successfully.'})
        return JsonResponse({'error': 'Invalid username or password.'})
    return JsonResponse({'error': 'Invalid request.'})

def logout_view(request):
    logout(request)
    return JsonResponse({'success': 'User logged out successfully.'})

def user_info(request):
    if request.user.is_authenticated:
        return JsonResponse({'username': request.user.username, 'email': request.user.email})
    return JsonResponse({'error': 'User is not authenticated.'})

def change_password(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        user = authenticate(username=request.user.username, password=old_password)
        if user is not None:
            user.set_password(new_password)
            user.save()
            return JsonResponse({'success': 'Password changed successfully.'})
        return JsonResponse({'error': 'Invalid password.'})
    return JsonResponse({'error': 'Invalid request.'})

def delete_user(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        user = authenticate(username=request.user.username, password=password)
        if user is not None:
            user.delete()
            return JsonResponse({'success': 'User deleted successfully.'})
        return JsonResponse({'error': 'Invalid password.'})
    return JsonResponse({'error': 'Invalid request.'})
