<?php
/** 
 *   
 * @author  Jonas Solsvik
 * @version 1.0
 * @created 25.05.16
 * @file    Index.php
 * @description 
 *      This is the server-root index.php.
 *      The purpose of index.php is to be the landing page for the domain.
 *      It handles all traffic to the http://domain.xyz/ - root HTTP path.
 *      This index.php does not contain much, but it runs a view-script which
 *      can be modified to the authors liking.
 */

$index_path = "view/blogView.php";

/* 
 *   About require and require_once:
 *
 *   From php.net
 *   " require is identical to include except upon failure it will also produce a fatal
 *   E_COMPILE_ERROR level error. In other words, it will halt the script whereas include
 *   only emits a warning (E_WARNING) which allows the script to continue. "
 *
 *   Furthermore:
 *   require_once make sure to check if a document has already been loaded, and will 
 *   not load it again if this is true.
 *
*/

require_once $index_path;

?>