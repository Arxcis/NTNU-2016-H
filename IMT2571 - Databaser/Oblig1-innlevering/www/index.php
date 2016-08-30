<?php
/** 
 *   
 * @author  Jonas Solsvik
 * @version 1.0
 * @uses viewBlog.php
 *
 * File    Index.php
 * Created 25.05.16
 *
 * Description 
 *      This is the server-root index.php.
 *      The purpose of index.php is to be the landing page for the domain.
 *      It handles all traffic to the http://domain.xyz/ - root HTTP path.
 *      This index.php does not contain much, but it runs a view-script which
 *      can be modified to the authors liking.
 */


$index_path = 'Location: view/viewBlog.php';

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
 *    NOTE: Require_once has been substituted with header(),
 *           as a method of routing to a landing page. After some testing 
 *            it was discovered that using require_once for this purpose, created inconsistent
 *             filepaths, across multiple pages. This could probably have been solved with
 *              structuring the system somewhat differentyl, but an easier solution was chosen
 *               short-term.
 *    
 *     
 *   From php.net: header() is used to send a raw HTTP header.
 *                  In practice the script changes the server location to a chosen address.
 */   

//require_once('view/viewBlog.php');

header('Location:  view/viewBlog.php');

?>