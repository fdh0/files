# BQ_PDF_Check  
  
![版本更新](https://img.shields.io/badge/build-passing-green.svg)
[![版本更新](https://img.shields.io/badge/release-v4.4.8.6634-blue.svg)](http://coding.daheng-imavision.com/p/BQ_PDF_Check/git/blob/master/README.md#user-content-%E7%89%88%E6%9C%AC%E6%9B%B4%E6%96%B0)
![logo](https://img.shields.io/badge/license-MIT-9cf.svg)

## 简介 

本项目是在线阵系统下，关于大变形票面检测的相关程序。

大变形的票面检测程序与之前的有所不同。之前的票面检测一般通过建立大小模板进行对比检测。

而基于大变形的票面检测，则是根据光流法，计算模板图与实际图之间的光流矢量矩阵，通过与校正后的实际图对比，进行缺陷检测。


## 先决条件

本程序是在 `Visual Studio 2010 `下生成的<B> DLL </B>动态链接库。  

动态库名称：` AlgPrintQIX64.dll `  

<b>版本号说明：</b>  前两位为系统结构位和系统一致，   

  第三位和算法管理层一致  
             
  最后一位为自定义升级  

所需动态库文件:  
```
release版本 
halconcpp.dll
opencv_imgproc231.dll
opencv_highgui231.dll
opencv_core231.dll
tbb.dll
BCGCBPRO2210d100.dll
debug版本 
halconcpp.dll
opencv_imgproc231d.dll
opencv_highgui231d.dll
opencv_core231d.dll
tbb_debug.dll
BCGCBPRO2210100.dll
```
系统配置文件:  对应动态库名算法默认配置文件夹下所有配置文件

数据库文件:  无

## 算法流程
```
获取检测图
  |
获取模板图
  |
根据光流法计算模板图到检测图的矢量变形矩阵
  |
根据矢量变形矩阵，校正检测图
  |
比较检测图与模板图
  |
Blob缺陷分析
```
## PDF转换及检测流程
```
PDF转换   —— 第一次转换的为建模模板图像，以后每次页码变换的为检测模板    
  |
模板图像
  |
 检测
```


## 软件界面

   <figure class="half">
  
   <img src="https://github.com/fdh0/files/blob/master/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20190214141957.jpg?raw=true" height="300" title="软件主界面">
   <img src="https://github.com/fdh0/files/blob/master/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20190214141852.jpg?raw=true" height="300" title="软件使用界面">

   </figure>  

## 注意事项

   1. 由于采用光流法，与之前的不同，可能有时候需要调整变形系数  
   
   2. 亮度增强系数，主要是针对PDF模板图纯底色，对于一般的织唛产品，无需增强亮度，设置为1即可。  


## 版本更新

#### 版本号：6634 --  `[2019-02-22]`

<b>主要更新如下:</b> 

1. 优化了大变形检测的时间。
   
   <b>原因：</b>在6633版本合并时，由于忽视了PDF边界区域与图像缩放没有保持一致，造成很多误报，且大大增加了检测时间，约300ms。 ![](https://github.com/fdh0/files/blob/master/solved.png?raw=true)  
   
   <b>解决方法：</b>将边界区域与图像的缩放系数保持一致。  
   
   <figure class="half">
   <img src="https://github.com/fdh0/files/blob/master/7.gif?raw=true" width="400" title="检测效果">
   <img src="https://github.com/fdh0/files/blob/master/9.gif?raw=true" width="400" title="检测时间">
   </figure>  
   
2. 先进行提取边界，再进行缩放。（如果先缩放提取边界再放大，边界会变异常。）  ![Solved](https://github.com/fdh0/files/blob/master/solved.png?raw=true)  
   	
   <figure class="half">
   <img src="https://github.com/fdh0/files/blob/master/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20190221161738.jpg?raw=true" width="400" title="先缩小后提取边界再放大">
   <img src="https://github.com/fdh0/files/blob/master/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20190221161730.jpg?raw=true" width="400" title="直接提取边界">
   </figure>  
   
3. 将数据与逻辑分离，将一些控制参数全部写入到配置文件中。(这样算法层面无需再改动，调动配置文件中的参数即可)  ![](https://github.com/fdh0/files/blob/master/improved.png?raw=true)

4. 分离Debug和Release模式。（现场均是使用Release模式，Debug里可以写出一些变量，这样便于调试。）  ![](https://github.com/fdh0/files/blob/master/improved.png?raw=true)

	关键代码:      
```
//--------TEST TIME-------
#ifdef DEBUG
CountSeconds(&hv_t2);
strErr.Format( "Erosion ModelImage :%.4f",(hv_t2[0].D()-hv_t1[0].D())*1000);
GenCurLog(strErr,1,0);
#endif // DEBUG
//--------TEST TIME END-----------
``` 
5.  <b>注意:</b>与此修改的对应的文件还有：  

* [票面默认参数](https://github.com/fdh0/files/blob/master/CheckParam.ini)  
* [建模程序](https://github.com/fdh0/files/blob/master/GCQIMission.exe)  
* [halcon调试程序](https://github.com/fdh0/files/blob/master/test_PDF.hdev)  

6. <b>问题:</b> 由于对图像进行了5倍缩放，图像质量下降。对于一些较小的区域，可能就损失厉害，在进行光流的时候，就可能校正不了。   ![](https://github.com/fdh0/files/blob/master/question.png?raw=true)

   <figure class="half">
   <img src="https://github.com/fdh0/files/blob/master/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20190222092938.jpg?raw=true" width="400" title="小区域灰度丢失">
   <img src="https://github.com/fdh0/files/blob/master/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20190222092945.jpg?raw=true" width="400" title="变形校正不好">
   </figure>  
 
 
#### 版本号：6633  -- `[2019-01-28]`  

<b>主要更新如下:</b>  

   1. 合并了织唛程序和PDF检测程序。（判断当前任务下是否有PDF转换的图像，有则增加PDF的特殊处理，无则进行一般的织唛产品检测）  
   
   2. 修复了找不到定位的Bug (增加了候选定位数目)  
   
   <b>PDF产品与一般的织唛产品检测的不同之处在于：</b>  
   
   1. 加载任务时，PDF会进入到PDF转换的模板图像中Crop出新的模板图像。  
   
   2. PDF为8K相机，图像缩放系数为0.2；一般的织唛产品为4K相机，图像缩放系数为0.5  
   
   3. * Emphasis对于PDF的效果较好，对于一般的织唛图像，需要用吗？效果如何？需要进一步确认。  
   
#### 版本号：6632  -- `[2019-01-26]`

<b>主要更新如下:</b>  

   1. 修复变形参数输入范围。（由于在输入小数时，编辑框会自动计算，因为很难输入0.2类似小数。——解决方法：在输入数时判断不在0.1-0.99,自动变为0.1，或者0.9）  

#### 版本号：6631  -- `[2019-01-24]` 

<b>主要更新如下:</b>  

   1. 修复了鼠标滚动的Bug。（鼠标滚动时，参数没有相应地改变。——<b>原因：</b>在BCGSlider事件中，重载与继承处没有相应地修改） 

#### 版本号：6630  -- `[2019-01-17]`

<b>主要更新如下:</b>  
  
   1. 测试水洗标产品  --6628--  
   
   2. 为了适用水洗标产品，去除了增强处理。（增强处理的目的主要是使一般的PDF标签的底色与纯白色的PDF模板图像更加接近，而一般的非PDF产品则不需要此操作） --6629---  
   
   3. 为了适用织唛产品，进行了模板灰度处理，修改了区域缩放系数（PDF为8K相机，缩放5倍，一般的织唛产品为4K相机，缩放2倍）  --6630--  

#### 版本号：6626  -- `[2019-01-14]`

<b>主要更新如下:</b>

   1. 算法的时间优化(总时间约120ms)，优化后提升15%-20%。  

   <b>优化项:</b> 把关于模板图像的Zoom缩放与膨胀操作置于加载任务中。  

   Zoom缩放:对于8192*2418大小的模板图像，耗时约15ms  

   灰度膨胀：对于8192*2418大小的模板图像，耗时约14ms  

#### 版本号：6625  -- `[2018-12-14]`

<b>主要更新如下:</b>  
    
   1. 在模板比较前增加增强处理，使能够检测白线；  

   2. 为减少条形码的误报，增加矩形度、椭圆度筛选；  

   3. 增加快速调参(尚未全部)；  

   4. 增加切换页码后自动加载模板[Guan]；  

   5. 为加快速度，减少自动找定位的数量[Guan]；  

   6.  根据现场需求，修改PDF模板边缘外扩像素数；   

#### 版本号：6622  -- `[2018-11-09]`
   
<b>主要更新如下:</b>
   
   1. 修改脏点浅白分开处理； 
   
#### 版本号：6618  -- `[2018-11-09]`

<b>主要更新如下:</b>  

   1. 在6895版的基础上，增加大变形的特检； 


## 作者
 
* ** 冯东海 **   -北京大恒图像视觉有限公司-


## 许可证

该项目根据MIT许可证授权。

版权所有©2019 北京大恒图像视觉有限公司




