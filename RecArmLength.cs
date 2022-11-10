using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.InputSystem;
using System;
using System.IO;

public class RecArmLength : MonoBehaviour
{
    public InputActionProperty pinchAnimationAction;
    public string fileName = "/PositionData.json";
    private Positions armData = new Positions();
    string saveFile;

    static float prev_trigger_val = 0;
    //private List<Vector3> positions;

    void SaveToJson(string fileName)
    {
        saveFile = Application.persistentDataPath + fileName;
        armData.positions.Add(new armPositions(transform.position));
        string line = JsonUtility.ToJson(armData, true);
        File.WriteAllText(saveFile, line);
        Debug.Log(saveFile);
       
    }

    void Update()
    {
        float triggerValue = pinchAnimationAction.action.ReadValue<float>();
        Debug.Log(triggerValue);
        
        if (prev_trigger_val == 1 && triggerValue < 1)
        {
            SaveToJson(fileName);
        }

        prev_trigger_val = triggerValue;
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
