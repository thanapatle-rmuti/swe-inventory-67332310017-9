# tests/test_inventory.py
import pytest

from inventory import Inventory, InventoryItem

# =====================================================================
# TDD: ชุดทดสอบสำหรับเมธอด low_stock_items (6 กรณีตามโจทย์ขั้นที่ 2)
# =====================================================================

def test_low_stock_all_above_threshold():
    """กรณีที่ 1: สินค้าทุกรายการมีจำนวนมากกว่า threshold -> คืน list ว่าง"""
    inv = Inventory()
    inv.add_item("สมุด", 15, 50.0)
    inv.add_item("ดินสอ", 20, 10.0)
    assert inv.low_stock_items(10) == []


def test_low_stock_exact_threshold():
    """กรณีที่ 2: มีสินค้าที่จำนวนเท่ากับ threshold พอดี -> ต้องถูกนับรวมด้วย"""
    inv = Inventory()
    inv.add_item("ปากกา", 5, 20.0)
    inv.add_item("ยางลบ", 12, 15.0)
    # threshold = 5 สินค้าปากกาต้องถูกรวมในผลลัพธ์
    assert inv.low_stock_items(5) == ["ปากกา"]


def test_low_stock_sorted_by_name():
    """กรณีที่ 3: มีสินค้าเข้าเกณฑ์หลายรายการ -> ผลลัพธ์เรียงตามชื่อ ก-ฮ/A-Z"""
    inv = Inventory()
    # เพิ่มโดยไม่ได้เรียงชื่อ (C, A, B)
    inv.add_item("Crayon", 3, 30.0)
    inv.add_item("Apple Pen", 2, 100.0)
    inv.add_item("Book", 1, 80.0)
    inv.add_item("Drafting Table", 10, 500.0)  # เกิน threshold
    
    # สินค้าที่เข้าเกณฑ์คือ Crayon, Apple Pen, Book แต่ต้องเรียงตามชื่อเป็น Apple Pen, Book, Crayon
    assert inv.low_stock_items(4) == ["Apple Pen", "Book", "Crayon"]


def test_low_stock_empty_inventory():
    """กรณีที่ 4: คลังว่าง -> คืน list ว่าง ไม่ใช่ error"""
    inv = Inventory()
    assert inv.low_stock_items(10) == []


def test_low_stock_threshold_zero():
    """กรณีที่ 5: threshold เป็น 0 -> คืนเฉพาะสินค้าที่เหลือ 0"""
    inv = Inventory()
    inv.add_item("สินค้าหมด", 0, 50.0)
    inv.add_item("สินค้าเหลือ 1", 1, 50.0)
    assert inv.low_stock_items(0) == ["สินค้าหมด"]


def test_low_stock_negative_threshold():
    """กรณีที่ 6: threshold ติดลบ -> คืน list ว่าง เพราะจำนวนสินค้าไม่มีทางติดลบ"""
    inv = Inventory()
    inv.add_item("ปากกา", 0, 20.0)
    inv.add_item("ดินสอ", 5, 10.0)
    # ไม่มีสินค้าใดมีจำนวน <= -1
    assert inv.low_stock_items(-1) == []


# =====================================================================
# ขั้นที่ 4: ชุดทดสอบสำหรับเมธอด sell (AI ให้มา vs ข้อที่เขียนเสริม)
# =====================================================================

def test_sell_basic_happy_path():
    """[กรณีที่ AI ให้มา] ขายสินค้าปกติ ยอดลดลงและคืนค่าถูกต้อง"""
    inv = Inventory()
    inv.add_item("ยางลบ", 10, 10.0)
    remaining = inv.sell("ยางลบ", 3)
    assert remaining == 7
    assert inv._items["ยางลบ"].quantity == 7


# --- ข้อเสริมที่ 1 (ค่าขอบ): ขายหมดเกลี้ยงเท่ากับจำนวนคงเหลือพอดี ---
def test_sell_exact_remaining_to_zero():
    """ค่าขอบ: ขายเท่ากับจำนวนที่เหลือทั้งหมดได้ไหม แล้วเหลือเท่าไร (ต้องเหลือ 0)"""
    inv = Inventory()
    inv.add_item("ไม้บรรทัด", 5, 15.0)
    remaining = inv.sell("ไม้บรรทัด", 5)
    assert remaining == 0
    assert inv._items["ไม้บรรทัด"].quantity == 0


# --- ข้อเสริมที่ 2 (ค่าที่ไม่ควรรับ): ขายจำนวน 0 ---
def test_sell_zero_amount_rejected():
    """ค่าที่ไม่ควรรับ: ขายจำนวน 0 ต้องถูกปฏิเสธและ raise ValueError"""
    inv = Inventory()
    inv.add_item("สมุด", 10, 25.0)
    with pytest.raises(ValueError, match="จำนวนที่ขายต้องมากกว่าศูนย์"):
        inv.sell("สมุด", 0)
    assert inv._items["สมุด"].quantity == 10  # สต็อกไม่เปลี่ยน


# --- ข้อเสริมที่ 3 (ค่าที่ไม่ควรรับ): ขายจำนวนติดลบ ---
def test_sell_negative_amount_rejected():
    """ค่าที่ไม่ควรรับ: ขายจำนวนติดลบ ต้องถูกปฏิเสธและ raise ValueError"""
    inv = Inventory()
    inv.add_item("สมุด", 10, 25.0)
    with pytest.raises(ValueError, match="จำนวนที่ขายต้องมากกว่าศูนย์"):
        inv.sell("สมุด", -4)
    assert inv._items["สมุด"].quantity == 10


# --- ข้อเสริมที่ 4 (ค่าที่ไม่ควรรับ): ขายเกินจำนวนคงเหลือ ---
def test_sell_exceeding_stock_rejected():
    """ค่าที่ไม่ควรรับ: ขายมากกว่าสต็อกคงเหลือ ต้อง raise ValueError พร้อมบอกคงเหลือ"""
    inv = Inventory()
    inv.add_item("ปากกาไฮไลท์", 3, 35.0)
    with pytest.raises(ValueError, match="คงเหลือ 3 ชิ้น ไม่เพียงพอสำหรับการขาย 4 ชิ้น"):
        inv.sell("ปากกาไฮไลท์", 4)
    assert inv._items["ปากกาไฮไลท์"].quantity == 3


# --- ข้อเสริมที่ 5 (เส้นทาง error): ขายสินค้าที่ไม่มีในคลัง ---
def test_sell_non_existent_item_raises_key_error():
    """เส้นทาง error: ขายสินค้าที่ไม่มีในคลัง ต้อง raise KeyError พร้อมชื่อสินค้า"""
    inv = Inventory()
    with pytest.raises(KeyError, match="ไม่พบสินค้า 'คัตเตอร์' ในระบบ"):
        inv.sell("คัตเตอร์", 1)


# =====================================================================
# ชุดทดสอบเสริมความครอบคลุม (InventoryItem, Restock, Value)
# =====================================================================

def test_inventory_item_validation():
    """ตรวจสอบการสร้าง InventoryItem"""
    with pytest.raises(ValueError, match="ชื่อสินค้าต้องไม่ว่างเปล่า"):
        InventoryItem("", 10, 10.0)
    with pytest.raises(ValueError, match="ชื่อสินค้าต้องไม่ว่างเปล่า"):
        InventoryItem("   ", 10, 10.0)
    with pytest.raises(ValueError, match="จำนวนสินค้าต้องไม่ติดลบ"):
        InventoryItem("ปากกา", -1, 10.0)
    with pytest.raises(ValueError, match="ราคาต้องมากกว่าศูนย์"):
        InventoryItem("ปากกา", 10, 0.0)
    with pytest.raises(ValueError, match="ราคาต้องมากกว่าศูนย์"):
        InventoryItem("ปากกา", 10, -5.0)


def test_add_item_duplicate_rejected():
    """เพิ่มสินค้าซ้ำต้อง raise ValueError"""
    inv = Inventory()
    inv.add_item("สมุด", 5, 20.0)
    with pytest.raises(ValueError, match="สินค้า 'สมุด' มีอยู่ในระบบแล้ว"):
        inv.add_item("สมุด", 10, 20.0)


def test_restock_cases():
    """การเติมสินค้า restock"""
    inv = Inventory()
    inv.add_item("ดินสอ", 10, 5.0)
    assert inv.restock("ดินสอ", 5) == 15
    with pytest.raises(KeyError, match="ไม่พบสินค้า"):
        inv.restock("ไม่มี", 5)
    with pytest.raises(ValueError, match="จำนวนที่เติมต้องมากกว่าศูนย์"):
        inv.restock("ดินสอ", 0)
    with pytest.raises(ValueError, match="จำนวนที่เติมต้องมากกว่าศูนย์"):
        inv.restock("ดินสอ", -3)


def test_get_total_value():
    """คำนวณมูลค่ารวมของสินค้าในคลัง"""
    inv = Inventory()
    assert inv.get_total_value() == 0.0
    inv.add_item("สินค้า 1", 10, 20.0)  # 200.0
    inv.add_item("สินค้า 2", 5, 50.0)   # 250.0
    assert inv.get_total_value() == 450.0

