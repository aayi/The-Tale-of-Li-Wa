# The-Tale-of-Li-Wa
This paper uses digital technology and spatial narrative theory to represent the narrative and narrative of experience of a Chinese classic novel, [*The Tale of Li Wa*]( https://en.m.wikipedia.org/wiki/The_Tale_of_Li_Wa), which has been favored by literature and historians in the past approximately 900 years. To help contemporary readers understand this classic narrative and its context more wholly and deeply, the spatio-temporal information, derived from its text, its author, and readers, is extracted and fused to map the instantaneous spatial pattern perceived by readers in the flow of reading time. These comparative patterns form a logical loop of “time–space–time–space” that helps contemporary readers once again observe the literary and historic value through spatio-temporal narratives.

![*Flows (black arrows) of variables and comparisons (white arrows) among variables in the logical loop of time–space-time–space.*]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/Fig2.tif)
# 0. Digitization
1. [Electronically scanned version]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/S1_File.pdf) of *The Tale of Li Wa* in *Complete Library in Four Sections* 四库全书
2. [Proofreading Text Edition]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/??.txt) of *The Tale of Li Wa* based on the version on [中国哲学书电子化计划（CText）]( https://ctext.org/wiki.pl?if=en&chapter=114571&remap=gb)
3. [*Raster map of Tang Chang'an with location information*](https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/S2_File.zip).  
It can be added in Arcmap/Qgis. It is an archaeological map in 「数字历史黄河·城市聚落资料集」from Remote Sensing Analysis of Historical Landscape and GIS Laboratory, Northwest Institute of Historical Environment and Socio-Economic Development, Shaanxi Normal University 陕西师范大学西北历史环境与经济社会发展研究院历史景观遥感分析与GIS实验室
4. 黄大宏. [A chronicle of Bai Xingjian](https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/31白行简年谱_黄大宏.pdf) 

# 1. Structuring
## 1.1 Text database on word level
[sheet1_name: *term*, sheet2_name: *POS*, sheet3_name: *so*, sheet4_name: *sentiment classification score*](https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/S1_Table.xlsx) 

we manually create this database including terms (unigram), parts of speech (POS), sentiment orientations (SO) value, and sentiment shifters by Excel. 

### 1)*term*  
Criteria: broadening, dictionary, and semantic transparency  
Reference dictionary: [国学大师](http://www.guoxuedashi.com/)  
Reference Word Segmentation platform: [语料库在线](http://www.aihanyu.org/cncorpus/CpsWParser.aspx)  

### 2)*POS*  

Tag  | n  | nt  | nd  | nl  | nh  | nhf  | nhs  | ns  | nn  | ni  | no  | nhh  | v  | vd  | vl  | vu  | a  | f  | m  | q  | d  | r  | p  | c  | u  | e  | o  | i  | w      
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---
 pos  | Noun-general  | Noun-time | Noun-direction | Noun-location | Noun-human | noun-last name | noun-first name | Noun-space | Noun-nation | Noun-institution | Noun-offical  | noun-human’s pronoun | Verb | Verb- direction | Verb-linking | Verb-auxiliary | adjective | difference | numeral | quantity  | adverb  | pronoun | preposition | conjunction | auxiliary | exclamation | onaomatopoeia | idiom | punctuation 
 
### 3)*so*  
The assignment of the SO value is as follows: each positive sentiment expression in the novel such as laugh (欢笑) (v.) and magnificent (瑰奇) (a.) is given an SO value of +1 (172 in total), and each negative sentiment expression such as whimper (呜咽) (v.) and poor (贫窭) (a.) is assigned a SO value of −1 (177 in total).  
We do two rounds of sentiment orientations (SO) value assignment(*LIU_SO value* and *MA_SO value*).  
The percentage of consent of two rounds of SO value assignment is 81.5%

### 4)*sentiment classification score*  

```
SO_value_effective = IF(sentiment_shifter_-1=-1,SO value * sentiment_shifter_-1,SO value)   

for_phrase_sentiment_classification_score = IF(POS<>"w",SO_value_effective,"")  
```
for_phrase_sentiment_classification_score = SUM(for_phrase_sentiment_classification_score))  
#tip: Ctrl+ G--> "Null(k)"--> "∑"( Automatic summation) #
```
phrase_sentiment_classification_score = IF(POS="w",for_phrase_sentiment_classification_score)
```
## 1.2 Text database on phrase level
[sheet1_name: *phrase*, sheet2_name: *time*, sheet3_name: *character*, sheet4_name: *character & SO*, sheet5_name: *place*, sheet6_name: *place & SO*](https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/S2_Table.xlsx) 

The phrase-level framework assigns the recalculated value of POS and SO value to a relevant phrase by Excel. These values can be applied to the next time level because the sequence number of phrases is defined as read-time. Specific data mining approaches for the following parameters, i.e. places, story-time, and sentiment classification scores are valuable.

### 1)*phrase*  
*sentiment_classification_score(SCS)* inherits the value of [*phrase_sentiment_classification_score*]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/README.md#4sentiment-classification-score)  
### 2)*time*  
*storytime_day*  
Noun-time (nt.) such as the Tianbao period (天宝), 10 years later (十年), more than a month later (月余), and another day (他日), which is 2.7% of the total texts, are used to simulate the whole story-time in an interval of every single day. The entire story timeline we constructed from the texts started from when Student Zheng entered Chang’an in 747A.D. and ended around the happy ending of the novel, that is, the year Zheng is appointed to become an officer is 754 A.D., and Li Wa is conferred the title Lady Qian‘guo (汧国夫人) in 775 A.D. The story-time is defined by the exact time record of the story that occurred during the period of 742 to 746 A.D.(天宝年间), Bai Xingjian wrote the tale in August of 795 A.D. (贞元中……乙亥岁秋八月) and the nt. phrases. 

*readtime_phrase*  
the sequence number of phrases is defined as read-time  
### 3)*character*  
*character1*， *character2*， *character3*， and *character4* contain up to 4 characters in each phrase.
### 4)*character & SO*  
```
ZHENG_SCS = IF(character1="郑生" or character2="郑生" or character3="郑生" or character4="郑生",sentiment_classification_score(SCS),"")  
```
ZHENG_so_IF= SUM(J15ZHENG_SCS)
#tip: ```K15=SUM(J$15:J15), K18=SUM(J$15:J18), K50=SUM(J$15:J50)```#
### 5)*place*  
A noun-space (ns.) such as Chang’an City, and specific place names inside the city such as the Buzheng Ward (布政坊) and Xingyuan Garden (杏园) (located in Tongshan Ward [通善坊]), account for 1.1% of the total texts tagged as the level of residential wards and streets directly mentioned (e.g., Buzheng Ward) or most likely to be located (e.g., Tongshan Ward). These uniformly fine-grained places are applied to cover the corresponding story phrases of which plot takes place in these places.
### 6)*place & SO*  
```
Anyi_SCS = IF(ward_in_chang'an="安邑坊",sentiment_classification_score(SCS),"")  
```
Anyi_so_IF= SUM(Anyi_SCS)
#tip: ```I526=SUM(H$526:H526), I535=SUM(H$526:H535), I606=SUM(H$526:H606)```#

## 1.3 Chronicle of Bai Xingjian
[sheet1_name: *circumstance*, sheet2_name: *poems*](https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/S3_Table.xlsx) 
it is bassed on [A chronicle of Bai Xingjian](https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/31白行简年谱_黄大宏.pdf) by 黄大宏 in Excel

*circumstance_orientation_value* is assigned manually based on *Detail*   

Circumstances_of_Bai = SUM(circumstance_orientation_value)
#tip: ```E2=SUM($D$2:D2), E10=SUM($D$2:D10), E52=SUM($D$2:D52)```#  
```
circumstance_orientation_value_chang'an = IF(Place="长安",circumstance_orientation_value,"")  
```
## 1.4 Spatial syntax of Chang'an
Vector file of street of chang'an is created by Autocad and then [imported into Depthmap](https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/S4_File.graph)(a technology used to analyze the spatial layouts, and human activity patterns in urban areas)  

![Integration analysis of the road network of Chang’an city by Depthmap]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/Fig4.tif)  
  
The degree of integration (a space syntax parameter) reflects the ease of access to streets, that is, it may determine which street is more likely to attract Zheng, as an explorer of Chang’an.  
## 1.5 Spatially embedded semantic data
Combine Text database with spatial data by Arcmap主要将文本中的数据导入GIS形成点数据、线数据及面数据。
### 1)Polygon
create shapefile of **Polygon**( Ward& Palace) based on[*Raster map of Tang Chang'an with location information*](https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/S2_File.zip)  
### 2)point(*shikong-vt.shp*)
create **Point**( centroid of **Polygon**)--> add field "ward_in_chang'an" and fill in  
[Text database on phrase level](https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/S2_Table.xlsx) is joined with **Point** by field "ward_in_chang'an"
依据GIS功能，将长安GIS中的坊和皇宫等面数据进行质心计算，得出每个面数据的质心。将文本数据库中的每个坊里所对应的信息通过GIS文件连接导入GIS数据集中，其中点数据包括以下信息：每个坊信息的文本句数、坊里的情感累加值、坊里人群活动的阶级值等信息。以便后续的插值分析计算。
### 3)polyline线数据
依托空间句法软件计算长安每个街道的可达性，并结合最短路径原则将小说人物在长安城中的活动轨迹进行模拟，并将路径在GIS中进行绘制。将该线数据进行相应的数据录入，包括：小说人物、人物身份及阶级等信息。



# 2. Representation
## 2.1 Time 
![Trajectory of the integral function of SO value by sigmaplot]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/Fig5.tif)  
create graph--> simple straight line--> data format--> XY Pair--> select data   
data for X: *storytime_day*  data for Y: *SO_value_Integral_function(so_IF)* 

![Trajectory of the integral function of SO value and characters’ appearance by sigmaplot]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/Fig6.tif)  
create graph--> multiple straight line--> data format--> XY Pair--> select data   
data for X: *storytime_day*  data for Y: *SO_value_Integral_function(so_IF)*   
data for X: *storytime_day*  data for Y: *ZHENG_so_IF*  
data for X: *storytime_day*  data for Y: *LI_Wa_so_IF*   
data for X: *storytime_day*  data for Y: *LI_Wa's_mother_so_IF*   
data for X: *storytime_day*  data for Y: *ZHENG's_father_so_IF*   

![Trajectory of the integral function of SO value and places’ appearance by sigmaplot]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/Fig7.tif)  
create graph--> simple straight line--> data format--> XY Pair--> select data   
data for X: *storytime_day*  data for Y: *SO_value_Integral_function(so_IF)*  

add new plot--> graph types--> vertical bar chart--> graph styles--> grouped bars--> data formats--> many Y   
data for Y: *Anyi_so_IF*  
data for Y: *Buzheng_so_IF*  
data for Y: *Chongren_so_IF*  
data for Y: *EastMarket_IF*  
data for Y: *Pingkang_IF*  
data for Y: *DepartmentOfStateAffairs_IF*  
data for Y: *TianmenStreet_so_IF*  
data for Y: *Tongshan_so_IF*  
data for Y: *Tongyi_so_IF*  
data for Y: *WestMarket_so_IF*  
data for Y: *XingqingPalace_IF*  
data for Y: *Xuanyang_so_IF*  

graph page--> add axist--> Y  
![Trajectory of the integral function of SO value versus the story-time’s appearance by sigmaplot]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/Fig8.tif)  
create graph--> multiple straight line--> data format--> XY Pair--> select data   
data for X: *storytime_day*  data for Y: *SO_value_Integral_function(so_IF)*   
data for X: *storytime_day*  data for Y: *readtime_phrase*   

graph page--> add axist--> Y  
# 2. Visualization in time level
## Sigmaplot 
# Gis
# Arcscene
# Gis
# Gephi 
## 二级标题  
### 三级标题  
#### 四级标题  
##### 五级标题  
###### 六级标题 
二、编辑基本语法  
1、字体格式强调
 我们可以使用下面的方式给我们的文本添加强调的效果
*强调*  (示例：斜体)  
 _强调_  (示例：斜体)  
**加重强调**  (示例：粗体)  
 __加重强调__ (示例：粗体)  
***特别强调*** (示例：粗斜体)  
___特别强调___  (示例：粗斜体)  
2、代码  
`<hello world>`  
3、代码块高亮  
```
@Override
protected void onDestroy() {
    EventBus.getDefault().unregister(this);
    super.onDestroy();
}
```  
4、表格 （建议在表格前空一行，否则可能影响表格无法显示）
 
 表头  | 表头  | 表头
 ---- | ----- | ------  
 单元格内容  | 单元格内容 | 单元格内容 
 单元格内容  | 单元格内容 | 单元格内容  
 
5、其他引用
图片  
![图片名称](https://www.baidu.com/img/bd_logo1.png)  
链接  
[链接名称](https://www.baidu.com/)    
6、列表 
1. 项目1  
2. 项目2  
3. 项目3  
   * 项目1 （一个*号会显示为一个黑点，注意⚠️有空格，否则直接显示为*项目1） 
   * 项目2   
 
7、换行（建议直接在前一行后面补两个空格）
直接回车不能换行，  
可以在上一行文本后面补两个空格，  
这样下一行的文本就换行了。
或者就是在两行文本直接加一个空行。
也能实现换行效果，不过这个行间距有点大。  
 
8、引用
> 第一行引用文字  
> 第二行引用文字
# Reference
[ArcGIS Desktop. Version 10.2.2]( https://arcgis_desktop.en.downloadastro.com/old_versions/)
[IDW]( http://desktop.arcgis.com/en/arcmap/latest/tools/3d-analyst-toolbox/idw.htm)
[Linear Density](http://desktop.arcgis.com/en/arcmap/10.3/tools/spatial-analyst-toolbox/line-density.htm)
[reference1]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/reference1.zip)
[reference2]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/reference2.zip)
[reference3]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/reference3.zip)
[reference4]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/reference4.zip)

