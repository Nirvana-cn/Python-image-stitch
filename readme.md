## Readme

使用python和opencv进行图片融合

根据环境选择index.py中合适的stitcher

```
# openCV 3
stitcher = cv.createStitcher(cv.Stitcher_PANORAMA)

# openCV 4
stitcher = cv.Stitcher_create(cv.Stitcher_PANORAMA)
```

### 参考

OpenCV探索之路（二十四）图像拼接和图像融合技术：[>>>点我进入](https://www.cnblogs.com/skyfsm/p/7411961.html)

python调用stitcher类进行图像拼接融合：[>>>点我进入](https://blog.csdn.net/yy2yy99/article/details/103034651)

AutoStitch: a new dimension in automatic image stitching：[>>>点我进入](http://matthewalunbrown.com/autostitch/autostitch.html)