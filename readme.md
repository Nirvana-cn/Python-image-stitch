## Readme

使用python和opencv进行图片融合

根据环境选择index.py中合适的stitcher

```
# openCV 3
stitcher = cv.createStitcher(cv.Stitcher_PANORAMA)

# openCV 4
stitcher = cv.Stitcher_create(cv.Stitcher_PANORAMA)
```