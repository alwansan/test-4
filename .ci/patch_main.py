#!/usr/bin/env python3
"""
patch_main.py
─────────────
يُعدَّل هذا السكريبت في GitHub Actions قبل بدء البناء.
يضيف إلى main.py:
  1. دالة request_android_permissions() التلقائية
  2. استدعاءها داخل open_browser()
"""

import os, sys, re

MAIN = os.path.join(os.path.dirname(__file__), "main.py")

if not os.path.exists(MAIN):
    print(f"❌ main.py not found at {MAIN}")
    sys.exit(1)

with open(MAIN, "r", encoding="utf-8") as f:
    code = f.read()

# ── كتلة الأذونات ──────────────────────────────────────────────────
PERMS_BLOCK = '''
# ══════════════════════════════════════════════
#  Android Runtime Permissions — تلقائي
# ══════════════════════════════════════════════
def request_android_permissions():
    """يطلب صلاحيات Android في وقت التشغيل — آمن على جميع الإصدارات"""
    try:
        from android.permissions import request_permissions, check_permission
        PERMISSIONS = [
            # Android 13+ (API 33+)
            "android.permission.READ_MEDIA_VIDEO",
            "android.permission.READ_MEDIA_AUDIO",
            "android.permission.READ_MEDIA_IMAGES",
            # Android ≤ 12
            "android.permission.READ_EXTERNAL_STORAGE",
            "android.permission.WRITE_EXTERNAL_STORAGE",
            # دائماً
            "android.permission.INTERNET",
        ]
        needed = []
        for p in PERMISSIONS:
            try:
                if not check_permission(p):
                    needed.append(p)
            except Exception:
                needed.append(p)
        if needed:
            request_permissions(needed)
            LOG(f"📋 طُلب {len(needed)} إذن Android")
        else:
            LOG("✅ جميع الأذونات ممنوحة")
    except ImportError:
        LOG("ℹ️ ليس Android — لا أذونات مطلوبة")
    except Exception as ex:
        LOG(f"⚠️ خطأ في الأذونات: {ex}", "WARN")

'''

# أضف كتلة الأذونات بعد آخر سطر LOG("="*60)
if "request_android_permissions" not in code:
    marker = 'LOG("=" * 60)\n'
    idx = code.rfind(marker)
    if idx != -1:
        insert_at = idx + len(marker)
        code = code[:insert_at] + PERMS_BLOCK + code[insert_at:]
        print("✅ أُضيفت دالة request_android_permissions()")
    else:
        print("⚠️ لم يُعثر على marker — ستُضاف الكتلة في البداية")
        code = PERMS_BLOCK + code
else:
    print("ℹ️ request_android_permissions موجودة مسبقاً — لا تعديل")

# ── تعديل open_browser ───────────────────────────────────────────────
OLD_OB = 'def open_browser():\n    """فتح المتصفح — يعمل في Termux وAndroid APK"""\n    time.sleep(2)'
NEW_OB = 'def open_browser():\n    """فتح المتصفح — يعمل في Termux وAndroid APK"""\n    request_android_permissions()  # طلب الأذونات أولاً\n    time.sleep(2)'

if OLD_OB in code:
    code = code.replace(OLD_OB, NEW_OB)
    print("✅ عُدِّلت open_browser()")
elif "request_android_permissions()" in code:
    print("ℹ️ open_browser() مُعدَّلة مسبقاً")
else:
    print("⚠️ لم يُعثر على open_browser() — تحقق يدوياً")

with open(MAIN, "w", encoding="utf-8") as f:
    f.write(code)

print(f"✅ main.py جاهز ({len(code)} حرف)")
