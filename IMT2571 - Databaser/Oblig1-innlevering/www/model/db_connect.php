<?php 

/**
 * @author  Jonas Solsvik
 * @file    db_connect.php
 * @created 25.08.16
 * @description
 *      This script creates a PDO object, which will be responsible
 *      for the connection between the php-preprocessor/server and the
 *      mysql database.
*/


/**
* @return PDO the PDO object connecting to the MySQL database.
* @throws PDOException
*/

function openDB(){

    /* About DSN:
     * From wiki.hashphp.com
     *
     * " A DSN is basically a string of options that tell PDO which driver to use, and the 
     *  connection details.. ""
     * 
     * DSN-prefix: in this case the prefix is mysql, but it can be changed according 
    *               to which database type is in use. 
    */

    $dsn =  'mysql:host=localhost;dbname=oblig_1;charset=utf-8;';
    $username = 'root';
    $password = '';

    $db = new PDO($dsn, $username, $password);

    
    /* ERRMODE_EXCEPTION - Makes the PDO object able to throw a PDO Exception,
     *                     which can be handled.  
    */

    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    return $db;

}
?>