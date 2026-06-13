from storage.disk_manager import calculate_disk_blocks
from storage.io_helper import safe_create_dir
from analytics.time_validator import parse_and_inspect_date

raw_files = [
    {"filename": "pod_ep1.mp3", "size_bytes": 4500, "duration_sec": 180, "upload_at": "2026-06-10"}, # Hợp lệ
    {"filename": "movie_trailer.mp4", "size_bytes": 105000, "duration_sec": 145, "upload_at": "2026-06-31"}, # Sai ngày (Tháng 6 chỉ có 30 ngày -> ValueError)
    {"filename": "clip_short.mp4", "size_bytes": 8200, "duration_sec": 15, "upload_at": "2026-05-15"} # Hợp lệ
]

print("======== HỆ THỐNG QUẢN LÝ LƯU TRỮ RIKKEI MEDIA ======")
safe_create_dir("media_vault")
print("[SYSTEM] Kiểm tra hạ tầng lưu trữ... Hoàn tất.")
print("-" * 75)
success_count = 0
for media_file in raw_files:
    print(f"[TỆP TIN: {media_file['filename']}]")
    upload_date = parse_and_inspect_date(media_file["upload_at"])

    if upload_date is None:
        print(f" + Trạng thái phân loại: 🔴 THẤT BẠI (Lỗi: Định dạng ngày upload '{media_file['upload_at']}' không tồn tại)")
        continue

    disk_blocks = calculate_disk_blocks(media_file["size_bytes"])
    extension = (media_file["filename"].split(".")[-1].lower())
    if extension == "mp3":
        media_type = "audio"
    else:
        media_type = "video"

    safe_create_dir(f"media_vault/{media_type}")
    print(f" + Dung lượng thực tế: {media_file['size_bytes']:,} Bytes")
    print(f" + Số khối phân vùng (4KB Block): {disk_blocks} Blocks")
    print(f" + Trạng thái phân loại: 🟢 HỢP LỆ (Lưu trữ vào thư mục '{media_type}')")
    success_count += 1
print("=" * 56)
print(f"TIẾN ĐỘ QUÉT: Hoàn thành xử lý {success_count}/{len(raw_files)} tệp tin thành công. Hệ thống ổn định.")