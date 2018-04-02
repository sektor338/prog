using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Falcon : MonoBehaviour
{
    private Rigidbody2D rb;
    public bool isAlive;
    public int Health;
    private Time time;
    // Use this for initialization
    void Start()
    {
        isAlive = true;
        Health = 100;
    }

    // Update is called once per frame
    void Update()
    {
        if (Time.deltaTime == 1000)
        {
            rb.gravityScale = -1;
        }

        if (Health == 0)
        {
            isAlive = false;
        }

        if (isAlive == false)
        {
            Time.timeScale = 0f;
            print("Game Over");
        }

        float translation = Time.deltaTime * 10;
        transform.Translate(0, 0, translation);
    }

    void DamagePlayer(int Damage)
    {
        Health -= Damage;
    }

    void OnCollisionEnter2D(Collision2D target)
    {
        if (target.gameObject.tag == "Asteroid")
        {
            DamagePlayer(10);
        }
    }
}