# The-Tale-of-Li-Wa
People living in the digital age usually has difficulties in reading classical novels, in terms of obscure words, contextual difference and reading habits. This paper proposes a framework of digital models integrating spatial narrative theories to represent the narrative and narrative of experience of a Chinese classic novel,  [*The Tale of Li Wa*]( https://en.m.wikipedia.org/wiki/The_Tale_of_Li_Wa), which has been diversely interpreted by literature and historians in the past approximately 900 years. To help contemporary readers understand this classic narrative and its context in an integrated and in-depth approach, based on its knowledge graph about “narratives, experiences and geographical spaces”, the spatio-temporal information, derived from its text, its author, and readers, is extracted and fused to map the instantaneous spatial pattern perceived by readers in the flow of reading time.The discussion presents one of these possible interpretations on illustrating the growth of  the novel’s male protagonist in the open framework of "Time-Space-time-Space", which unfolds dialogues between computation and literature, diachronic and synchronic, reader and the author.

##### *Flows (black arrows) of variables and comparisons (white arrows) among variables in the logical loop of time–space-time–space.*
![*Flows (black arrows) of variables and comparisons (white arrows) among variables in the logical loop of time–space-time–space.*]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/png/Fig2.png)
# 0. Digitization
1. [Electronically scanned version]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/S1%20File.pdf) of *The Tale of Li Wa* in *Complete Library in Four Sections* 四库全书
2. [Proofreading Text Edition]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/liwazhuang.txt) of *The Tale of Li Wa* based on the version on [中国哲学书电子化计划（CText）]( https://ctext.org/wiki.pl?if=en&chapter=114571&remap=gb)
3. [*Raster map of Tang Chang'an with location information*](https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/S2%20File.zip).  
It can be added in Arcmap/Qgis. It is an archaeological map in 「数字历史黄河·城市聚落资料集」from Remote Sensing Analysis of Historical Landscape and GIS Laboratory, Northwest Institute of Historical Environment and Socio-Economic Development, Shaanxi Normal University 陕西师范大学西北历史环境与经济社会发展研究院历史景观遥感分析与GIS实验室
4. 黄大宏. [A chronicle of Bai Xingjian](https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/31白行简年谱_黄大宏.pdf) 

# 1. Structuring
## 1.1 Text database on word level
[sheet1_name: *term*, sheet2_name: *POS*, sheet3_name: *so*, sheet4_name: *sentiment classification score*](https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/S1%20Table.xlsx) 

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
[sheet1_name: *phrase*, sheet2_name: *time*, sheet3_name: *character*, sheet4_name: *character & SO*, sheet5_name: *place*, sheet6_name: *place & SO*](https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/S2%20Table.xlsx) 

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
[sheet1_name: *circumstance*, sheet2_name: *poems*](https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/S3%20Table.xlsx) 
it is bassed on [A chronicle of Bai Xingjian](https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/31白行简年谱_黄大宏.pdf) by 黄大宏 in Excel

*circumstance_orientation_value* is assigned manually based on *Detail*   

Circumstances_of_Bai = SUM(circumstance_orientation_value)
#tip: ```E2=SUM($D$2:D2), E10=SUM($D$2:D10), E52=SUM($D$2:D52)```#  
```
circumstance_orientation_value_chang'an = IF(Place="长安",circumstance_orientation_value,"")  
```
## 1.4 Spatial syntax of Chang'an
Vector file of street of chang'an is created by Autocad and then [imported into Depthmap](https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/S4%20File.graph)(a technology used to analyze the spatial layouts, and human activity patterns in urban areas)  

##### *Integration analysis of the road network of Chang’an city by Depthmap*
![Integration analysis of the road network of Chang’an city by Depthmap]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/png/Fig4.png)   
Using CAD to depict the main road axis map of Chang'an map → Save as dxf file → Open the depthmap software and create a new workspace → Map-import-Choosing Changan Road Axis Chart → ap-convert drawing map→tools-axial/convex/pesh-run graph analysis-Radius/list of radii – input n,2,3,5,7-choose include choice（betweenness）/local measures/RA,RRA and total depth/weighted measures-length

The degree of integration (a space syntax parameter) reflects the ease of access to streets, that is, it may determine which street is more likely to attract Zheng, as an explorer of Chang’an.  

## 1.5 Spatially embedded semantic data
[Combine Text database with spatial data by Arcmap](https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/S3%20File.zip)  

### 1)Polygon
create shapefile of **Polygon**( Ward& Palace) based on[*Raster map of Tang Chang'an with location information*](https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/S2%20File.zip)  
### 2)point
#### shikong-vt.shp
- create **Point**( centroid of **Polygon**)--> add field "ward_in_chang'an" and fill in  
- [Text database on phrase level](https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/README.md#11-text-database-on-word-level) is joined with **Point** by field "ward_in_chang'an"  
#### [LIWA_data.shp](https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/S6%20File.zip)  
- create **Point**( centroid of **Polygon**)--> add field "ward_in_chang'an" and fill in 
- create **place.xlsx**( sheet1_name: *stratum_statistics*, sheet2_name: *place_statistics*) by Excel based on [Text database on phrase level](https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/README.md#11-text-database-on-word-level)  
 
 place  | sum_sentiment_effective_classification_score  | phrase_count  | averge_sentiment_classification_score  | effective_sum_sentiment_classification_score  | effective_phrase_count  | averge_sentiment_effective_classification_score  | averge_stratum  | STDEV_stratum  | COUNT_stratum      
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---
 ward  | SUM(place_SCS)  in sheet" place & SO"  | COUNT(place_SCS)  in sheet" place & SO"   |  AVERAGE(place_SCS)  in sheet" place & SO"  | IF place_SCS<>0,SUM(place_SCS),""  in sheet" place & SO" | IF place_SCS<>0,COUNT(place_SCS),""  in sheet" place & SO" | IF place_SCS<>0,AVERAGE(place_SCS),""  in sheet" place & SO" | AVERAGE(place_stratum)  in sheet" stratum_statistics" | STDEV(place_stratum)  in sheet" stratum_statistics" | COUNT(place_stratum)  in sheet" stratum_statistics"   
- **place.xlsx** is joined with **Point** by field "NAME"   
### 3)polyline
#### temporal simulation path in sapce.shp
Arcmap--> Toolbox--> XY to Line--> import *shikong-vt.shp*
#### [link_between_places.shp](https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/S5%20File.zip)
-  create **path.xlsx** by Excel based on [Text database on phrase level](https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/README.md#11-text-database-on-word-level)  
Each time when *ward_in_chang'an* in sheet "place & SO" changes, an *ID* is added in **path.xlsx** with *Origin* to *Destination*  
*sentiment score between places*: value difference of *sum_sentiment_effective_classification_score* between *Origin* and *Destination*

*straturm classification*: The classification of social stratum of the *character*
The classification of social stratum in the story from untouchable to nobles is as follows: (1) beggar, servant, and sex worker; (2) businessman, civilian, madam; (3) ward head (里胥), candidate student, successful candidate, county judicial official (贼曹); and (4) Chang’an officials (京尹) and officials from other places. 
-  create **polyline**
The rules of the simulation are from the characteristics of the streets: first, prefer the shortest path, and second, prefer the street sections with the highest degree of spatial syntax [integration](https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/S4%20File.graph). 
- **path.xlsx** is joined with **polyline** by field "ID" 

# 2. Representation
## 2.1 Time 
##### *Trajectory of the integral function of SO value by sigmaplot*
![Trajectory of the integral function of SO value by sigmaplot]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/png/Fig5.png)  
create graph--> simple straight line--> data format--> XY Pair--> select data   
data for X: *storytime_day*  data for Y: *SO_value_Integral_function(so_IF)* 

##### *Trajectory of the integral function of SO value and characters’ appearance by sigmaplot*
![Trajectory of the integral function of SO value and characters’ appearance by sigmaplot]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/png/Fig6.png)  
create graph--> multiple straight line--> data format--> XY Pair--> select data   
data for X: *storytime_day*  data for Y: *SO_value_Integral_function(so_IF)*   
data for X: *storytime_day*  data for Y: *ZHENG_so_IF*  
data for X: *storytime_day*  data for Y: *LI_Wa_so_IF*   
data for X: *storytime_day*  data for Y: *LI_Wa's_mother_so_IF*   
data for X: *storytime_day*  data for Y: *ZHENG's_father_so_IF*   

##### *Trajectory of the integral function of SO value and places’ appearance by sigmaplot*
![Trajectory of the integral function of SO value and places’ appearance by sigmaplot]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/png/Fig7.png)  
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
##### *Trajectory of the integral function of SO value versus the story-time’s appearance by sigmaplot*
![Trajectory of the integral function of SO value versus the story-time’s appearance by sigmaplot]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/png/Fig8.png)  
create graph--> multiple straight line--> data format--> XY Pair--> select data   
data for X: *storytime_day*  data for Y: *SO_value_Integral_function(so_IF)*   
data for X: *storytime_day*  data for Y: *readtime_phrase*   

graph page--> add axist--> Y  

##### *Bai Xingjian's up and down by sigmaplot*
![Bai Xingjian's up and down by sigmaplot]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/png/Fig21.png)   
create graph--> vertical bar chart--> graph styles--> grouped bar--> data format--> many Y   
data for X: *Age*  data for Y: *Circumstances_of_Bai* 
data for X: *Age*  data for Y: *Circumstances_of_Bai_Chang'an*   
# 2.2 Space-time
import "shikong-vt.shp", "temporal simulation path in sapce.shp" and "link_between_places.shp" into Arcscene
##### *Visualization of the integral function of SO value and places’ appearance by Arcscene*
![Visualization of the integral function of SO value and places’ appearance by Arcscene]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/png/Fig9.png)  
"shikong-vt.shp"--> properties--> Element--> Single symbol
"temporal simulation path in sapce.shp"--> properties--> Symbolic System--> Graded colour--> value--> sheet1_em     

##### *Visualization of path trajectory based on spatial discipline: characters’ appearance versus places’ appearance by Arcscene*
![Visualization of path trajectory based on spatial discipline: characters’ appearance versus places’ appearance by Arcscene]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/png/Fig10.png)  
"shikong-vt.shp"--> properties--> Element--> Single symbol   
"link_between_places.shp"--> properties--> Symbolic Systems--> category--> Unique value--> value--> 人物啊 

##### *Visualization of path trajectory based on spatial discipline: characters’ appearance and the integral function of SO value versus places’ appearance by Arcscene*
![Visualization of path trajectory based on spatial discipline: characters’ appearance and the integral function of SO value versus places’ appearance by Arcscene]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/png/Fig11.png)  
"shikong-vt.shp"--> properties--> Element--> Single symbol
"link_between_places.shp"--> properties--> Symbolic Systems--> Graded colour--> value--> 情感差  

##### *Visualization of path trajectory based on spatial discipline: characters’ appearance versus places’ appearance and the integral function of SO value by Arcscene*
![Visualization of path trajectory based on spatial discipline: characters’ appearance versus places’ appearance and the integral function of SO value by Arcscene]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/png/Fig12.png)  
"shikong-vt.shp"--> properties--> Symbolic System--> Graded colour--> value--> sheet1_em   
"link_between_places.shp"--> properties--> Symbolic Systems--> category--> Unique value--> value--> 阶级值    
# 2.3 Space
## POS map
##### *Statistics of the POS and places (noun-space of the whole document) by Photoshop*
![Statistics of the POS and places (noun-space of the whole document) by Photoshop]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/png/Fig13.png)  
##### *Statistics of the POS and places (adjective-space of the whole document) by Photoshop*
![Statistics of the POS and places (adjective-space of the whole document) by Photoshop]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/png/Fig14.png)  
##### *Visualization of path trajectory based on spatial discipline: characters’ appearance versus places’ appearance by Photoshop*
![Visualization of path trajectory based on spatial discipline: characters’ appearance versus places’ appearance by Photoshop]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/png/Fig15.png)  
create the wordcloud image of POS of each place by [wordart]（ https://wordart.com/） --> imported in Photoshop --> move to relevant place  
## Sentiment map
##### *Inverse distance weighted (IDW) interpolation by ArcGIS of the sentiment classification score and places (a. sentiment classification score of place attribute, b. sentiment classification score/effective read-time of place attribute) by Arcmap*
![Inverse distance weighted (IDW) interpolation by ArcGIS of the sentiment classification score and places (a. sentiment classification score of place attribute, b. sentiment classification score/effective read-time of place attribute) by Arcmap]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/png/Fig16.png) 
Toolbox → geostatistical analyst- interpolation analysis – IDW→ input layer“点数据” → Environment-range-“皇城里坊”
## [Social network](https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/S7%20File.zip)
if two *character* co-occurr within two adjacent phrases, one edge will be added between them.  

##### *Statistics of characters in co-occurrence network, modularity class, and betweenness centrality by Gephi*
![Statistics of characters in co-occurrence network, modularity class, and betweenness centrality by Gephi]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/png/Fig17.png)   

node：26  
edge：38  
Average Degree: 1.462  
Average Weighted Degree: 4.731  
Diameter: 5  
Radius: 1  
Average Path length: 2.265625  
Density: 0.095  
Randomize: On  
Use edge weights: Off  
Resolution: 0.8  
Modularity: 0.351  
Modularity with resolution: 0.218  
Number of Communities: 6  
Network Interpretation: undirectedAverage   
Clustering Coefficient: 0.506  
Total triangles: 6  

## [Spatially embedded network](https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/S8%20File.zip) 
it is based on **path.xlsx**
##### *Network analysis of characters and places in modularity class analysis and weighted degree centrality based on a full-text, spatially embedded, undirected network of characters by Gephi*
![Network analysis of characters and places in modularity class analysis and weighted degree centrality based on a full-text, spatially embedded, undirected network of characters by Gephi]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/png/Fig18.png)   
##### *[Network analysis of characters and places in closeness centrality and betweenness centrality based on a full-text spatially embedded undirected network of characters by Gephi*
![Network analysis of characters and places in closeness centrality and betweenness centrality based on a full-text spatially embedded undirected network of characters by Gephi]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/png/Fig19.png)   
##### *Network analysis of characters and places in authority and hub analysis based on a full-text spatially embedded directed network of characters by Gephi*
![Network analysis of characters and places in authority and hub analysis based on a full-text spatially embedded directed network of characters by Gephi]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/png/Fig20.png)   

node：16  
edge：24  
Average Degree: 3.000  
Average Weighted Degree: 7.750  
Diameter: 6  
Radius: 3  
Average Path length: 2.265625  
Density: 0.200  
Randomize: On  
Use edge weights: Off  
Resolution: 0.8  
Modularity: 0.326  
Modularity with resolution: 0.194  
Number of Communities: 4  
Network Interpretation: undirectedAverage   
Clustering Coefficient: 0.474  
Total triangles: 9  

# Reference
[ArcGIS Desktop. Version 10.2.2]( https://arcgis_desktop.en.downloadastro.com/old_versions/)
[IDW]( http://desktop.arcgis.com/en/arcmap/latest/tools/3d-analyst-toolbox/idw.htm)
[Linear Density](http://desktop.arcgis.com/en/arcmap/10.3/tools/spatial-analyst-toolbox/line-density.htm)
[reference1]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/reference1.zip)
[reference2]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/reference2.zip)
[reference3]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/reference3.zip)
[reference4]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/reference4.zip)
