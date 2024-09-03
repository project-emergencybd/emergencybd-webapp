from datetime import datetime, timezone, timedelta


def dhaka_current_time() -> str:
    tz = timedelta(hours=6)
    current_time = datetime.now(timezone(tz))
    formatted_time = current_time.strftime("%d %b, %Y  %H:%M")

    return formatted_time
