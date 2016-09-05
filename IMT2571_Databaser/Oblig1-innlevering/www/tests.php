<?php 

/**
*    @author   Jonas Solsvik
*    @uses     BlogModel
* 
*    File     tests.php
*    Created  30.08.16
*       
*    Description: 
*           As of 30.08 test.php contains all tests to perform an
*            automated unit-test of the class BlogModel
*             The most convenient way to do this is to visit localhost:8080/tests.php
*             In future revisions of this file one can imagine having several test-classes.
*             one for each model-class.
*             The script has a try-catch statement wrapped around it.
*             Right now it echoes the $e element. This may not be a good idea, going forward.
*             Especially regarding security.    
*/

require_once 'model/BlogModel.php';


$testID = 1;

try {
    $blogModel = new BlogModel();

    echo '<h1>Tests BlogModel()</h1>';

// ---------- BlogModel - TEST 1 - getPosts() -----------------

// Testing with htmlspecialchars() and nl2br()

    echo '================================';
    echo '<h2> Test 1 - getPosts() </h2>';
    echo '================================';
    echo '</br>Testing with htmlspecialchars() and nl2br()';

    $posts = $blogModel->getPosts();

    foreach ($posts as $post) {
        $tittel = $post['Tittel'];
        $innhold = nl2br(htmlspecialchars(($post['Innhold'])));

        echo "<h2> $tittel </h2>";
        echo "<p> $innhold </p></br>";
    }

// ------------------------------------------------------


// --------- BlogModel - TEST 2 - getPost() --------------

// Running this test without escaping htmlspecialchars()

    echo '================================';
    echo '<h2> Test 2 - getPost() </h2>';
    echo '================================';
    echo '</br>Testing without htmlspecialchars()';

    $post = $blogModel->getPost($testID);

    echo '<h2>' . $post['Tittel'] . '</h2>';
    echo '<p>' . nl2br($post['Innhold']) . '</p></br>';

// --------------------------------------------------------

// -------- BlogModel - TEST3 - createPost() -------------

    echo '================================';
    echo '<h2> Test 3 - createPost() </h2>';
    echo '================================';

    $tittel = 'created by $blogModel->createPost();';
    $innhold = '"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."';
    $forfatternavn = 'Test Testerson';
    $forfatterepost = 'test@testerson.com';

    $testID = $blogModel->createPost($tittel, $innhold, $forfatternavn, $forfatterepost);

    $post = $blogModel->getPost($testID);

    echo '<h2>Post['. $testID. '] ' . $post['Tittel'] . '</h2>';
    echo '<p>' . $post['Innhold'] . '</p></br>';


# ----------------------------------------------------------


// -------- BlogModel - TEST4 - editPost() -------------------

    echo '================================';
    echo '<h2> Test 4 - editPost() </h2>';
    echo '================================';


    $nytittel = 'Post['. $testID. '] edited by $blogModel->editPost();';
    $nyttinnhold = 'There are nine million bicycles in beijing';

    $blogModel->editPost($testID, $nytittel, $nyttinnhold);

    $post = $blogModel->getPost($testID);

    echo '<h2>' . $post['Tittel'] . '</h2>';
    echo '<p>' . $post['Innhold'] . '</p></br>';

// ----------------------------------------------------------

// --------- BlogModel - TEST5 - deletePost() ---------------

    echo '================================';
    echo '<h2> Test 5 - deletePost() </h2>';
    echo '================================';

    $blogModel->deletePost($testID);

    echo '<h2>Post['. $testID.'] deleted...</h2>';

//--------------------------------------------------------------

} catch (Exception $e){
    
    echo $e;
    die();
}
?>