
<!DOCTYPE html>
<!-- index.html -->
<html>
    <head>
    <meta charset="utf-8"/>

    <title>Blog - Diving into code</title>

    <style>
        
        html {
            font-family: sans-serif;
            color: #f2f2f2;
            display: flex; 
            justify-content: center;
            height: 2000px;

            background-image: url("diver.jpg");
            background-repeat: no-repeat;
            background-attachment: fixed;
        }

        header {

            display: flex;
            font-size: 20px;
            flex-direction: column;
            align-items: center;
            margin-top: 130px;
            margin-bottom: 100px;
        } 

        .blogginnlegg {

            margin-top: 20px;
            height: 200px;
            padding: 20px;
        }

        .whitebg {

            border-radius: 3px;
            color: #737373;
            background-color: #f2f2f2;
        }

        .transparentbg {

            border-radius: 3px;
            color: #f2f2f2;
            background-color: rgba(0,0,0,0.5);
        }

    </style>

</head>

<?php 
/*
 *  1. Create connection
 *  2. Send query and create blogs-object.
 *  3. Complete HTML code with info from Database.    
 *
*/



?>


<body>
    
    <header class="transparentbg">    
        <h2> Diving into code</h2>
        <h4> &lt; en blogg om programmering / &gt;</h4>
    </header>


    <main>

        <div class="blogginnlegg transparentbg">
            <h2>Innlegg 1 </h2>
            <p>ASDjadsfjaefoesfnvøkjdnvøsdnfosdajfdsjfawønføsnkfj.n ønwøeranfrjnfixpnvsidjfnwerøofnvxlndsafn</p>
        </div>

        <div class="blogginnlegg transparentbg">
            <h2>Innlegg 2 </h2>
            <p>Lorumsdkfjadsøofranvønvøoaernv4æjsdoøjnæzsdføweajfæadjzvønfoiwejfoewjfæsemføsdmfløsdnøvjna</p>
        </div>


    </main>


    </body>
</html>
