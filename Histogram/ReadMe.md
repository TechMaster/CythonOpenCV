
# Tính toán histogram của một bức ảnh
Trong 3 cách:
1. hist1.py: 2 vòng lặp loop cách dễ hiểu. Chạy cực chậm
2. hist2.py: Sử dụng Numpy, tối ưu tốc độ khá nhiều
3. hist3.py: Sử dụng hàm có sẵn trong OpenCV, cv2.calcHist tốc độ tốt nhất

Tốc độ sử dụng OpenCV nhanh hơn cách dùng Numpy 26 lần. Cách đầu tiên quá chậm
nên không tính đến.

# Điều chỉnh Auto Contrast của một bức ảnh

- ModifyContrast1.py: dùng 2 vòng lặp, lệnh dễ hiểu.
- ModifyContrast2.py: dùng Numpy + LUT nhưng hàm LUT lại rất chậm
- ModifyContrast3.py: Sử dụng 2 vòng lặp nhưng cho vào Cython tốc độ nhanh hơn hẳn