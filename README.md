# The-Tale-of-Li-Wa
People living in the digital age usually has difficulties in reading classical novels, in terms of obscure words, contextual difference and reading habits. This paper proposes a framework of digital models integrating spatial narrative theories to represent the narrative and narrative of experience of a Chinese classic novel,  [*The Tale of Li Wa*]( https://en.m.wikipedia.org/wiki/The_Tale_of_Li_Wa), which has been diversely interpreted by literature and historians in the past approximately 900 years. To help contemporary readers understand this classic narrative and its context in an integrated and in-depth approach, based on its knowledge graph about “narratives, experiences and geographical spaces”, the spatio-temporal information, derived from its text, its author, and readers, is extracted and fused to map the instantaneous spatial pattern perceived by readers in the flow of reading time.The discussion presents one of these possible interpretations on illustrating the growth of  the novel’s male protagonist in the open framework of "Time-Space-time-Space", which unfolds dialogues between computation and literature, diachronic and synchronic, reader and the author.

##### Flows (black arrows) of variables and comparisons (white arrows) among variables in the logical loop of time–space-time–space
![*Flows (black arrows) of variables and comparisons (white arrows) among variables in the logical loop of time–space-time–space.*]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/png/Fig2.png)
# 0. Digitization
1. [Electronically scanned version]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/S1%20File.pdf) of *The Tale of Li Wa* in *Complete Library in Four Sections* 四库全书
2. [Proofreading Text Edition]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/liwazhuang.txt) of *The Tale of Li Wa* based on the version on [中国哲学书电子化计划（CText）]( https://ctext.org/wiki.pl?if=en&chapter=114571&remap=gb)
3. [*Raster map of Tang Chang'an with location information*](https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/S2%20File.zip).  
It can be added in Arcmap/Qgis. It is an archaeological map in 「数字历史黄河·城市聚落资料集」from Remote Sensing Analysis of Historical Landscape and GIS Laboratory, Northwest Institute of Historical Environment and Socio-Economic Development, Shaanxi Normal University 陕西师范大学西北历史环境与经济社会发展研究院历史景观遥感分析与GIS实验室
4. 黄大宏. [A chronicle of Bai Xingjian](https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/31白行简年谱_黄大宏.pdf) 

# 1. Structuring
## 1.1 Text database on word level
[S1 Table.xlsx](https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/S1%20Table.xlsx) (sheet1_name: *term*, sheet2_name: *POS*, sheet3_name: *so*, sheet4_name: *sentiment classification score*)  

we manually create this database including terms (unigram), parts of speech (POS), sentiment orientations (SO) value, and sentiment shifters by Excel. 

### 1) *Term* 
Segment of `Term` Criteria: Broadening, Dictionary, and Semantic Transparency  

Reference dictionary: [国学大师](http://www.guoxuedashi.com/)  
Reference Word Segmentation platform: [语料库在线](http://www.aihanyu.org/cncorpus/CpsWParser.aspx)  

### 2) *Part of Speech*  

Tag  | n  | nt  | nd  | nl  | nh  | nhf  | nhs  | ns  | nn  | ni  | no  | nhh  | v  | vd  | vl  | vu  | a  | f  | m  | q  | d  | r  | p  | c  | u  | e  | o  | i  | w      
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---
 `pos`  | Noun-general  | Noun-time | Noun-direction | Noun-location | Noun-human | noun-last name | noun-first name | Noun-space | Noun-nation | Noun-institution | Noun-offical  | noun-human’s pronoun | Verb | Verb- direction | Verb-linking | Verb-auxiliary | adjective | difference | numeral | quantity  | adverb  | pronoun | preposition | conjunction | auxiliary | exclamation | onaomatopoeia | idiom | punctuation 
 
### 3) *Sentiment oritention(so)*  
The assignment of the SO value is as follows: each positive sentiment expression in the novel such as laugh (欢笑) (v.) and magnificent (瑰奇) (a.) is given an SO value of +1 (172 in total), and each negative sentiment expression such as whimper (呜咽) (v.) and poor (贫窭) (a.) is assigned a SO value of −1 (177 in total).  
We do two rounds of sentiment orientations (SO) value assignment(`LIU_SO value` and `MA_SO value`).  
The percentage of consent of two rounds of SO value assignment is 81.5%.  

##### Test about the sentiment words having context-dependent orientations:  
[word2vec_python_code&raw_data](https://github.com/aayi/The-Tale-of-Li-Wa/tree/master/word2vec_python_code)  
[sentiment_network_Gephi.zip](https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/sentiment_network.zip)  
[result_weighted_outdegree_distribution.xlsx](https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/result_weighted%20outdegree%20distribution.xlsx)  

We assumed that the sentiment words in ancient Chinese follow the same logic in today’s sentiment analysis–– sentiment words have context-dependent orientations, i.e., the total distance among words with the same orientation sentiment expression is closer than that among different.  
Based on the unigrams removing stop words, we complete the training of its [*word2vec*](https://radimrehurek.com/gensim/models/word2vec.html) model with [*gensim*](https://pypi.org/project/gensim/2.1.0/) package, and get the correlation(cosine_similarity, -0.4 ~ 1) between each two words.  

This correlation between word A (Source) and word B (Target) multiplied by the SO value of word B is taking as the weight of the edge, to set up a words’ sentiment network in [Gephi](https://gephi.org/users/quick-start/).  
#tips for create *edge to gephi.csv*

Source  | Target  | Weight        
|:---|:---|:---
 WordA  | WordB  | cosine_similarity*WordB_sentiment  
 
#tips for operation step in [Gephi](https://gephi.org/users/quick-start/):   
File → Improt spreadsheet → *edge to gephi.csv* → charset: GB2312 → Graph Type: directed    
run all analysis of "Avg. Weighted Degree" on the right manue  
Data Laboratory → Nodes → Export Table#  
The weighted output distribution calculated by gephi is divided into three different types of manually collected sentient words (1, - 1,0), which are made into scatter diagram by Excel.  
##### Weighted outdegree distribution of words’ sentiment network (a. SO=1, b. SO=-1, c. SO=0)
![*Weighted outdegree distribution of words’ sentiment network (a. SO=1, b. SO=-1, c. SO=0).*]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/png/Fig23.png)

### 4) *Sentiment classification score*  

```
SO_value_effective = IF(sentiment_shifter_-1=-1,SO value * sentiment_shifter_-1,SO value)   

for_phrase_sentiment_classification_score = IF(POS<>"w",SO_value_effective,"")  
```
`for_phrase_sentiment_classification_score` = SUM(`for_phrase_sentiment_classification_score`)
#tips for operation step: Ctrl+G--> "Null(k)"--> "∑"(which means Automatic summation) #
```
phrase_sentiment_classification_score = IF(POS="w",for_phrase_sentiment_classification_score)
```
## 1.2 Text database on phrase level
[S2 Table.xlsx](https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/S2%20Table.xlsx) (sheet1_name: *phrase*, sheet2_name: *time*, sheet3_name: *character*, sheet4_name: *character & SO*, sheet5_name: *place*, sheet6_name: *place & SO*)  

The phrase-level framework assigns the recalculated value of POS and SO value to a relevant phrase by Excel. These values can be applied to the next time level because the sequence number of phrases is defined as read-time. Specific data mining approaches for the following parameters, i.e. places, story-time, and sentiment classification scores are valuable.

### 1) *Phrase*  
`sentiment_classification_score(SCS)` inherits the value of [`phrase_sentiment_classification_score`]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/README.md#4sentiment-classification-score)  
### 2) *Time*  
`storytime_day`  
Noun-time (nt.) such as the Tianbao period (天宝), 10 years later (十年), more than a month later (月余), and another day (他日), which is 2.7% of the total texts, are used to simulate the whole story-time in an interval of every single day. The entire story timeline we constructed from the texts started from when Student Zheng entered Chang’an in 747A.D. and ended around the happy ending of the novel, that is, the year Zheng is appointed to become an officer is 754 A.D., and Li Wa is conferred the title Lady Qian‘guo (汧国夫人) in 775 A.D. The story-time is defined by the exact time record of the story that occurred during the period of 742 to 746 A.D.(天宝年间), Bai Xingjian wrote the tale in August of 795 A.D. (贞元中……乙亥岁秋八月) and the nt. phrases. 

`readtime_phrase`  
the sequence number of phrases is defined as read-time  
### 3) *Character*  
`character1`， `character2`， `character3`， and `character4` contain one character in each phrase(since one phrase contains at most 4 characters).  

### 4) *Character & SO*  
```
ZHENG_SCS = IF(character1="郑生" or character2="郑生" or character3="郑生" or character4="郑生",sentiment_classification_score(SCS),"")  
```
`ZHENG_so_IF`= SUM(`ZHENG_SCS`)
#tips for operation step: ```K15=SUM(J$15:J15), K18=SUM(J$15:J18), K50=SUM(J$15:J50)```#
### 5) *Place*  
A noun-space (ns.) such as Chang’an City, and specific place names inside the city such as the Buzheng Ward (布政坊) and Xingyuan Garden (杏园) (located in Tongshan Ward [通善坊]), account for 1.1% of the total texts tagged as the level of residential wards and streets directly mentioned (e.g., Buzheng Ward) or most likely to be located (e.g., Tongshan Ward). These uniformly fine-grained places are applied to cover the corresponding story phrases of which plot takes place in these places.
### 6) *Place & SO*  
```
Anyi_SCS = IF(ward_in_chang'an="安邑坊",sentiment_classification_score(SCS),"")  
```
`Anyi_so_IF`= SUM(`Anyi_SCS`)
#tips for operation step: ```I526=SUM(H$526:H526), I535=SUM(H$526:H535), I606=SUM(H$526:H606)```#

## 1.3 Chronicle of Bai Xingjian
[S3 Table.xlsx](https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/S3%20Table.xlsx) (sheet1_name: *circumstance*, sheet2_name: *poems*) is bassed on [A chronicle of Bai Xingjian](https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/31白行简年谱_黄大宏.pdf) collated by 黄大宏  

`Detail`  contians Bai's specific experience every year  
`circumstance_orientation_value` is assigned manually based on the good/bad of *Detail*. Such as "祖母殁于新郑县私第(Bai's grandmother died)"is assigned a value of −1, "行简进士及第...行简同年...应制举(Bai passed the Imperial Examination...Bai passed passed the Palace Examination)" is assigned a value of +2.   
`Circumstances_of_Bai` = SUM(`circumstance_orientation_value`)
#tips for operation step: ```E2=SUM($D$2:D2), E10=SUM($D$2:D10), E52=SUM($D$2:D52)```#  
```
circumstance_orientation_value_chang'an = IF(Place="长安",circumstance_orientation_value,"")  
```
## 1.4 [Spatial syntax of Chang'an]
[S4 File.graph](https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/S4%20File.graph)  
Vector file of street of chang'an is created by [Autocad]( https://www.autodesk.com/products/autocad/overview) and then imported into *Depthmap*([a technology used to analyze the spatial layouts, and human activity patterns in urban areas]( http://otp.spacesyntax.net/overview-2/))  

##### Integration analysis of the road network of Chang’an city by Depthmap
![Integration analysis of the road network of Chang’an city by Depthmap]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/png/Fig4.png)   
#tips for operation step:  
Using Autocad to depict the main road axis map of Chang'an map(Vector file of street of chang'an) → Save as *dxf* file → Open the depthmap software and create a new workspace → Map-import-Choosing Chang'an Road Axis Chart → ap-convert drawing map → tools-axial/convex/pesh-run graph analysis-Radius/list of radii – input n,2,3,5,7-choose include choice（betweenness）/local measures/RA,RRA and total depth/weighted measures-length#

The degree of integration (a space syntax parameter) reflects the ease of access to streets, that is, it may determine which street is more likely to attract Zheng, as an explorer of Chang’an.  

## 1.5 Spatially embedded semantic data
[S3 File.zip](https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/S3%20File.zip)(**path.xlsx**, **place.xlsx**, **shikong-vt.shp**, **link_between_places.shp**) combines Text database with spatial data by [Arcmap](http://desktop.arcgis.com/en/arcmap/10.3/main/map/what-is-arcmap-.htm).  

### 1) path.xlsx
create **path.xlsx** semi-manually by Excel based on [Text database on phrase level](https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/README.md#11-text-database-on-word-level)  
Each time when `ward_in_chang'an` in sheet "place & SO" changes, an `ID` is added in **path.xlsx** with `Origin` to `Destination`  
`sentiment score between places`: value difference of `sum_sentiment_effective_classification_score` between `Origin` and `Destination`

`straturm classification`: The classification of social `stratum` of the `character`
The classification of social stratum in the story from untouchable to nobles is as follows: (1) beggar, servant, and sex worker; (2) businessman, civilian, madam; (3) ward head (里胥), candidate student, successful candidate, county judicial official (贼曹); and (4) Chang’an officials (京尹) and officials from other places. 
### 2) place.xlsx
create **place.xlsx**( sheet1_name: *stratum_statistics*, sheet2_name: *place_statistics*) by Excel based on [Text database on phrase level](https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/README.md#11-text-database-on-word-level)  
*stratum_statistics* inherits the value in **path.xlsx**  
#tips for operation step in *place_statistics*:  

`place`  | `sum_sentiment_effective_classification_score`  | `phrase_count`  | `averge_sentiment_classification_score`  | `effective_sum_sentiment_classification_score`  | `effective_phrase_count`  | `averge_sentiment_effective_classification_score`  | `averge_stratum`  | `STDEV_stratum`  | `COUNT_stratum`      
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---
 ward  | SUM(`place_SCS`)  in sheet" place & SO"  | COUNT(`place_SCS`)  in sheet" place & SO"   |  AVERAGE(`place_SCS`)  in sheet" place & SO"  | IF `place_SCS`<>0,SUM(`place_SCS`),""  in sheet" place & SO" | IF `place_SCS<>0`,COUNT(`place_SCS`),""  in sheet" place & SO" | IF `place_SCS`<>0,AVERAGE(`place_SCS`),""  in sheet" place & SO" | AVERAGE(`place_stratum`)  in sheet" stratum_statistics" | STDEV(`place_stratum`)  in sheet" stratum_statistics" | COUNT(place_stratum)  in sheet" stratum_statistics"   
### 3) [Polygon](http://desktop.arcgis.com/en/arcmap/10.3/analyze/arcpy-classes/polygon.htm)
#tips for operation step:  
create shapefile of **Polygon**( Ward& Palace) based on[*Raster map of Tang Chang'an with location information*](https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/S2%20File.zip)#  
This shapefile is not uploaded to github due to copyright issues
### 4) [Point](http://desktop.arcgis.com/en/arcmap/10.3/analyze/arcpy-classes/point.htm)
#### shikong-vt.shp  
#tips for operation step:  
- create **Point**( centroid of **Polygon**)--> add field `ward_in_chang'an` and fill in  
- [Text database on phrase level](https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/README.md#11-text-database-on-word-level) is joined with **Point** by field `ward_in_chang'an`#  
#### LIWA_data.shp
[LIWA_data.shp](https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/S6%20File.zip)  
#tips for operation step:   
- create **Point**( centroid of **Polygon**)--> add field `ward_in_chang'an` and fill in 
- **place.xlsx** is joined with **Point** by field `NAME`#   
### 5) [Polyline](http://desktop.arcgis.com/en/arcmap/10.3/analyze/arcpy-classes/polyline.htm)
#### temporal simulation path in sapce.shp
[S5 File.zip](https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/S5%20File.zip)  
#tips for operation step:  
Arcmap--> Toolbox--> XY to Line--> import **shikong-vt.shp**#
#### [link_between_places.shp](https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/S5%20File.zip)
-  create **polyline**
The rules of the simulation are from the characteristics of the streets: first, prefer the shortest path, and second, prefer the street sections with the highest degree of spatial syntax [integration](https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/S4%20File.graph). 
- **path.xlsx** is joined with **polyline** by field `ID` 

# 2. Representation
## 2.1 Time 
##### Trajectory of the integral function of SO value by sigmaplot
![Trajectory of the integral function of SO value by sigmaplot]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/png/Fig5.png)  
#tips for operation step:  
create graph--> simple straight line--> data format--> XY Pair--> select data  
data for X: `storytime_day`  data for Y: `SO_value_Integral_function(so_IF)`#  

##### Trajectory of the integral function of SO value and characters’ appearance by sigmaplot
![Trajectory of the integral function of SO value and characters’ appearance by sigmaplot]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/png/Fig6.png)  
#tips for operation step:  
create graph--> multiple straight line--> data format--> XY Pair--> select data   
data for X: `storytime_day`  data for Y: `SO_value_Integral_function(so_IF)`   
data for X: `storytime_day`  data for Y: `ZHENG_so_IF`  
data for X: `storytime_day`  data for Y: `LI_Wa_so_IF`   
data for X: `storytime_day`  data for Y: `LI_Wa's_mother_so_IF`   
data for X: `storytime_day`  data for Y: `ZHENG's_father_so_IF`#   

##### Trajectory of the integral function of SO value and places’ appearance by sigmaplot
![Trajectory of the integral function of SO value and places’ appearance by sigmaplot]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/png/Fig7.png)  
#tips for operation step:  
create graph--> simple straight line--> data format--> XY Pair--> select data   
data for X: `storytime_day`  data for Y: `SO_value_Integral_function(so_IF)`  

add new plot--> graph types--> vertical bar chart--> graph styles--> grouped bars--> data formats--> many Y   
data for Y: `Anyi_so_IF`  
data for Y: `Buzheng_so_IF`  
data for Y: `Chongren_so_IF`  
data for Y: `EastMarket_IF`  
data for Y: `Pingkang_IF`  
data for Y: `DepartmentOfStateAffairs_IF`  
data for Y: `TianmenStreet_so_IF`  
data for Y: `Tongshan_so_IF`  
data for Y: `Tongyi_so_IF`  
data for Y: `WestMarket_so_IF`  
data for Y: `XingqingPalace_IF`  
data for Y: `Xuanyang_so_IF`  

graph page--> add axist--> Y#  
##### Trajectory of the integral function of SO value versus the story-time’s appearance by sigmaplot
![Trajectory of the integral function of SO value versus the story-time’s appearance by sigmaplot]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/png/Fig8.png)  
#tips for operation step:  
create graph--> multiple straight line--> data format--> XY Pair--> select data   
data for X: `storytime_day`  data for Y: `SO_value_Integral_function(so_IF)`   
data for X: `storytime_day`  data for Y: `readtime_phrase`   

graph page--> add axist--> Y#  

##### Bai Xingjian's up and down by sigmaplot
![Bai Xingjian's up and down by sigmaplot]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/png/Fig21.png)   
#tips for operation step:  
create graph--> vertical bar chart--> graph styles--> grouped bar--> data format--> many Y   
data for X: `Age`  data for Y: `Circumstances_of_Bai` 
data for X: `Age`  data for Y: `Circumstances_of_Bai_Chang'an`#   
# 2.2 Space-time
import **shikong-vt.shp**, **temporal simulation path in sapce.shp** and **link_between_places.shp** into [Arcscene](http://desktop.arcgis.com/en/arcmap/10.3/guide-books/extensions/3d-analyst/3d-analyst-and-arcscene.htm)
##### Visualization of the integral function of SO value and places’ appearance by Arcscene
![Visualization of the integral function of SO value and places’ appearance by Arcscene]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/png/Fig9.png)  
#tips for operation step:  
"shikong-vt.shp"--> properties--> Element--> Single symbol
"temporal simulation path in sapce.shp"--> properties--> Symbolic System--> Graded colour--> value--> `sheet1_em`#     

##### Visualization of path trajectory based on spatial discipline: characters’ appearance versus places’ appearance by Arcscene
![Visualization of path trajectory based on spatial discipline: characters’ appearance versus places’ appearance by Arcscene]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/png/Fig10.png)  
#tips for operation step:  
"shikong-vt.shp"--> properties--> Element--> Single symbol   
"link_between_places.shp"--> properties--> Symbolic Systems--> category--> Unique value--> value--> `人物啊`# 

##### Visualization of path trajectory based on spatial discipline: characters’ appearance and the integral function of SO value versus places’ appearance by Arcscene
![Visualization of path trajectory based on spatial discipline: characters’ appearance and the integral function of SO value versus places’ appearance by Arcscene]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/png/Fig11.png)  
#tips for operation step:  
"shikong-vt.shp"--> properties--> Element--> Single symbol
"link_between_places.shp"--> properties--> Symbolic Systems--> Graded colour--> value--> `情感差`#  

##### Visualization of path trajectory based on spatial discipline: characters’ appearance versus places’ appearance and the integral function of SO value by Arcscene
![Visualization of path trajectory based on spatial discipline: characters’ appearance versus places’ appearance and the integral function of SO value by Arcscene]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/png/Fig12.png)  
#tips for operation step:  
"shikong-vt.shp"--> properties--> Symbolic System--> Graded colour--> value--> sheet1_em   
"link_between_places.shp"--> properties--> Symbolic Systems--> category--> Unique value--> value--> `阶级值`#    
# 2.3 Space
## POS map
##### Statistics of the POS and places (noun-space of the whole document) by Photoshop
![Statistics of the POS and places (noun-space of the whole document) by Photoshop]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/png/Fig13.png)  
##### Statistics of the POS and places (adjective-space of the whole document) by Photoshop
![Statistics of the POS and places (adjective-space of the whole document) by Photoshop]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/png/Fig14.png)  
##### Visualization of path trajectory based on spatial discipline: characters’ appearance versus places’ appearance by Photoshop
![Visualization of path trajectory based on spatial discipline: characters’ appearance versus places’ appearance by Photoshop]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/png/Fig15.png)  
#tips for operation step:  
create the wordcloud image of POS of each place by [wordart]（ https://wordart.com/） --> imported in [Photoshop](https://www.adobe.com/products/photoshop.html?promoid=1NZGDDSP&mv=other&origref=https%3A%2F%2Fwww.photoshop.com%2F) --> move to relevant place --> export into png#    
## Sentiment map
##### Inverse distance weighted (IDW) interpolation by ArcGIS of the sentiment classification score and places (a. sentiment classification score of place attribute, b. sentiment classification score/effective read-time of place attribute) by Arcmap
![Inverse distance weighted (IDW) interpolation by ArcGIS of the sentiment classification score and places (a. sentiment classification score of place attribute, b. sentiment classification score/effective read-time of place attribute) by Arcmap]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/png/Fig16.png) 
#tips for operation step:  
Toolbox → geostatistical analyst- interpolation analysis – [IDW](http://desktop.arcgis.com/en/arcmap/latest/tools/3d-analyst-toolbox/idw.htm)→ input layer“点数据” → Environment-range-“皇城里坊”#
## [Social network]
[S7 File.zip](https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/S7%20File.zip)(edge.csv, node.csv)  
if two *character* co-occurr within two adjacent phrases, one edge will be added between them.  

##### Statistics of characters in co-occurrence network, Girvan-Newman clustering, and betweenness centrality by Gephi
![Statistics of characters in co-occurrence network, Girvan-Newman clustering, and betweenness centrality by Gephi]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/png/Fig17-1.png)   
##### Statistics of characters in co-occurrence network, modularity class, and betweenness centrality by Gephi
![Statistics of characters in co-occurrence network, modularity class, and betweenness centralityy by Gephi]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/png/Fig17.png)   
#tips for operation step in [Gephi](https://gephi.org/users/quick-start/):  
File → Improt spreadsheet → *edge.csv* → charset: GB2312 → Graph Type: indirected    
Tools → pluginss → Availible Plugins → Install  
run all analysis of "Statistics" on the right manue  
appearence → nodes → color → Partition → Modularity class → run  
appearence → nodes → color → Partition → Cluster-ID → run  
appearence → nodes → size → Ranking → Betweenness centrality → run#  

Network parameters:  
node：26  
edge：38  
Average Degree: 1.462  
Average Weighted Degree: 4.731  
Diameter: 5  
Radius: 1  
Average Path length: 2.265625  
Density: 0.095  
Randomize: On (Modularity)  
Use edge weights: Off (Modularity)  
Resolution: 0.8 (Modularity)  
Modularity: 0.351 (Modularity)  
Modularity with resolution: 0.218 (Modularity)  
Number of Communities: 6 (Modularity)  
Number of communities:4 (*Girvan-Newman* Clustering)  
Maximum found modularity:0.39129266 (*Girvan-Newman* Clustering)  
Network Interpretation: undirectedAverage  
Clustering Coefficient: 0.506  
Total triangles: 6  

## Spatially embedded network
[S8 File.zip](https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/S8%20File.zip)(direct-node.csv, edge.csv, indirect-node.csv) is based on **path.xlsx**
##### Network analysis of characters and places in modularity class analysis (use edge weights: On) and weighted degree centrality based on a full-text, spatially embedded, undirected network of characters by Gephi
![Network analysis of characters and places in modularity class analysis and weighted degree centrality based on a full-text, spatially embedded, undirected network of characters by Gephi]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/png/Fig18.png)   
##### . Network analysis of characters and places in Girvan-Newman clustering analysis and weighted degree centrality based on a full-text, spatially embedded, undirected network of characters by Gephi
![Network analysis of characters and places in Girvan-Newman clustering analysis and weighted degree centrality based on a full-text, spatially embedded, undirected network of characters by Gephi](https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/png/Fig24.png)   
#tips for operation step in [Gephi](https://gephi.org/users/quick-start/):  
File → Improt spreadsheet → *edge.csv* → charset: GB2312 → Graph Type: indirected    
Tools → pluginss → Availible Plugins → Install  
run all analysis of "Statistics" on the right manue  
appearence → nodes → color → Partition → Cluster-ID → run  
appearence → nodes → color → Partition → Modularity class → run  
appearence → nodes → size → Ranking → Weighed Degree → run#  
##### Network analysis of characters and places in closeness centrality and betweenness centrality based on a full-text spatially embedded undirected network of characters by Gephi
![Network analysis of characters and places in closeness centrality and betweenness centrality based on a full-text spatially embedded undirected network of characters by Gephi]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/png/Fig19.png)   
#tips for operation step in [Gephi](https://gephi.org/users/quick-start/):  
File → Improt spreadsheet → *edge.csv* → charset: GB2312 → Graph Type: indirected    
run all analysis of "Statistics" on the right manue  
appearence → nodes → color → Ranking → Closeness centrality → run  
appearence → nodes → size → Ranking → Betweenness centrality → run#  
##### Network analysis of characters and places in authority and hub analysis based on a full-text spatially embedded directed network of characters by Gephi
![Network analysis of characters and places in authority and hub analysis based on a full-text spatially embedded directed network of characters by Gephi]( https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/png/Fig20.png)   
#tips for operation step in [Gephi](https://gephi.org/users/quick-start/):  
File → Improt spreadsheet → *edge.csv* → charset: GB2312 → Graph Type: directed    
run all analysis of "Statistics" on the right manue  
appearence → nodes → color → Ranking → Authority → run  
appearence → nodes → size → Ranking → Hub → run#  

Network parameters:  
node：16  
edge：24  
Average Degree: 3.000  
Average Weighted Degree: 7.750  
Diameter: 6  
Radius: 3  
Average Path length: 2.265625  
Density: 0.200  
Randomize: On (Modularity)    
Use edge weights: On (Modularity)  
Resolution: 0.8 (Modularity)  
Modularity: 0.326 (Modularity)  
Modularity with resolution: 0.194 (Modularity)  
Number of Communities: 4 (Modularity)
Number of communities:4 (*Girvan-Newman* Clustering)  
Maximum found modularity:0.3949653 (*Girvan-Newman* Clustering)  
Network Interpretation: undirectedAverage   
Clustering Coefficient: 0.474  
Total triangles: 9  
# Authors
MA Zhaoyi <ayi987654321@163.com>  
LIU Shuaishuai <liushuai_1994@sina.com>  
Dr. HE Jie <janushe@tju.edu.cn>  
XIAO Tianyi <137365121@qq.com>  
# Acknowledgments
The authors gratefully acknowledge the Tang Chang’an GIS basemap provided by Prof. Pan Wei from Yunan University and his team from the GIS Lab at Northwest Institute of Historical Environment and Socio-Economic Development of Shaanxi Normal University. The first version of the historical GIS data of Tang Chang’an in this research are from Prof. Timothy Baker of National Dong Hwa University and Dr. Liao Hsiung-Ming of Acadmia Sinica.
# Reference
[1]Sarbin TR. The Narrative as a Root Metaphor for Psychology. In: Sarbin TR, editors. Narrative psychology: The storied nature of human conduct. Westport: Praeger; 1986. pp. 3-21. Available from:  https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/reference/01Theodore%20R.%20Sarbin%20-%20Narrative%20Psychology_%20The%20Storied%20Nature%20of%20Human%20Conduct%20%20%20(1986%2C%20Praeger%20Publishers).pdf  
[2]杨义. [Cultural Interpretation of Chinese Narrative Literature] 中国叙事学的文化阐释. Journal of Guangdong Polytechnic Normal University广东技术师范学院学报. 2003 Jun; 30(03): 27-35. Chinese.Available from:  https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/reference/02%E4%B8%AD%E5%9B%BD%E5%8F%99%E4%BA%8B%E5%AD%A6%E7%9A%84%E6%96%87%E5%8C%96%E9%98%90%E9%87%8A_%E6%9D%A8%E4%B9%89.pdf  
[3]王祥. [Tang Tales: a landmark of Tang Dynasty] 唐传奇——一代之奇. In:郭杰, 秋芙, 王祥, editors. History of Chinese Literature: Volumn on Sui中国文学史话:隋唐五代卷. Changchun: Jilin People’s Publishing House; 1998. pp. 583-586. Chinese. Available from:  https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/reference/03%E4%B8%AD%E5%9C%8B%E6%96%87%E5%AD%B8%E5%8F%B2%E8%A9%B1%EF%BC%88%E9%9A%8B%E5%94%90%E4%BA%94%E4%BB%A3%E5%8D%B7%EF%BC%89.pdf  
[4]吴海燕. [Review of the Biography of Li Wa Research in the Past Ten Years] 近十年《李娃传》研究述评. Journal of Shenyang Institute of Engineering (Social Sciences) 沈阳工程学院学报(社会科学版). 2017 Jan 15; 13(01): 12-18. Chinese. Available from:  https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/reference/04%E8%BF%91%E5%8D%81%E5%B9%B4_%E6%9D%8E%E5%A8%83%E4%BC%A0_%E7%A0%94%E7%A9%B6%E8%BF%B0%E8%AF%84_%E5%90%B4%E6%B5%B7%E7%87%95.pdf  
[5]龙迪勇. [On the New Field of Narratology: space narrotology] 空间叙事学：叙事学研究的新领域. Journal of Tianjin Normal University (Social Science) 天津师范大学学报(社会科学版). 2008 Nov 20;(06): 54-60. Chinese. Available from:  https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/reference/05%E7%A9%BA%E9%97%B4%E5%8F%99%E4%BA%8B%E5%AD%A6_%E5%8F%99%E4%BA%8B%E5%AD%A6%E7%A0%94%E7%A9%B6%E7%9A%84%E6%96%B0%E9%A2%86%E5%9F%9F_%E9%BE%99%E8%BF%AA%E5%8B%87.pdf  
[6]程锡麟.[Spatial Turn in Narrative Theories-A Summary of Spatial Theories in Narrative] 叙事理论的空间转向——叙事空间理论概述. Jiangxi Social Sciences 江西社会科学. 2007 Nov; 25 (11): 25-35. Chinese. Available from:  https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/reference/06%E5%8F%99%E4%BA%8B%E7%90%86%E8%AE%BA%E7%9A%84%E7%A9%BA%E9%97%B4%E8%BD%AC%E5%90%91_%E5%8F%99%E4%BA%8B%E7%A9%BA%E9%97%B4%E7%90%86%E8%AE%BA%E6%A6%82%E8%BF%B0_%E7%A8%8B%E9%94%A1%E9%BA%9F.pdf  
[7]朱明秋. [Shuli Criticism on the Plots of “The Story of Li Wa”] 《李娃传》情节数理批评. Journal of Guilin Normal College桂林师范高等专科学校学报. 2013 Jul 15; 27(03): 82-84+89. Chinese. Available from:  https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/reference/07%E3%80%8A%E6%9D%8E%E5%A8%83%E4%BC%A0%E3%80%8B%E6%83%85%E8%8A%82%E6%95%B0%E7%90%86%E6%89%B9%E8%AF%84.pdf  
[8]程国赋. [Research on the Evolution of The Tale of Li Wa] 《李娃传》嬗变研究. Journal of Nanjing University (Philosophy, Humanities and Social Sciences) 南京大学学报(哲学社会科学版). 1994 Jul 25; (03): 111-117. Chinese. Available from:  https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/reference/08_%E6%9D%8E%E5%A8%83%E4%BC%A0_%E5%AC%97%E5%8F%98%E7%A0%94%E7%A9%B6_%E7%A8%8B%E5%9B%BD%E8%B5%8B.pdf  
[9]妹尾达彦. [Chang’an and Tales in Late Tang Dynasty: Focusing on the Analysis of The Tale of Li Wa] 唐代后期的长安与传奇小说——以《李娃传》的分析为中心. In: 刘俊文, editors. 日本中青年学者论中国史•六朝隋唐卷. Shanghai: Shanghai Ancient Books Publishing House; 1995. pp. 509-553. Chinese. Available from:  https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/reference/09%E5%A6%B9%E5%B0%BE%E8%BE%BE%E5%BD%A6-%E5%94%90%E4%BB%A3%E5%90%8E%E6%9C%9F%E7%9A%84%E9%95%BF%E5%AE%89%E4%B8%8E%E4%BC%A0%E5%A5%87%E5%B0%8F%E8%AF%B4%E2%80%94%E2%80%94%E4%BB%A5%E3%80%8A%E6%9D%8E%E5%A8%83%E4%BC%A0%E3%80%8B%E7%9A%84%E5%88%86%E6%9E%90%E4%B8%BA%E4%B8%AD%E5%BF%83.pdf  
[10] Bakhtin MM. Forms of Time and of the Chronotope in the Novel: Notes toward a Historical Poetics. In: Richardson B, editors. Narrative dynamics: Essays on time, plot, closure, and frames. Columbus: The Ohio University; 2002. pp. 15-24. Available from:  https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/reference/10Forms%20of%20Time%20and%20of%20the%20Chronotope%20in%20the%20Novel.pdf  
[11] Zoran G. Towards a Theory of Space in Narrative. Poetics Today. 1984; 5(2): 309-335. Available from:  https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/reference/11Towards%20a%20Theory%20of%20Space%20in%20Narrative-Zoran.pdf  
[12] Mitchell WJT. Spatial Form in Literature: Toward a General Theory. Critical Inquiry. 1980; 6(3): 539-567. Available from:  https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/reference/12Spatial%20Form%20in%20Literature_Toward%20a%20General%20Theory.pdf   
[13] Moretti, F. Conjectures on world literature. New Left Review. 2000; 1(4): 54-68. Available from:  https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/reference/13moretti-conjectures-nlr_1.pdf  
[14] David JB. Making the Invisible Visible: Place, Spatial Stories and Deep Maps. In: David C, Donaldson C, Murrieta-Flores P, editors. Literary Mapping in the Digital Age. New York: Routledge; 2016. pp. 207-220. Available from:  https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/reference/14Literary-Mapping-in-the-Digital-Age.pdf  
[15] 王晓玉, 李斌. [Automatic Word Segmention of Middle Ancient Chinese Texts with CRFs] 基于CRFs和词典信息的中古汉语自动分词. Data Analysis and Knowledge Discovery数据分析与知识发现. 2017 May 25; 1(05): 62-70. Chinese. Available from:  https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/reference/15%E5%9F%BA%E4%BA%8ECRFs%E5%92%8C%E8%AF%8D%E5%85%B8%E4%BF%A1%E6%81%AF%E7%9A%84%E4%B8%AD%E5%8F%A4%E6%B1%89%E8%AF%AD%E8%87%AA%E5%8A%A8%E5%88%86%E8%AF%8D_%E7%8E%8B%E6%99%93%E7%8E%89.pdf  
[16] 靳光瑾, 肖航, 富丽. [Standard of POS Tag of Contemporary Chinese for CIP (revise)] 信息处理用现代汉语词类标记规范（修订). In: 中国应用语言学会, 教育部语言文字应用研究所, editors. 第四届全国语言文字应用学术研讨会论文集; 2005 Dec 15-18; Chengdu: Sichan University; 2007. pp. 600-608. Chinese. Available from:  https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/reference/17%E4%BF%A1%E6%81%AF%E5%A4%84%E7%90%86%E7%94%A8%E7%8E%B0%E4%BB%A3%E6%B1%89%E8%AF%AD%E8%AF%8D%E7%B1%BB%E6%A0%87%E8%AE%B0%E8%A7%84%E8%8C%83_%E4%BF%AE%E8%AE%A2_%E9%9D%B3%E5%85%89%E7%91%BE.pdf  
[17] Liu B. Sentiment Analysis: Mining Opinions, Sentiments, and Emotions. New York: Cambridge University; 2015. Available from:  https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/reference/16Sentiment-Analysis-Mining-Opinions-Sentiments-and-Emotions.pdf  
[18] 张永禄. [Dictionary of Tang Chang’an] 唐代长安词典. Xi’an: Shaanxi People’s Publishing House; 1990. Chinese. Available from:  https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/reference/18%E5%94%90%E4%BB%A3%E9%95%BF%E5%AE%89%E8%AF%8D%E5%85%B8.zip  
[19]Kiang HC. Visualizing Everyday Life in the City: A Categorization System for Residential Wards in Tang Chang’an. Journal of the Society of Architectural Historians. 2014 Mar; 73(1): 91-117. Available from:  https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/reference/19Visualizing%20Everyday%20Life%20in%20the%20City%20A%20Categorization%20System%20for%20Residential%20Wards%20in.pdf  
[20] Hillier B, Hanson, J. The Social Logic of Space. Cambridge: Cambridge University; 1984. Available from:  https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/reference/20%5BBill_Hillier%2C_Julienne_Hanson%5D_The_Social_Logic_o(z-lib.org).pdf  
[21] Reagan AJ, Mitchell L, Kiley D, Danforth CM, Dodds PS. The emotional arcs of stories are dominated by six basic shapes. EPJ Data Science. 2016 Nov 4; 5(1): 31. Available from: https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/reference/21The%20emotional%20arcs%20of%20stories%20are%20dominated%20by%20six%20basic%20shapes.pdf  
[22] Environmental Systems Research Institute. ArcGIS Desktop. Version 10.2.2 [software]. 2014 Feb 27 [cited 2019 Jun 8]. Available from: https://arcgis_desktop.en.downloadastro.com/old_versions/.  
[23] Bastian M, Heymann S, Jacomy M. Gephi: an open source software for exploring and manipulating networks. In: Adar E, Hurst M, Finin T, Glance N, Nicolov N, Tseng B, editors. Proceedings of the Third International Conference on Weblogs and Social Media; 2009 May 17-20; San Jose, California. Menlo Park: AAAI; 2009. pp. 361-362. Available from: https://aaai.org/ocs/index.php/ICWSM/09/paper/view/154/1009.
[24] Archer J, Jockers M. The Bestseller Code: Anatomy of the Blockbuster Novel. New York: St. Martin’s; 2016. Available from:  https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/reference/24%5BJodie_Archer%2C_Matthew_L._Jockers%5D_The_Bestseller_(b-ok.org).epub  
[25] Environmental Systems Research Institute. IDW [Internet]. Redlands: Environmental Systems Research Institute, Inc.; c2016 [cited 2019 June 12]. ArcGIS for Desktop; [about 8 screens]. Available from: http://desktop.arcgis.com/en/arcmap/latest/tools/3d-analyst-toolbox/idw.htm.  
[26] Blondel VD, Guillaume JL, Lambiotte R, Lefebvre E. Fast unfolding of communities in large networks. Journal of Statistical Mechanics: Theory and Experiment. 2008 Oct 9; 2008 (10): 1-12. Available from: https://pdfs.semanticscholar.org/b434/c0199bbf38163abd5f995e76aa1619d39db9.pdf.  
[27] Environmental Systems Research Institute. Linear Density [Internet]. Redlands: Environmental Systems Research Institute, Inc.; c2016 [cited 2019 June 12]. ArcGIS for Desktop; [about 8 screens]. Available from:  http://desktop.arcgis.com/en/arcmap/10.3/tools/spatial-analyst-toolbox/line-density.htm   
[28] Brandes U. A Faster Algorithm for Betweenness Centrality. Journal of Mathematical Sociology. 2010 Aug 26; 25(2): 163-177. Available from: https://pdfs.semanticscholar.org/ca67/490fe3be743d825438a20ee2b4652cc1565c.pdf.  
[29] Kleinberg JM. Authoritative Sources in a Hyperlinked Environment. Journal of the ACM. 1999 Sep; 46(5): 604-632. Available from: https://www.cs.cornell.edu/home/kleinber/auth.pdf.  
[30] Moretti F. Atlas of the European Novel: 1800-1900.. London and New York: Verso; 1999. Available from:  https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/reference/30Atlas-of-the-European-Novel-1800-1900.pdf  
[31] 黄大宏. [A chronicle of Bai Xingjian] 白行简年谱. Wen Xian 文献. 2002 Jul 13; (03): 65-78. Chinese. Available from:  https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/reference/31%E7%99%BD%E8%A1%8C%E7%AE%80%E5%B9%B4%E8%B0%B1_%E9%BB%84%E5%A4%A7%E5%AE%8F.pdf  
[32] Girvan M, Newman M E J. Community structure in social and biological networks. Proceedings of the national academy of sciences. 2002 Jun; 99(12): 7821-7826. Available from:  Available from:  https://github.com/aayi/The-Tale-of-Li-Wa/blob/master/reference/31%E7%99%BD%E8%A1%8C%E7%AE%80%E5%B9%B4%E8%B0%B1_%E9%BB%84%E5%A4%A7%E5%AE%8F.pdf    
