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
