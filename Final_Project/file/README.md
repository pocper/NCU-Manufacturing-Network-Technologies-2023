## Manufacturing Network Technologies
### Project File
- semester: 111-1
- team: 2
- last modified date: 2023/01/16
- creator
    - Name: Tommy Huang
    - Mail: pocper@gmail.com

### File Directory
Root directory = Project_File_Team_2
```
Project_File_Team_2
├─mini_5axis_Csharp
|    ├─mini_5axis
|    │  └─bin
|    |     └─x86
|    |       └─Release
|    └─mini_5axis.sln
├─mini_5axis_OPCUA.py
├─README.md
├─SyntecRemoteAPI__1.2.1.zip
└─variable_data.xlsx
```

### File Description
|   | Name                       | Description                                             |
| - | -------------------------- | ------------------------------------------------------- |
| d | mini_5axis_Csharp          | dotnet core with using Syntec API to collect mini-5axis's data and upload machine info to OPC UA Server |
| - | mini_5axis_OPCUA.py        | python code to start up OPC UA Server                   |
| - | README.md                  | describe the relationship in the root directory         |
| - | SyntecRemoteAPI__1.2.1.zip | file of Syntec API including manual and sample code     |
| - | variable_data.xlsx         | select a few important data in the manual to be collected by Syntec API |


### Progress
1. cmd > unzip SyntecRemoteAPI__1.2.1.zip
2. cmd > cp ~/SyntecRemoteAPI__1.2.1/SyntecRemoteAPI/DiskC/OpenCNC/Bin/*.dll ~/mini_5axis_Csharp/mini_5axis/bin/x86/Release
3. cmd > pip3 install opcua
4. cmd > python3 ~/mini_5axis_OPCUA.py
5. Visual Studio 2022 or other versions > open ~/mini_5axis_Csharp/mini_5axis.sln > choose Configuration = 'Release', Platform = 'x86' > compile
6. cmd > ~/mini_5axis_Csharp/mini_5axis/bin/x86/Release/mini_5axis.exe
7. Ignition 

### Environment
- Room: H5-203
- Device
  1. GIGABYTE Ultra Compact PC kit
     - System: 
     - System Account
       - account: 
       - password: 
     - Wifi Router
       - SSID: 
       - password: 
     - Network
       1. Private IP: 
       2. Private IP: 
          - Default Gateway: 
          - subnet mask: 
       - 
     - Ignition Account
       - account: 
       - password: 
     - PORT :
       - 4840: OPC UA
       - 8088: Ignition
       - 5568/TCP, 5570/TCP: Mini-5axis
  2. Mini-5axis
     - System: 
     - Network
       1. Private IP: 
          - Default Gateway: 
          - subnet mask: 
     - System Admin Account
       - account: 
       - Password: 

### Flow Chart
- Line
  - Red: Wireless
  - Green: Ethernet
```flow
op1=>operation: Wifi Router
op2=>operation: Compact PC kit
op3=>operation: Mini-5axis

op1(right)->op2(right)->op3

op1@>op2({"stroke":"Red"})
op2@>op3({"stroke":"Green"})
```

### Pseudo Code
- Python
    ```python
    1 opcua = OPCUA()    # Create OPC UA Server Instance
    2 opcua.set_endpoint("opc.tcp://0.0.0.0:4840/Mini-5axis/") # Set OPC UA Endpoint
    3 opcua.add_nodes()  # Add OPC UA Server nodes
    4 opcua.start()      # Start OPC UA Server
    5 while True:
    6     time.sleep(1)  # Running OPC UA Server
    ```
- C#
    ```csharp
    1 OpcClient client = new OpcClient("opc.tcp://127.0.0.1:4840/Mini-5axis"); // Create OPC UA Instance
    2 client.Connect(); // Connect to OPC UA Server
    3 SyntecRemoteCNC syntecRemoteCNC = new SyntecRemoteCNC("192.168.1.200"); // Create API Instance
    4 while (true){
    5   ReadValueFromMachine(syntecRemoteCNC, data); // Read value from Machine
    6   UpdateValue2OPCUA(client, data); // Update value to OPC UA Server
    7   Thread.Sleep(500);
    8 }
    9 syntecRemoteCNC.Close(); // Close connection between local and API 
    10 client.Disconnect(); // Close connection between OPC Server and Client
    ```

### Notice
1. :red_circle: IMPORTANT :exclamation: :red_circle:
Must open OPC UA server(mini_5axis_OPCUA.py) first, then c# dotnet core second.
2. dotnet core must run on the Windows system, due to Syntec API dynamic link library built in the 32-bit operating system, so the Linux system will hit the wall owing to Linux rarely downloading in the 32-bit operating system.
3. Sometimes, CNC machine operation surpasses the limits, and the mini-5axis monitor will pop out a warning message. At this movement, C# code will crash. I'm guessing that I didn't write any try-catch to catch the error.
4. Ignition File is in the system of the GIGABYTE Ultra Compact PC kit.
5. Syntec engineer suggest using VS2008, higer than VS2008 may confront compatibility issues. However, we use VS2022 and didn't encounter problems.


### Future Work
1. Fix C# crash sometimes - adding try-catch when reading data from mini-5axis.