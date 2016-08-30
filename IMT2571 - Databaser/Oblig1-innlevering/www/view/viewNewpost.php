

<?php 
    /**
     * @author Jonas Solsvik
     * @version 1.0
     * @uses header.php
     * 
     * File     viewNewpost.php
     * Created  26.08.16
     * 
     * Description:
     *          This file has very little php-logic, but still has a great significance
     *           This is because most of the work is beiing done by the HTML-code.
     *            Here we have a HTML-form which sets up a HTTP-post request, to send 
     *             information to the server about the contents of a new blog-post.
    */

require_once '../header.php';?>


    <main>
        <form id="newpostform" action="../index.php" method="post">

            <input name="tittel" id="newposttitle" class="transparentbg hoverme"/>
            <textarea name="innhold" id="newpostarea" class="transparentbg"></textarea>
            <button id="newpostsubmit" type="submit" class="transparentbg hoverme"><h4>Submit</h4></button>

        </form>
    </main>    


</body>
</html>