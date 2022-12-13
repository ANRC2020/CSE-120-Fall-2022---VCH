using UnityEngine;
using System.Collections;
using System.Collections.Generic;
using System;
using System.IO;
using System.Diagnostics;



public class RecPositions : MonoBehaviour {
    public string fileName = "/ObjectPositionData.json";
    private Positions armData = new Positions();
    string saveFile;
    private List<Vector3> positions;
    public float interval = 0.1f;
    public float tSample = 0.0f;
    public float time = 0.0f;

    void Start ()
    {
        positions = new List<Vector3>();
        InvokeRepeating("RecPoint", tSample, interval);
    }

    void RecPoint() 
    {
        time += interval;
        if (transform.parent != null){
            armData.ArmData.Add(new armPositions(transform.position, time));
        }
    }

    void SaveToJson(string fileName)
    {
        saveFile = Application.persistentDataPath + fileName;
        string line = JsonUtility.ToJson(armData, true);
        File.WriteAllText(saveFile, line);    
    }

    void Update()
    {
        
        if (transform.parent != null){
            SaveToJson(fileName);
        }
        
    }

}

[System.Serializable]
public class armPositions
{
    public armPositions(Vector3 pos, float time)
    {
        Position = pos;
        Time = time;
    }
    
    public Vector3 Position;
    public float Time;
}

[System.Serializable]
public class Positions
{
    public List<armPositions> ArmData = new List<armPositions>();

}
