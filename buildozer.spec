[app]
title           = B-Ultra
package.name    = bultra
package.domain  = org.bultra
version         = 14

source.dir          = .
source.include_exts = py,png,jpg,kv,atlas,json,txt
source.exclude_dirs = .git, .github, .ci, __pycache__, .buildozer

# متطلبات التطبيق
requirements = python3,flask,requests,certifi,urllib3,charset-normalizer,idna,werkzeug,jinja2,markupsafe,click,itsdangerous,blinker,setuptools

android.minapi  = 24
android.api     = 34
android.ndk_api = 25b
android.archs   = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True

android.permissions = INTERNET,ACCESS_NETWORK_STATE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,READ_MEDIA_VIDEO,READ_MEDIA_AUDIO,READ_MEDIA_IMAGES,MANAGE_EXTERNAL_STORAGE,FOREGROUND_SERVICE,WAKE_LOCK,VIBRATE
android.meta_data = android.requestLegacyExternalStorage:true

orientation      = portrait
fullscreen       = 0
android.allow_backup = True

p4a.bootstrap    = webview
p4a.port         = 8000
p4a.branch       = master

[buildozer]
log_level   = 2
warn_on_root = 0
