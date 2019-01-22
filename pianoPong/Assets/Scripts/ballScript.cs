using System.Collections;
using System.Collections.Generic;
using UnityEngine;
    
public class ballScript : MonoBehaviour{
    public GameManager gameManager;
    public GameObject star;
    public GameObject bomb;
    public Vector2 velocity = new Vector2(1.0f, 1.0f);//, 0f);
    public int upperBounce = 3;
    public int lowerBounce = -3; 

    void Start() {
        transform.position = new Vector3(0.0f, 1.5f, 0.0f);
    }

    bool flag = true;
    // Update is called once per frame
    void Update()
    {
        GetComponent<Rigidbody2D>().MovePosition(GetComponent<Rigidbody2D>().position + velocity * Time.deltaTime);
        if (this.transform.position[1] > upperBounce && flag){ //|| this.transform.position[1]<lowerBounce){
            velocity[1] = -velocity[1];
            flag = false;
        }
        if (this.transform.position[1] < lowerBounce && !flag)
        { //|| this.transform.position[1]<lowerBounce){
            velocity[1] = -velocity[1];
            flag = true;
        }

    }

    private void OnCollisionEnter2D(Collision2D collision) {
        print(collision.collider.gameObject.layer);
        if (collision.collider.gameObject.layer == LayerMask.NameToLayer("wall")) {
            velocity[0] = -velocity[0];
        }
    }

    void OnTriggerEnter2D(Collider2D other) {
        if(other.gameObject.CompareTag("Star")) {
            Destroy(other.gameObject);
            gameManager.UpdateScore(1);

            Instantiate(star, new Vector3(Random.Range(-7.0F, 7.0F), Random.Range(-4.0F, 4.0F), 0), Quaternion.identity);
        }
        if (other.gameObject.CompareTag("Bomb"))
        {
            Destroy(other.gameObject);
            gameManager.UpdateScore(-5);
            Instantiate(bomb, new Vector3(Random.Range(-7.0F, 7.0F), Random.Range(-4.0F, 4.0F), 0), Quaternion.identity);
        }

    }
}
