using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Asteroid : MonoBehaviour {

	private Rigidbody2D rb;
    private Time time;
	// Use this for initialization
	void Start () {
        
	}
	
	// Update is called once per frame
	void Update () {
		if (Time.deltaTime == 1000)
        {
            rb.gravityScale = -1;
        }
	}
}
