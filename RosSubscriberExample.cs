using UnityEngine;
using Unity.Robotics.ROSTCPConnector;
using RosColor = RosMessageTypes.UnityRoboticsDemo.UnityColorMsg;
//using RosMessageTypes.UnityRoboticsDemo;
using PosRot = RosMessageTypes.UnityRoboticsDemo.PosRotMsg;

public class RosSubscriberExample : MonoBehaviour
{
    public GameObject cube;
Vector3 targetPosition;
    void Start()
    {
        ROSConnection.GetOrCreateInstance().Subscribe<PosRot>("pos_rot_pub", PosChange);
    }

    void PosChange(PosRot posMessage)
    {
       // cube.GetComponent<Renderer>().material.color = new Color32((byte)colorMessage.pos_x, (byte)colorMessage.pos_y, (byte)colorMessage.pos_z, (byte)colorMessage.rot_w,  (byte)colorMessage.rot_x, (byte)colorMessage.rot_y, (byte)colorMessage.rot_z);
        
            //var c = (float)posMessage.pos_x;
            //Debug.Log(posMessage);
            cube.transform.rotation = new Quaternion((float)posMessage.rot_w, (float)posMessage.rot_x, (float)posMessage.rot_y, (float)posMessage.rot_z);
            cube.transform.localPosition = new Vector3((float)posMessage.pos_x,(float)posMessage.pos_y,(float)posMessage.pos_z);
        
            
    }
}
