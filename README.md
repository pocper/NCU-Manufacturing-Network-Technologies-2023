# NCU-Manufacturing-Network-Technologies-2023
## 簡介
- **學校** : 國立中央大學
- **開課單位** : 機械工程學系
- **課程名稱** : 製造聯網技術
- **授課教授** : 林錦德 助理教授
- **修課時間** : 2022年09月~2023年01月
- **最終成績** : 87

## 課程內容
1. Week 01 - Industrial Information System and its Future
2. Week 02 - Introduction of OPC UA and Information Model
3. Week 03 - Introduction SCADA
4. Week 04 - Database, SQL & NoSQL
5. Week 05 - Asset Administration Shell and Micro Service
6. Week 06 - Introduction of Industrial Internet Reference Architecture
7. Week 07 - Test #1
8. Week 08 - Cyber-Physical System
9.  Week 09 - Condition Monitoring: Sensor & Acutuator
10. Week 10 - Prognostics Health Management
11. Week 11 - Digital Twins
12. Week 12 - Test #2
13. Week 13 - Weekly Report
14. Week 14 - Weekly Report
15. Week 15 - Weekly Report
16. Week 16 - Final Project Presentation

## 期末專題
說明：本專題針對「利偉木工機械」之 Mini 5-Axis CNC 複合加工機進行遠端監控開發。由於傳統作業環境下，操作員必須親臨現場才能掌握刀具位置、進給速度及加工時間等即時資訊，存在監控受限之痛點。

系統架構：為了實現遠端化與數位化，本專題建立了一套整合流程：首先透過 C# 呼叫 新代 (Syntec) API 進行機台原始數據抓取，隨後將資料橋接至 OPC UA 通訊協定以標準化資料格式，最後透過 Ignition (SCADA/IoT 平台) 進行視覺化呈現，達成跨地域的機台即時動態監控。

結論：本專題成功實現 Mini 5-Axis CNC 的數據採集（包括座標、轉速、通訊狀態等），並透過 IoT 技術完成異質設備整合。系統統一介面不僅涵蓋本組機台，亦整合了雷切機與兩台 3D 列印機資訊，達成全設備聯網化與數據整合之目標。

## 作業介紹
1. Class Work #1 - Python
   > Transform the (x,y) format into the (r, theta) format
   
   $$ x = r\cos(\theta)$$
   $$ y = r\sin(\theta)$$

2. Class Work #2 - Docker & OPC UA
    > Construct an instance of the CncInterfaceType defined in VDW CNC information model standard. In this exercise, we only construct the nodes in the below table
   
   | Browse Name | Value |
   | :--- | :--- |
   | CncTypeName | Milling |
   | VendorName | \<Your name> |
   | VerdorRevision | \<Your student ID> |
   | Version | 1.0.0.0 |

3. Class Work #3 - Ignition SCADA
    > Use Ignition SCADA to develop a dashboard for the classroom. 
   
   Docker Image: https://hub.docker.com/r/linchinte/ncume5204
   Run Container: `docker run -p 8888:8888 -p 4840:4840 linchinte/ncume5204:1.0`
   There are the specifications for this homework:
      1. Display the basic information of the classroom.
      2. Show values of temperature and CO2 concentration.
      3. Show the history in charts of temperature and CO2 concentration.

4. Class Work #4 - SQLiteStudio
    > Subtract the time Start and End where ONo = "1000" from the table(tblFinOrderPos) in the database (FestoMES.db) and display it.

5. Class Work #5 - RestFul API Using Python Flask
    > Suppose today we want to set up the stock material number (PNo) of the Festo factory
   
   1. Check the information of tblBufferPos
   2. Change the PNo of all the information of tblBufferPos to 210, and change the TimeStamp to the current time.
   3. (optional): You can update the contents of the PNo of the specified Pos number, for example, change the PNo of Pos 12 to 211.

6. Class Work #6 - Node-RED
    Docker Image: https://hub.docker.com/r/nodered/node-red
    Run Container #1:`docker run -d -p 8888:8888 -p 4840:4840 --name notebook jupyter/minimal-notebook start.sh jupyter lab --LabApp.token=''`
    Run Container #2:`docker run -d -p 1880:1880 -v c:/nodered:/data --name nodered --link notebook:notebook nodered/node-red`
    Execute command: `docker exec it nodered /bin/bash`
   1. The information published from OPC UA Server is received by Node Red and stored in the SQLite database (CW6.db) for a total of eight nodes at a time.
   2. Display the information in the Node Red dashboard, using three groups: Identification, Monitor and Notification, as shown in the results on the following page

7. Class Work 7 - Jetson Nano
    > Use jetson nano to make the motor rotate

8. Class Work 8 - Pytorch Linear Regression
    > Take P, v, m in data.csv as input data, Width, Depth, Height as output data, and train the model through Pytorch (the smaller the loss, the better).

9. Class Work 9 - Pytorch Classification
    > data.csv containing coordinates (x, y), corresponding to labels (0, 1, 2), please train the model through Pytorch (the smaller the loss the better, the higher the prediction accuracy the better)

10. Class Work 10 - GPU
    > data.csv contains coordinates data (x, y), corresponding to labels (0, 1, 2)

    [YouTube - CW#10 GPU](https://youtu.be/qEU1Euz1pK0)
    1. Pull Notebook images
    `docker pull jupyter/minimal-notebook`
    2. Run up a container using cmd
    `docker run -p 8888:8888 -p 5000:5000 jupyter/minimal-notebook start.sh jupyter lab --LabApp.token=''`
    3. Open Notebook at 127.0.0.1:8888/lab
    4. Copy or Clone my_inputs.csv & my_labels.csv into workspace
    5. you can let the cloud start training the model through flask, and display the loss
    6. You can use the model on the cloud through flask

## 開發環境與需求
1. Python
2. UAExpert
3. Ignition SCADA
4. SQLite Studio
5. Postman
6. Node.JS
7. Node-Red
8. Jetson Nano
