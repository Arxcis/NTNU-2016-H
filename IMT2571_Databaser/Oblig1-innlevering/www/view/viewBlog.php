
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
require_once '../model/BlogModel.php';      // Makes the BlogModel-class available


// Since the script talks to the database on 3 potential procedures below, 
//  we throw a big try-catch around here.
try {
    $blogModel = new BlogModel();

    // Create new post if there has been a POST-request to this php-script from viewNewpost.php
    if (!empty($_POST['tittel']) && !empty($_POST['innhold'])) {
        $blogModel->createPost($_POST['tittel'], $_POST['innhold'], $DEFAULT_USER, $DEFAULT_EMAIL);

    } else if($_POST['tittel'] === '') {
        echo 'Your post had empty fields! Nothing was posted.';
    }

    $posts = $blogModel->getPosts();

} catch(Exception $e) {

    echo 'Oooooops! Something went wrong when loading viewBlog.php ....';

    $error_line = ((string)$e) . '/n';  // error_log() documentation -> 
    error_log($error_line, 0);          // http://php.net/manual/en/function.error-log.php
                                        // Prints the errormessage to the server/php 
                                        // default error_log if -> error_log(string,0).
}

?>

    <main>
        <a id="nypostlinker" href="viewNewpost.php">
        <div id="newpostbutton" class="megabutton transparentbg hoverme">
            <h2>__ny post__</h2>
        </div>
        </a>
        
    <?php
    /*
     * foreach - shows(echoes) all the blogposts, and specifies the HTML-element structure
     *  of which the data is represented in. This element-structure is used further for styling
     *   via static/style.css.
     *
     *  htmlspecialchars - is used to escape html-code(and also potentially javascript code i think)
     *                      that the user may have entered to a blog-code.
     *                       This is a security measure. If the user is allowed to type html directly 
     *                       into a post, they can place malicious javascript code, or potentially change
     *                       the look of the page with CSS and html elements.
     *                       The downside of this, is that the user writing the blog-post has less
     *                       flexibility when writing the post, in how it will look. 
     *                       Formatting features, have to be provided in some other way.
     *                     One could imagine that trusted users could be able to write posts,
     *                     without escaping characters.
     * 
     *          nl2br     - this converts all \n - characters to </br> so line-endings show properly
     * 
     *                      suggestion: It might be that if we use double quotes "", the \n  from 
     *                      blog content work properly without nl2br.
     *
     *                      Test result: I ran the test using localhost/tests.php. The double quotes
     *                                    did not preserve \n.
     *
     *    
     */
        foreach ($posts as $post) {

            echo '<div class="blogginnlegg transparentbg">';
            echo '<h2>' . htmlspecialchars($post['Tittel']) . '</h2>';
            echo '<p><i>Author: ' . htmlspecialchars($post['ForfatterNavn']) . '</i></br>';
            echo '<i>Email: ' . htmlspecialchars($post['ForfatterEpost']) . '</i></br>';
            echo '<i>Created: ' . htmlspecialchars($post['PubTime']) . '</i></p>';
            echo '<p>' . nl2br(htmlspecialchars($post['Innhold'])) . '</p>';
            echo '</div>';

/*
  Here we might use echo <<<HTML;
                      html-code
                  HTML;
   But what about php literal-variables in HEREDOC?
    Does it work?
    How does it work?
*/
        }
    ?>

    </main>


</body>
</html>
