import datetime
import ctypes

# تاریخ مبدا (هفته فرد: 23 فوریه - 1 مارس)
base_start = datetime.date(2025, 2, 23)  # یکشنبه، هفته فرد
base_end = base_start + datetime.timedelta(days=6)  # شنبه، 1 مارس 2025

# دریافت تاریخ امروز
today = datetime.date.today()

# اگر هنوز در هفته اول هستیم (23 فوریه تا 1 مارس)
if base_start <= today <= base_end:
    week_status = "❌ این هفته **فرد** است."
    start_str = base_start.strftime("%d %B %Y")
    end_str = base_end.strftime("%d %B %Y")

else:
    # محاسبه تعداد هفته‌های کامل از 2 مارس 2025 (شروع هفته زوج)
    weeks_passed = (today - datetime.date(2025, 3, 2)).days // 7

    # بررسی اینکه این هفته زوج است یا فرد
    if weeks_passed % 2 == 0:
        week_status = "✅ این هفته **زوج** است."
    else:
        week_status = "❌ این هفته **فرد** است."

    # پیدا کردن تاریخ شروع و پایان این هفته
    current_week_start = datetime.date(2025, 3, 2) + datetime.timedelta(weeks=weeks_passed)
    current_week_end = current_week_start + datetime.timedelta(days=6)

    start_str = current_week_start.strftime("%d %B %Y")
    end_str = current_week_end.strftime("%d %B %Y")

# پیام نهایی
message = f"{week_status}\n📅 {start_str} - {end_str}"

# نمایش پیام به کاربر
ctypes.windll.user32.MessageBoxW(0, message, "وضعیت هفته", 0x40)
