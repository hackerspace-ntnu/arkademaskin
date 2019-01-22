using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using MidiJack;

public class GameManager : MonoBehaviour {
	public Text scoreText;
	private int score = 0;
	

	// Use this for initialization
	void Start () {
		UpdateScore(0);
	}
	
	// Update is called once per frame
	void Update () {
        if (MidiMaster.GetKeyDown(277)){
            print("note down");
        }

    }

	public void UpdateScore(int i) {
		score += i;
		scoreText.text = "SCORE: " + score.ToString();
	}
}
