using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Weapon
{
    string weaponName;
    int damage;

    /** Default no param constructor.
    */
    public void Weapon()
    {
        this.weaponName = "";
        this.damage = 0;
    }

    /** 2 param constructor.
    */
    public void Weapon(string weaponName, string damage)
    {
        this.weaponName = weaponName;
        this.damage = damage;
    }

    public string GetWeaponName()
    {
        return weaponName;
    }

    public void SetWeaponName(string weaponName)
    {
        this.weaponName = weaponName;
    }

    public string GetDamage()
    {
        return damage;
    }

    public void SetDamage(int damage)
    {
        this.damage = damage;
    }
}
