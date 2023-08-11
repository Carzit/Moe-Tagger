# Moe-Tagger
Tagger for text areas of Moe-Captcha


# How to use
- 安装依赖：pip install -r requirement.txt 或 pip install opencv-python numpy
- 运行程序tagger.py
  运行后会弹出如下窗口

  请按如下蓝笔标示，按逆时针（或顺时针）顺序依次点击图像文字区域四角，使这四点连线而成的四边形可以覆盖验证码文字区域
  （点击后若标记成功，控制台会打印“successfully get point!”）
  每张图完成后，按p键进入下一张图（若无反应，请按两下）
  按q键退出标注程序

  标注出错程序会报错并自动结束
  手动按q退出或程序自动退出将会自动保存checkpoint日志，记录最后一次编辑的时间与截止图片的索引。
