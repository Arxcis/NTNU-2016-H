

<?php  

 /**
  * @author Jonas Solsvik
  * @version 1.0
  * @uses auth.py
  *
  * File  header.php
  * Created 28.08.16
  * 
  * Description
  *       This is a header template-file.
  *        This file is supposed to be included in most other HTML pages, to make 
  *         it easy to keep a consitent styling across multiple webpages.
  *          It is also usefull to put PHP-authentication information in here, so the
  *           information can be easilly access across the domain.
 */

require_once 'auth.php';  ?>

<!DOCTYPE html5>

<html>
<head>

    <title>Blog - Diving into code</title>
    <meta charset="UTF-8"/>
    <link type="text/css" rel="stylesheet" href="../static/style.css"/>

</head>


<body>
    
    <a href="index.php">
        <header class="transparentbg hoverme">    
            <h2> Diving into code</h2>
            <h4> &lt; en blogg om programmering / &gt;</h4>
        </header>
    </a>

