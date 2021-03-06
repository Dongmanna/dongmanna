# chat/views.py
from django.shortcuts import render, redirect, get_object_or_404
from chat.models import Room, Message
from main.models import Post
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required


# 채팅방에 입장하기 위해 room_number를 받아 chat room으로 이동한다
@login_required
def room(request, room_number):
    post = get_object_or_404(Post, pk=room_number)
    username = request.user.profile.nickname
    room_details = Room.objects.get(number=room_number)

    # 공구 참여자가 아니면 채팅방에 들어갈 수 없도록 함
    if not post.members.filter(user=request.user).exists():
        return redirect('detail', pk=room_number)

    return render(request, 'room.html', {
        'username': username,
        'room_number': room_number,
        'room_details': room_details,
    })


# 게시글을 작성하면 연결된 새로운 채팅방 생성
@login_required
def newRoom(request, pk):
    post = get_object_or_404(Post, pk = pk)
    
    if not Room.objects.filter(post=post).exists():
        new_room = Room.objects.create(post=post, number=pk)
        new_room.save()
    return redirect('detail', pk=pk)


# message 전송
def send(request):
    message = request.POST['message']
    username = request.user.profile.nickname
    room_number = request.POST['room_number']
    room_details = Room.objects.get(number=room_number)

    # 메시지 object 생성
    new_message = Message.objects.create(room=room_details, value=message, username=username)
    new_message.save()
    return HttpResponse('Message sent successfully')


# message 수신
def getMessages(request, room_number):
    room_details = Room.objects.get(number=room_number)
    messages = Message.objects.filter(room=room_details)
    return JsonResponse({"messages":list(messages.values())})


# 공지 message 전송
def sendNotice(message, pk):
    room_details = Room.objects.get(number=pk)
    username = "동만나 매니저"

    # 메시지 object 생성
    new_message = Message.objects.create(room=room_details, value=message, username=username)
    new_message.save()
    return HttpResponse('Message sent successfully')