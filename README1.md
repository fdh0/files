# YCH_Information
  
![版本更新](https://img.shields.io/badge/build-passing-green.svg)
![logo](https://img.shields.io/badge/license-MIT-9cf.svg)

## 简介 

本项目是针对烟叶项目，包括关于目前烟叶项目的论文，专利等，以及相关需要展开的研发计划任务，开发需求等。

## 前言

根据国家标准，烟叶可以分为烤烟、晾晒烟、再造烟叶等大类，其中烤烟为最常见的类型。

烤烟分级国家标准《烤烟GB 2635—92》规定了烤烟的技术要求、检验方法和验收规则等内容，是分级、收购、交接的依据。

烤烟烟叶可以分为共**8个正组、5个副组**，在此基础上还可根据**烟叶的成熟度、叶片结构、身份、油分、色度、长度、残伤**等七个外观品级因素分为**42**个级。

目前，我国烟叶分级收购仍以人工为主，存在着劳动强度大、主观性强、工作效率低、分级标准不易掌握、分级精度不稳定等缺点，人工烟叶分级的主观性还造成了收购分级专家的灰色利益、烟农和收购方因分级不同意见引起的质量纠纷等问题。



## 烟叶图像

   <figure class="half">
  
   <img src="http://coding.daheng-imavision.com/api/~/group0/M00/00/44/fwAAAV26eESAW2HOAAgIjXlM174570.PNG?t" height="300" title="烟叶图像">
   </figure>  

## 烟叶图像先分组，后定级


   <figure class="half">
  
   <img src="http://coding.daheng-imavision.com/api/~/group0/M00/00/44/fwAAAV26eD2ADjNJAAOWOGEioSQ719.PNG?t" height="300" title="烟叶图像">
   ## 分组
  <img src="http://coding.daheng-imavision.com/api/~/group0/M00/00/44/fwAAAV26dDaAXUsDAAEI-c-fdu4294.PNG?t" height="300" title="分组">
  ### 定级 
  <img src="http://coding.daheng-imavision.com/api/~/group0/M00/00/44/fwAAAV26dDqABnjoAAEY_Rz1scg776.PNG?t" height="300" title="分组">

   </figure>  
   
   


## 注意事项

1. 由于采用光流法，与之前的不同，需要调整变形系数。但具体调整多少，尚没有一个较好的定式，并且会出现校正过度的问题，因此调整参数是个问题。   ![](https://github.com/fdh0/files/blob/master/question.png?raw=true)
 
      
2. 由于使用了光流法，会导致缺陷的显示位置有所偏差，大约在几个像素内。  当前未想到较好的解决方法。   ![](https://github.com/fdh0/files/blob/master/question.png?raw=true)
   
   <figure class="center">
   <img src="https://github.com/fdh0/files/blob/master/position_shift_PDF.PNG?raw=true" width="800" title="位置偏移">
   </figure>    
   <br>
  
   <figure class="half">
   <img src="https://github.com/fdh0/files/blob/master/shape_factor_0.05.PNG?raw=true" width="400" title="变形因子0.05">
   <img src="https://github.com/fdh0/files/blob/master/shape_factor_0.15.PNG?raw=true" width="400" title="变形因子0.15">
   </figure>  


## 版本更新

#### 版本号：6637 --  `[2019-03-21]`

<b>主要更新如下:</b> 

1. 对于大变形区域，根据区域进行读取、保存参数。这样能够允许检测中绘制多个检测参数不同的大变形区域。![](https://github.com/fdh0/files/blob/master/improved.png?raw=true)

2. 修改大变形区域自动阈值的方法。 这一点需要说明，之前使用大小模板的时候，是将当前检测图像与大小模板进行比较，阈值范围比较小。

目前使用的是当前检测图直接与建模模板图比较，这就导致可能不同的环境下不同的检测产品，检测阈值就不同。没有一个较好的指导准则。
 
因此，引出自动阈值的方法。使其自动寻求一个较合理的阈值。

<b>关键代码：</b> 

ParaDlg.cpp   -- OnInitDialog  

搜索关键词： 3/21/2019

```
//[11/29//2018 fdh] 增加大变形特检对话框
if (PM_AT_DBX == nInnerAlgType)
{
  nParamID =  m_lstAlgRegPro.at(0).sAlgRegCheckPro.ParamID;
  // [3/21/2019 fdh] 在这里加上大变形按区域保存的参数
  m_sTempCheckParam.sDBXParam.nHThresh = m_sTempCheckParam.lstPrevelExt.at(nParamID).Upper.Tolerance;
  m_sTempCheckParam.sDBXParam.dArea_white=m_sTempCheckParam.lstPrevelExt.at(nParamID).Upper.dArea;		
  m_sTempCheckParam.sDBXParam.nLThresh = m_sTempCheckParam.lstPrevelExt.at(nParamID).Lower.Tolerance;
  m_sTempCheckParam.sDBXParam.dArea=m_sTempCheckParam.lstPrevelExt.at(nParamID).Lower.dArea;
}
```


## 作者
 
* ** 冯东海 ** 


## 许可证

该项目根据MIT许可证授权。

版权所有?2019 ****************公司



