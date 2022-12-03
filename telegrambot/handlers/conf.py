from django.urls import path, re_path

def command(command, view):
    return re_path(r'^/%s(\s)*(?P<param>\w*)' % command, view)

def unknown_command(view):
    return re_path(r'^/(?P<unknown_command>\w+).*', view)

def regex(pattern, view):
    return re_path(pattern, view)

def message(view):
    return re_path(r'^(?P<message>.*)', view)