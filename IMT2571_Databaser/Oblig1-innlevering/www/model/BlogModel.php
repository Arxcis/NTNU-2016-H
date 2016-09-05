<?php 

@require_once 'db_connect.php';

/**
 * @author Jonas Solsvik
 * @version 1.0
 * @uses db_connect.php
 *
 * File    BlogModel.php
 * Created 25.05.16
 * 
 * Description
 *     Used to display and handle the blog-posts in the blog.  
 *      The class is interfacing with a relational SQL-database and the
 *       specific table named 'blogginnlegg'. There are no try-catch or throw-statement
 *        in this class. PDO already throws an PDOexception, and the idea is to handle
 *         this exception further up.
 *       
 * 
 *     Relevant methods:
 *         getPosts()    - gets all posts
 *         getPost()     - gets a single post
 *         createPost()  - creates a single post
 *         editPost()    - edits a post
 *         deletePost()  - deletes a post
*/

class BlogModel {

    /**
     *   @var $db PDO database object
     */
    protected $db;

    /**
     *  Description: The constructor function of classes in PHP looks like this
     *  @throws PDOException 
     */
    public function __construct(){
        $this->db = openDB();       // Establishes a db-connected PDO-object.
    }

    /**
     * Description: Selects all rows in blogginnlegg-table and returns it as
     *               an array of associative arrays.
     *  @return array[] $res - an array of associative arrays which can be referenced
     *                          $res[0]['Tittel']  
     *  @throws PDOException 
     */
    public function getPosts(){

        $sql = "SELECT Tittel, ForfatterNavn,"
             . " ForfatterEpost, PubTime, Innhold"
             . " FROM"
             . " blogginnlegg ORDER BY ID DESC";
        $stmt = $this->db->prepare($sql);   // Send prepared statement

        $stmt->execute();               // execute()
        $res = $stmt->fetchAll(PDO::FETCH_ASSOC);   // fetch all rows

        return $res;
    }

    /**
     * Description: Selects a row in blogginnlegg-table which has a given ID, and 
     *               returns it to the user as an associative array.
     *  
     *  @param string $post_id - used to select ONE row in the database
     *  @return array[] $res - an associative arrays which can be 
     *                          referenced $res['Tittel'].
     *  @throws PDOException 
     */
    public function getPost($post_id){

        $sql = "SELECT Tittel, ForfatterNavn,"
             . " ForfatterEpost, PubTime, Innhold"
             . " FROM"
             . " blogginnlegg WHERE ID=:id";
             
        $stmt = $this->db->prepare($sql);   // Send prepared statement

        $stmt->bindValue(':id', $post_id, PDO::PARAM_INT);
        $stmt->execute();               // execute()
        $res = $stmt->fetch(PDO::FETCH_ASSOC);   // fetch all rows

        return $res;
    }

    /**
     *  Description: With the help of the parameterized data, this functions
     *                creates a new blog entry in the database with all necessary
     *                 fields. 
     * 
     *  @param string $tittel - the title of the blog post
     *  @param string $innhold - the html/text - body of the blog post.
     *  @param string $forfatternavn - the name of the author
     *  @param string $forfatterepost - the email of the author
     * 
     *  @return string $lastid - representing the row ID of the last row that was inserted into the 
     *                            database.
     *  @throws PDOException 
     */
    public function createPost($tittel, $innhold, $forfatternavn, $forfatterepost){

        $sql = "INSERT INTO blogginnlegg"
             . "(Tittel, Innhold, ForfatterNavn, ForfatterEpost) "
             . "VALUES"
             . "(:tittel, :innhold, :forfatternavn, :forfatterepost)";
        $stmt = $this->db->prepare($sql);

        $stmt->execute(array(
                        ':tittel' => $tittel,
                        ':innhold' => $innhold,
                        ':forfatternavn' => $forfatternavn,
                        ':forfatterepost' => $forfatterepost ));

        $lastid = $this->db->lastInsertId();
        return $lastid;
    }

    /**
     *  Description: Makes it possible to edit the title of a blog, the body of a blog
     *                or both, if the user wishes. NOT YET IMPLEMENTED!.
     * 
     *  @param string $post_id - ID of the post to be edited.
     *  @param string $nytittel - New title of the blog post, or the existing title
     *                             if no changes were made.
     *  @param string $nyttinnhold - New html/Text-body of the blogentry, or the old one
     *                                if no changes were made.
     * 
     *  @return string $msg - A statusmessage of what happened if the method ran
     *                         without any exceptions.
     *  @throws PDOException 
     */
    public function editPost($post_id, $nytittel, $nyttinnhold){

        $sql = "UPDATE blogginnlegg "
             . "SET Tittel=:tittel, Innhold=:innhold "
             . "WHERE ID=:id";
        $stmt = $this->db->prepare($sql);

        $stmt->execute(array(
                        ':tittel' => $nytittel,
                        ':innhold' => $nyttinnhold,
                        ':id' => $post_id  ));

        $msg = 'Post edited';
        return $msg;
    }

    /**
     * Description: Deletes a specific post. NOT YET IMPLEMENTED!.
     * 
     *  @param string $post_id - And ID reference to a specific blog-entry in blogginnlegg.
     *  @return string $msg - A statusmessage of what happened if the method ran
     *                         without any exceptions.
     *  @throws PDOException 
     */
    public function deletePost($post_id){

        $sql = "DELETE FROM blogginnlegg WHERE ID=:id";
        $stmt = $this->db->prepare($sql);

        $stmt->execute(array(':id' => $post_id));

        $msg = 'Post deleted';
        return $msg;
    }
}

?>