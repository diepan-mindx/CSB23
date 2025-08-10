import csv
import sys
sys.stdout.reconfigure(encoding='utf-8')

def process_csv(file_path):
    unique_emails = set()
    company_counts = {}

    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        # cat tung dong
        for row in reader:
            # kiem tra so luong cot (3)
            if len(row) != 3:
                continue  # bo qua neu sai dinh dang
            name, comp, email  = row
            # xoa khoang trang
            email = email.strip()
            comp = comp.strip()
            # kiem tra email da ton tai
            if email not in unique_emails:
                unique_emails.add(email)
                # cap nhat so luong dai bieu cua cong ty
                if comp in company_counts:
                    company_counts[comp] += 1
                else:
                    company_counts[comp] = 1

        # sap xep cong ty theo so luong dai bieu giam dan
        sorted_companies = sorted(
            company_counts.items(), key=(lambda item: item[1]), reverse=True
        )

        # in ket qua
        print(f"Số lượng đại biểu dự kiến tham dự: {len(unique_emails)}")
        print("Danh sách công ty và số lượng đại biểu:")
        for company, count in sorted_companies:
            print(f"{company}: {count}")


process_csv("L10/data.csv")
