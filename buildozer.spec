[app]

title = Bultra
package.name = bultra
package.domain = org.alwan

source.dir = .
source.include_exts = py,png,jpg,kv,html,js,css

version = 1.0

requirements = python3,flask,requests,certifi,urllib3,charset-normalizer,idna,werkzeug,jinja2,markupsafe,click,itsdangerous,blinker,setuptools

orientation = portrait
fullscreen = 0

android.permissions = INTERNET,READ_MEDIA_VIDEO,READ_MEDIA_AUDIO,READ_MEDIA_IMAGES,WRITE_EXTERNAL_STORAGE,MANAGE_EXTERNAL_STORAGE

android.api = 34
android.minapi = 24
android.ndk = 25b

android.archs = arm64-v8a, armeabi-v7a

android.allow_backup = True

android.logcat_filters = *:S python:D

p4a.bootstrap = webview
p4a.port = 8000

p4a.branch = stable

android.enable_androidx = True

[buildozer]
log_level = 2
warn_on_root = 1
