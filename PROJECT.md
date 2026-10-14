# PROJECT.md: ระบบสต็อกสินค้า (Inventory Management System)

> **โครงงานรายวิชา Software Engineering**  
> **รหัสนักศึกษา:** 67332310017-9  
> **GitHub Repository:** [https://github.com/thanapatle-rmuti/swe-inventory-67332310017-9](https://github.com/thanapatle-rmuti/swe-inventory-67332310017-9) (Public)

---

## 1. ข้อมูลโครงงานและผู้รับผิดชอบ

| ข้อมูล | รายละเอียด |
| :--- | :--- |
| **ชื่อโครงงาน** | ระบบจัดการสต็อกสินค้า (Inventory Management System) |
| **รหัสนักศึกษา** | 67332310017-9 |
| **GitHub Username** | `thanapatle-rmuti` |
| **สถานะ Repository** | Public |
| **ขอบเขตการทำงาน** | รองรับสินค้าทั้ง Physical (สินค้าจับต้องได้) และ Digital (สินค้าดิจิทัล/ไฟล์) |

---

## 2. ภาพรวมระบบ (System Overview)

ระบบบริหารจัดการสต็อกสินค้าสำหรับร้านค้าและคลังสินค้า โดยมุ่งเน้นการใช้งานที่ง่าย รวดเร็ว และแม่นยำ:
1. **การจัดการสินค้า:** ตรวจสอบรายการสินค้า, บันทึกการรับเข้า (Receive/Restock) และจ่ายออก (Sell/Issue)
2. **การแยกประเภทสินค้า:**
   - **Physical Product:** สินค้าที่ต้องนับจำนวนสต็อกจริงในคลัง (เช่น ปากกา, สมุด, สายไฟ)
   - **Digital Product:** สินค้าในรูปแบบไฟล์หรือใบอนุญาตดิจิทัล (เช่น E-Book, Software License Key)
3. **ระบบคิดส่วนลดและคำนวณยอด (Discount Module):** จัดการโปรโมชัน, คำนวณราคาสินค้ารวมพร้อมส่วนลด, หาค่าเฉลี่ย และหาสินค้าราคาถูกที่สุด
4. **การควบคุมคุณภาพโค้ด:** พัฒนาควบคู่กับ Automated Test (`pytest`) และการ Review ตามหลักวิศวกรรมซอฟต์แวร์

---

## 3. โครงสร้างไฟล์ใน Repository

```text
├── README.md                      # ภาพรวมของ Repository
├── PROJECT.md                     # ข้อมูลโครงงานฉบับสมบูรณ์ (ไฟล์นี้)
├── TEAM_CHARTER.md                # ข้อกำหนดการทำงาน กฎของทีม และนโยบาย AI
├── inventory.py                   # โมดูล Inventory ฐานอ้างอิง
└── lab04-ai-coding-ux/            # งาน Lab 4
    ├── findings-lab04.md          # ผลการสัมภาษณ์ผู้ใช้และ Point of View
    ├── persona.md                 # Persona และ User Journey Map
    ├── assets/
    │   ├── wireframe-ai.md        # Text Wireframe (3 หน้าจอ)
    │   └── mockup-link.txt        # ลิงก์ไปยัง UI Mockup
    ├── accessibility-review.md    # ตรวจสอบ Accessibility ตาม WCAG 2.1 AA
    ├── prompt-vs-context.md       # เปรียบเทียบ Prompt Engineering vs Context Engineering
    ├── code-review.md             # ผลการ Review โค้ด inventory_service.py
    ├── debug-log.md               # บันทึกการ Debug โค้ด discount.py
    ├── inventory.py               # โค้ด Inventory ฐานอ้างอิง
    ├── inventory_service.py       # โค้ด Service ที่ผ่านการ Review
    ├── discount.py                # โค้ดโมดูลส่วนลดที่ผ่านการ Debug ครบทุกข้อ
    └── tests/
        └── test_discount.py       # Unit Test ครบชุดผ่าน 100%
```

---

## 4. การติดตั้งและรันการทดสอบ (Getting Started)

### ติดตั้งเครื่องมือทดสอบ
```bash
pip install pytest
```

### การรัน Unit Test สำหรับ Lab 4
```bash
cd lab04-ai-coding-ux
python -m pytest tests/ -v
```
