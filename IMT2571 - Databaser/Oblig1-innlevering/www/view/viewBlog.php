
<?php 
/** 
 * @author Jonas Solsvik
 * @version 1.0
 * @uses header.php
 * @uses BlogModel
 * @uses db_connect.php
 * @param $_POST['tittel'] - (optional) - creates a new blog if all $_POST has value.
 * @param $_POST['innhold'] - (optional)
 * 
 * Created: 26.08.16
 * File   : viewBlog.php
 * 
 * Description:
 * 
 * This script basically does 3 things
 *  1. Create a BlogModel-object, which in turn creates a connection with
 *      the database.
 *  2. Send query to the database using BlogModel-object, and get an array of
 *      blog posts in return.
 *  3. Fill inn blog posts in the HTML -code below.
 * 
 * Extra:
 *       This script also handles POST-requests from viewNewpost.php.
 *        The data from the post-requests is used to create a new blog-entry
 *         in the database.
 *
*/

// Require necesarry source-files
require_once '../header.php';          /* header.php - a HTML/PHP header-template.
                                          *              Used for consistent user-interface across
                                          *               multiple pages, and loads auth.php.
                                          */ 
require_once 'model/BlogModel.php';      // Makes the BlogModel-class available


// Since the script talks to the database on 3 potential procedures below, 
//  we throw a big try-catch around here.
try {
    $blogModel = new BlogModel();

    // Create new post if there has been a POST-request to this php-script from viewNewpost.php
    if (!empty($_POST['tittel']) && !empty($_POST['innhold'])) {
        
        $blogModel->createPost($_POST['tittel'], $_POST['innhold'], $DEFAULT_USER, $DEFAULT_EMAIL);
    }
    $posts = $blogModel->getPosts();

} catch(Exception $e) {

    echo '500 SERVER ERROR: Oooooops something went wrong in loading viewBlog.php ....';
}

?>


    <main>
        <a href="view/viewNewpost.php">
        <div id="newpostbutton" class="megabutton transparentbg hoverme">
            <h2>__ny post__</h2>
        </div>
        </a>
        
    <?php
    /*
     * foreach - shows(echoes) all the blogposts, and specifies the HTML-element structure
     *  of which the data is represented in. This element-structure is used further for styling
     *   via static/style.css.
     */
        foreach ($posts as $post) {

            echo '<div class="blogginnlegg transparentbg">';
            echo '<h2>' . $post['Tittel'] . '</h2>';
            echo '<p><i>Author: ' . $post['ForfatterNavn'] . '</i></br>';
            echo '<i>Email: ' . $post['ForfatterEpost'] . '</i></br>';
            echo '<i>Created: ' . $post['PubTime'] . '</i></p>';
            echo '<p>' . nl2br($post['Innhold']) . '</p>';
            echo '</div>';
        }
    ?>

    </main>


</body>
</html>
