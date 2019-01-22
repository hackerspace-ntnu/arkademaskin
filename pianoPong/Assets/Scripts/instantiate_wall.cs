using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class instantiate_wall : MonoBehaviour {
    IDictionary<KeyCode, GameObject> wallDict = new Dictionary<KeyCode, GameObject>(); // todo: bruk dictionaries med nokkel nedtrykt bokstav i stedet.

    public GameObject white_line;
	// Use this for initialization
	void Start () {
        wallDict.Add(KeyCode.A, Instantiate(white_line, new Vector3(-6.0F, 0, 0), Quaternion.identity));
        wallDict.Add(KeyCode.S, Instantiate(white_line, new Vector3(-4.0F, 0, 0), Quaternion.identity));
        wallDict.Add(KeyCode.D, Instantiate(white_line, new Vector3(-2.0F, 0, 0), Quaternion.identity));
        wallDict.Add(KeyCode.F, Instantiate(white_line, new Vector3(0.0F, 0, 0), Quaternion.identity));
        wallDict.Add(KeyCode.G, Instantiate(white_line, new Vector3(2.0F, 0, 0), Quaternion.identity));
        wallDict.Add(KeyCode.H, Instantiate(white_line, new Vector3(4.0F, 0, 0), Quaternion.identity));
        wallDict.Add(KeyCode.J, Instantiate(white_line, new Vector3(6.0F, 0, 0), Quaternion.identity));
        wallDict.Add(KeyCode.K, Instantiate(white_line, new Vector3(8.0F, 0, 0), Quaternion.identity));
        wallDict.Add(KeyCode.L, Instantiate(white_line, new Vector3(10.0F, 0, 0), Quaternion.identity));
        foreach (KeyValuePair<KeyCode, GameObject> item in wallDict)
        {
            item.Value.SetActive(false);

        }
    }

	// Update is called once per frame
	void Update () {
        foreach (KeyValuePair<KeyCode, GameObject> item in wallDict)
        {
            if (Input.GetKeyDown(item.Key))
            {
                item.Value.SetActive(true);
            }
        }
        foreach (KeyValuePair<KeyCode, GameObject> item in wallDict)
        {
            if (Input.GetKeyUp(item.Key))
            {
                item.Value.SetActive(false);
            }

        }
    }
}

