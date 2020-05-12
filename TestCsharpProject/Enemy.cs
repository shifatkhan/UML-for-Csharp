using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Enemy : Person
{
    private string dialog;

    /** 2 param constructor.
    */
    public void Enemy(string name, string health, string dialog) : base(name, health)
    {
        this.dialog = dialog;
    }

    /** Makes the enemy shout out a certain dialog.
    */
    public void Shout()
    {
        if(dialog != null)
        {
            Debug.Log(dialog);
        }
    }
}
