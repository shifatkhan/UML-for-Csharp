using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Person : MonoBehaviour, TempParent
{
    protected string name;
    int health;

    /** Default no param constructor.
    */
    public void Person()
    {
        this.name = "";
        this.health = 0;
    }

    /** 2 param constructor.
    */
    public void Person(string name, string health)
    {
        this.name = name;
        this.health = health;
    }

    public string GetName()
    {
      return name;
    }

    public void SetName(string name)
    {
        this.name = name;
    }

    public string GetHealth()
    {
        return health;
    }

    public void SetHealth(int health)
    {
        this.health = health;
    }
}
