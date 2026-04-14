using System;
using System.Threading;

using Syntec.Remote;
using Opc.UaFx.Client;

namespace Mini_5axis
{
    // Reference File from variable_data.xlsx
    class Machine_data
    {
        public bool _isConnected = false;
        public bool _isUSBExist = false;
        public string _SeriesNo = "";
        public string _MainBoardPlatformName = "";
        public string[] _Gdata;
        public string _MainProg = "";
        public string _CurProg = "";
        public int _CurSeq = 0;
        public string _Mode = "";
        public string _Status = "";
        public string _Alarm = "";
        public string[] _AxisName;
        public short _DecPoint = 0;
        public string[] _Unit;
        public float[] _Machcoordi;
        public float[] _Abscoordi;
        public float[] _Relcoordi;
        public float[] _distance;
        public float _OvFeed = 0;
        public float _OvSpindle = 0;
        public float _ActFeed = 0;
        public int _ActSpindle = 0;
        public int _PowerOnTime = 0;
        public int _AccCuttingTime = 0;
        public int _CuttingCycle = 0;
        public int _WorkTime = 0;
        public int _part_count = 0;
        public int _require_part_count = 0;
        public int _total_part_count = 0;
        public bool _IsAlarm = false;
        public string[] _AlmMsg;
        public DateTime[] _AlmTime;
        public string[] _record;
        public int _recordcount = 0;

        public enum node
        {
            _isConnected = 2,
            _isUSBExist,
            _SeriesNo,
            _MainBoardPlatformName,
            _Gdata,
            _MainProg = 8,
            _CurProg,
            _CurSeq,
            _Mode,
            _Status,
            _Alarm,
            _AxisName = 15,
            _DecPoint,
            _Unit,
            _Machcoordi,
            _Abscoordi,
            _Relcoordi,
            _distance,
            _OvFeed = 23,
            _OvSpindle,
            _ActFeed,
            _ActSpindle,
            _PowerOnTime = 28,
            _AccCuttingTime,
            _CuttingCycle,
            _WorkTime,
            _part_count = 33,
            _require_part_count,
            _total_part_count,
            _IsAlarm = 37,
            _AlmMsg,
            _AlmTime,
            _record = 41,
            _recordcount,
            timestamp
        }
    }

    internal class Program
    {
        const string url_base = "opc.tcp://127.0.0.1:4840/Mini-5axis";
        const string Mini5Axis_IP = "192.168.1.200";

        static void Main(string[] args)
        {
            OpcClient client = new OpcClient(url_base);
            try
            {
                client.Connect();
            }
            catch (Exception ex)
            {
                throw new Exception("OPC UA Server did not start!");
            }

            SyntecRemoteCNC syntecRemoteCNC = new SyntecRemoteCNC(Mini5Axis_IP);
            Machine_data data = new Machine_data();

            while (true)
            {
                ReadValueFromMachine(syntecRemoteCNC, data);
                UpdateValue2OPCUA(client, data);
                string myDateString = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss");
                Console.WriteLine(myDateString);
                Thread.Sleep(500);
            }

            syntecRemoteCNC.Close();
            client.Disconnect();
        }

        private static void ReadValueFromMachine(SyntecRemoteCNC syntecRemoteCNC, Machine_data data)
        {
            string EMG;

            data._isConnected = syntecRemoteCNC.isConnected();
            data._isUSBExist = syntecRemoteCNC.isUSBExist();
            data._SeriesNo = syntecRemoteCNC.SeriesNo;
            data._MainBoardPlatformName = syntecRemoteCNC.MainBoardPlatformName;
            syntecRemoteCNC.READ_gcode(out data._Gdata);
            syntecRemoteCNC.READ_status(out data._MainProg, out data._CurProg, out data._CurSeq,
                out data._Mode, out data._Status, out data._Alarm, out EMG);
            syntecRemoteCNC.READ_position(out data._AxisName, out data._DecPoint,
                out data._Unit, out data._Machcoordi, out data._Abscoordi, out data._Relcoordi, out data._distance);
            syntecRemoteCNC.READ_spindle(out data._OvFeed, out data._OvSpindle, out data._ActFeed, out data._ActSpindle);
            syntecRemoteCNC.READ_time(out data._PowerOnTime, out data._AccCuttingTime, out data._CuttingCycle, out data._WorkTime);
            syntecRemoteCNC.READ_part_count(out data._part_count, out data._require_part_count, out data._total_part_count);
            syntecRemoteCNC.READ_alm_current(out data._IsAlarm, out data._AlmMsg, out data._AlmTime);
            data._recordcount = 0;
            syntecRemoteCNC.READ_nc_OPLog(out data._record, ref data._recordcount);
        }

        private static void UpdateValue2OPCUA(OpcClient client, Machine_data data)
        {
            const string node_info = "ns=2;i=";
            client.WriteNode(node_info + ((int)Machine_data.node._isConnected).ToString(), data._isConnected);
            client.WriteNode(node_info + ((int)Machine_data.node._isUSBExist).ToString(), data._isUSBExist);
            client.WriteNode(node_info + ((int)Machine_data.node._SeriesNo).ToString(), data._SeriesNo);
            client.WriteNode(node_info + ((int)Machine_data.node._MainBoardPlatformName).ToString(), data._MainBoardPlatformName);
            client.WriteNode(node_info + ((int)Machine_data.node._Gdata).ToString(), data._Gdata);
            client.WriteNode(node_info + ((int)Machine_data.node._MainProg).ToString(), data._MainProg);
            client.WriteNode(node_info + ((int)Machine_data.node._CurProg).ToString(), data._CurProg);
            client.WriteNode(node_info + ((int)Machine_data.node._CurSeq).ToString(), data._CurSeq);
            client.WriteNode(node_info + ((int)Machine_data.node._Mode).ToString(), data._Mode);
            client.WriteNode(node_info + ((int)Machine_data.node._Status).ToString(), data._Status);
            client.WriteNode(node_info + ((int)Machine_data.node._Alarm).ToString(), data._Alarm);
            client.WriteNode(node_info + ((int)Machine_data.node._AxisName).ToString(), data._AxisName);
            client.WriteNode(node_info + ((int)Machine_data.node._DecPoint).ToString(), data._DecPoint);
            client.WriteNode(node_info + ((int)Machine_data.node._Unit).ToString(), data._Unit);
            client.WriteNode(node_info + ((int)Machine_data.node._Machcoordi).ToString(), data._Machcoordi);
            client.WriteNode(node_info + ((int)Machine_data.node._Abscoordi).ToString(), data._Abscoordi);
            client.WriteNode(node_info + ((int)Machine_data.node._Relcoordi).ToString(), data._Relcoordi);
            client.WriteNode(node_info + ((int)Machine_data.node._distance).ToString(), data._distance);
            client.WriteNode(node_info + ((int)Machine_data.node._OvFeed).ToString(), data._OvFeed);
            client.WriteNode(node_info + ((int)Machine_data.node._OvSpindle).ToString(), data._OvSpindle);
            client.WriteNode(node_info + ((int)Machine_data.node._ActFeed).ToString(), data._ActFeed);
            client.WriteNode(node_info + ((int)Machine_data.node._ActSpindle).ToString(), data._ActSpindle);
            client.WriteNode(node_info + ((int)Machine_data.node._PowerOnTime).ToString(), data._PowerOnTime);
            client.WriteNode(node_info + ((int)Machine_data.node._AccCuttingTime).ToString(), data._AccCuttingTime);
            client.WriteNode(node_info + ((int)Machine_data.node._CuttingCycle).ToString(), data._CuttingCycle);
            client.WriteNode(node_info + ((int)Machine_data.node._WorkTime).ToString(), data._WorkTime);
            client.WriteNode(node_info + ((int)Machine_data.node._part_count).ToString(), data._part_count);
            client.WriteNode(node_info + ((int)Machine_data.node._require_part_count).ToString(), data._require_part_count);
            client.WriteNode(node_info + ((int)Machine_data.node._total_part_count).ToString(), data._total_part_count);
            client.WriteNode(node_info + ((int)Machine_data.node._IsAlarm).ToString(), data._IsAlarm);
            client.WriteNode(node_info + ((int)Machine_data.node._AlmMsg).ToString(), data._AlmMsg);
            client.WriteNode(node_info + ((int)Machine_data.node._AlmTime).ToString(), data._AlmTime);
            client.WriteNode(node_info + ((int)Machine_data.node._record).ToString(), data._record);
            client.WriteNode(node_info + ((int)Machine_data.node._recordcount).ToString(), data._recordcount);

            int timestamp = (int)DateTime.Now.Subtract(new DateTime(1970, 1, 1)).TotalSeconds;
            client.WriteNode(node_info + ((int)Machine_data.node.timestamp).ToString(), timestamp);
        }
    }
}
