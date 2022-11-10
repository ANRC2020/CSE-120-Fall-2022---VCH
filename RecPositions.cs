using UnityEngine;
using System.Collections;
using System.Collections.Generic;
//using UnityEngine.InputSystem;
using System;
using System.IO;

public class RecPositions : MonoBehaviour {
    public string fileName = "/ObjectPositionData.json";
    private Positions armData = new Positions();
    string saveFile;
    private List<Vector3> positions;
    public float interval = 0.1f;
    public float tSample = 10.0f;

    void Start ()
    {
        positions = new List<Vector3>();

        InvokeRepeating("RecPoint", tSample, interval);
    }

    void RecPoint() 
    {
        armData.positions.Add(new armPositions(transform.position));
    }

    void SaveToJson(string fileName)
    {
        saveFile = Application.persistentDataPath + fileName;
        //armData.positions.Add(new armPositions(transform.position));
        string line = JsonUtility.ToJson(armData, true);
        File.WriteAllText(saveFile, line);
        Debug.Log(saveFile);
       
    }


    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space))
        {
            CancelInvoke("RecPoint");
            SaveToJson(fileName);
        }
    }

}

[System.Serializable]
public class armPositions
{
    public armPositions(Vector3 pos)
    {
        x = pos.x;
        y = pos.y;
        z = pos.z;
    }
    public float x;
    public float y;
    public float z;
}

[System.Serializable]
public class Positions
{
    public List<armPositions> positions = new List<armPositions>();

}