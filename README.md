# Moe-Tagger
Tagger for text areas of Moe-Captcha


# How to use
- 安装依赖：`pip install -r requirement.txt` 或 `pip install opencv-python numpy`
- 下载后请将`Images`和`Tags`文件夹内用于占位的txt文件删除
- 运行程序`tagger.py`
  运行后会弹出如下窗口
  
![](https://github.com/Carzit/Moe-Tagger/blob/main/example/example1.PNG) 

-  请按如下蓝笔标示，按逆时针（或顺时针）顺序依次点击图像文字区域四角，使这四点连线而成的四边形可以覆盖验证码文字区域

![](https://github.com/Carzit/Moe-Tagger/blob/main/example/example2.PNG)

  点击后若标记成功，控制台会打印“successfully get point!”

![](https://github.com/Carzit/Moe-Tagger/blob/main/example/example3.PNG)

  点与点之间会自动连线，标定区域如图所示

-  每张图完成后，按`p`键进入下一张图
-  按`r`键重置在当前图上的所有操作
-  按`q`键退出标注程序

-  标注出错程序会报错并自动结束
-  手动按q退出或程序自动退出将会自动保存checkpoint日志，记录最后一次编辑的时间与截止图片的索引
-  代码很烂，给打标的佬先磕一个QAQ
