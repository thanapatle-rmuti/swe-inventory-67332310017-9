# TEAM_CHARTER.md

## สมาชิกและบทบาท

| ชื่อ-นามสกุล / รหัสนักศึกษา | GitHub Username | บทบาท |
|---|---|---|
| ธนภัทร (67332310017-9) | thanapatle-rmuti | Product Owner / Developer |
| AI Assistant | - | Scrum Master / Developer (Reviewer) |

## Branching Strategy

ใช้ GitHub Flow:
- `main` branch ต้อง deploy ได้เสมอ ห้าม commit โค้ดที่พังโดยตรง
- ทุก feature หรือ lab ใหม่ต้องสร้าง branch เช่น `feat/<issue-number>-<short-name>` หรือ `lab04-ux-review-debug`
- ทุก PR ต้องผ่านการ review ก่อน merge
  - ทำคนเดียว: AI ในบท reviewer review ตามเกณฑ์ วางผลลงใน PR และตอบทุกข้อก่อน merge

## WIP limit

- คอลัมน์ In Progress มีการ์ดพร้อมกันได้ไม่เกิน 1 ใบ (สำหรับการทำงานคนเดียว)
- เมื่อการ์ดเต็ม WIP limit ห้ามลากการ์ดใหม่เข้ามา ให้ทำการ์ดเดิมให้เสร็จ หรือ review PR ที่ค้างใน In Review ก่อน
- ปรับ WIP limit ระหว่าง sprint ได้ แต่ต้องเขียนเหตุผลกำกับไว้

## Sprint Goal

ส่งมอบงาน Lab 4: การออกแบบ UX/Mockup สำหรับสินค้า Physical & Digital, ทำ Code Review และ Debug โค้ดโมดูล Discount ให้ผ่าน Unit Test ครบ 100%

## AI Usage Policy

- ใช้ AI ช่วยเขียน draft code, draft wireframe และ draft commit message ได้
- ทุก commit message ที่ AI generate ต้องอ่านและแก้ให้ตรงกับ diff จริงก่อน commit
- ห้าม copy code จาก AI โดยไม่อ่านและทำความเข้าใจก่อน
- ใช้เฉพาะ AI ที่ไม่มีค่าใช้จ่าย
