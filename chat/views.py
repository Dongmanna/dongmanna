# chat/views.py
from django.shortcuts import render, redirect, get_object_or_404
from chat.models import Room, Message
from main.models import Post
from django.http import HttpResponse, JsonResponse

# 채팅방에 입장하기 위해 username, room_details를 받아 room.html로 넘겨준다
def room(request, room_number):
    username = request.user.username
    room_details = Room.objects.get(number=room_number)
    return render(request, 'room.html', {
        'username': username,
        'room_number': room_number,
        'room_name': room_details.post.title,
    })

# 게시글을 작성하면 연결된 새로운 채팅방 생성
def newRoom(request, pk):
    post = get_object_or_404(Post, pk = pk)
    
    if not Room.objects.filter(post=post).exists():
        new_room = Room.objects.create(post=post, number=pk)
        new_room.save()
    return redirect('chat:room', room_number=pk)

# 내가 입장하려는 채팅방을 찾아줌
def checkRoom(request):
    room_number = request.POST['room_number']
    post = get_object_or_404(Post, pk = room_number)

    # 찾는 채팅방이 있다면 바로 해당 url로 이동
    if Room.objects.filter(post=post).exists():
        return redirect('chat:room', room_number=room_number)
    # Error: 찾는 채팅방이 없는 경우 그대로 detail 페이지로
    else:
        return redirect('detail', pk=room_number)

# message 전송
def send(request):
    message = request.POST['message']
    username = request.user.username
    room_number = request.POST['room_number']
    room_details = Room.objects.get(number=room_number)

    # 메시지 object 생성
    new_message = Message.objects.create(room=room_details, value=message, user=username)
    new_message.save()
    return HttpResponse('Message sent successfully')

# message 수신
def getMessages(request, room_number):
    room_details = Room.objects.get(number=room_number)
    messages = Message.objects.filter(room=room_details)
    return JsonResponse({"messages":list(messages.values())})