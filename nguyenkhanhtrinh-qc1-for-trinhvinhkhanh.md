# Phiếu QC 1 — Road v1.0

Lô được kiểm (học viên): Trịnh Vĩnh Khánh (2A202603220)        Người kiểm (học viên): Nguyễn Khánh Trình (2A202603026)  
Ngày: 2026-11-20                Phiên bản guideline: Road v1.0  
File được kiểm (tên + `revision` trong manifest): trinhvinhkhanh-front.zip, trinhvinhkhanh-fisheye.zip — revision 1 (sha256 khớp manifest)  
Số ảnh kiểm: 6 (A01, A02, A04, A08, A12, B02) (+ 0 ảnh thêm)   Số nhãn đã kiểm (shape + tag): 89 (65 shape + 24 tag)  

## Tổng hợp theo mã
| Mã | Loại lỗi | Số mục kiểm | Số lỗi | Mức |
| --- | --- | ---: | ---: | --- |
| QC1-01 tag camera | sai thuộc tính / bỏ sót | 6 | 0 | nặng |
| QC1-02 đủ L1, R1 | bỏ sót | 5 | 0 | nặng |
| QC1-03 position | sai thuộc tính / thừa | 15 | 4 | nặng |
| QC1-04 tâm vạch, chiều, điểm dừng | sai phạm vi / bỏ sót | 19 | 0 | chính |
| QC1-05 vạch đứt, che | sai phạm vi / sai thuộc tính | 15 | 0 | chính |
| QC1-06 style, color, kind | sai thuộc tính | 15 | 0 | chính |
| QC1-07 vùng lái | sai phạm vi / bỏ sót / thừa | 13 | 0 | chính |
| QC1-08 đèn, màu | bỏ sót / sai phạm vi / sai thuộc tính | 15 | 0 | nặng / chính |
| QC1-09 facing, type, group, biển phụ | sai thuộc tính | 13 | 0 | chính |
| QC1-10 hình in, đủ biển | bỏ sót / sai phạm vi | 13 | 0 | chính |
| QC1-11 fisheye | sai phạm vi / sai thuộc tính | 3 | 0 | chính |
| QC1-12 file | lỗi file | 2 | 0 | nhẹ / nặng |

## Danh sách lỗi (mỗi lỗi một dòng)
| # | Mã | Ảnh | Nhãn (label, id) | Mức | Mô tả ngắn |
| --- | --- | --- | --- | --- | --- |
| 1 | QC1-03 | A02 | lane#5 @(432,720) | nặng | Vạch đứt tim đường sát bên trái xe là L1, đang gán L2 |
| 2 | QC1-03 | A02 | lane#4 @(0,585) | nặng | Vạch đứt xa bên trái là L2, đang gán L1 (đổi chỗ với lane#5) |
| 3 | QC1-03 | A04 | lane#1 @(28,552) | nặng | Nửa ngoài của cùng một vạch vàng đôi bị gán L2 |
| 4 | QC1-03 | A08 | lane#16 @(776,318) | nặng | Vạch liền nằm bên PHẢI xe (sau R1 #21) phải là R2, đang gán L2 |

Ảnh kiểm không thấy lỗi: **A01** (4 tag, L2/L1/R1, 2 road_curb, 3 drivable, 2 biển chỉ dẫn đều đúng), **A12**, **B02**.

## Ca mơ hồ
| Ảnh | Câu hỏi cho lead | Lời đáp (nếu có) |
| --- | --- | --- |
| A04 | Vạch vàng đôi: 1 polyline `kind=double` hay 2 polyline? | Coach hướng dẫn 2 polyline cùng L1 → nửa ngoài gán L2 vẫn là sai position |
| A08 | Không có L1: bên trái làn xe đang đi có vạch sơn không? | chưa có |

## Quyết định
Lỗi nặng: 4   Lỗi chính: 0 / 89 nhãn = 0 %   Lỗi nhẹ: 0   Ca chờ lead: 1  
Quyết định (Release / Hold / Rework): **Rework**  
Lý do (theo luật của phiếu): còn 4 lỗi nặng (QC1-03 sai position ở A02, A04, A08). Tỉ lệ lỗi chính 0 % ≤ 5 % nhưng lỗi nặng đủ để Rework; ca chờ lead không đổi quyết định.

Loại lỗi: bỏ sót = thiếu nhãn phải có; thừa = gán cái không phải đối tượng; sai phạm vi = hình lệch, sai chiều, dừng sai chỗ, tràn vùng. Ba loại này theo cách chia lỗi gán nhãn của ISO/IEC 5259-4 (mục 8.4.2); "sai thuộc tính" và "lỗi file" là khóa học thêm. Cách xếp mức: [thang mức lỗi](../docs/qc_severity_road_v1.0.md).
